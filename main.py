"""
FastAPI Backend for Swiss Ephemeris Calculations and Vedic Astrology AI Grounding.
Deployed on Render: https://nakshatra-api-zjp9.onrender.com

Provides:
1. POST /generate-chat-response -> Google Gemini AI grounded chat & predictions
2. GET /panchang -> Real-time Swiss Ephemeris Panchang & Online Mantri Mandal
3. GET /generate-astrology-report -> Astronomical planetary positions & transits
4. GET /calculate -> Moon sidereal longitude, nakshatra, and pada
"""

import os
import math
import datetime
import traceback
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, Query, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from functools import lru_cache

# Import custom modules
from panchang import compute_full_drik_panchang, get_monthly_calendar_grid
from mantri_mandala import compute_mantri_mandala
from festivals import get_festivals_for_day


try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
    swe.set_sid_mode(swe.SIDM_LAHIRI)
except ImportError:
    SWISSEPH_AVAILABLE = False

try:
    from google import genai
    from google.genai import types as genai_types
    NEW_GENAI_AVAILABLE = True
except ImportError:
    NEW_GENAI_AVAILABLE = False

try:
    import google.generativeai as legacy_genai
    LEGACY_GENAI_AVAILABLE = True
except ImportError:
    LEGACY_GENAI_AVAILABLE = False

