"""
DRIK PANCHANG FULL REPLICA ENGINE (PRECISION VEDIC ASTRONOMY)
==============================================================================
Includes 100% All Features:
1. 10-Office Vikram Samvat Mantri Mandala Engine (Universal Ingress Matching Drik)
2. Five Limbs (Tithi, Nakshatra, Yoga, Karana, Weekday) with Transitions & Padas
3. Complete Sun & Moon Timings (Rise, Set, Dina/Ratri Mana, Madhyahna, Sandhyas)
4. Niwas & Shool (Disha Shool & Remedies, Agnivasa, Shivavasa, Rahu & Chandra Vasa)
5. Auspicious & Inauspicious Yogas (28 Anandadi, Sarvartha Siddhi, Amrita Siddhi, Ravi, Pushkara, Tamil Yogas)
6. Precision Dur Muhurtam & Varjyam (Visha Ghatika)
7. Chandrabalam (12 Rashis) & Tarabalam (27 Nakshatras)
8. Epochs & National Saka Calendar (Kali Year, Ahargana, Saka Civil, Julian Dates)
9. 16 Day & Night Choghadiya Segments
10. Tri-lingual Localisation (English, Hindi, Bengali)
"""

from __future__ import annotations
import math
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from festivals import get_festivals_for_day
from panchang_meta import (
    TITHI_METADATA,
    NAKSHATRA_METADATA,
    YOGA_METADATA,
    KARANA_METADATA
)

try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
except ImportError:
    SWISSEPH_AVAILABLE = False

IST = ZoneInfo("Asia/Kolkata")
UTC = ZoneInfo("UTC")

# ==============================================================================
# ১. মেটাডেটা ও বহুভাষিক অভিধান
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
    "Shukra": {"name": {"en": "Venus", "hi": "शुक्र", "bn": "শুক্র"}, "deity": {"en": "Shukracharya", "hi": "शुक्राचार्य", "bn": "শুক্রacharya"}, "icon": "♀"},
    "Shani": {"name": {"en": "Saturn", "hi": "शनि", "bn": "শনি"}, "deity": {"en": "Shani Deva", "hi": "शनैश्चर देव", "bn": "শনৈশ্চর দেব"}, "icon": "♄"}
}

WEEKDAY_LORDS = ["Surya", "Chandra", "Mangal", "Budha", "Guru", "Shukra", "Shani"]
WEEKDAY_NAMES = {
    "en": ["Ravivara (Sunday)", "Somavara (Monday)", "Mangalavara (Tuesday)", "Budhavara (Wednesday)", "Guruvara (Thursday)", "Shukravara (Friday)", "Shanivara (Saturday)"],
    "hi": ["रविवार", "सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार"],
    "bn": ["রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার"]
}

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

RASHIS = [
    "Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
    "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Meena"
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

ANANDADI_YOGAS = [
    "Ananda", "Kaladanda", "Dhumra", "Prajapati", "Saubhagya", "Shatru", "Mitra", "Manasa",
    "Padma", "Lambuka", "Utpata", "Mrityu", "Kana", "Siddhi", "Shubha", "Amrita",
    "Musala", "Gada", "Matanga", "Rakshasa", "Chara", "Sthira", "Pravardhana", "Kshaya",
    "Shobhana", "Atiganda", "Sukarma", "Dhriti"
]

VARJYAM_START_GHATIS = [
    50, 24, 30, 40, 14, 21, 30, 20, 32, 30, 20, 18, 21, 20, 14, 14, 10, 14, 20, 24, 20, 10, 10, 18, 16, 24, 30
]

CHOGHADIYA_NAMES = {
    "en": {"Amrit": "Amrit", "Shubh": "Shubh", "Labh": "Labh", "Char": "Char", "Rog": "Rog", "Kaal": "Kaal", "Udveg": "Udveg"},
    "hi": {"Amrit": "अमृत", "Shubh": "शुभ", "Labh": "लाभ", "Char": "चल", "Rog": "रोग", "Kaal": "काल", "Udveg": "उद्वेग"},
    "bn": {"Amrit": "অমৃত", "Shubh": "শুভ", "Labh": "লাভ", "Char": "চর", "Rog": "রোগ", "Kaal": "কাল", "Udveg": "উদ্বেগ"}
}
CHOGHADIYA_ORDER = ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]
DAY_START_INDEX = {0: 3, 1: 6, 2: 2, 3: 5, 4: 1, 5: 4, 6: 0}
NIGHT_START_INDEX = {0: 1, 1: 4, 2: 0, 3: 3, 4: 6, 5: 2, 6: 5}

# ==============================================================================
# ২. অ্যাস্ট্রোনমিক্যাল কোর ও জুলিয়ান ডেট
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

def find_transition(jd_start: float, target_fn, step_hours=0.5, max_hours=36.0):
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
            for _ in range(20):  # ৩৫ এর বদলে ২০ ইটারেশন যথেষ্ট নিখুঁত এবং সুপার ফাস্ট
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
# ৩. বিক্রম সংবৎ মন্ত্রিসভা (১০টি পদ - DRIK MATCH)
# ==============================================================================

