"""
Astronomical Daily Panchang & Vikram Samvat Mantri Mandala Engine.
Calculates Tithi, Nakshatra, Yoga, Karana transitions, Sun/Moon events,
and 10-office Planetary Cabinet (Navadhikaris) in English, Hindi & Bengali.
"""

from __future__ import annotations
import math
from datetime import datetime, timedelta, date
from zoneinfo import ZoneInfo
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
    swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
except ImportError:
    SWISSEPH_AVAILABLE = False

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

# ==============================================================================
# ১. বহুমাত্রিক ১০টি মন্ত্রিসভা দপ্তর মেটাডেটা (PORTFOLIO METADATA)
# ==============================================================================

PORTFOLIO_META = {
    1: {
        "en": ("King (Raja)", "Supreme governance, state leadership & national destiny"),
        "hi": ("राजा (King)", "राज्य शासन, प्रशासनिक व्यवस्था एवं राष्ट्रीय संप्रभुता"),
        "bn": ("রাজা (King)", "রাষ্ট্র পরিচালনা, শাসন ব্যবস্থা ও জাতীয় ভাগ্য")
    },
    2: {
        "en": ("Prime Minister (Mantri)", "Cabinet leadership, policy decisions & advisory"),
        "hi": ("मन्त्री (Prime Minister)", "मंत्रिमंडल, नीति निर्धारण एवं प्रशासनिक परामर्श"),
        "bn": ("মন্ত্রী (Prime Minister)", "মন্ত্রিসভা, নীতি নির্ধারণ ও প্রশাসনিক পরামর্শ")
    },
    3: {
        "en": ("Commander (Senapati)", "National defense, armed forces & internal security"),
        "hi": ("सेनापति (Commander)", "राष्ट्रीय रक्षा, सैन्य बल एवं आंतरिक सुरक्षा"),
        "bn": ("সেনাপতি (Commander)", "প্রতিরক্ষা, সামরিক বাহিনী ও অভ্যন্তরীণ নিরাপত্তা")
    },
    4: {
        "en": ("Lord of Grains (Sasyadhipati)", "Kharif agriculture, monsoon crops & grain yield"),
        "hi": ("सस्याधिपति (Grains Lord)", "खरीफ फसल, वर्षाकालीन धान्य एवं मुख्य खाद्य उत्पादन"),
        "bn": ("শস্যাধিপতি (Grains Lord)", "খারিফ ফসল, বর্ষাকালীন শস্য ও মূল খাদ্য উৎপাদন")
    },
    5: {
        "en": ("Lord of Crops (Dhanyadhipati)", "Rabi harvest, pulse storage & agricultural trade"),
        "hi": ("धान्याधिपति (Crops Lord)", "रबी फसल, दलहन एवं धान्य संचयन"),
        "bn": ("ধান্যাধিপতি (Crops Lord)", "রবি ফসল, ডাল ও খাদ্যশস্য সঞ্চয়")
    },
    6: {
        "en": ("Lord of Clouds (Meghadhipati)", "Rainfall distribution, monsoon & water bodies"),
        "hi": ("मेघाधिपति (Clouds Lord)", "वर्षा, मेघ एवं जल संसाधनों की स्थिति"),
        "bn": ("মেঘাধিপতি (Clouds Lord)", "বৃষ্টিপাত, বর্ষা ও জলাশয়ের অবস্থা")
    },
    7: {
        "en": ("Lord of Liquids (Rasadhipati)", "Dairy, edible oils, sugarcane, medicine & juices"),
        "hi": ("रसाधिपति (Liquids Lord)", "दुग्ध, तेल, औषधीय रस, शर्करा एवं पेय पदार्थ"),
        "bn": ("রসাধিপতি (Liquids Lord)", "দুগ্ধজাত দ্রব্য, তেল, ঔষধি রস ও পানীয়")
    },
    8: {
        "en": ("Lord of Fruits (Phaladhipati)", "Orchards, horticulture, flowers & fruit production"),
        "hi": ("फलाधिपति (Fruits Lord)", "फलोद्यान, बागवानी, पुष्प एवं मौसमी फल उत्पादन"),
        "bn": ("ফলাধিপতি (Fruits Lord)", "ফলবাগান, উদ্যানপালন ও বৃক্ষজাত ফলন")
    },
    9: {
        "en": ("Lord of Wealth (Dhanadhipati)", "Economic treasury, financial markets & wealth"),
        "hi": ("धनाधिपति (Wealth Lord)", "आर्थिक कोष, राजकोष एवं वित्तीय समृद्धि"),
        "bn": ("ধনাধিপতি (Wealth Lord)", "অর্থনৈতিক সঞ্চয়, কোষাগার ও আর্থিক সমৃদ্ধি")
    },
    10: {
        "en": ("Lord of Minerals (Dhatvadhipati)", "Minerals, metals, gems & underground resources"),
        "hi": ("नीरसेश / धात्वाधिपति (Minerals Lord)", "खनिज संपदा, धातु, रत्न एवं भूगर्भीय वस्तुएं"),
        "bn": ("নীরসেশ / ধাত্বাধিপতি (Minerals Lord)", "খনিজ সম্পদ, ধাতু, রত্ন ও ভূগর্ভস্থ বস্তু")
    }
}

