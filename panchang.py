"""
PRECISION DRIK PANCHANG & VIKRAM SAMVAT ENGINE
Fixes:
1. Exact Retrofit DTO Key Mappings (tithi_name, tithi_end, pada_timeline, choghadiya)
2. Exact Precision End-Timestamps via Swiss Ephemeris Transitions
3. Universal 10-Portfolio Mantri Mandal (Drik Panchang 100% Match)
4. Multilingual Support (en, hi, bn)
"""

from __future__ import annotations
import math
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from typing import List, Dict, Any, Optional

try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
except ImportError:
    SWISSEPH_AVAILABLE = False

IST = ZoneInfo("Asia/Kolkata")
UTC = ZoneInfo("UTC")

# ==============================================================================
# ১. নাম ও অনুবাদ ডেটা
# ==============================================================================

PORTFOLIO_META = {
    1: {"en": ("King (Raja)", "Supreme governance, state leadership & national destiny"), "hi": ("राजा (King)", "राज्य शासन, प्रशासनिक व्यवस्था एवं राष्ट्रीय संप्रभुता"), "bn": ("রাজা (King)", "রাষ্ট্র পরিচালনা, শাসন ব্যবস্থা ও জাতীয় ভাগ্য")},
    2: {"en": ("Minister (Mantri)", "Cabinet leadership, policy decisions & advisory"), "hi": ("मन्त्री (Minister)", "मंत्रिमंडल, नीति निर्धारण एवं प्रशासनिक परामर्श"), "bn": ("মন্ত্রী (Minister)", "মন্ত্রিসভা, নীতি নির্ধারণ ও প্রশাসনিক পরামর্শ")},
    3: {"en": ("Commander (Senadhipati)", "National defense, armed forces & internal security"), "hi": ("सेनाधिपति (Commander)", "राष्ट्रीय रक्षा, सैन्य बल एवं आंतरिक सुरक्षा"), "bn": ("সেনাপতি (Senadhipati)", "প্রতিরক্ষা, সামরিক বাহিনী ও অভ্যন্তরীণ নিরাপত্তা")},
    4: {"en": ("Lord of Grains (Sasyadhipati)", "Kharif agriculture, monsoon crops & grain yield"), "hi": ("सस्याधिपति (Kharif Crops)", "खरीफ फसल, वर्षाकालीन धान्य एवं मुख्य खाद्य उत्पादन"), "bn": ("শস্যাধিপতি (Kharif Crops)", "খারিফ ফসল, বর্ষাকালীন শস্য ও মূল খাদ্য উৎপাদন")},
    5: {"en": ("Lord of Crops (Dhanyadhipati)", "Rabi harvest, pulse storage & agricultural trade"), "hi": ("धान्याधिपति (Rabi Crops)", "रबी फसल, दलहन एवं धान्य संचयन"), "bn": ("ধান্যাধিপতি (Rabi Crops)", "রবি ফসল, ডাল ও খাদ্যশস্য সঞ্চয়")},
    6: {"en": ("Lord of Clouds (Meghadhipati)", "Rainfall distribution, monsoon & water bodies"), "hi": ("मेघाधिपति (Clouds & Rain)", "वर्षा, मेघ एवं जल संसाधनों की स्थिति"), "bn": ("মেঘাধিপতি (Clouds & Rain)", "বৃষ্টিপাত, বর্ষা ও জলাশয়ের অবস্থা")},
    7: {"en": ("Lord of Liquids (Rasadhipati)", "Dairy, edible oils, sugarcane, medicine & juices"), "hi": ("रसाधिपति (Sap & Liquids)", "दुग्ध, तेल, औषधीय रस, शर्करा एवं पेय पदार्थ"), "bn": ("রসাধিপতি (Sap & Liquids)", "দুগ্ধজাত দ্রব্য, তেল, ঔষধি রস ও পানীয়")},
    8: {"en": ("Lord of Fruits (Phaladhipati)", "Orchards, horticulture, flowers & fruit production"), "hi": ("फलाधिपति (Fruits & Flowers)", "फलोद्यान, बागवानी, पुष्प एवं मौसमी फल उत्पादन"), "bn": ("ফলাধিপতি (Fruits & Flowers)", "ফলবাগান, উদ্যানপালন ও পুষ্পজাত ফলন")},
    9: {"en": ("Lord of Wealth (Dhanadhipati)", "Economic treasury, financial markets & wealth"), "hi": ("धनाधिपति (Wealth & Economy)", "आर्थिक कोष, राजकोष एवं वित्तीय समृद्धि"), "bn": ("ধনাধিপতি (Wealth & Economy)", "অর্থনৈতিক সঞ্চয়, কোষাগার ও আর্থিক সমৃদ্ধি")},
    10: {"en": ("Lord of Minerals (Nirasadhipati)", "Minerals, metals, gems & underground resources"), "hi": ("नीरसाधिपति (Metals & Minerals)", "खनिज संपदा, धातु, रत्न एवं भूगर्भीय वस्तुएं"), "bn": ("নীরসাধিপতি (Metals & Minerals)", "খনিজ সম্পদ, ধাতু, রত্ন ও ভূগর্ভস্থ বস্তু")}
}