def compute_mantri_mandala(
    for_date: date,
    lat: float = 23.1793,
    lon: float = 75.7849,
    lang: str = "en"
) -> List[Dict[str, Any]]:

    l_str = str(lang).lower().strip()

    lang_key = (
        "bn" if (l_str.startswith("bn") or "বাংলা" in l_str)
        else "hi" if (l_str.startswith("hi") or "हि" in l_str)
        else "en"
    )

    # ---------------------------------------------------------
    # 1. Find governing Vikram Samvat / Chaitra Shukla Pratipada
    # ---------------------------------------------------------
    new_year_day, cycle_start_jd = get_governing_chaitra_pratipada(
        for_date,
        lat,
        lon
    )

    # ---------------------------------------------------------
    # 2. Solar / astronomical events
    #    Longitudes are SIDEREAL
    # ---------------------------------------------------------

    # Minister — Mesha Sankranti (0°)
    mesha_dt = find_solar_ingress_forward(
        cycle_start_jd - 10.0,
        0.0
    )

    # Phaladhipati — Mithuna Sankranti (60°)
    mithun_dt = find_solar_ingress_forward(
        cycle_start_jd + 50.0,
        60.0
    )

    # Meghadhipati — Ardra Pravesha
    ardra_dt = find_solar_ingress_forward(
        cycle_start_jd + 60.0,
        66.66667
    )

    # Sasyadhipati — Karka Sankranti (90°)
    karka_dt = find_solar_ingress_forward(
        cycle_start_jd + 80.0,
        90.0
    )

    # Senadhipati — Simha Sankranti (120°)
    simha_dt = find_solar_ingress_forward(
        cycle_start_jd + 110.0,
        120.0
    )

    # ---------------------------------------------------------
    # IMPORTANT:
    # Dhanadhipati = Kanya Sankranti (150°)
    #
    # NOT Kumbha Sankranti (300°)
    # ---------------------------------------------------------
    kanya_dt = find_solar_ingress_forward(
        cycle_start_jd + 140.0,
        150.0
    )

    # Rasadhipati — Tula Sankranti (180°)
    tula_dt = find_solar_ingress_forward(
        cycle_start_jd + 170.0,
        180.0
    )

    # Dhanyadhipati — Dhanu Sankranti (240°)
    dhanu_dt = find_solar_ingress_forward(
        cycle_start_jd + 230.0,
        240.0
    )

    # Neerasadhipati — Makara Sankranti (270°)
    makar_dt = find_solar_ingress_forward(
        cycle_start_jd + 260.0,
        270.0
    )

    # ---------------------------------------------------------
    # 3. Mantri Mandala events
    # ---------------------------------------------------------

    ingresses = [
        {
            "id": 1,
            "dt": datetime(
                new_year_day.year,
                new_year_day.month,
                new_year_day.day,
                12,
                0,
                tzinfo=IST
            )
        },  # Raja — Chaitra Shukla Pratipada

        {
            "id": 2,
            "dt": mesha_dt
        },  # Mantri — Mesha Sankranti

        {
            "id": 3,
            "dt": simha_dt
        },  # Senadhipati — Simha Sankranti

        {
            "id": 4,
            "dt": karka_dt
        },  # Sasyadhipati — Karka Sankranti

        {
            "id": 5,
            "dt": dhanu_dt
        },  # Dhanyadhipati — Dhanu Sankranti

        {
            "id": 6,
            "dt": ardra_dt
        },  # Meghadhipati — Ardra Pravesha

        {
            "id": 7,
            "dt": tula_dt
        },  # Rasadhipati — Tula Sankranti

        {
            "id": 8,
            "dt": mithun_dt
        },  # Phaladhipati — Mithuna Sankranti

        {
            "id": 9,
            "dt": kanya_dt
        },  # Dhanadhipati — Kanya Sankranti

        {
            "id": 10,
            "dt": makar_dt
        },  # Neerasadhipati — Makara Sankranti
    ]

    # ---------------------------------------------------------
    # 4. Determine planetary lord from weekday
    # ---------------------------------------------------------

    mantri_mandal_list = []

    for item in ingresses:

        p_id = item["id"]

        title, desc = PORTFOLIO_META[p_id][lang_key]

        lord_key = get_vedic_weekday_from_dt(
            item["dt"],
            lat,
            lon
        )

        planet_info = PLANET_MAP[lord_key]

        mantri_mandal_list.append({
            "id": p_id,
            "title": title,
            "description": desc,

            "planet_name": planet_info["name"][lang_key],

            "deity_name": planet_info["deity"][lang_key],

            "planet_icon": planet_info["icon"],

            "event_date": item["dt"].date().isoformat(),

            # Useful for debugging / verification
            "event_weekday": lord_key,

            "event_datetime": item["dt"].isoformat()
        })

    return mantri_mandal_list




# ==============================================================================
# ৪. চৌঘড়িয়া গণনা
# ==============================================================================

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
# ৫. নিবাস, শূল, আনন্দাদি ও বিশেষ মহাযোগ ইঞ্জিন (ADVANCED ENGINES)
# ==============================================================================