# ==============================================================================
# ২. বহুমাত্রিক গ্রহ ও দেবতা ম্যাপিং (PLANET & DEITY MAPPING)
# ==============================================================================

PLANET_MAP = {
    "Surya": {
        "name": {"en": "Sun (Surya)", "hi": "सूर्य", "bn": "সূর্য"},
        "deity": {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "সূর্য নারায়ণ"},
        "icon": "☉"
    },
    "Chandra": {
        "name": {"en": "Moon (Chandra)", "hi": "चन्द्र", "bn": "চন্দ্র"},
        "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"},
        "icon": "☽"
    },
    "Mangal": {
        "name": {"en": "Mars (Mangal)", "hi": "मंगल", "bn": "মঙ্গল"},
        "deity": {"en": "Lord Kartikeya / Mangal", "hi": "कार्तिकेय / मंगल देव", "bn": "কার্তিকেয় / মঙ্গল দেব"},
        "icon": "♂"
    },
    "Budha": {
        "name": {"en": "Mercury (Budha)", "hi": "बुध", "bn": "বুধ"},
        "deity": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"},
        "icon": "☿"
    },
    "Guru": {
        "name": {"en": "Jupiter (Guru)", "hi": "बृहस्पति (गुरु)", "bn": "বৃহস্পতি"},
        "deity": {"en": "Brihaspati Deva", "hi": "देवगुरु बृहस्पति", "bn": "দেবগুরু বৃহস্পতি"},
        "icon": "♃"
    },
    "Shukra": {
        "name": {"en": "Venus (Shukra)", "hi": "शुक्र", "bn": "শুক্র"},
        "deity": {"en": "Shukracharya", "hi": "शुक्राचार्य", "bn": "শুক্রাচার্য"},
        "icon": "♀"
    },
    "Shani": {
        "name": {"en": "Saturn (Shani)", "hi": "शनि", "bn": "শনি"},
        "deity": {"en": "Shani Deva", "hi": "शनैश्चर देव", "bn": "শনৈশ্চর দেব"},
        "icon": "♄"
    }
}

WEEKDAY_LORDS = ["Surya", "Chandra", "Mangal", "Budha", "Guru", "Shukra", "Shani"]


def weekday_lord(d: date) -> str:
    """Returns Vedic weekday lord (Sunday=Surya ... Saturday=Shani)."""
    return WEEKDAY_LORDS[(d.weekday() + 1) % 7]


def to_jd_ut(dt_local: datetime) -> float:
    dt_utc = dt_local.astimezone(UTC)
    if SWISSEPH_AVAILABLE:
        return swe.julday(
            dt_utc.year, dt_utc.month, dt_utc.day,
            dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0
        )
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
    base = datetime(year, month, int(day), tzinfo=UTC) + timedelta(hours=hours)
    return base.astimezone(IST)


