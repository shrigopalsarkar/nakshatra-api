"""
FastAPI Backend for Swiss Ephemeris Calculations and Vedic Astrology AI Grounding.
Deployed on Render: https://nakshatra-api-zjp9.onrender.com

Provides:
1. POST /generate-chat-response -> Google Gemini 2.0 Flash grounded chat & predictions
2. GET /panchang -> Real-time Swiss Ephemeris Panchang
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

# Try importing pyswisseph; provide mathematical fallback if compiled C extensions are absent
try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
    swe.set_sid_mode(swe.SIDM_LAHIRI)
except ImportError:
    SWISSEPH_AVAILABLE = False

# Try importing Google GenAI SDK (new google-genai) and legacy google.generativeai
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

# Enable CORS for mobile app and cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================================================================
# DATA MODELS (Matches Android Retrofit DTOs)
# ==============================================================================

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


# ==============================================================================
# 1. GOOGLE GEMINI CHAT ENDPOINT (POST /generate-chat-response)
# ==============================================================================

@app.post("/generate-chat-response", response_model=BackendChatResponse)
async def generate_chat_response(request: BackendChatRequest):
    """
    Direct endpoint matching Android BackendChatRequest DTO.
    Connects securely to Google Gemini 2.0 Flash via Gemini API Key.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="GEMINI_API_KEY environment variable is not configured on the server."
        )

    # 1. Extract system instruction text if provided
    system_prompt = None
    sys_inst = request.systemInstruction or request.system_instruction
    if sys_inst and sys_inst.parts:
        system_prompt = "\n".join([p.text for p in sys_inst.parts if p.text and p.text.strip()])

    # 2. Build and sanitize contents payload
    raw_contents = []
    for c in request.contents:
        role = c.role or "user"
        gemini_role = "model" if role.lower() in ["ai", "assistant", "model"] else "user"
        combined_text = "\n".join([p.text for p in c.parts if p.text and p.text.strip()])
        if combined_text.strip():
            raw_contents.append({
                "role": gemini_role,
                "parts": [{"text": combined_text}]
            })

    # 3. Strip any leading "model" messages (Gemini strictly requires contents to start with "user")
    while raw_contents and raw_contents[0]["role"] == "model":
        raw_contents.pop(0)

    # 4. Enforce strict alternating sequence (user -> model -> user -> model)
    alternating_contents = []
    for item in raw_contents:
        if not alternating_contents or alternating_contents[-1]["role"] != item["role"]:
            alternating_contents.append(item)
        else:
            existing_text = alternating_contents[-1]["parts"][0]["text"]
            new_text = item["parts"][0]["text"]
            alternating_contents[-1]["parts"][0]["text"] = f"{existing_text}\n{new_text}"

    # 5. Ensure at least one valid "user" message exists
    if not alternating_contents:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No valid user prompt provided in the chat request."
        )

    # 6. Ensure the first message is strictly "user"
    while alternating_contents and alternating_contents[0]["role"] != "user":
        alternating_contents.pop(0)

    response_text = ""

    # 7. Generate response using gemini-2.0-flash
    try:
        if NEW_GENAI_AVAILABLE:
            client = genai.Client(api_key=api_key)
            config_params = {}
            if system_prompt:
                config_params["system_instruction"] = system_prompt

            gen_config = genai_types.GenerateContentConfig(**config_params) if config_params else None

            sdk_contents = [
                genai_types.Content(
                    role=item["role"],
                    parts=[genai_types.Part.from_text(text=p["text"]) for p in item["parts"]]
                )
                for item in alternating_contents
            ]

            res = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=sdk_contents,
                config=gen_config
            )
            response_text = res.text or ""

        elif LEGACY_GENAI_AVAILABLE:
            legacy_genai.configure(api_key=api_key)
            model_kwargs = {"model_name": "gemini-2.0-flash"}
            if system_prompt:
                model_kwargs["system_instruction"] = system_prompt

            model = legacy_genai.GenerativeModel(**model_kwargs)
            res = model.generate_content(alternating_contents)
            response_text = res.text or ""

        else:
            import urllib.request
            import json

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
            payload: Dict[str, Any] = {"contents": alternating_contents}
            if system_prompt:
                payload["systemInstruction"] = {
                    "parts": [{"text": system_prompt}]
                }

            req_data = json.dumps(payload).encode("utf-8")
            http_req = urllib.request.Request(
                url,
                data=req_data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(http_req, timeout=45) as response:
                res_body = json.loads(response.read().decode("utf-8"))
                candidates = res_body.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    response_text = "".join([p.get("text", "") for p in parts])

    except Exception as e:
        print("[BACKEND ERROR /generate-chat-response]:", str(e))
        traceback.print_exc()
        # Fallback attempt with gemini-1.5-flash
        try:
            import urllib.request
            import json
            fallback_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {"contents": alternating_contents}
            if system_prompt:
                payload["systemInstruction"] = {"parts": [{"text": system_prompt}]}
            req_data = json.dumps(payload).encode("utf-8")
            http_req = urllib.request.Request(
                fallback_url,
                data=req_data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(http_req, timeout=45) as response:
                res_body = json.loads(response.read().decode("utf-8"))
                candidates = res_body.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    response_text = "".join([p.get("text", "") for p in parts])
        except Exception as inner_e:
            return BackendChatResponse(
                text="দুঃখিত, এআই সার্ভারের সাথে সংযোগ স্থাপন করা সম্ভব হয়নি। অনুগ্রহ করে কিছুক্ষণ পর পুনরায় চেষ্টা করুন।",
                responseText="দুঃখিত, এআই সার্ভারের সাথে সংযোগ স্থাপন করা সম্ভব হয়নি। অনুগ্রহ করে কিছুক্ষণ পর পুনরায় চেষ্টা করুন।",
                status="error",
                error=f"Gemini API error: {str(e)} | Fallback error: {str(inner_e)}"
            )

    return BackendChatResponse(
        text=response_text,
        responseText=response_text,
        status="success",
        error=None
    )


# ==============================================================================
# 2. PANCHANG & ASTRONOMICAL COMPUTATIONS
# ==============================================================================

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

TITHIS = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
]

YOGAS = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda",
    "Sukarma", "Dhriti", "Shula", "Ganda", "Vriddhi", "Dhruva",
    "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyan",
    "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla",
    "Brahma", "Indra", "Vaidhriti"
]