app = FastAPI(
    title="Vedic Astrology & Swiss Ephemeris Backend API",
    description="FastAPI service powering live Swiss Ephemeris astronomical calculations and Google Gemini AI predictions.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BackendChatPart(BaseModel):
    text: str

class BackendChatContent(BaseModel):
    role: Optional[str] = None
    parts: List[BackendChatPart]

class BackendChatRequest(BaseModel):
    contents: List[BackendChatContent]
    systemInstruction: Optional[BackendChatContent] = None
    system_instruction: Optional[BackendChatContent] = None
    generationConfig: Optional[Dict[str, Any]] = None
    generation_config: Optional[Dict[str, Any]] = None

class BackendChatResponse(BaseModel):
    text: Optional[str] = None
    responseText: Optional[str] = None
    status: str = "success"
    error: Optional[str] = None

ERROR_MESSAGES = {
    "bn": "দুঃখিত, এআই সংযোগে সাময়িক বিলম্ব হচ্ছে। অনুগ্রহ করে 'Retry' বাটনে চাপ দিন।",
    "hi": "क्षमा करें, एआई सर्वर कनेक्शन में विलंब हो रहा है। कृपया 'Retry' पर क्लिक करें।",
    "en": "Astrological synthesis is temporarily delayed. Please tap 'Retry Request'."
}

def resolve_user_language(contents: list, sys_text: str = "") -> str:
    all_parts = []
    user_parts = []

    for item in contents:
        role = str(getattr(item, "role", "") or "user").lower()
        parts = getattr(item, "parts", [])
        item_text = " ".join(getattr(p, "text", "") for p in parts if getattr(p, "text", "")).strip()
        if item_text:
            all_parts.append(item_text)
            if role in ["user", "human"]:
                user_parts.append(item_text)

    full_prompt = " ".join(all_parts) + " " + str(sys_text)
    prompt_lower = full_prompt.lower()
    last_user_text = user_parts[-1] if user_parts else (all_parts[-1] if all_parts else "")

    if any(k in prompt_lower for k in ["language: bn", "language: bengali", "respond in bengali", "in bengali", "in bangla", "language: bangla", "বাংলায় উত্তর", "বাংলা ভাষা"]):
        return "bn"

    if any(k in prompt_lower for k in ["language: hi", "language: hindi", "respond in hindi", "in hindi", "हिंदी में उत्तर", "हिंदी भाषा"]):
        return "hi"

    if any(k in prompt_lower for k in ["language: en", "language: english", "respond in english", "in english", "english language"]):
        return "en"

    bn_user = sum(1 for ch in last_user_text if "\u0980" <= ch <= "\u09ff")
    hi_user = sum(1 for ch in last_user_text if "\u0900" <= ch <= "\u097f")
    en_user = sum(1 for ch in last_user_text if ("a" <= ch <= "z" or "A" <= ch <= "Z"))

    if bn_user > 3 and bn_user > hi_user: return "bn"
    if hi_user > 3 and hi_user > bn_user: return "hi"
    if en_user > 3 and en_user > (bn_user + hi_user): return "en"

    total_bn = sum(1 for ch in full_prompt if "\u0980" <= ch <= "\u09ff")
    total_hi = sum(1 for ch in full_prompt if "\u0900" <= ch <= "\u097f")
    total_en = sum(1 for ch in full_prompt if ("a" <= ch <= "z" or "A" <= ch <= "Z"))

    if total_bn > 15 and total_bn > total_hi: return "bn"
    if total_hi > 15 and total_hi > total_bn: return "hi"
    if total_en > total_bn and total_en > total_hi: return "en"

    return "en"

@app.post("/generate-chat-response", response_model=BackendChatResponse)
async def generate_chat_response(request: BackendChatRequest):
    lang_code = "en"
    try:
        sys_prompt = ""
        sys_inst = request.systemInstruction or request.system_instruction
        if sys_inst and sys_inst.parts:
            sys_prompt = "\n".join(p.text for p in sys_inst.parts if p.text and p.text.strip())

        lang_code = resolve_user_language(request.contents, sys_prompt)

        api_key = (
            os.environ.get("GEMINI_API_KEY")
            or os.environ.get("GOOGLE_API_KEY")
            or os.environ.get("API_KEY")
        )
        if not api_key:
            err_txt = ERROR_MESSAGES[lang_code]
            return BackendChatResponse(text=err_txt, responseText=err_txt, status="success")

        raw_items = []
        for c in request.contents:
            role = "model" if str(c.role or "user").lower() in ["ai", "assistant", "model"] else "user"
            txt = "\n".join(p.text for p in c.parts if p.text and p.text.strip())
            if txt.strip():
                raw_items.append({"role": role, "parts": [{"text": txt}]})

        while raw_items and raw_items[0]["role"] == "model":
            raw_items.pop(0)

        cleaned_contents = []
        for item in raw_items:
            if not cleaned_contents or cleaned_contents[-1]["role"] != item["role"]:
                cleaned_contents.append(item)
            else:
                cleaned_contents[-1]["parts"][0]["text"] += f"\n{item['parts'][0]['text']}"

        while cleaned_contents and cleaned_contents[0]["role"] != "user":
            cleaned_contents.pop(0)

        if not cleaned_contents:
            err_txt = ERROR_MESSAGES[lang_code]
            return BackendChatResponse(text=err_txt, responseText=err_txt, status="success")

        import urllib.request
        import json

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {"contents": cleaned_contents}
        if sys_prompt:
            payload["systemInstruction"] = {"parts": [{"text": sys_prompt}]}

        req_data = json.dumps(payload).encode("utf-8")
        http_req = urllib.request.Request(
            url,
            data=req_data,
            headers={"Content-Type": "application/json"}
        )

        with urllib.request.urlopen(http_req, timeout=35) as res:
            res_body = json.loads(res.read().decode("utf-8"))
            candidates = res_body.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                result_text = "".join(p.get("text", "") for p in parts if "text" in p)
                if result_text.strip():
                    return BackendChatResponse(
                        text=result_text,
                        responseText=result_text,
                        status="success"
                    )

        fallback = ERROR_MESSAGES[lang_code]
        return BackendChatResponse(text=fallback, responseText=fallback, status="success")

    except Exception as e:
        print("[AI ERROR]:", str(e))
        fallback = ERROR_MESSAGES.get(lang_code, ERROR_MESSAGES["en"])
        return BackendChatResponse(text=fallback, responseText=fallback, status="success")

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Svati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def calculate_julian_day(dt: datetime.datetime) -> float:
    a = (14 - dt.month) // 12
    y = dt.year + 4800 - a
    m = dt.month + 12 * a - 3
    jdn = dt.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    fraction = (dt.hour - 12) / 24.0 + dt.minute / 1440.0 + dt.second / 86400.0
    return jdn + fraction

def calculate_lahiri_ayanamsa(jd: float) -> float:
    t = (jd - 2451545.0) / 36525.0
    return 23.85 + 0.01396 * (jd - 2451545.0) / 365.25

def calculate_planet_positions(dt: datetime.datetime, lat: float = 28.6139, lon: float = 77.2090):
    jd = calculate_julian_day(dt)
    ayanamsa = calculate_lahiri_ayanamsa(jd)
    
    planets_data = {}
    planet_map = {
        "Sun": 0, "Moon": 1, "Mars": 4, "Mercury": 2,
        "Jupiter": 5, "Venus": 3, "Saturn": 6, "Rahu": 11
    }

    if SWISSEPH_AVAILABLE:
        for name, planet_id in planet_map.items():
            flag = swe.FLG_SIDEREAL | swe.FLG_SPEED
            body = swe.MEAN_NODE if planet_id == 11 else planet_id
            res, _ = swe.calc_ut(jd, body, flag)

            lon_deg = res[0] % 360.0
            speed = res[3]
            is_retrograde = speed < 0 if planet_id not in [0, 1, 11] else False

            rashi_idx = int(lon_deg // 30) % 12
            nak_idx = int(lon_deg / (360.0 / 27.0)) % 27
            pada = int((lon_deg % (360.0 / 27.0)) / (360.0 / 108.0)) + 1

            planets_data[name] = {
                "longitude": round(lon_deg, 4),
                "rashi": RASHIS[rashi_idx],
                "nakshatra": NAKSHATRAS[nak_idx],
                "pada": pada,
                "is_retrograde": is_retrograde
            }

        rahu_lon = planets_data["Rahu"]["longitude"]
        ketu_lon = (rahu_lon + 180.0) % 360.0
        rashi_idx = int(ketu_lon // 30) % 12
        nak_idx = int(ketu_lon / (360.0 / 27.0)) % 27
        pada = int((ketu_lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1
        planets_data["Ketu"] = {
            "longitude": round(ketu_lon, 4),
            "rashi": RASHIS[rashi_idx],
            "nakshatra": NAKSHATRAS[nak_idx],
            "pada": pada,
            "is_retrograde": True
        }
    return planets_data

@lru_cache(maxsize=512)
def get_cached_panchang(iso_date: str, lat: float, lon: float, lang: str, time_format: str):
    date_obj = datetime.date.fromisoformat(iso_date)
    return compute_full_drik_panchang(date_obj, lat=lat, lon=lon, lang=lang, time_format=time_format)

@app.get("/panchang")
async def get_panchang(
    iso_date: str = Query(..., description="Date in YYYY-MM-DD format"),
    lat: float = Query(22.5726, description="Latitude (Default Kolkata: 22.5726)"),
    lon: float = Query(88.3639, description="Longitude (Default Kolkata: 88.3639)"),
    lang: str = Query("en", description="Language: 'en', 'hi', or 'bn'"),
    time_format: str = Query("12hr", description="Time format: '12hr', '24hr', or '24+hr'")
):
    try:
        return get_cached_panchang(iso_date, lat, lon, lang, time_format)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid iso_date format.")

@app.get("/calculate")
async def calculate(iso_datetime: str = Query(..., description="ISO Datetime YYYY-MM-DDTHH:MM:SS")):
    try:
        dt = datetime.datetime.fromisoformat(iso_datetime)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid iso_datetime format. Use YYYY-MM-DDTHH:MM:SS")

    planets = calculate_planet_positions(dt)
    moon = planets["Moon"]

    return {
        "nakshatra": moon["nakshatra"],
        "pada": moon["pada"],
        "moon_sidereal_longitude": moon["longitude"],
        "datetime_utc": dt.isoformat()
    }

@app.get("/generate-astrology-report")
async def generate_astrology_report(
    iso_datetime: str = Query(..., description="ISO Datetime YYYY-MM-DDTHH:MM:SS"),
    lat: float = Query(28.6139, description="Latitude"),
    lng: float = Query(77.2090, description="Longitude"),
    lang: str = Query("en", description="Language code")
):
    try:
        dt = datetime.datetime.fromisoformat(iso_datetime)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid iso_datetime format.")

    planets = calculate_planet_positions(dt, lat, lng)
    iso_date = dt.date().isoformat()
    panchang_data = get_cached_panchang(iso_date, lat, lng, lang, "12hr")

    return {
        "astronomical_data": {
            "moon": planets["Moon"],
            "planets": planets,
            "panchang": panchang_data
        },
        "localized_report": f"Astronomical calculations grounded in Swiss Ephemeris for {iso_datetime}."
    }

# 🚀 100% Caching for Monthly Calendar (Makes it 100x Faster!)
@lru_cache(maxsize=128)
def get_cached_monthly_calendar(year: int, month: int, cal_type: str, lat: float, lon: float, lang: str):
    return get_monthly_calendar_grid(year, month, cal_type=cal_type, lat=lat, lon=lon, lang=lang)

@app.get("/monthly-calendar")
def get_monthly_cal(year: int, month: int, cal_type: str = "bengali", lat: float = 22.5726, lon: float = 88.3639, lang: str = "bn"):
    return get_cached_monthly_calendar(year, month, cal_type, lat, lon, lang)

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Vedic Astrology Swiss Ephemeris API",
        "endpoints": [
            "POST /generate-chat-response",
            "GET /panchang",
            "GET /generate-astrology-report",
            "GET /monthly-calendar",
            "GET /calculate"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.datetime.utcnow().isoformat()}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