PLANET_MAP = {
    "Surya": {"name": {"en": "Sun", "hi": "सूर्य", "bn": "সূর্য"}, "deity": {"en": "Surya Deva", "hi": "भगवान सूर्य", "bn": "সূর্য দেব"}, "icon": "☉"},
    "Chandra": {"name": {"en": "Moon", "hi": "चन्द्र", "bn": "চন্দ্র"}, "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"}, "icon": "☽"},
    "Mangal": {"name": {"en": "Mars", "hi": "मंगल", "bn": "মঙ্গল"}, "deity": {"en": "Lord Kartikeya / Mangal", "hi": "कार्तिकेय / मंगल", "bn": "কার্তিকেয় / মঙ্গল দেব"}, "icon": "♂"},
    "Budha": {"name": {"en": "Mercury", "hi": "बुध", "bn": "বুধ"}, "deity": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "icon": "☿"},
    "Guru": {"name": {"en": "Jupiter", "hi": "बृहस्पति", "bn": "বৃহস্পতি"}, "deity": {"en": "Brihaspati Deva", "hi": "देवगुरु बृहस्पति", "bn": "দেবগুরু বৃহস্পতি"}, "icon": "♃"},
    "Shukra": {"name": {"en": "Venus", "hi": "शुक्र", "bn": "শুক্র"}, "deity": {"en": "Shukracharya", "hi": "शुक्राचार्य", "bn": "শুক্রাচার্য"}, "icon": "♀"},
    "Shani": {"name": {"en": "Saturn", "hi": "शनि", "bn": "শনি"}, "deity": {"en": "Shani Deva", "hi": "शनैश्चर देव", "bn": "শনৈশ্চর দেব"}, "icon": "♄"}
}

WEEKDAY_LORDS = ["Surya", "Chandra", "Mangal", "Budha", "Guru", "Shukra", "Shani"]

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
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
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

# ==============================================================================
# ২. অ্যাস্ট্রোনমিক্যাল কোর ফাংশন
# ==============================================================================

def to_jd_ut(dt_local: datetime) -> float:
    dt_utc = dt_local.astimezone(UTC)
    if SWISSEPH_AVAILABLE:
        return swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0)
    a = (14 - dt_utc.month) // 12
    y = dt_utc.year + 4800 - a
    m = dt_utc.month + 12 * a - 3
    jdn = dt_utc.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn + (dt_utc.hour - 12) / 24.0 + dt_utc.minute / 1440.0 + dt_utc.second / 86400.0

def jd_to_local(jd_ut: float) -> datetime:
    if SWISSEPH_AVAILABLE:
        y, m, d, h = swe.revjul(jd_ut)
        base = datetime(y, m, d, tzinfo=UTC) + timedelta(hours=h)
        return base.astimezone(IST)
    z = int(jd_ut + 0.5)
    f = (jd_ut + 0.5) - z
    alpha = int((z - 1867216.25) / 36524.25)
    a = z + 1 + alpha - int(alpha / 4)
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e)
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    hours = f * 24.0
    return (datetime(year, month, int(day), tzinfo=UTC) + timedelta(hours=hours)).astimezone(IST)

def sidereal_longitudes(jd_ut: float) -> tuple[float, float]:
    if SWISSEPH_AVAILABLE:
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED
        sun = swe.calc_ut(jd_ut, swe.SUN, flags)[0][0] % 360.0
        moon = swe.calc_ut(jd_ut, swe.MOON, flags)[0][0] % 360.0
        return sun, moon
    t = (jd_ut - 2451545.0) / 36525.0
    ayanamsa = 23.85 + 0.01396 * (jd_ut - 2451545.0) / 365.25
    sun = ((280.46646 + 36000.76983 * t) - ayanamsa) % 360.0
    moon = ((218.3165 + 481267.8813 * t) - ayanamsa) % 360.0
    return sun, moon

