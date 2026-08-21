"""
main.py
FastAPI backend for Vedic Astrology & Panchang Calculations.
Uses Swiss Ephemeris for 100% deterministic astronomical math and 
Gemini exclusively for natural language synthesis and native script localization.
"""

from __future__ import annotations
import os
from datetime import datetime, date as date_type
from zoneinfo import ZoneInfo
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
import swisseph as swe
from google import genai

from panchang import compute_panchang, compute_mantri_mandala

IST = ZoneInfo("Asia/Kolkata")
UTC = ZoneInfo("UTC")

from muhurta import (compute_kaal_periods, compute_choghadiya,
                     compute_muhurtas, compute_samvatsara, vedic_weekday)

def _parse_local(s: str) -> datetime:
    """Panchang strings are '%Y-%m-%d %I:%M:%S %p' in IST."""
    return datetime.strptime(s, "%Y-%m-%d %I:%M:%S %p").replace(tzinfo=IST)
    
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

app = FastAPI(title="Panchang & Vedic Astrology API")

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Sravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

PLANETS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,
}

RASHIS = [
    "Mesha", "Vrishabha", "Mithuna", "Karka",
    "Simha", "Kanya", "Tula", "Vrishchika",
    "Dhanu", "Makara", "Kumbha", "Meena"
]


def parse_to_utc_jd(iso_datetime_str: str) -> tuple[float, datetime]:
    """Parses an ISO datetime string and returns (Julian Day UT, UTC Datetime)."""
    dt = datetime.fromisoformat(iso_datetime_str)
    if dt.tzinfo is None:
        # Default naive datetimes to IST
        dt = dt.replace(tzinfo=IST)
    dt_utc = dt.astimezone(UTC)
    jd = swe.julday(
        dt_utc.year, dt_utc.month, dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0
    )
    return jd, dt_utc