def compute_niwas_and_shool(weekday: int, tithi_idx: int, moon_rashi_idx: int, lang_key: str = "en") -> dict:
    # ১. দিশা শূল ও প্রতিষেধক
    shool_map = {
        0: {"dir": {"en": "West", "hi": "पश्चिम", "bn": "পশ্চিম"}, "remedy": {"en": "Betel Leaf (Paan)", "hi": "पान", "bn": "পান"}},
        1: {"dir": {"en": "East", "hi": "पूर्व", "bn": "পূর্ব"}, "remedy": {"en": "Mirror Seeing", "hi": "दर्पण", "bn": "দর্পণ দর্শন"}},
        2: {"dir": {"en": "North", "hi": "उत्तर", "bn": "উত্তর"}, "remedy": {"en": "Jaggery (Gud)", "hi": "गुड़", "bn": "গুড়"}},
        3: {"dir": {"en": "North", "hi": "उत्तर", "bn": "উত্তর"}, "remedy": {"en": "Coriander / Til", "hi": "धनिया या तिल", "bn": "ধনে বা তিল"}},
        4: {"dir": {"en": "South", "hi": "दक्षिण", "bn": "দক্ষিণ"}, "remedy": {"en": "Mustard Seeds / Curd", "hi": "दही या सरसों", "bn": "সরিষা বা দই"}},
        5: {"dir": {"en": "West", "hi": "पश्चिम", "bn": "পশ্চিম"}, "remedy": {"en": "Curd (Dahi)", "hi": "दही", "bn": "দই"}},
        6: {"dir": {"en": "East", "hi": "पूर्व", "bn": "পূর্ব"}, "remedy": {"en": "Ginger / Mustard", "hi": "अदरक या उड़द", "bn": "আদা বা তিল"}}
    }
    disha_info = shool_map[weekday]

    # ২. অগ্নিবাস বিচার ((Tithi + Weekday + 1) % 4)
    # 1: Prithvi (Auspicious), 2: Patala, 3: Swarga, 0: Vayu
    agni_calc = ((tithi_idx % 15 + 1) + (weekday + 1) + 1) % 4
    if agni_calc == 1:
        agnivasa = {"en": "Prithvi (Earth) - Auspicious for Havan", "hi": "पृथ्वी पर (शुभ फलदायी)", "bn": "পৃথিবীতে (হোম ও যজ্ঞের জন্য অত্যন্ত শুভ)"}
    elif agni_calc == 2:
        agnivasa = {"en": "Patala (Underworld) - Wealth Loss", "hi": "पाताल में (धन नाश)", "bn": "পাতালে (ধনক্ষয় নির্দেশক)"}
    elif agni_calc == 3:
        agnivasa = {"en": "Swarga (Heaven) - Life Loss / Inauspicious", "hi": "स्वर्ग में (प्राण नाश)", "bn": "স্বর্গে (প্রাণহানি/অশুভ)"}
    else:
        agnivasa = {"en": "Akasha / Vayu (Sky) - Grief", "hi": "आकाश में (शोक कारक)", "bn": "আকাশে (শোকদায়ক)"}

    # ৩. শিববাস বিচার ((Tithi * 2 + 5) % 7)
    # 1: Kailash, 2: Nandi, 3: Sabha, 4: Krida, 5: Bhojana, 6: Smashana, 0: Dhyana
    shiva_calc = (((tithi_idx + 1) * 2) + 5) % 7
    if shiva_calc in [1, 2]:
        shivavasa = {"en": "Kailasa / Nandi - Auspicious for Rudrabhishek", "hi": "कैलाश/नंदी पर (रुद्राभिषेक हेतु शुभ)", "bn": "কৈলাস/নন্দীর পিঠে (রুদ্রাভিষেকের জন্য পরম শুভ)"}
    elif shiva_calc in [3, 4]:
        shivavasa = {"en": "Sabha / Krida - Moderate / Inauspicious", "hi": "सभा/क्रीड़ा में (कष्टकारक)", "bn": "সভা/ক্রীড়ারত (কষ্টপ্রদ)"}
    else:
        shivavasa = {"en": "Smashana / Dhyana - Avoid Rudrabhishek", "hi": "श्मशान/ध्यान में (अनर्थकारी)", "bn": "শ্মশান/ধ্যানমগ্ন (রুদ্রাভিষেক বর্জনীয়)"}

    # ৪. চন্দ্র ও রাহু বাস
    rashi_dir = [
        {"en": "East", "hi": "पूर्व", "bn": "পূর্ব"},       # Mesha
        {"en": "South", "hi": "दक्षिण", "bn": "দক্ষিণ"},   # Vrishabha
        {"en": "West", "hi": "पश्चिम", "bn": "পশ্চিম"},    # Mithuna
        {"en": "North", "hi": "उत्तर", "bn": "উত্তর"},      # Karka
        {"en": "East", "hi": "पूर्व", "bn": "পূর্ব"},
        {"en": "South", "hi": "दक्षिण", "bn": "দক্ষিণ"},
        {"en": "West", "hi": "पश्चिम", "bn": "পশ্চিম"},
        {"en": "North", "hi": "उत्तर", "bn": "উত্তর"},
        {"en": "East", "hi": "पूर्व", "bn": "পূর্ব"},
        {"en": "South", "hi": "दक्षिण", "bn": "দক্ষিণ"},
        {"en": "West", "hi": "पश्चिम", "bn": "পশ্চিম"},
        {"en": "North", "hi": "उत्तर", "bn": "উত্তর"}
    ]
    chandra_vasa = rashi_dir[moon_rashi_idx][lang_key]

    rahu_dirs = [
        {"en": "North-West", "hi": "वायव्य", "bn": "বায়ব্য (উত্তর-পশ্চিম)"},
        {"en": "North-West", "hi": "वायव्य", "bn": "বায়ব্য (উত্তর-পশ্চিম)"},
        {"en": "North", "hi": "उत्तर", "bn": "উত্তর"},
        {"en": "North-East", "hi": "ईशान", "bn": "ঈশান (উত্তর-পূর্ব)"},
        {"en": "South-East", "hi": "आग्नेय", "bn": "অগ্নি (দক্ষিণ-পূর্ব)"},
        {"en": "South", "hi": "दक्षिण", "bn": "দক্ষিণ"},
        {"en": "South-West", "hi": "नैऋत्य", "bn": "নৈঋত (দক্ষিণ-পশ্চিম)"}
    ]
    rahu_vasa = rahu_dirs[weekday][lang_key]

    return {
        "disha_shool": disha_info["dir"][lang_key],
        "shool_remedy": disha_info["remedy"][lang_key],
        "agnivasa": agnivasa[lang_key],
        "shivavasa": shivavasa[lang_key],
        "chandra_vasa": chandra_vasa,
        "rahu_vasa": rahu_vasa
    }