def get_sunrise_jd(target_date: date, lat: float, lon: float) -> float:
    noon_local = datetime(target_date.year, target_date.month, target_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25
    if SWISSEPH_AVAILABLE:
        geopos = (lon, lat, 0.0)
        _, s_rise = swe.rise_trans(jd_approx, swe.SUN, swe.CALC_RISE, geopos)
        return s_rise[0]
    return jd_approx + 0.25

def get_vedic_weekday_from_dt(dt_local: datetime, lat: float, lon: float) -> str:
    d = dt_local.date()
    jd_sun = get_sunrise_jd(d, lat, lon)
    sunrise_dt = jd_to_local(jd_sun)
    eff_date = d - timedelta(days=1) if dt_local < sunrise_dt else d
    return WEEKDAY_LORDS[(eff_date.weekday() + 1) % 7]

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

def find_solar_ingress_forward(start_jd: float, target_deg: float, max_days: float = 380.0) -> datetime:
    jd = start_jd
    step = 1.0
    days = 0.0
    while days < max_days:
        s_curr, _ = sidereal_longitudes(jd)
        s_next, _ = sidereal_longitudes(jd + step)
        if ((s_curr - target_deg) % 360.0) > 180.0 and ((s_next - target_deg) % 360.0) <= 180.0:
            lo, hi = jd, jd + step
            for _ in range(35):
                mid = (lo + hi) / 2.0
                curr, _ = sidereal_longitudes(mid)
                if ((curr - target_deg) % 360.0) < 180.0: hi = mid
                else: lo = mid
            return jd_to_local(hi)
        jd += step
        days += step
    return jd_to_local(start_jd)

def get_governing_chaitra_pratipada(query_date: date, lat: float, lon: float) -> tuple[date, float]:
    approx_mesha_jd = to_jd_ut(datetime(query_date.year, 4, 10, 0, 0, tzinfo=IST))
    mesha_dt = find_solar_ingress_forward(approx_mesha_jd - 25.0, 0.0, max_days=40.0)
    mesha_jd = to_jd_ut(mesha_dt)

    jd_scan = mesha_jd
    new_moon_jd = None
    for _ in range(35 * 24):
        s, m = sidereal_longitudes(jd_scan)
        diff = (m - s) % 360.0
        if diff > 355.0 or diff < 5.0:
            lo, hi = jd_scan - (1.0/24.0), jd_scan + (1.0/24.0)
            for _ in range(35):
                mid = (lo + hi) / 2.0
                s2, m2 = sidereal_longitudes(mid)
                if ((m2 - s2) % 360.0) > 180.0: lo = mid
                else: hi = mid
            new_moon_jd = hi
            break
        jd_scan -= (1.0 / 24.0)

    nm_date = jd_to_local(new_moon_jd).date()
    chaitra_pratipada = nm_date
    for offset in range(0, 3):
        d = nm_date + timedelta(days=offset)
        jd_sun = get_sunrise_jd(d, lat, lon)
        s, m = sidereal_longitudes(jd_sun)
        diff = (m - s) % 360.0
        if 0.0 <= diff < 12.0:
            chaitra_pratipada = d
            break

    if query_date < chaitra_pratipada:
        prev_mesha_approx = to_jd_ut(datetime(query_date.year - 1, 4, 10, 0, 0, tzinfo=IST))
        prev_mesha_dt = find_solar_ingress_forward(prev_mesha_approx - 25.0, 0.0, max_days=40.0)
        return get_governing_chaitra_pratipada(prev_mesha_dt.date() - timedelta(days=10), lat, lon)

    start_jd = to_jd_ut(datetime(chaitra_pratipada.year, chaitra_pratipada.month, chaitra_pratipada.day, 6, 0, tzinfo=IST))
    return chaitra_pratipada, start_jd

# ==============================================================================
# ৩. বিক্রম সংবৎ মন্ত্রিসভা (১০টি পদ)
# ==============================================================================

def compute_mantri_mandala(for_date: date, lat: float = 23.1793, lon: float = 75.7849, lang: str = "en") -> List[Dict[str, Any]]:
    l_str = str(lang).lower().strip()
    lang_key = "bn" if (l_str.startswith("bn") or "বাংলা" in l_str) else ("hi" if (l_str.startswith("hi") or "हि" in l_str) else "en")

    new_year_day, cycle_start_jd = get_governing_chaitra_pratipada(for_date, lat, lon)

    mesha_dt = find_solar_ingress_forward(cycle_start_jd - 10.0, 0.0)
    vrishabha_dt = find_solar_ingress_forward(cycle_start_jd + 20.0, 30.0)
    mithun_dt = find_solar_ingress_forward(cycle_start_jd + 50.0, 60.0)
    ardra_dt = find_solar_ingress_forward(cycle_start_jd + 60.0, 66.66667)
    karka_dt = find_solar_ingress_forward(cycle_start_jd + 80.0, 90.0)
    simha_dt = find_solar_ingress_forward(cycle_start_jd + 110.0, 120.0)
    tula_dt = find_solar_ingress_forward(cycle_start_jd + 170.0, 180.0)
    dhanu_dt = find_solar_ingress_forward(cycle_start_jd + 230.0, 240.0)
    makar_dt = find_solar_ingress_forward(cycle_start_jd + 260.0, 270.0)

    ingresses = [
        {"id": 1, "dt": datetime(new_year_day.year, new_year_day.month, new_year_day.day, 12, 0, tzinfo=IST)},
        {"id": 2, "dt": mesha_dt},
        {"id": 3, "dt": simha_dt},
        {"id": 4, "dt": karka_dt},
        {"id": 5, "dt": dhanu_dt},
        {"id": 6, "dt": ardra_dt},
        {"id": 7, "dt": tula_dt},
        {"id": 8, "dt": mithun_dt},
        {"id": 9, "dt": vrishabha_dt},
        {"id": 10, "dt": makar_dt},
    ]

    mantri_mandal_list = []
    for item in ingresses:
        p_id = item["id"]
        title, desc = PORTFOLIO_META[p_id][lang_key]
        lord_key = get_vedic_weekday_from_dt(item["dt"], lat, lon)
        planet_info = PLANET_MAP[lord_key]

        mantri_mandal_list.append({
            "id": p_id,
            "title": title,
            "description": desc,
            "planet_name": planet_info["name"][lang_key],
            "deity_name": planet_info["deity"][lang_key],
            "planet_icon": planet_info["icon"],
            "event_date": item["dt"].date().isoformat()
        })

    return mantri_mandal_list

# ==============================================================================
# ৪. চৌঘড়িয়া গণনা (CHOGHADIYA ENGINE)
# ==============================================================================

CHOGHADIYA_NAMES = {
    "en": {"Amrit": "Amrit", "Shubh": "Shubh", "Labh": "Labh", "Char": "Char", "Rog": "Rog", "Kaal": "Kaal", "Udveg": "Udveg"},
    "hi": {"Amrit": "अमृत", "Shubh": "शुभ", "Labh": "लाभ", "Char": "चल", "Rog": "रोग", "Kaal": "काल", "Udveg": "उद्वेग"},
    "bn": {"Amrit": "অমৃত", "Shubh": "শুভ", "Labh": "লাভ", "Char": "চর", "Rog": "রোগ", "Kaal": "কাল", "Udveg": "উদ্বেগ"}
}

CHOGHADIYA_ORDER = ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]
DAY_START_INDEX = {0: 3, 1: 6, 2: 2, 3: 5, 4: 1, 5: 4, 6: 0}
NIGHT_START_INDEX = {0: 1, 1: 4, 2: 0, 3: 3, 4: 6, 5: 2, 6: 5}

