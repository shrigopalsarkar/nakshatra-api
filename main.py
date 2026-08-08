from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import swisseph as swe

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
        swe.set_sidmode(swe.SIDM_LAHIRI, 0, 0)
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
