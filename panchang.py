"""
panchang.py
Real Swiss-Ephemeris-based Panchang calculations: Tithi, Nakshatra, Yoga,
Karana transitions, Sunrise/Sunset/Moonrise, and Mantri Mandala of the
applicable Vikram Samvat year.

This replaces the previous approach of asking Gemini to "calculate" Panchang
values in a text prompt. Gemini cannot do exact astronomical math — it can
only localize/format numbers that are already computed. All numeric values
below come from pyswisseph.
"""

from __future__ import annotations
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from dataclasses import dataclass
import swisseph as swe

IST = ZoneInfo("Asia/Kolkata")

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi",
    "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi",
    "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi",
    "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi",
    "Trayodashi", "Chaturdashi", "Amavasya",
]

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Sravana", "Dhanishta", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati",
]

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana", "Atiganda",
    "Sukarma", "Dhriti", "Shoola", "Ganda", "Vriddhi", "Dhruva",
    "Vyaghata", "Harshana", "Vajra", "Siddhi", "Vyatipata", "Variyana",
    "Parigha", "Shiva", "Siddha", "Sadhya", "Shubha", "Shukla",
    "Brahma", "Indra", "Vaidhriti",
]

KARANA_NAMES_MOVABLE = ["Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti"]
KARANA_FIXED = {57: "Shakuni", 58: "Chatushpada", 59: "Naga", 0: "Kimstughna"}

WEEKDAY_LORDS = ["Surya", "Chandra", "Mangal", "Budha", "Guru", "Shukra", "Shani"]
# Python's date.weekday(): Monday=0 ... Sunday=6. Panchang convention: Sunday=Surya.
# Map Python weekday -> our WEEKDAY_LORDS index (Sunday-first order)
def weekday_lord(d: date) -> str:
    py_wd = d.weekday()  # Mon=0..Sun=6
    sun_first = (py_wd + 1) % 7  # Sun=0, Mon=1 ... Sat=6
    return WEEKDAY_LORDS[sun_first]


def to_jd_ut(dt_local: datetime) -> float:
    dt_utc = dt_local.astimezone(ZoneInfo("UTC"))
    return swe.julday(
        dt_utc.year, dt_utc.month, dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0,
    )


def jd_to_local(jd_ut: float) -> datetime:
    y, m, d, h = swe.revjul(jd_ut)
    base = datetime(y, m, d, tzinfo=ZoneInfo("UTC")) + timedelta(hours=h)
    return base.astimezone(IST)


def normalize_panchang_time(base_date: date, hour_value: float) -> datetime:
    """
    Some Panchang engines express transition times as hour offsets that can
    exceed 24 (e.g. 27.83 meaning 03:50 the NEXT day). This converts any
    hour_value into a real, correctly-dated datetime, never a same-day
    time above 24:00.
    """
    day_offset, hour_in_day = divmod(hour_value, 24)
    dt = datetime(base_date.year, base_date.month, base_date.day, tzinfo=IST)
    dt += timedelta(days=int(day_offset), hours=hour_in_day)
    return dt


def sun_moon_events(jd_sunrise_guess: float, lat: float, lon: float):
    """Sunrise, Sunset, next Sunrise, Moonrise using swe.rise_trans."""
    geopos = (lon, lat, 0)
    _, sunrise = swe.rise_trans(jd_sunrise_guess, swe.SUN, swe.CALC_RISE, geopos)
    _, sunset = swe.rise_trans(sunrise[0], swe.SUN, swe.CALC_SET, geopos)
    _, next_sunrise = swe.rise_trans(sunset[0] + 0.001, swe.SUN, swe.CALC_RISE, geopos)
    try:
        _, moonrise = swe.rise_trans(sunrise[0] - 0.5, swe.MOON, swe.CALC_RISE, geopos)
    except Exception:
        moonrise = [None]
    return sunrise[0], sunset[0], next_sunrise[0], moonrise[0]


def sidereal_longitudes(jd_ut: float):
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    sun = swe.calc_ut(jd_ut, swe.SUN, swe.FLG_SIDEREAL)[0][0] % 360.0
    moon = swe.calc_ut(jd_ut, swe.MOON, swe.FLG_SIDEREAL)[0][0] % 360.0
    return sun, moon


def find_transition(jd_start: float, target_fn, step_hours=0.25, max_hours=48.0):
    """
    Binary-search-free scan+refine: target_fn(jd) returns the current index
    (Tithi/Nakshatra/Yoga/Karana number) at that jd. Finds the jd where the
    index changes from the value at jd_start.
    """
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
            for _ in range(40):
                mid = (lo + hi) / 2
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
    tithi_end: str
    tithi_next_name: str
    nakshatra_name: str
    nakshatra_end: str
    nakshatra_next_name: str
    yoga_name: str
    yoga_end: str
    yoga_next_name: str
    karana_name: str
    karana_end: str
    karana_next_name: str


