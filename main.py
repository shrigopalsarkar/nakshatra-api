from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import swisseph as swe
import os
from google import genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
app = FastAPI(title="Nakshatra API")

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Sravana", "Dhanishta", "Shatabhisha",
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
        dt = datetime.fromisoformat(iso_datetime)
        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute/60.0 + dt.second/3600.0)
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        res, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
        moon_lon = res[0] % 360.0
        
        nak_index = int(moon_lon / (360.0 / 27))
        pada = int((moon_lon % (360.0 / 27)) / (360.0 / 108)) + 1
        nakshatra_name = NAKSHATRAS[nak_index]

       prompt = f"""
        Analyze the exact Swiss Ephemeris math for Vedic astrology:
        - Nakshatra: {nakshatra_name}
        - Pada: {pada}
        - Moon Sidereal Longitude: {round(moon_lon, 6)}°
        
        STRICT LOCALIZATION & TRANSLATION DIRECTIVE: 
        You are translating a complete Vedic astrology and compatibility report into language code: {lang}. 
        1. Translate 100% of the text into fluent script of the requested language.
        2. Do NOT include any English words, English terms, or English section titles anywhere. 
        3. Completely translate and remove all English bracketed headers like (Relationship Overview), (Compatibility Summary), (Key Strengths), (Areas of Mindful Effort), and (Future & Life Timeline Prediction) into pure localized equivalents. 
        4. Every single heading, subheading, and description must be in local script. No English should remain.
        """
        response = client.models.generate_content(
            model='gemini-3.5-flash',
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

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