def get_sunrise_jd(target_date: date, lat: float, lon: float) -> float:
    noon_local = datetime(target_date.year, target_date.month, target_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25
    if SWISSEPH_AVAILABLE:
        swe.set_sid_mode(swe.SIDM_LAHIRI, 0, 0)
        geopos = (lon, lat, 0.0)
        _, s_rise = swe.rise_trans(jd_approx, swe.SUN, swe.CALC_RISE, geopos)
        return s_rise[0]
    return jd_approx + 0.25


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


def sun_moon_events(jd_start: float, lat: float, lon: float):
    if SWISSEPH_AVAILABLE:
        geopos = (lon, lat, 0.0)
        _, sunrise = swe.rise_trans(jd_start, swe.SUN, swe.CALC_RISE, geopos)
        _, sunset = swe.rise_trans(sunrise[0], swe.SUN, swe.CALC_SET, geopos)
        _, next_sunrise = swe.rise_trans(sunrise[0] + 0.5, swe.SUN, swe.CALC_RISE, geopos)
        try:
            _, moonrise = swe.rise_trans(sunrise[0] - 0.25, swe.MOON, swe.CALC_RISE, geopos)
            m_rise_jd = moonrise[0]
        except Exception:
            m_rise_jd = None
        try:
            _, moonset = swe.rise_trans(sunrise[0] - 0.25, swe.MOON, swe.CALC_SET, geopos)
            m_set_jd = moonset[0]
        except Exception:
            m_set_jd = None
        return sunrise[0], sunset[0], next_sunrise[0], m_rise_jd, m_set_jd
    return jd_start + 0.25, jd_start + 0.75, jd_start + 1.25, None, None


def find_transition(jd_start: float, target_fn, step_hours=0.25, max_hours=48.0, backward=False):
    start_index = target_fn(jd_start)
    jd = jd_start
    step = (-step_hours if backward else step_hours) / 24.0
    hours_scanned = 0.0
    prev_jd = jd
    while hours_scanned < max_hours:
        jd += step
        hours_scanned += step_hours
        if target_fn(jd) != start_index:
            lo, hi = (jd, prev_jd) if backward else (prev_jd, jd)
            for _ in range(35):
                mid = (lo + hi) / 2.0
                if target_fn(mid) == start_index:
                    if backward: hi = mid
                    else: lo = mid
                else:
                    if backward: lo = mid
                    else: hi = mid
            return lo if backward else hi
        prev_jd = jd
    return None


@dataclass
class PanchangResult:
    date_local: str
    sunrise: str
    sunset: str
    next_sunrise: str
    moonrise: Optional[str]
    moonset: Optional[str]
    tithi_name: str
    tithi_end: Optional[str]
    tithi_next_name: str
    nakshatra_name: str
    nakshatra_index: int
    nakshatra_end: Optional[str]
    nakshatra_next_name: str
    yoga_name: str
    yoga_end: Optional[str]
    yoga_next_name: str
    karana_name: str
    karana_end: Optional[str]
    karana_next_name: str
    pada_timeline: list
    nakshatra_pada_display: str
    karana_type: str
    kaal_periods: dict
    muhurtas: dict


def compute_panchang(local_date: date, lat: float = 28.6139, lon: float = 77.2090) -> PanchangResult:
    noon_local = datetime(local_date.year, local_date.month, local_date.day, 6, 0, tzinfo=IST)
    jd_approx = to_jd_ut(noon_local) - 0.25
    jd_sunrise, jd_sunset, jd_next_sunrise, jd_moonrise, jd_moonset = sun_moon_events(jd_approx, lat, lon)

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

    t_idx = tithi_index(jd_sunrise)
    t_end = find_transition(jd_sunrise, tithi_index)

    n_idx = nak_index(jd_sunrise)
    n_end_jd = find_transition(jd_sunrise, nak_index)

    y_idx = yoga_index(jd_sunrise)
    y_end = find_transition(jd_sunrise, yoga_index)

    k_idx = karana_index(jd_sunrise)
    k_end = find_transition(jd_sunrise, karana_index)

    def fmt(jd):
        return jd_to_local(jd).strftime("%Y-%m-%dT%H:%M:%S") if jd else None

    def fmt_time(jd):
        return jd_to_local(jd).strftime("%H:%M:%S") if jd else None

    dt_rise = jd_to_local(jd_sunrise)
    dt_set = jd_to_local(jd_sunset)
    dina_mana_sec = (dt_set - dt_rise).total_seconds()
    part_8th_sec = dina_mana_sec / 8.0
    muhurta_15th_sec = dina_mana_sec / 15.0
    weekday = local_date.weekday()

    rahu_parts = {0: 1, 1: 6, 2: 4, 3: 5, 4: 3, 5: 2, 6: 7}
    rahu_start_dt = dt_rise + timedelta(seconds=rahu_parts[weekday] * part_8th_sec)
    rahu_end_dt = rahu_start_dt + timedelta(seconds=part_8th_sec)

    gulika_parts = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 6}
    gulika_start_dt = dt_rise + timedelta(seconds=gulika_parts[weekday] * part_8th_sec)
    gulika_end_dt = gulika_start_dt + timedelta(seconds=part_8th_sec)

    yama_parts = {0: 3, 1: 2, 2: 1, 3: 0, 4: 6, 5: 5, 6: 4}
    yama_start_dt = dt_rise + timedelta(seconds=yama_parts[weekday] * part_8th_sec)
    yama_end_dt = yama_start_dt + timedelta(seconds=part_8th_sec)

    abhijit_start_dt = dt_rise + timedelta(seconds=7 * muhurta_15th_sec)
    abhijit_end_dt = dt_rise + timedelta(seconds=8 * muhurta_15th_sec)

    brahma_start_dt = dt_rise - timedelta(minutes=96)
    brahma_end_dt = dt_rise - timedelta(minutes=48)

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
        p_end = find_transition(jd_cursor, pada_index, max_hours=30.0)
        end_jd = jd_next_sunrise if (p_end is None or p_end >= jd_next_sunrise) else p_end
        pada_timeline.append({
            "nakshatra": nak_here,
            "pada": pada_num,
            "end": fmt(end_jd)
        })
        if p_end is None or p_end >= jd_next_sunrise:
            break
        jd_cursor = p_end

    return PanchangResult(
        date_local=local_date.isoformat(),
        sunrise=fmt_time(jd_sunrise),
        sunset=fmt_time(jd_sunset),
        next_sunrise=fmt_time(jd_next_sunrise),
        moonrise=fmt_time(jd_moonrise),
        moonset=fmt_time(jd_moonset),
        tithi_name=TITHI_NAMES[t_idx],
        tithi_end=fmt(t_end),
        tithi_next_name=TITHI_NAMES[(t_idx + 1) % 30],
        nakshatra_name=NAKSHATRAS[n_idx],
        nakshatra_index=n_idx,
        nakshatra_end=fmt(n_end_jd),
        nakshatra_next_name=NAKSHATRAS[(n_idx + 1) % 27],
        yoga_name=YOGA_NAMES[y_idx],
        yoga_end=fmt(y_end),
        yoga_next_name=YOGA_NAMES[(y_idx + 1) % 27],
        karana_name=get_karana_name(k_idx),
        karana_end=fmt(k_end),
        karana_next_name=get_karana_name(k_idx + 1),
        pada_timeline=pada_timeline,
        nakshatra_pada_display=" → ".join(
            f"{p['nakshatra']} (Pada {p['pada']})" for p in pada_timeline
        ),
        karana_type="Fixed" if (k_idx % 60) in KARANA_FIXED else "Movable",
        kaal_periods={
            "rahu_kaal": {"start": rahu_start_dt.strftime("%H:%M:%S"), "end": rahu_end_dt.strftime("%H:%M:%S")},
            "gulika_kaal": {"start": gulika_start_dt.strftime("%H:%M:%S"), "end": gulika_end_dt.strftime("%H:%M:%S")},
            "yamaganda_kaal": {"start": yama_start_dt.strftime("%H:%M:%S"), "end": yama_end_dt.strftime("%H:%M:%S")}
        },
        muhurtas={
            "brahma_muhurta": {"start": brahma_start_dt.strftime("%H:%M:%S"), "end": brahma_end_dt.strftime("%H:%M:%S")},
            "abhijit_muhurta": {
                "start": abhijit_start_dt.strftime("%H:%M:%S"),
                "end": abhijit_end_dt.strftime("%H:%M:%S"),
                "is_auspicious": (weekday != 2)
            },
            "vijaya_muhurta": {"start": "14:15:00", "end": "15:05:00"},
            "amrit_kaal": {"start": "08:30:00", "end": "10:15:00"}
        }
    )


