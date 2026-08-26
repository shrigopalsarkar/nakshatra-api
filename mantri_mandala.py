"""
Mantri Mandala (Varshaphal / Tajik Council of Ministers) calculator.

Basis:
- Sidereal zodiac, Lahiri ayanamsa (the most widely used standard in
  Indian panchangs and by the Government of India / Indian Astronomical
  Ephemeris).
- Solar ingress (sankranti) times computed from true geocentric solar
  longitude via Swiss Ephemeris — accurate to within seconds for any
  date roughly 1800-2200 CE without special handling, and centuries
  further with only a hardware/precision limit (not a "wrong era"
  limit like polynomial ayanamsa approximations have).
- Chaitra Shukla Pratipada (Vikram Samvat new year) found via true
  lunar-solar tithi calculation, not a fixed calendar date.

IMPORTANT ON "100% ACCURATE":
No two panchang-making traditions agree on every rule (which sankranti
governs which minister varies by text; ayanamsa choice varies by
publisher). This code commits to ONE well-documented convention
(Tajik Neelakanthi-style assignment, Lahiri ayanamsa) and computes it
correctly and consistently. If you follow a different published
panchang, compare a few dates against it and adjust PORTFOLIO_SANKRANTI
mapping below if needed -- that mapping is a convention, not a physics
constant.
"""

import swisseph as swe
from datetime import datetime, timedelta, date, timezone
from typing import List, Dict, Any, Tuple

# ---------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------

IST = timezone(timedelta(hours=5, minutes=30))
swe.set_sid_mode(swe.SIDM_LAHIRI)  # standard Lahiri ayanamsa

SUN = swe.SUN

PLANET_MAP = {
    "sun": {"name": {"en": "Sun", "hi": "सूर्य", "bn": "সূর্য"}, "deity": {"en": "Surya", "hi": "सूर्य", "bn": "সূর্য"}, "icon": "☀️"},
    "moon": {"name": {"en": "Moon", "hi": "चन्द्र", "bn": "চন্দ্র"}, "deity": {"en": "Chandra", "hi": "चन्द्र", "bn": "চন্দ্র"}, "icon": "🌙"},
    "mars": {"name": {"en": "Mars", "hi": "मंगल", "bn": "মঙ্গল"}, "deity": {"en": "Mangal", "hi": "मंगल", "bn": "মঙ্গল"}, "icon": "♂️"},
    "mercury": {"name": {"en": "Mercury", "hi": "बुध", "bn": "বুধ"}, "deity": {"en": "Budh", "hi": "बुध", "bn": "বুধ"}, "icon": "☿"},
    "jupiter": {"name": {"en": "Jupiter", "hi": "गुरु", "bn": "বৃহস্পতি"}, "deity": {"en": "Guru", "hi": "गुरु", "bn": "বৃহস্পতি"}, "icon": "♃"},
    "venus": {"name": {"en": "Venus", "hi": "शुक्र", "bn": "শুক্র"}, "deity": {"en": "Shukra", "hi": "शुक्र", "bn": "শুক্র"}, "icon": "♀️"},
    "saturn": {"name": {"en": "Saturn", "hi": "शनि", "bn": "শনি"}, "deity": {"en": "Shani", "hi": "शनि", "bn": "শনি"}, "icon": "♄"},
}

# Weekday (as ruled by sunrise-to-sunrise vedic day) -> planet lord
WEEKDAY_LORD = ["sun", "moon", "mars", "mercury", "jupiter", "venus", "saturn"]  # Sun=0 .. Sat=6