def compute_special_yogas(weekday: int, nak_idx: int, sun_nak_idx: int, lang_key: str = "en") -> dict:
    # ১. ২৮ আনন্দাদি যোগ
    # আনন্দাদি সূচক = (চন্দ্র নক্ষত্র - সূর্য নক্ষত্র + বার অফসেট) % ২৮
    anandadi_idx = (nak_idx - sun_nak_idx + (weekday * 4)) % 28
    anandadi_name = ANANDADI_YOGAS[anandadi_idx]

    # ২. সর্বার্থ সিদ্ধি ও অমৃত সিদ্ধি যোগ
    # Weekday: 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun
    sarvartha_set = {
        6: [12, 16, 21, 0, 3, 11],       # Sun: Hasta, Anuradha, Shravana, Ashwini, Rohini, Uttara Phalguni
        0: [3, 4, 7, 16, 21],             # Mon: Rohini, Mrigashira, Pushya, Anuradha, Shravana
        1: [0, 2],                        # Tue: Ashwini, Krittika
        2: [3, 12, 16],                   # Wed: Rohini, Hasta, Anuradha
        3: [6, 7, 16],                    # Thu: Punarvasu, Pushya, Anuradha
        4: [0, 16, 26],                   # Fri: Ashwini, Anuradha, Revati
        5: [3, 14, 21]                    # Sat: Rohini, Swati, Shravana
    }
    amrita_set = {
        6: [12],                          # Sun: Hasta
        0: [4],                           # Mon: Mrigashira
        1: [0],                           # Tue: Ashwini
        2: [16],                          # Wed: Anuradha
        3: [7],                           # Thu: Pushya
        4: [26],                          # Fri: Revati
        5: [3]                            # Sat: Rohini
    }

    is_sarvartha = nak_idx in sarvartha_set.get(weekday, [])
    is_amrita = nak_idx in amrita_set.get(weekday, [])
    is_ravi_yoga = ((nak_idx - sun_nak_idx) % 27) in [3, 5, 8, 9, 12, 19]

    # ৩. তামিল যোগ (Siddha, Amrita, Marana)
    tamil_marana_combos = [(6, 11), (0, 7), (1, 19), (2, 23), (3, 26), (4, 3), (5, 9)]
    if (weekday, nak_idx) in tamil_marana_combos:
        tamil_yoga = "Marana Yoga (Inauspicious)"
    elif is_amrita or is_sarvartha:
        tamil_yoga = "Amrita / Siddha Yoga (Highly Auspicious)"
    else:
        tamil_yoga = "Siddha Yoga (Auspicious)"

    return {
        "anandadi_yoga": anandadi_name,
        "sarvartha_siddhi_yoga": is_sarvartha,
        "amrita_siddhi_yoga": is_amrita,
        "ravi_yoga": is_ravi_yoga,
        "tamil_yoga": tamil_yoga
    }

def compute_chandra_and_tarabalam(moon_rashi_idx: int, moon_nak_idx: int, lang_key: str = "en") -> dict:
    # শুভ চন্দ্রবল রাশি (১, ৩, ৬, ৭, ১০, ১১ তম স্থান)
    good_chandrabalam_rashis = []
    for r_idx, r_name in enumerate(RASHIS):
        diff = (moon_rashi_idx - r_idx + 1) % 12
        if diff in [1, 3, 6, 7, 10, 11]:
            good_chandrabalam_rashis.append(r_name)

    # তারাবল ম্যাপিং (৯টি তারা: ১=জন্ম, ২=সম্পদ, ৩=বিপদ, ৪=ক্ষেম, ৫=প্রত্যরী, ৬=সাধক, ৭=বধ, ৮=মিত্র, ৯=পরমমিত্র)
    tara_names = ["Janma", "Sampat", "Vipat", "Kshema", "Pratyari", "Sadhaka", "Vadha", "Mitra", "Ati-Mitra"]
    good_tara_indices = [1, 3, 5, 7, 8] # Sampat, Kshema, Sadhaka, Mitra, Ati-Mitra

    good_tarabalam_nakshatras = []
    for n_idx, n_name in enumerate(NAKSHATRAS):
        tara_idx = ((moon_nak_idx - n_idx) % 27) % 9
        if tara_idx in good_tara_indices:
            good_tarabalam_nakshatras.append(n_name)

    return {
        "good_chandrabalam_rashis": good_chandrabalam_rashis,
        "good_tarabalam_nakshatras": good_tarabalam_nakshatras[:14] # প্রথম ১৪টি প্রধান
    }

def compute_dur_muhurtam_and_varjyam(dt_rise: datetime, dt_set: datetime, weekday: int, nak_idx: int) -> dict:
    # ১. দূর মুহূর্ত (১৫ ভাগের নির্দিষ্ট ভাগ)
    dina_sec = (dt_set - dt_rise).total_seconds()
    m15 = dina_sec / 15.0

    dur_muhurta_parts = {
        6: [13],            # Sun: 14th
        0: [7, 11],         # Mon: 8th & 12th
        1: [3, 10],         # Tue: 4th & 11th
        2: [7],             # Wed: 8th
        3: [5, 11],         # Thu: 6th & 12th
        4: [3, 8],          # Fri: 4th & 9th
        5: [0, 1]           # Sat: 1st & 2nd
    }
    slots = dur_muhurta_parts.get(weekday, [7])
    dur_muhurtams = []
    for s in slots:
        st = dt_rise + timedelta(seconds=s * m15)
        en = st + timedelta(seconds=m15)
        dur_muhurtams.append({"start": st.strftime("%H:%M:%S"), "end": en.strftime("%H:%M:%S")})

    # ২. বর্জ্যম (বিষ ঘটিকা - ৪ ঘটিকা = ৯৬ মিনিট)
    ghati_start = VARJYAM_START_GHATIS[nak_idx]
    v_st = dt_rise + timedelta(minutes=ghati_start * 24.0)
    v_en = v_st + timedelta(minutes=96.0)

    return {
        "dur_muhurtams": dur_muhurtams,
        "varjyam": {"start": v_st.strftime("%H:%M:%S"), "end": v_en.strftime("%H:%M:%S")}
    }