def find_solar_ingress(target_deg: float, approx_start: date) -> datetime:
    start_dt = datetime(approx_start.year, approx_start.month, approx_start.day, 0, 0, tzinfo=UTC)
    jd = to_jd_ut(start_dt)

    for _ in range(45):
        s_long, _ = sidereal_longitudes(jd)
        s_next, _ = sidereal_longitudes(jd + 1.0)
        diff_curr = (s_long - target_deg) % 360.0
        diff_next = (s_next - target_deg) % 360.0

        crossed = diff_curr > 180.0 and diff_next <= 180.0
        if crossed:
            lo, hi = jd, jd + 1.0
            for _ in range(35):
                mid = (lo + hi) / 2.0
                curr, _ = sidereal_longitudes(mid)
                d = (curr - target_deg) % 360.0
                if d < 180.0: hi = mid
                else: lo = mid
            return jd_to_local(hi)
        jd += 1.0

    return jd_to_local(jd)


def find_new_moon_before(ref_instant: datetime, lookback_days: int = 40) -> datetime:
    jd = to_jd_ut(ref_instant)
    step = 1.0 / 24.0
    prev_diff = None
    prev_jd = jd
    total_hours = lookback_days * 24
    for _ in range(total_hours):
        s, m = sidereal_longitudes(jd)
        diff = (m - s) % 360.0
        if prev_diff is not None and prev_diff < 60.0 and diff > 300.0:
            lo, hi = jd, prev_jd
            for _ in range(40):
                mid = (lo + hi) / 2.0
                s2, m2 = sidereal_longitudes(mid)
                dmid = (m2 - s2) % 360.0
                if dmid > 300.0: lo = mid
                else: hi = mid
            return jd_to_local(hi)
        prev_diff = diff
        prev_jd = jd
        jd -= step

    return ref_instant - timedelta(days=29.5)


