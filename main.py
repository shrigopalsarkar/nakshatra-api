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
        - Language Code: {lang}

        STRICT ABSOLUTE LOCALIZATION & TRANSLATION DIRECTIVE:
        You are generating a 100% natively localized Vedic astrology and compatibility report for language code: {lang}.
        1. 100% NATIVE SCRIPT: Translate EVERY SINGLE WORD, heading, subheading, bullet point, description, strength, and advice point entirely into the native script of the selected language (Bengali script if {lang} is 'bn', Hindi script if {lang} is 'hi').
        2. ZERO ENGLISH WORDS OR DIGITS: Do NOT output any English words, technical terms, headers, or English digits (1, 2, 3...). 
        3. LOCALIZED NUMBERS & DATES: Convert all numbers into native local digits (e.g., Bengali: ১, ২, ৩... or Hindi: १, २, ३...). Translate all month names and date formats completely into native script equivalents.
        4. ABSOLUTE PURITY: Completely translate or remove all English titles and bracketed terms (like 'Relationship Overview', 'Compatibility Summary', 'Key Strengths'). The entire response from start to finish must be 100% in the native script of {lang}.

        STRICT DOSHA & TERM TRANSLATION DIRECTIVE:
        You are translating and generating a 100% natively localized Vedic astrology report for language code: {lang}.
        1. Translate 100% of the text, headings, dosha names, and bracketed terms entirely into the native script of the selected language (Bengali script if {lang} is 'bn', Hindi script if {lang} is 'hi').
        2. NEVER output English dosha names or terms in parentheses/brackets. Always convert them to native script terms:
           - Nadi Dosha -> (Bengali: নাড়ী দোষ | Hindi: नाड़ी दोष)
           - Bhakoot Dosha -> (Bengali: ভাকুট দোষ | Hindi: भाकूट दोष)
           - Rajju Dosha -> (Bengali: রজ্জু দোষ | Hindi: रज्जू दोष)
           - Vedha Dosha -> (Bengali: বেধ দোষ | Hindi: वेध दोष)
           - Manglik Dosha / Mangal Dosha -> (Bengali: মঙ্গল দোষ | Hindi: मंगलिक दोष / मंगल दोष)
           - Graha Maitri -> (Bengali: গ্রহ মৈত্রী | Hindi: ग्रह मैत्री)
           - Gana Gun -> (Bengali: গণ গুণ | Hindi: गण गुण)
           - Bharna / Yoni -> (Bengali: যোনি গুণ | Hindi: योनि गुण)
        3. The entire response from start to finish must be completely free of English astrological terms and bracketed English words.
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