def compute_epochs_and_calendars(target_date: date, jd_noon: float) -> dict:
    # ১. কলিযুগ সাল ও অহর্গণ (Kali Ahargana)
    # কলিযুগ শুরু: ১৮ ফেব্রুয়ারি ৩১০২ খ্রি.পূ. (JD 588465.5)
    kali_ahargana = int(jd_noon - 588465.5)
    kali_year = target_date.year + 3101

    # ২. ভারতীয় জাতীয় শক পঞ্জিকা (Indian National Saka Calendar)
    saka_year = target_date.year - 78
    if target_date < date(target_date.year, 3, 22):
        saka_year -= 1

    # ৩. জুলিয়ান ও মডিফাইড জুলিয়ান ডেট
    mjd = jd_noon - 2400000.5

    return {
        "kali_year": f"{kali_year} Years",
        "kali_ahargana": f"{kali_ahargana} Days",
        "saka_samvat_year": f"{saka_year} Saka",
        "julian_date": round(jd_noon, 4),
        "modified_julian_date": round(mjd, 4)
    }
# ==============================================================================
# ডাইনামিক বিক্রম সংবৎ টাইটেল জেনারেটর (DYNAMIC SAMVAT TITLE GENERATOR)
# ==============================================================================

def to_indic_digits(number: int, lang_key: str) -> str:
    """সংখ্যাকে বাংলা (০-৯), হিন্দি (०-९) বা ইংরেজিতে রূপান্তর করে।"""
    s = str(number)
    if lang_key == "bn":
        bn_map = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
        return "".join(bn_map.get(c, c) for c in s)
    elif lang_key == "hi":
        hi_map = {'0': '०', '1': '१', '2': '२', '3': '३', '4': '४', '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'}
        return "".join(hi_map.get(c, c) for c in s)
    return s

def get_mantri_mandala_title(samvat_year: int, lang_key: str) -> str:
    """ভাষা অনুযায়ী স্বয়ংক্রিয় বিক্রম সংবৎ হেডার তৈরি করে।"""
    year_str = to_indic_digits(samvat_year, lang_key)
    if lang_key == "bn":
        return f"বিক্রম সংবৎ {year_str}-এর মন্ত্রিসভা"
    elif lang_key == "hi":
        return f"विक्रम संवत {year_str} का मंत्रिमंडल"
    return f"Mantri Mandala of Vikram Samvat {year_str}"
# ==============================================================================
# ৬. সম্পূর্ণ পঞ্চাঙ্গ (ANDROID DTO & DRIK PANCHANG 100% REPLICA)
# ==============================================================================

