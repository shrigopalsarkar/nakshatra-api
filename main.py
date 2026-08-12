from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import swisseph as swe
import os
from google import genai  # Google GenAI SDK

# Render ke environment variable se securely key uthayega
GEMINI_API_KEY = os.environ.get("AQ.Ab8RN6LILqU2YzhTZbo2S_5Tt73nW845JNBzzwz1VbqwoxJeww")
client = genai.Client(api_key=GEMINI_API_KEY)
app = FastAPI(title="Nakshatra API")

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/calculate")
def calculate(iso_datetime: str):
    try:
        dt = datetime.fromisoformat(iso_datetime)
        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60.0 + dt.second/3600.0)
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        res, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
        moon_lon = res[0] % 360.0
        
        nak_index = int(moon_lon / (360.0 / 27))
        pada = int((moon_lon % (360.0 / 27)) / (360.0 / 108)) + 1
        
        return {
            "nakshatra": NAKSHATRAS[nak_index],
            "pada": pada,
            "moon_sidereal_longitude": round(moon_lon, 6),
            "datetime_utc": dt.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        @app.get("/generate-astrology-report")
def generate_report(iso_datetime: str, lang: str = "bn"):
    try:
        # Wahi same Swiss Ephemeris calculation jo aapke /calculate mein hai
        dt = datetime.fromisoformat(iso_datetime)
        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60.0 + dt.second/3600.0)
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        res, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
        moon_lon = res[0] % 360.0
        
        nak_index = int(moon_lon / (360.0 / 27))
        pada = int((moon_lon % (360.0 / 27)) / (360.0 / 108)) + 1
        nakshatra_name = NAKSHATRAS[nak_index]

        # Gemini AI se report generate karwana
        prompt = """
        Analyze the exact Swiss Ephemeris math:
        - Nakshatra: {nakshatra_name}
        - Pada: {pada}
        - Moon Sidereal Longitude: {round(moon_lon, 6)}°
        Provide a detailed Vedic astrology breakdown for career and wealth in language code: {lang}.
        """

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )

        return {
            "nakshatra": nakshatra_name,
            "pada": pada,
            "longitude": round(moon_lon, 6),
            "ai_report": response.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