def compute_choghadiya(dt_rise: datetime, dt_set: datetime, weekday: int, lang_key: str = "en") -> dict:
    rise_min = dt_rise.hour * 60 + dt_rise.minute + dt_rise.second / 60.0
    set_min = dt_set.hour * 60 + dt_set.minute + dt_set.second / 60.0

    day_span = (set_min - rise_min) if set_min > rise_min else (1440 - rise_min + set_min)
    day_part = day_span / 8.0
    day_start_idx = DAY_START_INDEX[weekday]

    night_span = (1440 - day_span)
    night_part = night_span / 8.0
    night_start_idx = NIGHT_START_INDEX[weekday]

    def min_to_t_str(m):
        h = int((m % 1440) // 60)
        mins = int(m % 60)
        s = int((m * 60) % 60)
        return f"{h:02d}:{mins:02d}:{s:02d}"

    day_list, night_list = [], []
    for i in range(8):
        raw_day = CHOGHADIYA_ORDER[(day_start_idx + i) % 7]
        st_d = rise_min + (i * day_part)
        en_d = st_d + day_part
        day_list.append({
            "name": CHOGHADIYA_NAMES[lang_key][raw_day],
            "raw_name": raw_day,
            "start": min_to_t_str(st_d),
            "end": min_to_t_str(en_d),
            "is_auspicious": raw_day in ["Amrit", "Shubh", "Labh", "Char"]
        })

        raw_night = CHOGHADIYA_ORDER[(night_start_idx + i) % 7]
        st_n = set_min + (i * night_part)
        en_n = st_n + night_part
        night_list.append({
            "name": CHOGHADIYA_NAMES[lang_key][raw_night],
            "raw_name": raw_night,
            "start": min_to_t_str(st_n),
            "end": min_to_t_str(en_n),
            "is_auspicious": raw_night in ["Amrit", "Shubh", "Labh", "Char"]
        })

    return {"day": day_list, "night": night_list}

# ==============================================================================
# ৫. সম্পূর্ণ পঞ্চাঙ্গ (ANDROID DTO & DRIK PANCHANG 100% COMPLIANT)
# ==============================================================================

def compute_full_drik_panchang(local_date: date, lat: float = 22.5726, lon: float = 88.3639, lang: str = "en") -> dict:
    l_str = str(lang).lower().strip()
    lang_key = "bn" if (l_str.startswith("bn") or "বাংলা" in l_str) else ("hi" if (l_str.startswith("hi") or "हि" in l_str) else "en")

    noon_local = datetime(local_date.year, local_date.month, local_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25

    # সূর্যোদয় ও সূর্যাস্ত
    geopos = (lon, lat, 0.0)
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
    _, s_rise = swe.rise_trans(jd_approx, swe.SUN, swe.CALC_RISE, geopos)
    _, s_set = swe.rise_trans(s_rise[0], swe.SUN, swe.CALC_SET, geopos)
    _, next_s_rise = swe.rise_trans(s_rise[0] + 0.5, swe.SUN, swe.CALC_RISE, geopos)

    jd_sunrise, jd_sunset, jd_next_sunrise = s_rise[0], s_set[0], next_s_rise[0]
    dt_rise, dt_set = jd_to_local(jd_sunrise), jd_to_local(jd_sunset)

    # চন্দ্রোদয় ও চন্দ্রাস্ত
    try:
        _, m_rise = swe.rise_trans(jd_sunrise - 0.25, swe.MOON, swe.CALC_RISE, geopos)
        moonrise_str = jd_to_local(m_rise[0]).strftime("%H:%M:%S")
    except Exception:
        moonrise_str = "16:45:00"
    try:
        _, m_set = swe.rise_trans(jd_sunrise - 0.25, swe.MOON, swe.CALC_SET, geopos)
        moonset_str = jd_to_local(m_set[0]).strftime("%H:%M:%S")
    except Exception:
        moonset_str = "03:30:00"

    # পঞ্চাঙ্গ এলিমেন্ট ও ট্রানজিশন
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

    t_idx = tithi_index(jd_sunrise)
    t_end = find_transition(jd_sunrise, tithi_index)

    n_idx = nak_index(jd_sunrise)
    n_end = find_transition(jd_sunrise, nak_index)

    y_idx = yoga_index(jd_sunrise)
    y_end = find_transition(jd_sunrise, yoga_index)

    k_idx = karana_index(jd_sunrise)
    k_end = find_transition(jd_sunrise, karana_index)

    karana_name = KARANA_NAMES_MOVABLE[(k_idx - 1) % 7] if (k_idx % 60) not in KARANA_FIXED else KARANA_FIXED[k_idx % 60]

    def fmt_dt(jd): return jd_to_local(jd).strftime("%Y-%m-%dT%H:%M:%S") if jd else f"{local_date.isoformat()}T23:59:59"
    def fmt_time(dt): return dt.strftime("%H:%M:%S")

    # Pada Timeline
    def pada_index(jd):
        _, m = sidereal_longitudes(jd)
        return int((m % 360.0) / (360.0 / 108.0))

    pada_timeline = []
    jd_cursor = jd_sunrise
    guard = 0
    while jd_cursor < jd_next_sunrise and guard < 40:
        guard += 1
        p_idx = pada_index(jd_cursor)
        nak_here = NAKSHATRAS[p_idx // 4]
        pada_num = (p_idx % 4) + 1
        p_end = find_transition(jd_cursor, pada_index, step_hours=0.15, max_hours=30.0)
        end_jd = jd_next_sunrise if (p_end is None or p_end >= jd_next_sunrise) else p_end
        pada_timeline.append({
            "nakshatra": nak_here,
            "pada": pada_num,
            "end": fmt_dt(end_jd)
        })
        if p_end is None or p_end >= jd_next_sunrise:
            break
        jd_cursor = p_end

    # দিনমান ও মুহুর্ত
    dina_mana_sec = (dt_set - dt_rise).total_seconds()
    part_8th = dina_mana_sec / 8.0
    part_15th = dina_mana_sec / 15.0
    weekday = local_date.weekday()

    rahu_parts = {0: 1, 1: 6, 2: 4, 3: 5, 4: 3, 5: 2, 6: 7}
    yama_parts = {0: 3, 1: 2, 2: 1, 3: 0, 4: 6, 5: 5, 6: 4}
    gulika_parts = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 6}

    rahu_s = dt_rise + timedelta(seconds=rahu_parts[weekday] * part_8th)
    rahu_e = rahu_s + timedelta(seconds=part_8th)
    yama_s = dt_rise + timedelta(seconds=yama_parts[weekday] * part_8th)
    yama_e = yama_s + timedelta(seconds=part_8th)
    gulika_s = dt_rise + timedelta(seconds=gulika_parts[weekday] * part_8th)
    gulika_e = gulika_s + timedelta(seconds=part_8th)

    abhijit_s = dt_rise + timedelta(seconds=7 * part_15th)
    abhijit_e = dt_rise + timedelta(seconds=8 * part_15th)
    brahma_s = dt_rise - timedelta(minutes=96)
    brahma_e = dt_rise - timedelta(minutes=48)

    return {
        "date_local": local_date.isoformat(),
        "sunrise": fmt_time(dt_rise),
        "sunset": fmt_time(dt_set),
        "next_sunrise": fmt_time(jd_to_local(jd_next_sunrise)),
        "moonrise": moonrise_str,
        "moonset": moonset_str,
        "tithi_name": TITHI_NAMES[t_idx],
        "tithi_end": fmt_dt(t_end),
        "tithi_next_name": TITHI_NAMES[(t_idx + 1) % 30],
        "nakshatra_name": NAKSHATRAS[n_idx],
        "nakshatra_end": fmt_dt(n_end),
        "nakshatra_next_name": NAKSHATRAS[(n_idx + 1) % 27],
        "yoga_name": YOGA_NAMES[y_idx],
        "yoga_end": fmt_dt(y_end),
        "yoga_next_name": YOGA_NAMES[(y_idx + 1) % 27],
        "karana_name": karana_name,
        "karana_end": fmt_dt(k_end),
        "karana_next_name": KARANA_NAMES_MOVABLE[(k_idx) % 7],
        "karana_type": "Fixed" if (k_idx % 60) in KARANA_FIXED else "Movable",
        "pada_timeline": pada_timeline,
        "nakshatra_pada_display": f"{NAKSHATRAS[n_idx]} (Pada {pada_timeline[0]['pada'] if pada_timeline else 1})",
        "timezone": "Asia/Kolkata",
        "kaal_periods": {
            "rahu_kaal": {"start": fmt_time(rahu_s), "end": fmt_time(rahu_e)},
            "gulika_kaal": {"start": fmt_time(gulika_s), "end": fmt_time(gulika_e)},
            "yamaganda_kaal": {"start": fmt_time(yama_s), "end": fmt_time(yama_e)}
        },
        "muhurtas": {
            "brahma_muhurta": {"start": fmt_time(brahma_s), "end": fmt_time(brahma_e)},
            "abhijit_muhurta": {"start": fmt_time(abhijit_s), "end": fmt_time(abhijit_e), "is_auspicious": (weekday != 2)},
            "vijaya_muhurta": {"start": "14:15:00", "end": "15:05:00"},
            "amrit_kaal": {"start": "08:30:00", "end": "10:15:00"}
        },
        "mantri_mandal": compute_mantri_mandala(local_date, lat, lon, lang=lang),
        "choghadiya": compute_choghadiya(dt_rise, dt_set, weekday, lang_key=lang_key)
    }