PORTFOLIO_META = {
    1:  {"en": ("King", "Raja - governs the overall year"), "hi": ("राजा", "वर्ष का प्रमुख शासक"), "bn": ("রাজা", "বর্ষের প্রধান শাসক")},
    2:  {"en": ("Minister", "Mantri - governs policy and administration"), "hi": ("मंत्री", "नीति एवं प्रशासन का कारक"), "bn": ("মন্ত্রী", "নীতি ও প্রশাসনের কারক")},
    3:  {"en": ("Commander-in-Chief", "Senapati - governs conflict, war, security"), "hi": ("सेनापति", "युद्ध एवं सुरक्षा का कारक"), "bn": ("সেনাপতি", "যুদ্ধ ও নিরাপত্তার কারক")},
    4:  {"en": ("Grain Lord", "Sasyadhipati - governs crop yield"), "hi": ("सस्याधिपति", "फसल उत्पादन का कारक"), "bn": ("সস্যাধিপতি", "ফসল উৎপাদনের কারক")},
    5:  {"en": ("Cereal Lord", "Dhanyadhipati - governs grain/food supply"), "hi": ("धान्याधिपति", "अन्न आपूर्ति का कारक"), "bn": ("ধান্যাধিপতি", "অন্ন সরবরাহের কারক")},
    6:  {"en": ("Cloud Lord", "Meghadhipati - governs rainfall"), "hi": ("मेघाधिपति", "वर्षा का कारक"), "bn": ("মেঘাধিপতি", "বৃষ্টিপাতের কারক")},
    7:  {"en": ("Essence Lord", "Rasadhipati - governs liquids/prices"), "hi": ("रसाधिपति", "रस/मूल्य का कारक"), "bn": ("রসাধিপতি", "রস/মূল্যের কারক")},
    8:  {"en": ("Fruit Lord", "Phaladhipati - governs fruit yield"), "hi": ("फलाधिपति", "फल उत्पादन का कारक"), "bn": ("ফলাধিপতি", "ফল উৎপাদনের কারক")},
    9:  {"en": ("Wealth Lord", "Dhanadhipati - governs wealth/economy"), "hi": ("धनाधिपति", "अर्थव्यवस्था का कारक"), "bn": ("ধনাধিপতি", "অর্থনীতির কারক")},
    10: {"en": ("Sap/Moisture Lord", "Neerasadhipati - governs residual moisture/drought"), "hi": ("नीरसाधिपति", "शुष्कता/नमी का कारक"), "bn": ("নীরসাধিপতি", "শুষ্কতা/আর্দ্রতার কারক")},
}

# Sidereal longitude (0=Aries start) at which each ministry's governing
# ingress happens. id 6 (Meghadhipati) uses Ardra nakshatra entry
# (66*40' = 66.6667 deg), not a rashi sankranti -- this is the standard
# Tajik-system distinction between rashi and nakshatra based offices.
PORTFOLIO_SANKRANTI = {
    2: 0.0,        # Mesha (Aries) sankranti -> Mantri
    3: 120.0,      # Simha (Leo) sankranti -> Senapati
    4: 90.0,       # Karka (Cancer) sankranti -> Sasyadhipati
    5: 240.0,      # Dhanu (Sagittarius) sankranti -> Dhanyadhipati
    6: 66.66667,   # Ardra nakshatra entry -> Meghadhipati
    7: 180.0,      # Tula (Libra) sankranti -> Rasadhipati
    8: 60.0,       # Mithuna (Gemini) sankranti -> Phaladhipati
    9: 300.0,      # Kumbha (Aquarius) sankranti -> Dhanadhipati
    10: 270.0,     # Makara (Capricorn) sankranti -> Neerasadhipati
}


# ---------------------------------------------------------------------
# Core astronomy helpers
# ---------------------------------------------------------------------

def _jd_ut(dt_utc: datetime) -> float:
    return swe.julday(dt_utc.year, dt_utc.month, dt_utc.day,
                       dt_utc.hour + dt_utc.minute / 60 + dt_utc.second / 3600)


def sidereal_sun_longitude(jd_ut: float) -> float:
    """True geocentric sidereal longitude of the Sun (Lahiri), 0-360."""
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
    res, _ = swe.calc_ut(jd_ut, SUN, flags)
    return res[0] % 360.0


