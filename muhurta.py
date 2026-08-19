"""
muhurta.py
Kaal (Rahu / Gulika / Yamaganda), Choghadiya, Muhurta (Abhijit / Durmuhurat)
and Samvatsara naming. All segment boundaries derive from the location's own
sunrise/sunset, so nothing is hard-coded to a meridian.
"""

from __future__ import annotations
from datetime import datetime, timedelta

# Vedic weekday index: 0 = Sunday ... 6 = Saturday
def vedic_weekday(d) -> int:
    return (d.weekday() + 1) % 7


# Segment number (1-8) of the daytime, per weekday (Sun..Sat)
RAHU_SEGMENT      = {0: 8, 1: 2, 2: 7, 3: 5, 4: 6, 5: 4, 6: 3}
GULIKA_SEGMENT    = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
YAMAGANDA_SEGMENT = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 7, 6: 6}

CHOGHADIYA_CYCLE = ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]
CHOGHADIYA_FIRST_DAY = {
    0: "Udveg", 1: "Amrit", 2: "Rog",
    3: "Labh", 4: "Shubh", 5: "Char", 6: "Kaal"
}
CHOGHADIYA_FIRST_NIGHT = {
    0: "Shubh", 1: "Char", 2: "Kaal",
    3: "Udveg", 4: "Amrit", 5: "Rog", 6: "Labh"
}
CHOGHADIYA_NATURE = {
    "Amrit": "good", "Shubh": "good", "Labh": "good",
    "Char": "neutral", "Udveg": "bad", "Kaal": "bad", "Rog": "bad"
}

SAMVATSARA_NAMES = [
    "Prabhava", "Vibhava", "Shukla", "Pramoda", "Prajapati", "Angirasa",
    "Shrimukha", "Bhava", "Yuva", "Dhatri", "Ishvara", "Bahudhanya",
    "Pramathi", "Vikrama", "Vrushaprajapati", "Chitrabhanu", "Subhanu",
    "Tarana", "Parthiva", "Vyaya", "Sarvajit", "Sarvadhari", "Virodhi",
    "Vikrita", "Khara", "Nandana", "Vijaya", "Jaya", "Manmatha",
    "Durmukha", "Hemalamba", "Vilamba", "Vikari", "Sharvari", "Plava",
    "Shubhakrita", "Shobhakrita", "Krodhi", "Vishvavasu", "Parabhava",
    "Plavanga", "Kilaka", "Saumya", "Sadharana", "Virodhakrita", "Paridhavi",
    "Pramadicha", "Ananda", "Rakshasa", "Anala", "Pingala", "Kalayukta",
    "Siddharthi", "Raudra", "Durmati", "Dundubhi", "Rudhirodgari",
    "Raktakshi", "Krodhana", "Kshaya"
]


def _fmt(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %I:%M:%S %p")


def compute_kaal_periods(sunrise: datetime, sunset: datetime, weekday_idx: int) -> dict:
    """Calculates Rahu Kaal, Gulika Kaal, and Yamaganda Kaal periods."""
    day_duration = sunset - sunrise
    segment_duration = day_duration / 8

    def get_period(segment_num: int) -> dict:
        start = sunrise + segment_duration * (segment_num - 1)
        end = sunrise + segment_duration * segment_num
        return {"start": _fmt(start), "end": _fmt(end)}

    return {
        "rahu_kaal": get_period(RAHU_SEGMENT[weekday_idx]),
        "gulika_kaal": get_period(GULIKA_SEGMENT[weekday_idx]),
        "yamaganda_kaal": get_period(YAMAGANDA_SEGMENT[weekday_idx])
    }


def compute_choghadiya(sunrise: datetime, sunset: datetime, next_sunrise: datetime, weekday_idx: int) -> dict:
    """Calculates Day and Night Choghadiya intervals."""
    day_slot = (sunset - sunrise) / 8
    night_slot = (next_sunrise - sunset) / 8

    first_day_chog = CHOGHADIYA_FIRST_DAY[weekday_idx]
    start_idx_day = CHOGHADIYA_CYCLE.index(first_day_chog)

    day_periods = []
    for i in range(8):
        name = CHOGHADIYA_CYCLE[(start_idx_day + i) % 7]
        st = sunrise + day_slot * i
        en = sunrise + day_slot * (i + 1)
        day_periods.append({
            "name": name,
            "nature": CHOGHADIYA_NATURE[name],
            "start": _fmt(st),
            "end": _fmt(en)
        })

    first_night_chog = CHOGHADIYA_FIRST_NIGHT[weekday_idx]
    start_idx_night = CHOGHADIYA_CYCLE.index(first_night_chog)

    night_periods = []
    for i in range(8):
        name = CHOGHADIYA_CYCLE[(start_idx_night + i) % 7]
        st = sunset + night_slot * i
        en = sunset + night_slot * (i + 1)
        night_periods.append({
            "name": name,
            "nature": CHOGHADIYA_NATURE[name],
            "start": _fmt(st),
            "end": _fmt(en)
        })

    return {"day": day_periods, "night": night_periods}


def compute_muhurtas(sunrise: datetime, sunset: datetime, weekday_idx: int) -> dict:
    """Calculates key Muhurtas (Abhijit, Durmuhurat, Brahma Muhurta, etc.)."""
    day_duration = sunset - sunrise
    muhurta_len = day_duration / 15

    # Brahma Muhurta: 2 muhurtas (96 mins approx) before sunrise
    brahma_start = sunrise - timedelta(minutes=96)
    brahma_end = sunrise - timedelta(minutes=48)

    # Abhijit Muhurta: 8th muhurta of the day (not recommended on Wednesday / index 3)
    abhijit_start = sunrise + muhurta_len * 7
    abhijit_end = sunrise + muhurta_len * 8
    abhijit = {
        "start": _fmt(abhijit_start),
        "end": _fmt(abhijit_end),
        "is_auspicious": weekday_idx != 3
    }

    # Durmuhurat slots per weekday
    durmuhurta_slots = {
        0: [14],
        1: [8, 12],
        2: [2, 7],
        3: [8],
        4: [6, 12],
        5: [4, 9],
        6: [1, 2]
    }
    dur_list = []
    for slot in durmuhurta_slots.get(weekday_idx, [8]):
        st = sunrise + muhurta_len * (slot - 1)
        en = sunrise + muhurta_len * slot
        dur_list.append({"start": _fmt(st), "end": _fmt(en)})

    return {
        "brahma_muhurta": {"start": _fmt(brahma_start), "end": _fmt(brahma_end)},
        "abhijit_muhurta": abhijit,
        "durmuhurta": dur_list
    }


def compute_samvatsara(vikram_year: int) -> dict:
    """Computes Jovian 60-year cycle name (North/South Samvatsara)."""
    # 60 Samvatsara index calculation
    idx = (vikram_year + 9) % 60
    return {
        "samvatsara_name": SAMVATSARA_NAMES[idx],
        "samvatsara_number": idx + 1,
        "vikram_samvat": vikram_year
    }
