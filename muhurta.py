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

# --- BUG 1: these three tables were conflated ------------------------------
# Segment number (1-8) of the daytime, per weekday (Sun..Sat)
RAHU_SEGMENT      = {0: 8, 1: 2, 2: 7, 3: 5, 4: 6, 5: 4, 6: 3}
GULIKA_SEGMENT    = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
YAMAGANDA_SEGMENT = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 7, 6: 6}

CHOGHADIYA_CYCLE = ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]
CHOGHADIYA_FIRST_DAY = {0: "Udveg", 1: "Amrit", 2: "Rog",
                        3: "Labh", 4: "Shubh", 5: "Char", 6: "Kaal"}
CHOGHADIYA_NATURE = {"Amrit": "good", "Shubh": "good", "Labh": "good",
                     "Char": "neutral", "Udveg": "bad", "Kaal": "bad", "Rog": "bad"}