def find_solar_ingress(jd_search_start: float, target_lon: float) -> datetime:
    """
    Find the exact UTC moment the Sun's sidereal longitude crosses
    target_lon, searching forward from jd_search_start.
    Uses coarse daily scan + bisection for sub-second precision.
    Handles the 360->0 wraparound correctly.
    """
    def angle_diff(lon):
        # signed distance from target, in range (-180, 180]
        d = (lon - target_lon + 180.0) % 360.0 - 180.0
        return d

    # Coarse scan: sun moves ~0.9-1.02 deg/day, so daily steps cannot skip a crossing
    step = 1.0
    jd = jd_search_start
    prev_diff = angle_diff(sidereal_sun_longitude(jd))
    max_days = 400  # more than a full solar year of safety margin
    for _ in range(max_days):
        jd_next = jd + step
        diff_next = angle_diff(sidereal_sun_longitude(jd_next))
        if prev_diff <= 0.0 < diff_next or (prev_diff < 0.0 <= diff_next):
            # crossing happened in [jd, jd_next); bisect
            lo, hi = jd, jd_next
            lo_diff = prev_diff
            for _ in range(60):  # converges far past sub-second
                mid = (lo + hi) / 2
                mid_diff = angle_diff(sidereal_sun_longitude(mid))
                if (lo_diff <= 0.0) == (mid_diff <= 0.0):
                    lo, lo_diff = mid, mid_diff
                else:
                    hi = mid
                if hi - lo < 1e-8:
                    break
            jd_hit = (lo + hi) / 2
            y, m, d, h = swe.revjul(jd_hit)
            base = datetime(y, m, d, tzinfo=timezone.utc)
            return base + timedelta(hours=h)
        jd, prev_diff = jd_next, diff_next
    raise RuntimeError(f"Could not find solar ingress to {target_lon} deg within {max_days} days")


def get_sunrise_utc(for_date: date, lat: float, lon: float) -> datetime:
    """Sunrise (UTC) for given civil date at given location."""
    jd0 = swe.julday(for_date.year, for_date.month, for_date.day, 0.0)
    geopos = (lon, lat, 0.0)
    res_flag, tret = swe.rise_trans(jd0, SUN, swe.CALC_RISE, geopos, 0.0, 0.0, swe.FLG_SWIEPH)
    if res_flag != 0:
        raise RuntimeError("Sunrise calculation failed")
    y, m, d, h = swe.revjul(tret[0])
    base = datetime(y, m, d, tzinfo=timezone.utc)
    return base + timedelta(hours=h)


def get_vedic_weekday_lord(dt_utc: datetime, lat: float, lon: float) -> str:
    """
    Vedic day boundary is sunrise-to-sunrise. Given an event's UTC datetime,
    determine which sunrise-bounded day it falls in and return that
    weekday's planetary lord.
    """
    local_civil_date = dt_utc.astimezone(IST).date()
    sunrise_today = get_sunrise_utc(local_civil_date, lat, lon)
    if dt_utc < sunrise_today:
        eff_date = local_civil_date - timedelta(days=1)
    else:
        eff_date = local_civil_date
    # Python weekday(): Mon=0..Sun=6 -> convert to Sun=0..Sat=6
    py_wd = eff_date.weekday()
    sun0_wd = (py_wd + 1) % 7
    return WEEKDAY_LORD[sun0_wd]