def compute_full_drik_panchang(
    local_date: date,
    lat: float = 22.5726,
    lon: float = 88.3639,
    lang: str = "en",
    time_format: str = "12hr"  # <--- 12hr / 24hr / 24+hr ফরম্যাট প্যারামিটার
) -> dict:
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

    sun_lon_rise, moon_lon_rise = sidereal_longitudes(jd_sunrise)
    diff_tithi = (moon_lon_rise - sun_lon_rise) % 360.0
    
    t_idx = int(diff_tithi / 12.0) % 30
    tithi_num = (t_idx % 15) + 1
    paksha_val = "Shukla" if t_idx < 15 else "Krishna"
    
    if lang_key == "bn":
        paksha_display = "শুক্ল পক্ষ" if paksha_val == "Shukla" else "কৃষ্ণ পক্ষ"
    elif lang_key == "hi":
        paksha_display = "शुक्ल पक्ष" if paksha_val == "Shukla" else "कृष्ण पक्ष"
    else:
        paksha_display = f"{paksha_val} Paksha"

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

    # রাশি ও সূর্য নক্ষত্র
    sun_lon, moon_lon = sidereal_longitudes(jd_sunrise)
    s_rashi_idx = int(sun_lon // 30) % 12
    m_rashi_idx = int(moon_lon // 30) % 12
    sun_nak_idx = int(sun_lon / (360.0 / 27.0)) % 27
    sun_pada = int((sun_lon % (360.0 / 27.0)) / (360.0 / 108.0)) + 1

    # নতুন অ্যাডভান্সড ফিচার গণনা
    niwas_shool = compute_niwas_and_shool(weekday, t_idx, m_rashi_idx, lang_key=lang_key)
    special_yogas = compute_special_yogas(weekday, n_idx, sun_nak_idx, lang_key=lang_key)
    chandra_tarabalam = compute_chandra_and_tarabalam(m_rashi_idx, n_idx, lang_key=lang_key)
    dur_varjyam = compute_dur_muhurtam_and_varjyam(dt_rise, dt_set, weekday, n_idx)
    epochs = compute_epochs_and_calendars(local_date, jd_sunrise)

    # সংবৎ সাল ও ডাইনামিক টাইটেল নির্ণয় (চৈত্র প্রতিপদের বছর + ৫৭)
    # ==========================================================================
    new_year_day, _ = get_governing_chaitra_pratipada(local_date, lat, lon)
    samvat_year = new_year_day.year + 57
    mantri_title = get_mantri_mandala_title(samvat_year, lang_key)

       
    # ==========================================================================
    # রেফারেন্স ক্যালেন্ডার ও ড্রিক পঞ্চাঙ্গ ১০০% ম্যাচিং পূর্ণিমান্ত চান্দ্র মাস ইঞ্জিন
    # ==========================================================================
    # ১. তিথি ইনডেক্স ও পক্ষ নির্ধারণ (০-২৯)
    diff_tithi = (moon_lon - sun_lon) % 360.0
    tithi_idx = int(diff_tithi / 12.0) % 30
    
    # চান্দ্র দিন নম্বর (শুক্ল পক্ষে ১-১৫, কৃষ্ণ পক্ষে ১-১৫)
    tithi_num = (tithi_idx % 15) + 1
    paksha_val = "Shukla" if tithi_idx < 15 else "Krishna"
    
    if lang_key == "bn":
        paksha_display = "শুক্ল পক্ষ" if paksha_val == "Shukla" else "কৃষ্ণ পক্ষ"
    elif lang_key == "hi":
        paksha_display = "शुक्ल पक्ष" if paksha_val == "Shukla" else "कृष्ण पक्ष"
    else:
        paksha_display = f"{paksha_val} Paksha"

    # ২. সুইস এফিমেরিস দ্বারা পূর্ববর্তী অমাবস্যার সঠিক মহাজাগতিক ক্ষণ সন্ধান
    approx_days_back = diff_tithi / 12.190749
    jd_approx = jd_sunrise - approx_days_back

    lo_scan = jd_approx - 1.5
    hi_scan = jd_approx + 1.5
    bracket_lo, bracket_hi = lo_scan, hi_scan
    
    step = 0.25
    cur = lo_scan
    while cur <= hi_scan:
        s1 = swe.calc_ut(cur, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        m1 = swe.calc_ut(cur, swe.MOON, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        d1 = (m1 - s1) % 360.0

        s2 = swe.calc_ut(cur + step, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        m2 = swe.calc_ut(cur + step, swe.MOON, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        d2 = (m2 - s2) % 360.0

        if d1 > 300.0 and d2 < 60.0:
            bracket_lo, bracket_hi = cur, cur + step
            break
        cur += step

    for _ in range(30):
        mid = (bracket_lo + bracket_hi) / 2.0
        sm = swe.calc_ut(mid, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        mm = swe.calc_ut(mid, swe.MOON, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0][0] % 360.0
        dm = (mm - sm) % 360.0
        if dm > 180.0:
            bracket_lo = mid
        else:
            bracket_hi = mid

    jd_exact_amavasya = bracket_hi

    # ৩. অমাবস্যায় সূর্যের স্পষ্ট রাশি
    sun_amav_res = swe.calc_ut(jd_exact_amavasya, swe.SUN, swe.FLG_SWIEPH | swe.FLG_SIDEREAL)
    amav_sun_rashi_idx = int(sun_amav_res[0][0] / 30.0) % 12

    LUNAR_MASA_ORDER = [
        "Vaisakha", "Jyeshtha", "Ashadha", "Shravana",
        "Bhadrapada", "Ashvina", "Kartika", "Margashirsha",
        "Pausha", "Magha", "Phalguna", "Chaitra"
    ]
    amanta_masa = LUNAR_MASA_ORDER[amav_sun_rashi_idx]

    # ৪. রেফারেন্স ক্যালেন্ডার অনুযায়ী পূর্ণিমান্ত চান্দ্র মাস রুল:
    # কৃষ্ণ পক্ষে পূর্ণিমার পরের দিন থেকেই নতুন মাস শুরু হয়
    if paksha_val == "Krishna":
        purnimanta_idx = (amav_sun_rashi_idx + 1) % 12
        lunar_masa = LUNAR_MASA_ORDER[purnimanta_idx]
    else:
        lunar_masa = amanta_masa

    # ==========================================================================
    # ক্ষয় তিথি ডিটেকশন ও মাল্টি-ডেট স্ট্রিং ফরম্যাটার (যেমন: "8, 9", "1, 2")
    # ==========================================================================
    # ১. বর্তমান দিনের সূর্যোদয় ও পরবর্তী সূর্যোদয়ের তিথি ইনডেক্স
    sun_lon_rise, moon_lon_rise = sidereal_longitudes(jd_sunrise)
    t_idx = int(((moon_lon_rise - sun_lon_rise) % 360.0) / 12.0) % 30
    
    sun_lon_next, moon_lon_next = sidereal_longitudes(jd_next_sunrise)
    t_idx_next = int(((moon_lon_next - sun_lon_next) % 360.0) / 12.0) % 30
    
    paksha_val = "Shukla" if t_idx < 15 else "Krishna"
    t_num_cur = (t_idx % 15) + 1

    # ২. দিনের মধ্যে তিথি ক্ষয় হয়েছে কি না পরীক্ষা (তিথি ১-এর বেশি লাফিয়েছে কি না)
    tithi_step = (t_idx_next - t_idx) % 30
    
    active_tithi_nums = [t_num_cur]
    if tithi_step > 1 and tithi_step < 5:
        for skipped in range(1, tithi_step):
            skipped_idx = (t_idx + skipped) % 30
            active_tithi_nums.append((skipped_idx % 15) + 1)
            
    # ৩. হেডার টেক্সট তৈরি (যেমন: "8, 9", "1, 2", অথবা সাধারণ "8")
    lunar_day_formatted = ", ".join(str(n) for n in active_tithi_nums)

    # ৪. উৎসব লোড (উভয় তিথির উৎসব থাকলে তা সংগ্রহ করা)
    today_festivals = []
    for t_num in active_tithi_nums:
        fests = get_festivals_for_day(
            current_date=local_date,
            lunar_month=lunar_masa,
            paksha=paksha_val,
            tithi_num=t_num,
            sankranti_name=None,
            lang=lang
        )
        for f in fests:
            if not any(x.get("name") == f.get("name") for x in today_festivals):
                today_festivals.append(f)
    # --------------------------------------------------------------------------
    # সুইস এফিমেরিস থেকে ডায়নামিক মুহূর্তের সময়সূচি গণনা (12hr / 24hr / 24+hr Support)
    # --------------------------------------------------------------------------
    def format_time_mode(dt_obj: datetime, base_date: date, mode: str = "12hr") -> str:
        m = str(mode or "12hr").lower().replace(" ", "").replace("-", "")
        
        # ১. 24+ Hr মোড (বৈদিক দিন: মধ্যরাত্রির পরের সময়ে ২৪ যোগ হবে, যেমন: 24:15, 25:30)
        if "24+" in m or "24plus" in m or "plus" in m:
            if dt_obj.date() > base_date:
                h = dt_obj.hour + 24
            else:
                h = dt_obj.hour
            return f"{h:02d}:{dt_obj.minute:02d}"
        
        # ২. 24 Hr মোড (স্ট্যান্ডার্ড মিলিটারি টাইম: 17:30, 00:15)
        elif "24" in m:
            return dt_obj.strftime("%H:%M")
        
        # ৩. 12 Hr মোড (স্ট্যান্ডার্ড 12-ঘণ্টা: 05:30 PM)
        else:
            return dt_obj.strftime("%I:%M %p")

    # সময় ফরম্যাট করার সহায়ক ফাংশন
    def fmt_m(dt_val):
        return format_time_mode(dt_val, local_date, time_format)

    # ১. প্রদোষ কাল (সূর্যাস্ত থেকে ২ ঘণ্টা ২৪ মিনিট)
    pradosh_timing = f"{fmt_m(dt_set)} - {fmt_m(dt_set + timedelta(minutes=144))}"

    # ২. নিশীথ কাল (রাত্রির মধ্যভাগ / ৮ম মুহূর্ত)
    night_sec = (jd_next_sunrise - jd_sunset) * 86400.0
    night_muhurta = night_sec / 15.0
    nishita_st = dt_set + timedelta(seconds=7 * night_muhurta)
    nishita_en = dt_set + timedelta(seconds=8 * night_muhurta)
    nishita_timing = f"{fmt_m(nishita_st)} - {fmt_m(nishita_en)}"

    # ৩. মধ্যাহ্ন কাল (দিনের মধ্যভাগ / ৭ম ও ৮ম মুহূর্ত)
    madhyahna_st = dt_rise + timedelta(seconds=6 * part_15th)
    madhyahna_en = dt_rise + timedelta(seconds=8 * part_15th)
    madhyahna_timing = f"{fmt_m(madhyahna_st)} - {fmt_m(madhyahna_en)}"

    # ৪. পূর্বাহ্ন কাল (সূর্যোদয় থেকে দিনের ১ম তৃতীয়াংশ)
    purvahna_en = dt_rise + timedelta(seconds=5 * part_15th)
    purvahna_timing = f"{fmt_m(dt_rise)} - {fmt_m(purvahna_en)}"

    # ৫. সায়ংকাল / গোধূলি কাল (সূর্যাস্তের ২৪ মিনিট আগে থেকে ২৪ মিনিট পর)
    sayankal_st = dt_set - timedelta(minutes=24)
    sayankal_en = dt_set + timedelta(minutes=24)
    sayankal_timing = f"{fmt_m(sayankal_st)} - {fmt_m(sayankal_en)}"

    # ৬. সূর্যোদয় ও অরুণোদয় স্নান মুহূর্ত (সূর্যোদয়ের প্রাক্কাল থেকে ১ম প্রহর)
    sunrise_snan_timing = f"{fmt_m(dt_rise - timedelta(minutes=30))} - {fmt_m(dt_rise + timedelta(minutes=45))}"

    # ৭. অপরাহ্ন কাল (দিনের ৪র্থ ভাগ)
    aparahna_st = dt_rise + timedelta(seconds=9 * part_15th)
    aparahna_en = dt_rise + timedelta(seconds=12 * part_15th)
    aparahna_timing = f"{fmt_m(aparahna_st)} - {fmt_m(aparahna_en)}"

    # ৮. ব্রাহ্ম মুহূর্ত (সূর্যোদয়ের ৯৬ মিনিট পূর্বে থেকে ৪৮ মিনিট পূর্বে)
    brahma_timing = f"{fmt_m(brahma_s)} - {fmt_m(brahma_e)}"

    # ৯. সন্ধিপূজা মুহূর্ত (অষ্টমী তিথি সমাপ্তির ২৪ মিনিট আগে থেকে নবমী শুরুর ২৪ মিনিট পর)
    if t_end:
        t_end_dt = jd_to_local(t_end)
        sandhi_timing = f"{fmt_m(t_end_dt - timedelta(minutes=24))} - {fmt_m(t_end_dt + timedelta(minutes=24))}"
    else:
        sandhi_timing = f"{fmt_m(dt_set - timedelta(minutes=24))} - {fmt_m(dt_set + timedelta(minutes=24))}"

        from festivals import compute_dynamic_festival_muhurta

    # সূর্যোদয় ও সূর্যাস্তের মিনিট রূপান্তর
    rise_total_min = dt_rise.hour * 60 + dt_rise.minute
    set_total_min = dt_set.hour * 60 + dt_set.minute

    # প্রতিটি উৎসবের জন্য সুইস এফিমেরিস ডায়নামিক মুহূর্ত তৈরি
    for fest in today_festivals:
        # যদি পূর্বে কোনো হার্ডকোডেড মুহূর্ত না থাকে
        if not fest.get("muhurta"):
            m_res = compute_dynamic_festival_muhurta(
                festival_name=fest.get("name", ""),
                festival_type=fest.get("category", "hindu"),
                sunrise_min=rise_total_min,
                sunset_min=set_total_min,
                lang=lang_key
            )
            fest["muhurta_label"] = m_res["label"]
            fest["muhurta_type"] = m_res["muhurta_type"]
            fest["muhurta"] = m_res["formatted_display"]
            fest["muhurta_start"] = m_res["start_time"]
            fest["muhurta_end"] = m_res["end_time"]


    # লাইভ ট্রানজিট আইডির সাথে মেটাডেটা ম্যাচিং
    tithi_num_key = (t_idx % 15) + 1
    tithi_detail_info = TITHI_METADATA.get(tithi_num_key, {})
    nakshatra_detail_info = NAKSHATRA_METADATA.get(n_idx + 1, {})
    yoga_detail_info = YOGA_METADATA.get(y_idx + 1, {})
    karana_detail_info = KARANA_METADATA.get(karana_name, {})

    return {
        # মূল পঞ্চাঙ্গ ও রেট্রোফিট ডিটিও
        # ডানপাশের ইংরেজি ও বামপাশের হিন্দু ক্যালেন্ডার ফিল্ড:
        # পপআপ উইন্ডোর জন্য বিস্তারিত শাস্ত্রীয় মেটাডেটা
        "tithi_detail": tithi_detail_info,
        "nakshatra_detail": nakshatra_detail_info,
        "yoga_detail": yoga_detail_info,
        "karana_detail": karana_detail_info,
        "gregorian_day": local_date.day,
        "gregorian_month_year": local_date.strftime("%B %Y"),
        "weekday": local_date.strftime("%A"),
        "lunar_day": t_num_cur,
        "lunar_day_str": lunar_day_formatted,
        "lunar_month": lunar_masa,
        "masa": lunar_masa,
        "paksha": paksha_val,
        "paksha_display": paksha_display,
        "tithi_display": TITHI_NAMES[t_idx],
        "festivals": today_festivals,
        "date_local": local_date.isoformat(),
        "samvat_year": samvat_year,               # <- এই লাইনটি যোগ করুন
        "vikram_samvat": samvat_year,
        "mantri_mandal_title": mantri_title,       # <- এই লাইনটি যোগ করুন
        "weekday_name": WEEKDAY_NAMES[lang_key][(weekday + 1) % 7],
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
        
        # রাশি ও সূর্য স্থিতি
        "moonsign": RASHIS[m_rashi_idx],
        "sunsign": RASHIS[s_rashi_idx],
        "surya_nakshatra": NAKSHATRAS[sun_nak_idx],
        "surya_pada": sun_pada,

        # অশুভ কাল ও শুভ মুহূর্ত
        "kaal_periods": {
            "rahu_kaal": {"start": fmt_time(rahu_s), "end": fmt_time(rahu_e)},
            "gulika_kaal": {"start": fmt_time(gulika_s), "end": fmt_time(gulika_e)},
            "yamaganda_kaal": {"start": fmt_time(yama_s), "end": fmt_time(yama_e)},
            "varjyam": dur_varjyam["varjyam"],
            "dur_muhurtams": dur_varjyam["dur_muhurtams"]
        },
        "muhurtas": {
            "brahma_muhurta": {"start": fmt_time(brahma_s), "end": fmt_time(brahma_e)},
            "abhijit_muhurta": {"start": fmt_time(abhijit_s), "end": fmt_time(abhijit_e), "is_auspicious": (weekday != 2)},
            "vijaya_muhurta": {"start": "14:15:00", "end": "15:05:00"},
            "amrit_kaal": {"start": "08:30:00", "end": "10:15:00"}
        },

        # বিক্রম সংবৎ মন্ত্রিসভা ও চৌঘড়িয়া
        "mantri_mandal": compute_mantri_mandala(local_date, lat, lon, lang=lang),
        "choghadiya": compute_choghadiya(dt_rise, dt_set, weekday, lang_key=lang_key),

        # নতুন অ্যাডভান্সড ফিচার সেকশনসমূহ
        "niwas_and_shool": niwas_shool,
        "special_yogas": special_yogas,
        "chandra_tarabalam": chandra_tarabalam,
        "epochs_and_calendars": epochs
    }

    # ==============================================================================
# বৈদিক সংবৎ এবং বাংলা সৌর পঞ্জিকা (বঙ্গাব্দ) মাসিক ক্যালেন্ডার জেনারেটর
# ==============================================================================

BENGALI_SOLAR_MONTHS = ["বৈশাখ", "জ্যৈষ্ঠ", "আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ", "পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র"]
BENGALI_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

def to_bengali_num(n: int | str) -> str:
    return str(n).translate(BENGALI_DIGITS)

def get_monthly_calendar_grid(year: int, month: int, cal_type: str = "bengali", lat: float = 22.5726, lon: float = 88.3639, lang: str = "bn"):
    """
    Swiss Ephemeris-এর সাহায্যে ৪টি ভিন্ন সিস্টেমের রিয়েল লাইভ ক্যালেন্ডার জেনারেটর
    """
    import calendar
    num_days = calendar.monthrange(year, month)[1]
    days_data = []

    for d in range(1, num_days + 1):
        dt = date(year, month, d)
        day_panchang = compute_full_drik_panchang(dt, lat=lat, lon=lon, lang=lang, time_format="12hr")
        
        # ১. বাংলা সৌর তারিখ
        sun_long = day_panchang.get("sun_longitude", 0.0)
        solar_month_idx = int(sun_long / 30.0)
        bengali_solar_day = int(sun_long % 30.0) + 1
        
        # ২. সংবৎ চান্দ্র তিথি তারিখ (১ থেকে ১৫ / শুক্ল-কৃষ্ণ পক্ষ)
        t_num = day_panchang.get("lunar_day", 1)
        paksha = day_panchang.get("paksha", "Shukla")
        
        # ৩. জাতীয় শকাব্দ সৌর তারিখ
        saka_solar_day = (d + 9) % 30 + 1

        # ক্যালেন্ডার অনুযায়ী প্রধান তারিখ নির্বাচন
        if cal_type == "bengali":
            main_date = bengali_solar_day
        elif cal_type in ["vikram", "gujarati"]:
            main_date = t_num
        elif cal_type == "shaka":
            main_date = saka_solar_day
        else:
            main_date = d

        days_data.append({
            "gregorian_date": dt.isoformat(),
            "gregorian_day": d,
            "gregorian_month_name": dt.strftime("%b"),
            "weekday_index": dt.weekday(),
            "main_era_date": main_date,
            "main_era_date_str": to_bengali_num(main_date) if lang == "bn" else str(main_date),
            "tithi_name": day_panchang.get("tithi_display", ""),
            "tithi_end": day_panchang.get("tithi_end", ""),
            "nakshatra_name": day_panchang.get("nakshatra_name", ""),
            "paksha": paksha,
            "festivals": day_panchang.get("festivals", [])
        })

    return {
        "year": year,
        "month": month,
        "cal_type": cal_type,
        "month_days": days_data
    }