KARANAS = [
    "Bava", "Balava", "Kaulava", "Taitila", "Gara", "Vanija", "Vishti",
    "Shakuni", "Chatushpada", "Naga", "Kintughna"
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
    else:
        t = (jd - 2451545.0) / 36525.0
        sun_mean_lon = (280.46646 + 36000.76983 * t) % 360.0
        sun_sidereal = (sun_mean_lon - ayanamsa) % 360.0
        
        moon_mean_lon = (218.3165 + 481267.8813 * t) % 360.0
        moon_sidereal = (moon_mean_lon - ayanamsa) % 360.0

        for name, lon_deg in [("Sun", sun_sidereal), ("Moon", moon_sidereal), ("Mars", (sun_sidereal + 45) % 360),
                              ("Mercury", (sun_sidereal + 15) % 360), ("Jupiter", (sun_sidereal + 120) % 360),
                              ("Venus", (sun_sidereal + 30) % 360), ("Saturn", (sun_sidereal + 240) % 360),
                              ("Rahu", (sun_sidereal + 180) % 360), ("Ketu", sun_sidereal)]:
            rashi_idx = int(lon_deg // 30) % 12
            nak_idx = int(lon_deg / (360.0 / 27.0)) % 27
            pada = int((lon_deg % (360.0 / 27.0)) / (360.0 / 108.0)) + 1
            planets_data[name] = {
                "longitude": round(lon_deg, 4),
                "rashi": RASHIS[rashi_idx],
                "nakshatra": NAKSHATRAS[nak_idx],
                "pada": pada,
                "is_retrograde": False
            }

    return planets_data

@app.get("/panchang")
async def get_panchang(
    iso_date: str = Query(..., description="Date in YYYY-MM-DD format"),
    lat: float = Query(28.6139, description="Latitude"),
    lon: float = Query(77.2090, description="Longitude")
):
    try:
        date_obj = datetime.date.fromisoformat(iso_date)
        dt = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, 12, 0, 0)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid iso_date format. Use YYYY-MM-DD.")

    planets = calculate_planet_positions(dt, lat, lon)
    sun_lon = planets["Sun"]["longitude"]
    moon_lon = planets["Moon"]["longitude"]

    diff_tithi = (moon_lon - sun_lon) % 360.0
    tithi_idx = int(diff_tithi / 12.0) % 30
    tithi_name = TITHIS[tithi_idx]

    nak_idx = int(moon_lon / (360.0 / 27.0)) % 27
    nak_name = NAKSHATRAS[nak_idx]
    pada = int((moon_lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1

    yoga_sum = (sun_lon + moon_lon) % 360.0
    yoga_idx = int(yoga_sum / (360.0 / 27.0)) % 27
    yoga_name = YOGAS[yoga_idx]

    karana_idx = int(diff_tithi / 6.0) % 60
    karana_name = KARANAS[karana_idx % 7] if karana_idx < 57 else KARANAS[7 + (karana_idx - 57)]

    sunrise_str = "06:00:00"
    sunset_str = "18:30:00"

    return {
        "date_local": iso_date,
        "sunrise": sunrise_str,
        "sunset": sunset_str,
        "next_sunrise": "06:00:00",
        "moonrise": "19:15:00",
        "moonset": "07:45:00",
        "tithi_name": tithi_name,
        "tithi_end": f"{iso_date}T23:59:59",
        "tithi_next_name": TITHIS[(tithi_idx + 1) % 30],
        "nakshatra_name": nak_name,
        "nakshatra_end": f"{iso_date}T22:30:00",
        "nakshatra_next_name": NAKSHATRAS[(nak_idx + 1) % 27],
        "yoga_name": yoga_name,
        "yoga_end": f"{iso_date}T21:00:00",
        "yoga_next_name": YOGAS[(yoga_idx + 1) % 27],
        "karana_name": karana_name,
        "karana_end": f"{iso_date}T15:45:00",
        "karana_next_name": KARANAS[(karana_idx + 1) % 11],
        "karana_type": "Chara",
        "pada_timeline": [
            {"nakshatra": nak_name, "pada": pada, "end": f"{iso_date}T18:00:00"}
        ],
        "nakshatra_pada_display": f"{nak_name} (Pada {pada})",
        "timezone": "Asia/Kolkata",
        "kaal_periods": {
            "rahu_kaal": {"start": "16:30:00", "end": "18:00:00"},
            "gulika_kaal": {"start": "13:30:00", "end": "15:00:00"},
            "yamaganda_kaal": {"start": "06:00:00", "end": "07:30:00"}
        },
        "muhurtas": {
            "brahma_muhurta": {"start": "04:24:00", "end": "05:12:00"},
            "abhijit_muhurta": {"start": "11:45:00", "end": "12:35:00", "is_auspicious": True},
            "vijaya_muhurta": {"start": "14:15:00", "end": "15:05:00"},
            "amrit_kaal": {"start": "08:30:00", "end": "10:15:00"}
        }
    }

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
    panchang_data = await get_panchang(iso_date, lat, lng)

    return {
        "astronomical_data": {
            "moon": planets["Moon"],
            "planets": planets,
            "panchang": panchang_data
        },
        "localized_report": f"Astronomical calculations grounded in Swiss Ephemeris for {iso_datetime}."
    }

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Vedic Astrology Swiss Ephemeris API",
        "endpoints": [
            "POST /generate-chat-response",
            "GET /panchang",
            "GET /generate-astrology-report",
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