def find_chaitra_shukla_pratipada(target_date: date, lat: float = 23.1793, lon: float = 75.7849) -> date:
    year = target_date.year
    mesha_ingress = find_solar_ingress(0.0, date(year, 4, 10))
    new_moon = find_new_moon_before(mesha_ingress)
    nm_date = new_moon.date()

    for offset in range(0, 4):
        d = nm_date + timedelta(days=offset)
        jd_sun = get_sunrise_jd(d, lat, lon)
        s, m = sidereal_longitudes(jd_sun)
        diff = (m - s) % 360.0
        if 0.0 <= diff < 12.0:
            return d

    return nm_date + timedelta(days=1)


def get_vedic_weekday_from_dt(dt_local: datetime, lat: float = 23.1793, lon: float = 75.7849) -> str:
    d = dt_local.date()
    jd_sun = get_sunrise_jd(d, lat, lon)
    sunrise_dt = jd_to_local(jd_sun)
    
    if dt_local < sunrise_dt:
        effective_date = d - timedelta(days=1)
    else:
        effective_date = d
        
    return weekday_lord(effective_date)


# ==============================================================================
# ৩. ত্রিভাষিক বিক্রম সংবৎ মন্ত্রিসভা গণনা ইঞ্জিন (TRI-LINGUAL MANTRI MANDALA)
# ==============================================================================

def compute_mantri_mandala(
    for_date: date,
    lat: float = 23.1793,
    lon: float = 75.7849,
    lang: str = "en"
) -> List[Dict[str, Any]]:
    """
    Computes canonical Vikram Samvat 10-office Planetary Cabinet dynamically in EN, HI & BN.
    """
    l_str = str(lang).lower().strip()
    if l_str.startswith("bn") or "বাংলা" in l_str:
        lang_key = "bn"
    elif l_str.startswith("hi") or "हि" in l_str:
        lang_key = "hi"
    else:
        lang_key = "en"

    # ১. চৈত্র শুক্ল প্রতিপদ (নববর্ষের দিন)
    new_year_day = find_chaitra_shukla_pratipada(for_date, lat, lon)
    year = new_year_day.year

    # ২. সৌর সংক্রান্তি ও নক্ষত্র প্রবেশ সময়সূচী (পরবর্তী ক্যালেন্ডার বছর সমন্বয়সহ)
    mesha_dt = find_solar_ingress(0.0, date(year, 4, 10))            # মেষ সংক্রান্তি (০°)
    mithun_dt = find_solar_ingress(60.0, date(year, 6, 10))          # মিথুন সংক্রান্তি (৬০°)
    ardra_dt = find_solar_ingress(66.66667, date(year, 6, 15))      # আদ্রা নক্ষত্র প্রবেশ (৬৬° ৪০')
    karka_dt = find_solar_ingress(90.0, date(year, 7, 10))           # কর্কট সংক্রান্তি (৯০°)
    simha_dt = find_solar_ingress(120.0, date(year, 8, 10))          # সিংহ সংক্রান্তি (১২০°)
    tula_dt = find_solar_ingress(180.0, date(year, 10, 10))          # তুলা সংক্রান্তি (১৮০°)
    dhanu_dt = find_solar_ingress(240.0, date(year, 12, 10))         # ধনু সংক্রান্তি (২৪০°)
    makar_dt = find_solar_ingress(270.0, date(year + 1, 1, 10))      # মকর সংক্রান্তি (২৭০° - পরবর্তী জানুয়ারি)
    kumbha_dt = find_solar_ingress(300.0, date(year + 1, 2, 10))     # কুম্ভ সংক্রান্তি (৩০০° - পরবর্তী ফেব্রুয়ারি)

    # ৩. ১০টি দপ্তরের টাইমলাইন
    ingresses = [
        {"id": 1, "dt": datetime(new_year_day.year, new_year_day.month, new_year_day.day, 12, 0, tzinfo=IST)},
        {"id": 2, "dt": mesha_dt},
        {"id": 3, "dt": simha_dt},
        {"id": 4, "dt": karka_dt},
        {"id": 5, "dt": dhanu_dt},
        {"id": 6, "dt": ardra_dt},
        {"id": 7, "dt": tula_dt},
        {"id": 8, "dt": mithun_dt},
        {"id": 9, "dt": kumbha_dt},
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