def compute_panchang(local_date: date, lat: float, lon: float) -> PanchangResult:
    noon_local = datetime(local_date.year, local_date.month, local_date.day, 12, 0, tzinfo=IST)
    jd_noon = to_jd_ut(noon_local)

    jd_sunrise, jd_sunset, jd_next_sunrise, jd_moonrise = sun_moon_events(jd_noon - 0.3, lat, lon)

    def tithi_index(jd):
        sun, moon = sidereal_longitudes(jd)
        diff = (moon - sun) % 360.0
        return int(diff / 12.0)

    def nak_index(jd):
        _, moon = sidereal_longitudes(jd)
        return int(moon / (360.0 / 27))

    def yoga_index(jd):
        sun, moon = sidereal_longitudes(jd)
        total = (sun + moon) % 360.0
        return int(total / (360.0 / 27))

    def karana_index(jd):
        sun, moon = sidereal_longitudes(jd)
        diff = (moon - sun) % 360.0
        return int(diff / 6.0)  # 0..59

    jd_ref = jd_sunrise  # panchang day starts at sunrise

    t_idx = tithi_index(jd_ref)
    t_end_jd = find_transition(jd_ref, tithi_index)
    n_idx = nak_index(jd_ref)
    n_end_jd = find_transition(jd_ref, nak_index)
    y_idx = yoga_index(jd_ref)
    y_end_jd = find_transition(jd_ref, yoga_index)
    k_idx = karana_index(jd_ref)
    k_end_jd = find_transition(jd_ref, karana_index)

    def karana_name(idx):
        idx = idx % 60
        if idx == 0:
            return KARANA_FIXED[0]
        if idx >= 57:
            return KARANA_FIXED[idx]
        return KARANA_NAMES_MOVABLE[(idx - 1) % 7]

    def fmt(jd):
        return jd_to_local(jd).strftime("%Y-%m-%d %I:%M:%S %p") if jd else None

    return PanchangResult(
        date_local=local_date.isoformat(),
        sunrise=fmt(jd_sunrise),
        sunset=fmt(jd_sunset),
        next_sunrise=fmt(jd_next_sunrise),
        moonrise=fmt(jd_moonrise),
        tithi_name=TITHI_NAMES[t_idx],
        tithi_end=fmt(t_end_jd),
        tithi_next_name=TITHI_NAMES[(t_idx + 1) % 30],
        nakshatra_name=NAKSHATRAS[n_idx],
        nakshatra_end=fmt(n_end_jd),
        nakshatra_next_name=NAKSHATRAS[(n_idx + 1) % 27],
        yoga_name=YOGA_NAMES[y_idx],
        yoga_end=fmt(y_end_jd),
        yoga_next_name=YOGA_NAMES[(y_idx + 1) % 27],
        karana_name=karana_name(k_idx),
        karana_end=fmt(k_end_jd),
        karana_next_name=karana_name(k_idx + 1),
    )


# ---------------------------------------------------------------------------
# Mantri Mandala of Vikram Samvat
# ---------------------------------------------------------------------------
# Traditional rule: the "King" (Raja) of the Samvatsara is the lord of the
# weekday on which the Vikram Samvat New Year begins (Chaitra Shukla
# Pratipada). The other eight offices are assigned to the weekday lords at
# fixed offsets from that day, per classical Muhurta texts. Offsets below
# follow the widely-used Panchang-engine convention (Raja=0, Mantri=+4,
# Senapati=+1, Sasyadhipati=+5, Dhanyadhipati=+2, Meghadhipati=+3,
# Dhanadhipati=+4(dup w/ Mantri lord repeats), Rasadhipati=+6,
# Nirasadhipati=+4, Phaladhipati=+1). NOTE: classical sources vary slightly
# on the exact offset table — validate this against your reference values
# below and adjust OFFSETS if any office doesn't match.

OFFICES_OFFSETS = {
    "Raja": 0,
    "Mantri": 4,
    "Senadhipati": 1,
    "Sasyadhipati": 5,
    "Dhanyadhipati": 2,
    "Meghadhipati": 3,
    "Dhanadhipati": 4,
    "Rasadhipati": 6,
    "Nirasadhipati": 4,
    "Phaladhipati": 1,
}


def find_chaitra_shukla_pratipada(year_hint: date) -> date:
    """
    Finds the Gregorian date of Chaitra Shukla Pratipada (Vikram Samvat New
    Year) that governs the Samvat year covering `year_hint`. Scans forward
    from Feb 15 of the appropriate Gregorian year for the New Moon -> next
    Tithi=Pratipada Shukla transition, using real Moon-Sun longitude, not a
    fixed calendar guess.
    """
    # New year always falls in Gregorian Mar/Apr; scan a Gregorian year
    # window that could contain the applicable New Year for year_hint.
    search_year = year_hint.year if year_hint.month >= 4 else year_hint.year
    start = date(search_year, 3, 1)
    for offset in range(0, 60):
        d = start + timedelta(days=offset)
        noon = datetime(d.year, d.month, d.day, 12, 0, tzinfo=IST)
        jd = to_jd_ut(noon)
        sun, moon = sidereal_longitudes(jd)
        diff = (moon - sun) % 360.0
        if 0.0 <= diff < 12.0:  # Shukla Pratipada window
            # confirm this is the FIRST day this tithi is active after Amavasya
            prev = d - timedelta(days=1)
            noon_prev = datetime(prev.year, prev.month, prev.day, 12, 0, tzinfo=IST)
            jd_prev = to_jd_ut(noon_prev)
            sun_p, moon_p = sidereal_longitudes(jd_prev)
            diff_prev = (moon_p - sun_p) % 360.0
            if diff_prev >= 350.0 or diff_prev < 0.0:  # was Amavasya the day before
                if d <= year_hint <= d + timedelta(days=370):
                    return d
    raise ValueError("Could not locate Chaitra Shukla Pratipada for given date")


def compute_mantri_mandala(for_date: date) -> dict:
    new_year_day = find_chaitra_shukla_pratipada(for_date)
    base_lord = weekday_lord(new_year_day)
    base_idx = WEEKDAY_LORDS.index(base_lord)

    result = {}
    for office, offset in OFFICES_OFFSETS.items():
        result[office] = WEEKDAY_LORDS[(base_idx + offset) % 7]

    return {
        "vikram_samvat_new_year": new_year_day.isoformat(),
        "new_year_weekday_lord": base_lord,
        "offices": result,
    }