def get_planetary_positions(jd_ut: float) -> dict:
    """Calculates sidereal positions for all major bodies."""
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
    positions = {}

    for name, body_id in PLANETS.items():
        res, _ = swe.calc_ut(jd_ut, body_id, flags)
        lon = res[0] % 360.0
        speed = res[3]
        rashi_idx = int(lon / 30.0)
        nak_idx = int(lon / (360.0 / 27.0))
        pada = int((lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1

        positions[name] = {
            "longitude": round(lon, 4),
            "rashi": RASHIS[rashi_idx],
            "nakshatra": NAKSHATRAS[nak_idx],
            "pada": pada,
            "is_retrograde": speed < 0
        }

    # Ketu is exactly 180 degrees from Rahu
    rahu_lon = positions["Rahu"]["longitude"]
    ketu_lon = (rahu_lon + 180.0) % 360.0
    positions["Ketu"] = {
        "longitude": round(ketu_lon, 4),
        "rashi": RASHIS[int(ketu_lon / 30.0)],
        "nakshatra": NAKSHATRAS[int(ketu_lon / (360.0 / 27.0))],
        "pada": int((ketu_lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1,
        "is_retrograde": positions["Rahu"]["is_retrograde"]
    }
    return positions


@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/calculate")
def calculate(iso_datetime: str):
    try:
        jd, dt_utc = parse_to_utc_jd(iso_datetime)
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        res, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)
        moon_lon = res[0] % 360.0

        nak_index = int(moon_lon / (360.0 / 27.0))
        pada = int((moon_lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1

        return {
            "nakshatra": NAKSHATRAS[nak_index],
            "pada": pada,
            "moon_sidereal_longitude": round(moon_lon, 6),
            "datetime_utc": dt_utc.isoformat(),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/panchang")
def panchang_endpoint(iso_date: str, lat: float = 28.6139, lon: float = 77.2090):
    try:
        d = date_type.fromisoformat(iso_date)
        p_res = compute_panchang(d, lat, lon)
        mm_data = compute_mantri_mandala(d, lat, lon)
        w_idx = vedic_weekday(p_res.raw_sunrise_dt)

        kaal_data = compute_kaal_periods(p_res.raw_sunrise_dt, p_res.raw_sunset_dt, w_idx)
        muhurta_data = compute_muhurtas(
            p_res.raw_sunrise_dt, p_res.raw_sunset_dt, w_idx,
            p_res.nakshatra_index, p_res.nakshatra_start_dt, p_res.nakshatra_end_dt
        )
        choghadiya_data = compute_choghadiya(p_res.raw_sunrise_dt, p_res.raw_sunset_dt, p_res.raw_next_sunrise_dt, w_idx)

        response = {
            "date_local": p_res.date_local,
            "sunrise": p_res.sunrise,
            "sunset": p_res.sunset,
            "next_sunrise": p_res.next_sunrise,
            "moonrise": p_res.moonrise,
            "moonset": p_res.moonset,
            "tithi_name": p_res.tithi_name,
            "tithi_end": p_res.tithi_end,
            "tithi_next_name": p_res.tithi_next_name,
            "nakshatra_name": p_res.nakshatra_name,
            "nakshatra_end": p_res.nakshatra_end,
            "nakshatra_next_name": p_res.nakshatra_next_name,
            "yoga_name": p_res.yoga_name,
            "yoga_end": p_res.yoga_end,
            "yoga_next_name": p_res.yoga_next_name,
            "karana_name": p_res.karana_name,
            "karana_end": p_res.karana_end,
            "karana_next_name": p_res.karana_next_name,
            "karana_type": p_res.karana_type,
            "pada_timeline": p_res.pada_timeline,
            "nakshatra_pada_display": p_res.nakshatra_pada_display,
            "timezone": "Asia/Kolkata",
            "mantri_mandala": mm_data,
            "kaal_periods": kaal_data,
            "muhurtas": muhurta_data,
            "choghadiya": choghadiya_data
        }
        vikram_samvat_num = int(mm_data["vikram_samvat_new_year"][:4]) + 57
        response["samvatsara"] = compute_samvatsara(vikram_samvat_num)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/generate-astrology-report")
def generate_report(
    iso_datetime: str,
    lat: float = 23.1793,
    lng: float = 75.7849,
    lang: str = Query(default="bn", description="Language code: bn, hi, en, etc.")
):
    if not client:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY environment variable is not configured.")

    try:
        jd, dt_utc = parse_to_utc_jd(iso_datetime)
        local_date = dt_utc.astimezone(IST).date()

        # Deterministic ephemeris math calculated in Python
        panchang_data = compute_panchang(local_date, lat, lng)
        planetary_positions = get_planetary_positions(jd)
        moon_details = planetary_positions["Moon"]

        # Provide exact astronomical data to Gemini for translation & astrological analysis
        prompt = f"""
You are a master Vedic Astrologer. Analyze the following astronomical calculations and generate a detailed report.

--- COMPUTED ASTRONOMICAL DATA ---
Target Date & Time (IST): {dt_utc.astimezone(IST).isoformat()}
Location: Latitude {lat}, Longitude {lng}

Panchang Elements:
- Tithi: {panchang_data.tithi_name} (Ends at: {panchang_data.tithi_end})
- Nakshatra: {panchang_data.nakshatra_name} (Ends at: {panchang_data.nakshatra_end})
- Yoga: {panchang_data.yoga_name} (Ends at: {panchang_data.yoga_end})
- Karana: {panchang_data.karana_name} (Ends at: {panchang_data.karana_end})
- Sunrise: {panchang_data.sunrise} | Sunset: {panchang_data.sunset}

Moon Details:
- Longitude: {moon_details['longitude']}°
- Nakshatra: {moon_details['nakshatra']}, Pada: {moon_details['pada']}
- Rashi: {moon_details['rashi']}

Planetary Placements:
{planetary_positions}

--- LOCALIZATION & FORMATTING REQUIREMENTS ---
Language Code: {lang}
1. Native Script: Translate all headings, descriptions, and astrological analysis into the native script of {lang} (e.g., Bengali script for 'bn', Devanagari for 'hi').
2. Numbers & Dates: Convert all numerals into the target script's native digits (e.g., ১, ২, ৩ for Bengali; १, २, ३ for Hindi).
3. Do NOT recalculate astronomical times; use the pre-computed timestamps above.
4. Output a clean astrological analysis including:
   - Nature & Characteristics of the Janma Nakshatra & Pada
   - Panchang summary & Tithi significance
   - Graha Dignities & dosha analysis (e.g., Nadi, Bhakoot, Manglik considerations)
   - Practical astrological guidance
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return {
            "astronomical_data": {
                "moon": moon_details,
                "panchang": panchang_data.__dict__,
                "planets": planetary_positions
            },
            "localized_report": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