def get_chaitra_shukla_pratipada(year_ce: int, lat: float, lon: float) -> Tuple[date, float]:
    """
    Find Chaitra Shukla Pratipada (Vikram Samvat New Year) for the given
    Gregorian year, using true tithi (Sun-Moon elongation) computation.
    Returns (civil_date, jd_ut of the moment tithi 1 begins on/after
    Mesha-adjacent search window).
    Search window: mid-March to mid-April, where this new year always
    falls (Amanta/Purnimanta Chaitra shukla paksha).
    """
    # Search window: Mar 10 - Apr 25 covers all historical/ future drift
    # for centuries around present era.
    start = datetime(year_ce, 3, 10, tzinfo=timezone.utc)
    jd = _jd_ut(start)
    step = 0.5  # half-day steps; tithi changes slower than this resolves safely

    def tithi_index(jd_ut):
        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
        moon = swe.calc_ut(jd_ut, swe.MOON, flags)[0][0]
        sun = swe.calc_ut(jd_ut, swe.SUN, flags)[0][0]
        elong = (moon - sun) % 360.0
        return int(elong // 12.0) + 1  # 1..30

    prev_t = tithi_index(jd)
    for _ in range(120):  # ~60 days of half-day steps
        jd_next = jd + step
        t_next = tithi_index(jd_next)
        if prev_t != t_next and t_next == 1:
            # bisect to find exact start of tithi 1
            lo, hi = jd, jd_next
            for _ in range(40):
                mid = (lo + hi) / 2
                if tithi_index(mid) == 1:
                    hi = mid
                else:
                    lo = mid
            jd_start_tithi = hi
            # The civil (sunrise-based) date on which this Pratipada is
            # observed is the sunrise day during which tithi 1 is active
            # at sunrise, per standard panchang rule.
            y, m, d, h = swe.revjul(jd_start_tithi)
            tithi_start_dt = datetime(y, m, d, tzinfo=timezone.utc) + timedelta(hours=h)
            civil_date = tithi_start_dt.astimezone(IST).date()
            sunrise = get_sunrise_utc(civil_date, lat, lon)
            if sunrise < tithi_start_dt:
                # tithi started after sunrise -> observed next day
                civil_date = civil_date + timedelta(days=1)
            return civil_date, jd_start_tithi
        jd, prev_t = jd_next, t_next
    raise RuntimeError(f"Could not locate Chaitra Shukla Pratipada for {year_ce}")


# ---------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------

def compute_mantri_mandala(for_date: date, lat: float = 23.1793, lon: float = 75.7849,
                            lang: str = "en") -> List[Dict[str, Any]]:
    """
    Compute the Mantri Mandala (Varshaphal council) governing the
    Vikram Samvat year that `for_date` falls in.

    Accurate for the current era (roughly 1900-2100 CE) using Swiss
    Ephemeris with Lahiri ayanamsa. Reliable indefinitely further out
    too, subject only to Swiss Ephemeris's own long-term file coverage
    (the bundled files cover a huge historical range) -- but ayanamsa
    convention differences among panchang publishers become more
    debatable the further from present you go, so results near "today"
    are the least ambiguous / most verifiable against published panchangs.
    """
    l_str = str(lang).lower().strip()
    lang_key = "bn" if (l_str.startswith("bn") or "বাংলা" in l_str) else (
        "hi" if (l_str.startswith("hi") or "हि" in l_str) else "en")

    # Step 1: find the Chaitra Shukla Pratipada that GOVERNS for_date.
    # If for_date is before this year's Pratipada, the governing new
    # year is the previous Gregorian year's Pratipada.
    ny_this_year, jd_this_year = get_chaitra_shukla_pratipada(for_date.year, lat, lon)
    if for_date < ny_this_year:
        new_year_day, cycle_start_jd = get_chaitra_shukla_pratipada(for_date.year - 1, lat, lon)
    else:
        new_year_day, cycle_start_jd = ny_this_year, jd_this_year

    # Step 2: for each ministry (2-10), find its governing solar ingress,
    # searching forward from the new year moment. (id 1, the King, is
    # the new year moment itself, not a solar ingress.)
    ingress_dt: Dict[int, datetime] = {}
    for p_id, target_lon in PORTFOLIO_SANKRANTI.items():
        ingress_dt[p_id] = find_solar_ingress(cycle_start_jd, target_lon)

    king_dt = datetime(new_year_day.year, new_year_day.month, new_year_day.day,
                        12, 0, tzinfo=timezone.utc)  # noon placeholder for display only

    ordered_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mantri_mandal_list = []
    for p_id in ordered_ids:
        dt_utc = king_dt if p_id == 1 else ingress_dt[p_id]
        title, desc = PORTFOLIO_META[p_id][lang_key]
        lord_key = get_vedic_weekday_lord(dt_utc, lat, lon)
        planet_info = PLANET_MAP[lord_key]

        mantri_mandal_list.append({
            "id": p_id,
            "title": title,
            "description": desc,
            "planet_name": planet_info["name"][lang_key],
            "deity_name": planet_info["deity"][lang_key],
            "planet_icon": planet_info["icon"],
            "event_date": dt_utc.astimezone(IST).date().isoformat(),
            "event_datetime_ist": dt_utc.astimezone(IST).isoformat(),
        })

    return mantri_mandal_list


if __name__ == "__main__":
    today = date.today()
    result = compute_mantri_mandala(today, lang="en")
    print(f"Mantri Mandala for cycle governing {today}:\n")
    for r in result:
        print(f"{r['id']:>2}. {r['title']:<20} {r['planet_name']:<10} ({r['deity_name']:<8}) "
              f"-> {r['event_date']}  [{r['event_datetime_ist']}]")
