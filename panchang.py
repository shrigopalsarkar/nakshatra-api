"""
panchang.py
Astronomical Daily Panchang & Vikram Samvat Mantri Mandala Engine.
Calculates Tithi, Nakshatra, Yoga, Karana transitions, Sun/Moon events,
and true solar-ingress-based Planetary Cabinet (Navadhikaris).
"""

from __future__ import annotations
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from dataclasses import dataclass
import swisseph as swe

IST = ZoneInfo("Asia/Kolkata")
UTC = ZoneInfo("UTC")

TITHI_NAMES = [
    "Shukla Pratipada", "Shukla Dwitiya", "Shukla Tritiya", "Shukla Chaturthi", "Shukla Panchami",
    "Shukla Shashthi", "Shukla Saptami", "Shukla Ashtami", "Shukla Navami", "Shukla Dashami",
    "Shukla Ekadashi", "Shukla Dwadashi", "Shukla Trayodashi", "Shukla Chaturdashi", "Purnima",
    "Krishna Pratipada", "Krishna Dwitiya", "Krishna Tritiya", "Krishna Chaturthi", "Krishna Panchami",
    "Krishna Shashthi", "Krishna Saptami", "Krishna Ashtami", "Krishna Navami", "Krishna Dashami",
    "Krishna Ekadashi", "Krishna Dwadashi", "Krishna Trayodashi", "Krishna Chaturdashi", "Amavasya"
]

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Sravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda",
    "Sukarma", "Dhriti", "Shoola", "Ganda", "Vriddhi", "Dhruva",
    "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyana",
    "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla",
    "Brahma", "Indra", "Vaidhriti"
]

KARANA_NAMES_MOVABLE = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]
KARANA_FIXED = {0: "Kimstughna", 57: "Shakuni", 58: "Chatushpada", 59: "Naga"}
WEEKDAY_LORDS = ["Surya", "Chandra", "Mangal", "Budha", "Guru", "Shukra", "Shani"]


def weekday_lord(d: date) -> str:
    """Returns Vedic weekday lord (Sunday=Surya ... Saturday=Shani)."""
    return WEEKDAY_LORDS[(d.weekday() + 1) % 7]


def to_jd_ut(dt_local: datetime) -> float:
    dt_utc = dt_local.astimezone(UTC)
    return swe.julday(
        dt_utc.year, dt_utc.month, dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0
    )


def jd_to_local(jd_ut: float) -> datetime:
    y, m, d, h = swe.revjul(jd_ut)
    base = datetime(y, m, d, tzinfo=UTC) + timedelta(hours=h)
    return base.astimezone(IST)


