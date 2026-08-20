"""
muhurta.py
Calculates Kaal periods (Rahu / Gulika / Yamaganda), Choghadiya,
Muhurtas (Abhijit, Brahma, Vijaya, Durmuhurat, Amrit Kaal, Varjyam),
and Samvatsara naming strictly derived from local astronomical events.
"""

from __future__ import annotations
from datetime import datetime, timedelta

def vedic_weekday(dt: datetime) -> int:
    """0 = Sunday, 1 = Monday, ..., 6 = Saturday"""
    return (dt.weekday() + 1) % 7

# Standard 1/8th Day Segments (1 to 8)
RAHU_SEGMENTS      = {0: 8, 1: 2, 2: 7, 3: 5, 4: 6, 5: 4, 6: 3}
GULIKA_SEGMENTS    = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
YAMAGANDA_SEGMENTS = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 7, 6: 6}

# Nakshatra Varjyam and Amrit Kaal offsets in Ghatis (1 Ghati = 24 mins / 1/60th of Nakshatra)
NAKSHATRA_VARJYAM_GHATIS = [
    50, 24, 30, 40, 14, 21, 30, 20, 32, 30, 20, 18,
    21, 20, 14, 14, 10, 14, 56, 24, 20, 10, 10, 18,
    16, 24, 30
]

NAKSHATRA_AMRIT_GHATIS = [
    42, 48, 54, 52, 38, 35, 54, 44, 56, 54, 48, 48,
    45, 45, 38, 38, 34, 38, 52, 44, 44, 34, 34, 42,
    44, 48, 54
]

CHOGHADIYA_CYCLE = ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]
CHOGHADIYA_FIRST_DAY = {0: "Udveg", 1: "Amrit", 2: "Rog", 3: "Labh", 4: "Shubh", 5: "Char", 6: "Kaal"}
CHOGHADIYA_FIRST_NIGHT = {0: "Shubh", 1: "Char", 2: "Kaal", 3: "Udveg", 4: "Amrit", 5: "Rog", 6: "Labh"}
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
    day_duration = sunset - sunrise
    segment_duration = day_duration / 8.0

    def get_period(seg_num: int) -> dict:
        st = sunrise + segment_duration * (seg_num - 1)
        en = sunrise + segment_duration * seg_num
        return {"start": _fmt(st), "end": _fmt(en)}

    return {
        "rahu_kaal": get_period(RAHU_SEGMENTS[weekday_idx]),
        "gulika_kaal": get_period(GULIKA_SEGMENTS[weekday_idx]),
        "yamaganda_kaal": get_period(YAMAGANDA_SEGMENTS[weekday_idx])
    }


def compute_muhurtas(sunrise: datetime, sunset: datetime, weekday_idx: int,
                     nak_idx: int, nak_start: datetime | None, nak_end: datetime | None) -> dict:
    day_duration = sunset - sunrise
    muhurta_len = day_duration / 15.0

    # Brahma Muhurta: 96 to 48 mins before sunrise
    brahma_start = sunrise - timedelta(minutes=96)
    brahma_end = sunrise - timedelta(minutes=48)

    # Abhijit Muhurta: 8th Muhurta
    abhijit_start = sunrise + muhurta_len * 7
    abhijit_end = sunrise + muhurta_len * 8

    # Vijaya Muhurta: 11th Muhurta
    vijaya_start = sunrise + muhurta_len * 10
    vijaya_end = sunrise + muhurta_len * 11

    # Durmuhurta Slots (1-based index)
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

    # Varjyam & Amrit Kaal relative to Nakshatra duration
    ref_nak_start = nak_start or (sunrise - timedelta(hours=6))
    ref_nak_end = nak_end or (sunrise + timedelta(hours=18))
    nak_duration = ref_nak_end - ref_nak_start
    ghati_unit = nak_duration / 60.0

    varjyam_ghati = NAKSHATRA_VARJYAM_GHATIS[nak_idx % 27]
    varjyam_start = ref_nak_start + ghati_unit * varjyam_ghati
    varjyam_end = varjyam_start + ghati_unit * 4.0  # 4 Ghatis duration

    amrit_ghati = NAKSHATRA_AMRIT_GHATIS[nak_idx % 27]
    amrit_start = ref_nak_start + ghati_unit * amrit_ghati
    amrit_end = amrit_start + ghati_unit * 4.0

    return {
        "brahma_muhurta": {"start": _fmt(brahma_start), "end": _fmt(brahma_end)},
        "abhijit_muhurta": {
            "start": _fmt(abhijit_start),
            "end": _fmt(abhijit_end),
            "is_auspicious": weekday_idx != 3
        },
        "vijaya_muhurta": {"start": _fmt(vijaya_start), "end": _fmt(vijaya_end)},
        "durmuhurta": dur_list,
        "amrit_kaal": {"start": _fmt(amrit_start), "end": _fmt(amrit_end)},
        "varjyam": {"start": _fmt(varjyam_start), "end": _fmt(varjyam_end)}
    }


def compute_choghadiya(sunrise: datetime, sunset: datetime, next_sunrise: datetime, weekday_idx: int) -> dict:
    day_slot = (sunset - sunrise) / 8.0
    night_slot = (next_sunrise - sunset) / 8.0

    start_idx_day = CHOGHADIYA_CYCLE.index(CHOGHADIYA_FIRST_DAY[weekday_idx])
    start_idx_night = CHOGHADIYA_CYCLE.index(CHOGHADIYA_FIRST_NIGHT[weekday_idx])

    day_periods = [
        {
            "name": CHOGHADIYA_CYCLE[(start_idx_day + i) % 7],
            "nature": CHOGHADIYA_NATURE[CHOGHADIYA_CYCLE[(start_idx_day + i) % 7]],
            "start": _fmt(sunrise + day_slot * i),
            "end": _fmt(sunrise + day_slot * (i + 1))
        } for i in range(8)
    ]

    night_periods = [
        {
            "name": CHOGHADIYA_CYCLE[(start_idx_night + i) % 7],
            "nature": CHOGHADIYA_NATURE[CHOGHADIYA_CYCLE[(start_idx_night + i) % 7]],
            "start": _fmt(sunset + night_slot * i),
            "end": _fmt(sunset + night_slot * (i + 1))
        } for i in range(8)
    ]

    return {"day": day_periods, "night": night_periods}


def compute_samvatsara(vikram_year: int) -> dict:
    """Computes Jovian 60-year cycle name (North/South Samvatsara)."""
    idx = (vikram_year + 9) % 60
    return {
        "samvatsara_name": SAMVATSARA_NAMES[idx],
        "samvatsara_number": idx + 1,
        "vikram_samvat": vikram_year
    }