def get_sunrise_jd(target_date: date, lat: float, lon: float) -> float:
    """Calculates sunrise for a specific local date."""
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    noon_local = datetime(target_date.year, target_date.month, target_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25
    geopos = (lon, lat, 0.0)
    flags = swe.CALC_RISE | swe.BIT_DISC_CENTER
    _, s_rise = swe.rise_trans(jd_approx, swe.SUN, flags, geopos)
    return s_rise[0]


def sidereal_longitudes(jd_ut: float) -> tuple[float, float]:
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
    sun = swe.calc_ut(jd_ut, swe.SUN, flags)[0][0] % 360.0
    moon = swe.calc_ut(jd_ut, swe.MOON, flags)[0][0] % 360.0
    return sun, moon


def sun_moon_events(jd_start: float, lat: float, lon: float):
    geopos = (lon, lat, 0.0)
    flags = swe.CALC_RISE | swe.BIT_DISC_CENTER
    _, sunrise = swe.rise_trans(jd_start, swe.SUN, flags, geopos)
    _, sunset = swe.rise_trans(sunrise[0], swe.SUN, swe.CALC_SET | swe.BIT_DISC_CENTER, geopos)
    _, next_sunrise = swe.rise_trans(sunrise[0] + 0.5, swe.SUN, flags, geopos)
    try:
        _, moonrise = swe.rise_trans(sunrise[0] - 0.25, swe.MOON, flags, geopos)
        m_jd = moonrise[0]
    except Exception:
        m_jd = None
    return sunrise[0], sunset[0], next_sunrise[0], m_jd


def find_transition(jd_start: float, target_fn, step_hours=0.25, max_hours=48.0):
    start_index = target_fn(jd_start)
    jd = jd_start
    step = step_hours / 24.0
    hours_scanned = 0.0
    prev_jd = jd
    while hours_scanned < max_hours:
        jd += step
        hours_scanned += step_hours
        if target_fn(jd) != start_index:
            lo, hi = prev_jd, jd
            for _ in range(35):
                mid = (lo + hi) / 2.0
                if target_fn(mid) == start_index:
                    lo = mid
                else:
                    hi = mid
            return hi
        prev_jd = jd
    return None


@dataclass
class PanchangResult:
    date_local: str
    sunrise: str
    sunset: str
    next_sunrise: str
    moonrise: str | None
    tithi_name: str
    tithi_end: str | None
    tithi_next_name: str
    nakshatra_name: str
    nakshatra_end: str | None
    nakshatra_next_name: str
    yoga_name: str
    yoga_end: str | None
    yoga_next_name: str
    karana_name: str
    karana_end: str | None
    karana_next_name: str


def compute_panchang(local_date: date, lat: float, lon: float) -> PanchangResult:
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    noon_local = datetime(local_date.year, local_date.month, local_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25
    jd_sunrise, jd_sunset, jd_next_sunrise, jd_moonrise = sun_moon_events(jd_approx, lat, lon)

    def tithi_index(jd):
        s, m = sidereal_longitudes(jd)
        return int(((m - s) % 360.0) / 12.0)

    def nak_index(jd):
        _, m = sidereal_longitudes(jd)
        return int((m % 360.0) / (360.0 / 27.0))

    def yoga_index(jd):
        s, m = sidereal_longitudes(jd)
        return int(((s + m) % 360.0) / (360.0 / 27.0))

    def karana_index(jd):
        s, m = sidereal_longitudes(jd)
        return int(((m - s) % 360.0) / 6.0)

    def get_karana_name(idx):
        idx = idx % 60
        if idx in KARANA_FIXED:
            return KARANA_FIXED[idx]
        return KARANA_NAMES_MOVABLE[(idx - 1) % 7]

    # Evaluate all Panchang elements as per Udaya Tithi (at Sunrise)
    t_idx = tithi_index(jd_sunrise)
    t_end = find_transition(jd_sunrise, tithi_index)

    n_idx = nak_index(jd_sunrise)
    n_end = find_transition(jd_sunrise, nak_index)

    y_idx = yoga_index(jd_sunrise)
    y_end = find_transition(jd_sunrise, yoga_index)

    k_idx = karana_index(jd_sunrise)
    k_end = find_transition(jd_sunrise, karana_index)

    def fmt(jd):
        return jd_to_local(jd).strftime("%Y-%m-%d %I:%M:%S %p") if jd else None

    return PanchangResult(
        date_local=local_date.isoformat(),
        sunrise=fmt(jd_sunrise),
        sunset=fmt(jd_sunset),
        next_sunrise=fmt(jd_next_sunrise),
        moonrise=fmt(jd_moonrise),
        tithi_name=TITHI_NAMES[t_idx],
        tithi_end=fmt(t_end),
        tithi_next_name=TITHI_NAMES[(t_idx + 1) % 30],
        nakshatra_name=NAKSHATRAS[n_idx],
        nakshatra_end=fmt(n_end),
        nakshatra_next_name=NAKSHATRAS[(n_idx + 1) % 27],
        yoga_name=YOGA_NAMES[y_idx],
        yoga_end=fmt(y_end),
        yoga_next_name=YOGA_NAMES[(y_idx + 1) % 27],
        karana_name=get_karana_name(k_idx),
        karana_end=fmt(k_end),
        karana_next_name=get_karana_name(k_idx + 1),
    )


# ---------------------------------------------------------------------------
# True Solar Ingress (Sankranti) & Mantri Mandala Engine
# ---------------------------------------------------------------------------

def find_solar_ingress(target_deg: float, approx_start: date) -> datetime:
    """Finds exact moment Sun reaches a specific sidereal longitude."""
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    start_dt = datetime(approx_start.year, approx_start.month, approx_start.day, 0, 0, tzinfo=UTC)
    jd = to_jd_ut(start_dt)
    
    # 45-day scan window in 1-day increments
    for _ in range(45):
        s_long, _ = sidereal_longitudes(jd)
        s_next, _ = sidereal_longitudes(jd + 1.0)
        
        diff_curr = (s_long - target_deg) % 360.0
        diff_next = (s_next - target_deg) % 360.0
        
        # Crossed target degree
        if diff_curr > 180.0 and diff_next < 180.0 or (diff_curr <= diff_next and diff_curr < 5.0):
            lo, hi = jd, jd + 1.0
            for _ in range(35):
                mid = (lo + hi) / 2.0
                curr, _ = sidereal_longitudes(mid)
                d = (curr - target_deg) % 360.0
                if d < 180.0:
                    hi = mid
                else:
                    lo = mid
            return jd_to_local(hi)
        jd += 1.0
        
    raise ValueError(f"Could not locate Solar Ingress for {target_deg}° around {approx_start}")


def find_chaitra_shukla_pratipada(target_date: date, lat: float, lon: float) -> date:
    """Locates the Chaitra Shukla Pratipada (Udaya Tithi) governing the target date."""
    for test_year in (target_date.year, target_date.year - 1):
        start = date(test_year, 3, 1)
        for offset in range(0, 50):
            d = start + timedelta(days=offset)
            jd_sun = get_sunrise_jd(d, lat, lon)
            s_long, m_long = sidereal_longitudes(jd_sun)
            diff = (m_long - s_long) % 360.0
            
            # Sun must be near Pisces/Aries (330° to 30°) and Tithi is Shukla Pratipada (0° to 12°)
            if (s_long >= 330.0 or s_long <= 30.0) and (0.0 <= diff < 12.0):
                next_year_start = date(test_year + 1, 3, 1)
                if d <= target_date < (next_year_start + timedelta(days=45)):
                    return d
    raise ValueError(f"Could not locate Chaitra Shukla Pratipada for date: {target_date}")


def compute_mantri_mandala(for_date: date, lat: float, lon: float) -> dict:
    """
    Computes Navadhikaris using true astronomical Ingresses (Sankrantis).
    """
    new_year_day = find_chaitra_shukla_pratipada(for_date, lat, lon)
    year = new_year_day.year

    # Astronomical ingress points for governing offices
    ingresses = {
        "Raja": ("Chaitra Shukla Pratipada", new_year_day),
        "Mantri": ("Mesha Sankranti (0°)", find_solar_ingress(0.0, date(year, 4, 10)).date()),
        "Senadhipati": ("Simha Sankranti (120°)", find_solar_ingress(120.0, date(year, 8, 10)).date()),
        "Sasyadhipati": ("Karka Sankranti (90°)", find_solar_ingress(90.0, date(year, 7, 10)).date()),
        "Dhanyadhipati": ("Dhanu Sankranti (240°)", find_solar_ingress(240.0, date(year, 12, 10)).date()),
        "Meghadhipati": ("Ardra Pravesha (66°40')", find_solar_ingress(66.66667, date(year, 6, 15)).date()),
        "Rasadhipati": ("Tula Sankranti (180°)", find_solar_ingress(180.0, date(year, 10, 10)).date()),
        "Nirasadhipati": ("Makara Sankranti (270°)", find_solar_ingress(270.0, date(year + (1 if new_year_day.month > 1 else 0), 1, 10)).date()),
        "Phaladhipati": ("Mithuna Sankranti (60°)", find_solar_ingress(60.0, date(year, 6, 10)).date()),
    }

    offices = {}
    for office, (desc, d_event) in ingresses.items():
        offices[office] = {
            "lord": weekday_lord(d_event),
            "basis": desc,
            "date": d_event.isoformat()
        }

    return {
        "vikram_samvat_new_year": new_year_day.isoformat(),
        "raja": offices["Raja"]["lord"],
        "offices": offices
    }


if __name__ == "__main__":
    swe.set_ephe_path(".")
    ujjain_lat, ujjain_lon = 23.1793, 75.7849
    test_date = date(2026, 8, 16)

    print("=== Panchang for Ujjain (16 Aug 2026) ===")
    res = compute_panchang(test_date, ujjain_lat, ujjain_lon)
    for k, v in res.__dict__.items():
        print(f"  {k:20s}: {v}")

    print("\n=== Mantri Mandala (VS 2083) ===")
    mm = compute_mantri_mandala(test_date, ujjain_lat, ujjain_lon)
    for office, details in mm["offices"].items():
        print(f"  {office:15s} -> {details['lord']:8s} ({details['basis']} on {details['date']})")
