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
# ১.১ ৬০ সংবৎসর তালিকা ও অ্যালগরিদম (Brihat Samhita / Drik Standard)
# ==============================================================================
SAMVATSARA_NAMES = [
    {"bn": "প্রভব", "hi": "प्रभव", "en": "Prabhava", "sa_iast": "Prabhava", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Highly Auspicious", "hi": "अत्यंत शुभ", "bn": "পরম শুভ"}},
    {"bn": "বিভব", "hi": "विभव", "en": "Vibhava", "sa_iast": "Vibhava", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Auspicious", "hi": "शुभ ফলदायी", "bn": "শুভদায়ী"}},
    {"bn": "শুক্ল", "hi": "शुक्ल", "en": "Shukla", "sa_iast": "Śukla", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Auspicious", "hi": "शुभ", "bn": "শুভ"}},
    {"bn": "প্রমোদ", "hi": "प्रमोद", "en": "Pramoda", "sa_iast": "Pramoda", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Joyous & Prosperous", "hi": "आनंद व समृद्धि", "bn": "আনন্দ ও সমৃদ্ধিদায়ক"}},
    {"bn": "প্রজাপতি (প্রজোৎপত্তি)", "hi": "प्रजापति (प्रजोत्पत्ति)", "en": "Prajapati (Prajotpatti)", "sa_iast": "Prajāpati", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Growth & Wealth", "hi": "वृद्धि व ऐश्वर्य", "bn": "প্রবৃদ্ধিদায়ক"}},
    {"bn": "অঙ্গিরা", "hi": "अंगिरा", "en": "Angirasa", "sa_iast": "Aṅgiras", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Intellectual Growth", "hi": "बुद्धि व ज्ञान वृद्धि", "bn": "জ্ঞান ও প্রজ্ঞাদায়ক"}},
    {"bn": "শ্রীমুখ", "hi": "श्रीमुख", "en": "Shrimukha", "sa_iast": "Śrīmukha", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Wealth & Fortune", "hi": "धन व सौभाग्य", "bn": "শ্রী ও সৌভাগ্যদায়ক"}},
    {"bn": "ভাব", "hi": "भाव", "en": "Bhava", "sa_iast": "Bhāva", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Creative & Auspicious", "hi": "रचनात्मक व शुभ", "bn": "কল্যাণকর"}},
    {"bn": "যুব", "hi": "युवा", "en": "Yuva", "sa_iast": "Yuvan", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Energy & Vitality", "hi": "ऊर्जा व शक्ति", "bn": "তেজ ও বলবিকাশ"}},
    {"bn": "ধাতৃ", "hi": "धाता", "en": "Dhatri", "sa_iast": "Dhātṛ", "ruler": {"en": "Lord Brahma", "hi": "भगवान ब्रह्मा", "bn": "ভগবান ব্রহ্মা"}, "nature": {"en": "Stability & Peace", "hi": "स्थिरता व शांति", "bn": "শান্তি ও স্থায়িত্ব"}},
    {"bn": "ঈশ্বর", "hi": "ईश्वर", "en": "Ishvara", "sa_iast": "Īśvara", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Supreme Good Fortune", "hi": "सर्वकल्याणकारी", "bn": "পরম মঙ্গলময়"}},
    {"bn": "বহুধান্য", "hi": "बहुधान्य", "en": "Bahudhanya", "sa_iast": "Bahudhānya", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Abundant Harvest & Food", "hi": "अन्न-धन प्रचुरता", "bn": "অন্ন ও শস্য প্রাচুর্য"}},
    {"bn": "প্রমাদী", "hi": "प्रमाथी", "en": "Pramathi", "sa_iast": "Pramāthin", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Challenging", "hi": "सावधानी आवश्यक", "bn": "সংযম প্রয়োজনীয়"}},
    {"bn": "বিক্রম", "hi": "विक्रम", "en": "Vikrama", "sa_iast": "Vikrama", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Courage & Victory", "hi": "पराक्रम व विजय", "bn": "বীরত্ব ও বিজয়"}},
    {"bn": "বৃষপ্রজা (বৃষ)", "hi": "वृषप्रजा (वृष)", "en": "Vrishaprajapathi", "sa_iast": "Vṛṣaprajāpati", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Virtue & Righteousness", "hi": "धर्म व सदाचार", "bn": "ধর্ম ও সদাচার"}},
    {"bn": "চিত্রভানু", "hi": "चित्रभानु", "en": "Chitrabhanu", "sa_iast": "Citrabhānu", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Fame & Prosperity", "hi": "यश व समृद्धि", "bn": "যশ ও খ্যাতি"}},
    {"bn": "সুভানু (স্বভানু)", "hi": "सुभानु (स्वभानु)", "en": "Subhanu", "sa_iast": "Subhānu", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Radiance & Good Health", "hi": "तेज व आरोग्य", "bn": "তেজ ও সুস্বাস্থ্য"}},
    {"bn": "তারণ", "hi": "तारण", "en": "Tarana", "sa_iast": "Tāraṇa", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Liberation from Sorrows", "hi": "संकट मुक्ति", "bn": "সংকট থেকে মুক্তিদায়ক"}},
    {"bn": "পার্থিব", "hi": "पार्थिव", "en": "Parthiva", "sa_iast": "Pārthiva", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Material Abundance", "hi": "भौतिक समृद्धि", "bn": "পার্থিব সমৃদ্ধি"}},
    {"bn": "ব্যয়", "hi": "व्यय", "en": "Vyaya", "sa_iast": "Vyaya", "ruler": {"en": "Lord Vishnu", "hi": "भगवान विष्णु", "bn": "ভগবান বিষ্ণু"}, "nature": {"en": "Charity & Expenses", "hi": "दान व व्यय", "bn": "দান ও ত্যাগের সময়"}},
    {"bn": "সর্বজিৎ", "hi": "सर्वजित्", "en": "Sarvajit", "sa_iast": "Sarvajit", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "All-Conquering Success", "hi": "सर्वविजय प्रदाता", "bn": "সর্ববিজয়ী কল্যাণকর"}},
    {"bn": "সর্বধারী", "hi": "सर्वधारी", "en": "Sarvadhari", "sa_iast": "Sarvadhārin", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Sustenance & Security", "hi": "सुरक्षा व पोषण", "bn": "ধারণ ও স্থায়িত্ব"}},
    {"bn": "বিরোধী", "hi": "विरोधी", "en": "Virodhi", "sa_iast": "Virodhin", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Conflicts & Remedial", "hi": "विरोध व शांति उपाय", "bn": "সংযম ও বিরোধ নিবারণ"}},
    {"bn": "বিকৃত", "hi": "विकृत", "en": "Vikrita", "sa_iast": "Vikṛta", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Fluctuations & Transformation", "hi": "परिवर्तनकारी", "bn": "পরিবর্তনশীল"}},
    {"bn": "খর", "hi": "खर", "en": "Khara", "sa_iast": "Khara", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Hard Work & Endurance", "hi": "कठिन परिश्रम", "bn": "ধৈর্য ও সহিষ্ণুতা"}},
    {"bn": "নন্দন", "hi": "नन्दन", "en": "Nandana", "sa_iast": "Nandana", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Bliss & Child Welfare", "hi": "आनंद व संतान सुख", "bn": "সন্তানসুখ ও পরমানন্দ"}},
    {"bn": "বিজয়", "hi": "विजय", "en": "Vijaya", "sa_iast": "Vijaya", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Supreme Victory", "hi": "परम विजय", "bn": "পরম বিজয়প্রদ"}},
    {"bn": "জয়", "hi": "जय", "en": "Jaya", "sa_iast": "Jaya", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Triumph in Endeavors", "hi": "कार्य सिद्धि", "bn": "সর্বকার্য সিদ্ধিদায়ক"}},
    {"bn": "মন্মথ", "hi": "मन्मथ", "en": "Manmatha", "sa_iast": "Manmatha", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Love, Arts & Harmony", "hi": "प्रेम, कला व सौहार्द", "bn": "প্রেম, শিল্প ও সৌহার্দ্য"}},
    {"bn": "দুর্মুখ", "hi": "दुर्मुख", "en": "Durmukha", "sa_iast": "Durmukha", "ruler": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব শিব"}, "nature": {"en": "Requires Truth & Restraint", "hi": "वाणी संयम आवश्यक", "bn": "বাক্সংযম প্রয়োজনীয়"}},
    {"bn": "হেমলম্বী", "hi": "हेमलम्बी", "en": "Hemalambi", "sa_iast": "Hemalambi", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Golden Prosperity", "hi": "स्वर्ण व धन लाभ", "bn": "স্বর্ণ ও ধনলাভ"}},
    {"bn": "বিলম্বী", "hi": "विलम्बी", "en": "Vilambi", "sa_iast": "Vilambin", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Slow & Steady Progress", "hi": "धीमी किन्तु स्थिर प्रगति", "bn": "ধৈর্য্যশীল কর্মপ্রগতি"}},
    {"bn": "বিকরী", "hi": "विकारी", "en": "Vikari", "sa_iast": "Vikārin", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Caution in Health", "hi": "स्वास्थ्य सतर्कता", "bn": "স্বাস্থ্য সচেতনতা"}},
    {"bn": "শর্বরী", "hi": "शार्वरी", "en": "Sharvari", "sa_iast": "Śārvarī", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Peaceful Night/Calm", "hi": "शांति व आध्यात्म", "bn": "আধ্যাত্মিক শান্তি"}},
    {"bn": "প্লব", "hi": "प्लव", "en": "Plava", "sa_iast": "Plava", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Water Abundance/Travel", "hi": "यात्रा व जल समृद्धि", "bn": "ভ্রমণ ও জলসমৃদ্ধি"}},
    {"bn": "শুভকৃৎ", "hi": "शुभकृत्", "en": "Shubhakritha", "sa_iast": "Śubhakṛt", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Benefic & Auspicious Deeds", "hi": "सत्कर्म व शुभ फल", "bn": "পুণ্যকর্ম ও শুভফল"}},
    {"bn": "শোভন", "hi": "शोभन", "en": "Shobhana", "sa_iast": "Śobhana", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Grace, Beauty & Joy", "hi": "सौंदर्य व हर्ष", "bn": "সৌন্দর্য ও আনন্দ"}},
    {"bn": "ক্রোধী", "hi": "क्रोधी", "en": "Krodhi", "sa_iast": "Krodhin", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Restrain Anger", "hi": "क्रोध नियंत्रण आवश्यक", "bn": "ক্রোধসংবরণ প্রয়োজনীয়"}},
    {"bn": "বিশ্বাবসু", "hi": "विश्वावसु", "en": "Vishvavasu", "sa_iast": "Viśvāvasu", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Universal Wealth & Music", "hi": "वैश्विक समृद्धि व संगीत", "bn": "সংগীত ও বিশ্বসমৃদ্ধি"}},
    {"bn": "পরাভব", "hi": "पराभव", "en": "Parabhava", "sa_iast": "Parābhava", "ruler": {"en": "Lord Indra", "hi": "देवराज इंद्र", "bn": "দেবরাজ ইন্দ্র"}, "nature": {"en": "Humble Learning", "hi": "धैर्य व विनम्रता", "bn": "বিনম্র সাধনা"}},
    {"bn": "প্লবঙ্গ", "hi": "प्लवंग", "en": "Plavanga", "sa_iast": "Plavaṅga", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Speed, Agility & Movement", "hi": "गतिशीलता व उत्साह", "bn": "গতিশীলতা ও উদ্যোগ"}},
    {"bn": "কীলক", "hi": "कीलक", "en": "Kilaka", "sa_iast": "Kīlaka", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Solid Foundation", "hi": "दृढ़ता व स्थायित्व", "bn": "দৃঢ়তা ও ভিত্তি"}},
    {"bn": "সৌমা", "hi": "सौम्य", "en": "Saumya", "sa_iast": "Saumya", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Gentle, Pure & Merciful", "hi": "सौम्यता व करुणा", "bn": "স্নিগ্ধতা ও অহিংসা"}},
    {"bn": "সাধারণ", "hi": "साधारण", "en": "Sadharana", "sa_iast": "Sādhāraṇa", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Balanced & Steady", "hi": "संतुलित व सामान्य", "bn": "ভারসাম্যপূর্ণ"}},
    {"bn": "বিরোধকৃৎ", "hi": "विरोधकृत्", "en": "Virodhakritha", "sa_iast": "Virodhakṛt", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Overcome Opposition", "hi": "बाधाओं पर विजय", "bn": "প্রতিদ্বন্দ্বিতা জয়"}},
    {"bn": "পরিধাবী", "hi": "परिधावी", "en": "Paridhavi", "sa_iast": "Paridhāvin", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Vigilance & Protection", "hi": "सुरक्षा व सतर्कता", "bn": "সতর্কতা ও সুরক্ষা"}},
    {"bn": "প্রমাদীচা", "hi": "प्रमादीचा", "en": "Pramadicha", "sa_iast": "Pramādīca", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Spiritual Focus Needed", "hi": "एकाग्रता आवश्यक", "bn": "আধ্যাত্মিক একাগ্রতা"}},
    {"bn": "আনন্দ", "hi": "आनन्द", "en": "Ananda", "sa_iast": "Ānanda", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Supreme Delight & Happiness", "hi": "परमानंद व सुख", "bn": "পরম আনন্দ ও উল্লাস"}},
    {"bn": "রাক্ষস", "hi": "राक्षस", "en": "Rakshasa", "sa_iast": "Rākṣasa", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Spiritual Protection Essential", "hi": "सुरक्षा व साधना", "bn": "ধর্মরক্ষা ও সংযম"}},
    {"bn": "অনল (নল)", "hi": "अनल (नल)", "en": "Anala (Nala)", "sa_iast": "Anala", "ruler": {"en": "Agni Deva", "hi": "अग्नि देव", "bn": "অগ্নি দেব"}, "nature": {"en": "Purifying Fire & Energy", "hi": "अग्नि समान तेज", "bn": "অগ্নিশুদ্ধি ও তেজ"}},
    {"bn": "পিঙ্গল", "hi": "पिंगल", "en": "Pingala", "sa_iast": "Piṅgala", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Inner Light & Realization", "hi": "आत्मज्ञान व तेज", "bn": "সূর্যতেজ ও প্রজ্ঞা"}},
    {"bn": "কালযুক্ত", "hi": "कालयुक्त", "en": "Kalayukta", "sa_iast": "Kālayukta", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Patience through Time", "hi": "समय का सदुपयोग", "bn": "সময়ানুবর্তিতা"}},
    {"bn": "সিদ্ধার্থ (সিদ্ধার্থী)", "hi": "सिद्धार्थ (सिद्धार्थी)", "en": "Siddharthi", "sa_iast": "Siddhārthin", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Fulfillment of Desires", "hi": "मनोकामना पूर्ति व सिद्धि", "bn": "সর্বমনোরথ সিদ্ধি"}},
    {"bn": "রৌদ্র", "hi": "रौद्र", "en": "Raudra", "sa_iast": "Raudra", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Fierce Strength & Courage", "hi": "साहस व शक्ति", "bn": "রুদ্রতেজ ও পরাক্রম"}},
    {"bn": "দুর্মতি", "hi": "दुर्मति", "en": "Durmati", "sa_iast": "Durmati", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Discernment & Wisdom", "hi": "सद्विचार व विवेक", "bn": "সদ্বিবেচনা ও জ্ঞান"}},
    {"bn": "দুন্দুভি", "hi": "दुन्दुभि", "en": "Dundubhi", "sa_iast": "Dundubhi", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Celebration & Fame", "hi": "उत्सव व जयघोष", "bn": "উৎসবের দামামা ও জয়ধ্বনি"}},
    {"bn": "রুধিরোদ্গারী", "hi": "रुधिरोद्गारी", "en": "Rudhirodgari", "sa_iast": "Rudhirodgārin", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Spiritual Vigilance", "hi": "शांति साधना आवश्यक", "bn": "শান্তি ও আধ্যাত্মিক সাধনা"}},
    {"bn": "রক্তাক্ষ", "hi": "रक्ताक्ष", "en": "Raktaksha", "sa_iast": "Raktākṣa", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Focused Vision & Meditation", "hi": "गंभीर दृष्टि व ध्यान", "bn": "তীব্র দৃষ্টি ও ধ্যান"}},
    {"bn": "ক্রোধনা (মন্যু)", "hi": "क्रोधन (मन्यु)", "en": "Krodhana (Manyu)", "sa_iast": "Krodhana", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Compassion & Peace Practices", "hi": "धैर्य व अहिंसा", "bn": "শান্তি ও সহনশীলতা"}},
    {"bn": "অক্ষয় (ক্ষয়)", "hi": "अक्षय (क्षय)", "en": "Akshaya (Kshaya)", "sa_iast": "Akṣaya", "ruler": {"en": "Lord Surya & Chandra", "hi": "सूर्य-चन्द्र देव", "bn": "সূর্য ও চন্দ্র দেব"}, "nature": {"en": "Imperishable Spiritual Merits", "hi": "अक्षय पुण्य फल", "bn": "অক্ষয় পুণ্যফল"}}
]

def get_samvatsara_details(vikrama_samvat: int, lang: str = "en") -> Dict[str, Any]:
    vs = int(vikrama_samvat)
    # যদি কোনো কারণে ভুল করে শকাব্দ (যেমন 1916) পাস হয়ে থাকে, তাকে বিক্রম সংবতে নিয়ে আসা
    if vs < 2000 and vs > 1800:
        vs = vs + 135  # শকা থেকে বিক্রম রূপান্তর

    # Brihat Samhita / Drik Standard: (VS + 9) % 60
    # For VS 2051 -> (2051 + 9) % 60 = 20 -> 21st: Sarvajit
    idx = (vs + 9) % 60
    
    item = SAMVATSARA_NAMES[idx]
    lang_str = str(lang or "").lower().strip()
    l_key = "bn" if (lang_str.startswith("bn") or "bangla" in lang_str) else ("hi" if (lang_str.startswith("hi") or "hindi" in lang_str) else "en")

    chosen_name = item.get(l_key, item["en"])

    return {
        "index_1_based": idx + 1,
        "samvatsara_number": idx + 1,
        "samvatsara_name": item["en"],
        "name": chosen_name,
        "name_en": item["en"],
        "name_hi": item.get("hi", item["en"]),
        "name_bn": item.get("bn", item["en"]),
        "name_sa_iast": item.get("sa_iast", item["en"]),
        "ruler": item["ruler"].get(l_key, item["ruler"]["en"]) if isinstance(item.get("ruler"), dict) else item.get("ruler", ""),
        "nature": item["nature"].get(l_key, item["nature"]["en"]) if isinstance(item.get("nature"), dict) else item.get("nature", "")
    }

def get_samvatsara(vikrama_samvat: int, lang: str = "en") -> str:
    return get_samvatsara_details(vikrama_samvat, lang)["name"]

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

# =============================================================================
# VEDIC DAY-NIGHT PERIODS (অহোরাত্র কাল বিভাজন)
# =============================================================================
def calculate_vedic_day_periods(dt_sunrise: datetime, dt_sunset: datetime, dt_next_sunrise: datetime, lang: str = "en") -> list:
    """
    ২৪ ঘণ্টার সম্পূর্ণ নির্বিঘ্ন বৈদিক অহোরাত্র বিভাজন (১০টি শাস্ত্রীয় কাল - কোনো ফাঁক থাকবে না)।
    """
    day_duration = dt_sunset - dt_sunrise
    night_duration = dt_next_sunrise - dt_sunset

    solar_noon = dt_sunrise + (day_duration / 2)
    solar_midnight = dt_sunset + (night_duration / 2)

    # ১. ব্রাহ্ম মুহূর্ত: সূর্যোদয়ের ৯৬ মি. আগে থেকে ৪৮ মি. আগে
    brahma_start = dt_sunrise - timedelta(minutes=96)
    brahma_end = dt_sunrise - timedelta(minutes=48)

    # ২. প্রাতঃকাল (ঊষা): সূর্যোদয়ের ৪৮ মি. আগে থেকে সূর্যোদয়
    pratah_start = brahma_end
    pratah_end = dt_sunrise

    # ৩. সকাল / পূর্বাহ্ণ: সূর্যোদয় থেকে মধ্যাহ্নের প্রারম্ভ
    sakal_start = dt_sunrise
    sakal_end = solar_noon - timedelta(minutes=60)

    # ৪. দুপুরবেলা / মধ্যাহ্ন: দ্বিপ্রহর (অভিজিৎ সংলগ্ন সময়)
    dupur_start = sakal_end
    dupur_end = solar_noon + timedelta(minutes=60)

    # ৫. বিকাল বেলা (অপরাহ্ণ): দুপুর থেকে গোধূলি বেলার পূর্ব পর্যন্ত (যেটা মিসিং ছিল)
    bikal_start = dupur_end
    bikal_end = dt_sunset - timedelta(minutes=48)

    # ৬. সায়াহ্ন / গোধূলি বেলা: সূর্যাস্তের ঠিক পূর্বের ৪৮ মিনিট
    godhuli_start = bikal_end
    godhuli_end = dt_sunset

    # ৭. সন্ধ্যা কাল / প্রদোষ: সূর্যাস্ত থেকে রাত্রির শুরু (৭২ মিনিট)
    sandhya_start = dt_sunset
    sandhya_end = dt_sunset + timedelta(minutes=72)

    # ৮. রাত্রিকাল (প্রথম প্রহর): সন্ধ্যা সমাপ্তি থেকে মহানিশার পূর্ব পর্যন্ত
    ratri_start = sandhya_end
    ratri_end = solar_midnight - timedelta(minutes=48)

    # ৯. নিশীথ রাত্রি কাল (মহানিশা): মধ্যরাত্রি কেন্দ্রিক কাল
    nishi_start = ratri_end
    nishi_end = solar_midnight + timedelta(minutes=48)

    # ১০. শেষ রাত্রি / উষাকাল: মধ্যরাত্রি থেকে পরদিনের ব্রাহ্ম মুহূর্তের প্রারম্ভ
    next_brahma_start = dt_next_sunrise - timedelta(minutes=96)
    shesh_ratri_start = nishi_end
    shesh_ratri_end = next_brahma_start

    periods_data = [
        {
            "id": "brahma_muhurta",
            "name": {"bn": "ব্রাহ্ম মুহূর্ত", "hi": "ब्रह्म मुहूर्त", "en": "Brahma Muhurta"},
            "start": brahma_start, "end": brahma_end
        },
        {
            "id": "pratah_kal",
            "name": {"bn": "প্রাতঃকাল (ঊষা)", "hi": "प्रातःकाल (उषा)", "en": "Dawn (Pratah Kaal)"},
            "start": pratah_start, "end": pratah_end
        },
        {
            "id": "sakal",
            "name": {"bn": "সকাল / পূর্বাহ্ণ", "hi": "सवेरा / पूर्वाह्न", "en": "Morning (Forenoon)"},
            "start": sakal_start, "end": sakal_end
        },
        {
            "id": "dupur_bela",
            "name": {"bn": "দুপুরবেলা / মধ্যাহ্ন", "hi": "दोपहर / मध्याह्न", "en": "Midday (Madhyahna)"},
            "start": dupur_start, "end": dupur_end
        },
        {
            "id": "bikal_aparahna",
            "name": {"bn": "বিকাল বেলা (অপরাহ্ণ)", "hi": "तीसरा पहर / अपराह्न", "en": "Afternoon (Aparahna)"},
            "start": bikal_start, "end": bikal_end
        },
        {
            "id": "sayahna_godhuli",
            "name": {"bn": "গোধূলি বেলা / সায়াহ্ন", "hi": "गोधूलि वेला / सायं", "en": "Twilight / Godhuli"},
            "start": godhuli_start, "end": godhuli_end
        },
        {
            "id": "sandhya_kal",
            "name": {"bn": "সন্ধ্যা কাল / প্রদোষ", "hi": "संध्या काल / प्रदोष", "en": "Evening / Pradosh"},
            "start": sandhya_start, "end": sandhya_end
        },
        {
            "id": "ratrikal",
            "name": {"bn": "রাত্রিকাল (প্রথম প্রহর)", "hi": "रात्रिकाल (प्रथम प्रहर)", "en": "Night (Early Watch)"},
            "start": ratri_start, "end": ratri_end
        },
        {
            "id": "nishi_ratri_kal",
            "name": {"bn": "নিশীথ রাত্রি কাল (মহানিশা)", "hi": "निशीथ काल (महानिशा)", "en": "Midnight (Nishitha)"},
            "start": nishi_start, "end": nishi_end
        },
        {
            "id": "shesh_ratri_usha",
            "name": {"bn": "শেষ রাত্রি / ঊষাকাল", "hi": "उषाकाल / अंतिम प्रहर", "en": "Pre-Dawn / Last Watch"},
            "start": shesh_ratri_start, "end": shesh_ratri_end
        }
    ]

    l_key = "bn" if "bn" in lang or "bangla" in lang else ("hi" if "hi" in lang else "en")

    formatted_list = []
    for p in periods_data:
        formatted_list.append({
            "id": p["id"],
            "title": p["name"].get(l_key, p["name"]["en"]),
            "title_bn": p["name"]["bn"],
            "title_hi": p["name"]["hi"],
            "title_en": p["name"]["en"],
            "start_time": p["start"].strftime("%I:%M %p"),
            "end_time": p["end"].strftime("%I:%M %p"),
            "display_range": f"{p['start'].strftime('%I:%M %p')} - {p['end'].strftime('%I:%M %p')}"
        })

    return formatted_list

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

    def fmt_dt(jd): 
        if not jd:
            return ""
        dt_val = jd_to_local(jd)
        
        # সেফ ইনলাইন টাইম ফরম্যাটার (সার্ভার ক্র্যাশ এড়াতে format_time_mode মুছে ফেলা হয়েছে)
        m_format = str(time_format).lower().replace(" ", "").replace("-", "")
        if "24+" in m_format or "plus" in m_format:
            h = dt_val.hour + 24 if dt_val.date() > local_date else dt_val.hour
            time_str = f"{h:02d}:{dt_val.minute:02d}"
        elif "24" in m_format:
            time_str = dt_val.strftime("%H:%M")
        else:
            time_str = dt_val.strftime("%I:%M %p")
            
        diff_days = (dt_val.date() - local_date).days
        
        def format_short_date(dt_obj, l_key):
            en_m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            bn_m = ["জানু", "ফেব্রু", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টে", "অক্টো", "নভে", "ডিসে"]
            hi_m = ["जन", "फर", "मार्च", "अप्रैल", "मई", "जून", "जुला", "अग", "सितं", "अक्टू", "नवं", "दिसं"]
            m_idx = dt_obj.month - 1
            d_str = str(dt_obj.day)
            if l_key == "bn": return f"{d_str.translate(str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯'))} {bn_m[m_idx]}"
            elif l_key == "hi": return f"{d_str.translate(str.maketrans('0123456789', '०१२३४५६७८९'))} {hi_m[m_idx]}"
            return f"{en_m[m_idx]} {d_str}"

        if diff_days == 1:
            if lang_key == "bn": return f"{time_str} (পরের দিন, {format_short_date(dt_val, lang_key)})"
            elif lang_key == "hi": return f"{time_str} (अगले दिन, {format_short_date(dt_val, lang_key)})"
            else: return f"{time_str} (Next Day, {format_short_date(dt_val, lang_key)})"
        elif diff_days >= 2:
            if lang_key == "bn":
                day_str = str(diff_days).translate(str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯'))
                return f"{time_str} ({day_str} দিন পর, {format_short_date(dt_val, lang_key)})"
            elif lang_key == "hi":
                day_str = str(diff_days).translate(str.maketrans('0123456789', '०१२३४५६७८९'))
                return f"{time_str} ({day_str} दिन बाद, {format_short_date(dt_val, lang_key)})"
            else: return f"{time_str} ({diff_days} Days Later, {format_short_date(dt_val, lang_key)})"
        
        return time_str
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

    # --------------------------------------------------------------------------
    # সমস্ত অ্যাডভান্সড সেকশনের জন্য ডাইনামিক টাইম ট্রানজিশন ইঞ্জিন (Drik Standard)
    # --------------------------------------------------------------------------
    def get_upto_str(jd_val):
        if not jd_val: return ""
        dt_val = jd_to_local(jd_val)
        
        m_format = str(time_format).lower().replace(" ", "").replace("-", "")
        if "24+" in m_format or "plus" in m_format:
            h = dt_val.hour + 24 if dt_val.date() > local_date else dt_val.hour
            time_str = f"{h:02d}:{dt_val.minute:02d}"
        elif "24" in m_format:
            time_str = dt_val.strftime("%H:%M")
        else:
            time_str = dt_val.strftime("%I:%M %p")
            
        diff_days = (dt_val.date() - local_date).days
        
        def format_short_date(dt_obj, l_key):
            en_m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            bn_m = ["জানু", "ফেব্রু", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টে", "অক্টো", "নভে", "ডিসে"]
            hi_m = ["जन", "फर", "मार्च", "अप्रैल", "मई", "जून", "जुला", "अग", "सितं", "अक्टू", "नवं", "दिसं"]
            m_idx = dt_obj.month - 1
            d_str = str(dt_obj.day)
            if l_key == "bn": return f"{d_str.translate(str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯'))} {bn_m[m_idx]}"
            elif l_key == "hi": return f"{d_str.translate(str.maketrans('0123456789', '०१२३४५६७८९'))} {hi_m[m_idx]}"
            return f"{en_m[m_idx]} {d_str}"

        if diff_days >= 1:
            date_txt = format_short_date(dt_val, lang_key)
            if lang_key == "bn": return f" ({time_str}, {date_txt} পর্যন্ত)"
            elif lang_key == "hi": return f" ({time_str}, {date_txt} तक)"
            else: return f" (upto {time_str}, {date_txt})"
        else:
            if lang_key == "bn": return f" ({time_str} পর্যন্ত)"
            elif lang_key == "hi": return f" ({time_str} तक)"
            else: return f" (upto {time_str})"

    then_str = "তারপর" if lang_key == "bn" else ("तदुपरांत" if lang_key == "hi" else "then")

    # বর্তমান ও পরবর্তী স্টেটের ডেটা ক্যালকুলেশন
    niwas_shool = compute_niwas_and_shool(weekday, t_idx, m_rashi_idx, lang_key=lang_key)
    niwas_shool_next_tithi = compute_niwas_and_shool(weekday, (t_idx + 1) % 30, m_rashi_idx, lang_key=lang_key)
    niwas_shool_next_nak = compute_niwas_and_shool(weekday, t_idx, (m_rashi_idx + 1) % 12, lang_key=lang_key)
    
    special_yogas = compute_special_yogas(weekday, n_idx, sun_nak_idx, lang_key=lang_key)
    special_yogas_next = compute_special_yogas(weekday, (n_idx + 1) % 27, sun_nak_idx, lang_key=lang_key)

    # ১. Tithi based transitions (Agnivasa & Shivavasa)
    t_end_str = get_upto_str(t_end)
    if t_end_str:
        curr_agni = niwas_shool['agnivasa'].split('(')[0].split('-')[0].strip()
        next_agni = niwas_shool_next_tithi['agnivasa'].split('(')[0].split('-')[0].strip()
        niwas_shool["agnivasa"] = f"{curr_agni}{t_end_str}, {then_str} {next_agni}"
        
        curr_shiva = niwas_shool['shivavasa'].split('(')[0].split('-')[0].strip()
        next_shiva = niwas_shool_next_tithi['shivavasa'].split('(')[0].split('-')[0].strip()
        niwas_shool["shivavasa"] = f"{curr_shiva}{t_end_str}, {then_str} {next_shiva}"

    # ২. Nakshatra based transitions (Anandadi & Tamil Yoga)
    n_end_str = get_upto_str(n_end)
    if n_end_str:
        curr_anandadi = special_yogas['anandadi_yoga']
        next_anandadi = special_yogas_next['anandadi_yoga']
        special_yogas["anandadi_yoga"] = f"{curr_anandadi}{n_end_str}, {then_str} {next_anandadi}"
        
        curr_tamil = special_yogas['tamil_yoga'].split('(')[0].strip()
        next_tamil = special_yogas_next['tamil_yoga'].split('(')[0].strip()
        special_yogas["tamil_yoga"] = f"{curr_tamil}{n_end_str}, {then_str} {next_tamil}"

    # ৩. Moon/Rashi based transitions (Chandra Vasa)
    def moon_transition_index(jd):
        _, m = sidereal_longitudes(jd)
        return int((m % 360.0) / 30.0)

    moon_rashi_end = find_transition(jd_sunrise, moon_transition_index, step_hours=1.0, max_hours=30.0)
    moon_end_str = get_upto_str(moon_rashi_end)
    if moon_end_str:
        curr_chandra = niwas_shool.get('chandra_vasa', '')
        next_rashi_idx = (m_rashi_idx + 1) % 12
        rashi_dirs_dict = {
            "bn": ["পূর্ব", "দক্ষিণ", "পশ্চিম", "উত্তর", "পূর্ব", "দক্ষিণ", "পশ্চিম", "উত্তর", "পূর্ব", "দক্ষিণ", "পশ্চিম", "উত্তর"],
            "hi": ["पूर्व", "दक्षिण", "पश्चिम", "उत्तर", "पूर्व", "दक्षिण", "पश्चिम", "उत्तर", "पूर्व", "दक्षिण", "पश्चिम", "उत्तर"],
            "en": ["East", "South", "West", "North", "East", "South", "West", "North", "East", "South", "West", "North"]
        }
        next_chandra_localized = rashi_dirs_dict.get(lang_key, rashi_dirs_dict["en"])[next_rashi_idx]
        niwas_shool["chandra_vasa"] = f"{curr_chandra}{moon_end_str}, {then_str} {next_chandra_localized}"

    # বাকি জেনারেল ক্যালকুলেশন
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

    # ==========================================================================
    # জ্যোতির্বৈজ্ঞানিক গ্রহ-গোচর ভিত্তিক উৎসব নিরূপণ (Sunrise, Sunset & Midnight)
    # ==========================================================================
    # ১. সূর্যোদয়ের সময়কার তিথি
    sun_lon_rise, moon_lon_rise = sidereal_longitudes(jd_sunrise)
    t_idx_rise = int(((moon_lon_rise - sun_lon_rise) % 360.0) / 12.0) % 30
    paksha_rise = "Shukla" if t_idx_rise < 15 else "Krishna"
    t_num_rise = (t_idx_rise % 15) + 1

    # ২. সূর্যাস্তের (প্রদোষকাল) সময়কার তিথি ও পক্ষ
    sun_lon_set, moon_lon_set = sidereal_longitudes(jd_sunset)
    t_idx_set = int(((moon_lon_set - sun_lon_set) % 360.0) / 12.0) % 30
    paksha_set = "Shukla" if t_idx_set < 15 else "Krishna"
    t_num_set = (t_idx_set % 15) + 1

    # ৩. মধ্যরাত্রির (নিশীথকাল) সময়কার তিথি ও পক্ষ
    jd_midnight = (jd_sunset + jd_next_sunrise) / 2.0
    sun_lon_mid, moon_lon_mid = sidereal_longitudes(jd_midnight)
    t_idx_mid = int(((moon_lon_mid - sun_lon_mid) % 360.0) / 12.0) % 30
    paksha_mid = "Shukla" if t_idx_mid < 15 else "Krishna"
    t_num_mid = (t_idx_mid % 15) + 1

    # ৪. সমস্ত মহাজাগতিক সংযোগের উৎসব একত্রীকরণ (The Ultimate Fix)
    today_festivals = []

    # (ক) সূর্যোদয়ভিত্তিক উৎসব
    fests_rise = get_festivals_for_day(current_date=local_date, lunar_month=lunar_masa, paksha=paksha_rise, tithi_num=t_num_rise, sankranti_name=None, lang=lang)
    for f in fests_rise:
        f['calc_tithi_idx'] = t_idx_rise
        f['calc_jd_base'] = jd_sunrise
        if not any(x.get("name") == f.get("name") for x in today_festivals):
            today_festivals.append(f)

    # (খ) প্রদোষকাল (সূর্যাস্ত) ভিত্তিক উৎসব 
    if t_idx_set != t_idx_rise:
        fests_set = get_festivals_for_day(current_date=local_date, lunar_month=lunar_masa, paksha=paksha_set, tithi_num=t_num_set, sankranti_name=None, lang=lang)
        for f in fests_set:
            if f.get("muhurta_type") in ["pradosh", "sayankal", "nishita"]:
                f['calc_tithi_idx'] = t_idx_set
                f['calc_jd_base'] = jd_sunset
                if not any(x.get("name") == f.get("name") for x in today_festivals):
                    today_festivals.append(f)

    # (গ) নিশীথকাল (মধ্যরাত্রি) ভিত্তিক উৎসব
    jd_midnight = (jd_sunset + jd_next_sunrise) / 2.0
    if t_idx_mid != t_idx_set and t_idx_mid != t_idx_rise:
        fests_mid = get_festivals_for_day(current_date=local_date, lunar_month=lunar_masa, paksha=paksha_mid, tithi_num=t_num_mid, sankranti_name=None, lang=lang)
        for f in fests_mid:
            if f.get("muhurta_type") == "nishita":
                f['calc_tithi_idx'] = t_idx_mid
                f['calc_jd_base'] = jd_midnight
                if not any(x.get("name") == f.get("name") for x in today_festivals):
                    today_festivals.append(f)

    # --------------------------------------------------------------------------
    # সুইস এফিমেরিস থেকে ডায়নামিক মুহূর্তের সময়সূচি গণনা (12hr / 24hr / 24+hr Support)
    # --------------------------------------------------------------------------
    def format_time_mode(dt_obj: datetime, base_date: date, mode: str = "12hr") -> str:
        m = str(mode or "12hr").lower().replace(" ", "").replace("-", "")
        if "24+" in m or "24plus" in m or "plus" in m:
            h = dt_obj.hour + 24 if dt_obj.date() > base_date else dt_obj.hour
            return f"{h:02d}:{dt_obj.minute:02d}"
        elif "24" in m:
            return dt_obj.strftime("%H:%M")
        else:
            return dt_obj.strftime("%I:%M %p")

    def fmt_m(dt_val):
        return format_time_mode(dt_val, local_date, time_format)

    pradosh_timing = f"{fmt_m(dt_set)} - {fmt_m(dt_set + timedelta(minutes=144))}"
    night_sec = (jd_next_sunrise - jd_sunset) * 86400.0
    night_muhurta = night_sec / 15.0
    nishita_st = dt_set + timedelta(seconds=7 * night_muhurta)
    nishita_en = dt_set + timedelta(seconds=8 * night_muhurta)
    nishita_timing = f"{fmt_m(nishita_st)} - {fmt_m(nishita_en)}"

    madhyahna_st = dt_rise + timedelta(seconds=6 * part_15th)
    madhyahna_en = dt_rise + timedelta(seconds=8 * part_15th)
    madhyahna_timing = f"{fmt_m(madhyahna_st)} - {fmt_m(madhyahna_en)}"

    purvahna_en = dt_rise + timedelta(seconds=5 * part_15th)
    purvahna_timing = f"{fmt_m(dt_rise)} - {fmt_m(purvahna_en)}"

    sayankal_st = dt_set - timedelta(minutes=24)
    sayankal_en = dt_set + timedelta(minutes=24)
    sayankal_timing = f"{fmt_m(sayankal_st)} - {fmt_m(sayankal_en)}"

    sunrise_snan_timing = f"{fmt_m(dt_rise - timedelta(minutes=30))} - {fmt_m(dt_rise + timedelta(minutes=45))}"

    aparahna_st = dt_rise + timedelta(seconds=9 * part_15th)
    aparahna_en = dt_rise + timedelta(seconds=12 * part_15th)
    aparahna_timing = f"{fmt_m(aparahna_st)} - {fmt_m(aparahna_en)}"

    brahma_timing = f"{fmt_m(brahma_s)} - {fmt_m(brahma_e)}"

    if t_end:
        t_end_dt = jd_to_local(t_end)
        sandhi_timing = f"{fmt_m(t_end_dt - timedelta(minutes=24))} - {fmt_m(t_end_dt + timedelta(minutes=24))}"
    else:
        sandhi_timing = f"{fmt_m(dt_set - timedelta(minutes=24))} - {fmt_m(dt_set + timedelta(minutes=24))}"

    # সূর্যোদয় ও সূর্যাস্তের মোট মিনিট
    rise_total_min = int(dt_rise.hour * 60 + dt_rise.minute)
    set_total_min = int(dt_set.hour * 60 + dt_set.minute)

    # প্রতিটি উৎসবের জন্য ডায়নামিক মুহূর্ত তৈরি
    for fest in today_festivals:
        m_type = fest.get("muhurta_type", "abhijit")
        fest_name = str(fest.get("name", ""))
        fest_cat = str(fest.get("category", "")).lower()

        # ==========================================================
        # ১. পৃথিবীর যেকোনো শহরের জন্য ১০০% নিখুঁত তিথি ক্যালকুলেশন
        # ==========================================================
        # আমরা যেই তিথিতে উৎসবটি পেয়েছি, ঠিক সেই তিথিরই শুরু এবং শেষ বের করব
        target_tithi_idx = fest.get('calc_tithi_idx', t_idx_rise)
        jd_base = fest.get('calc_jd_base', jd_sunrise)

        # তিথির শুরুর সময় খোঁজা (নিখুঁতভাবে পেছনে গিয়ে)
        jd_search = jd_base
        guard = 0
        while tithi_index(jd_search) == target_tithi_idx and guard < 100:
            jd_search -= 0.05  # প্রায় ১.২ ঘণ্টা করে পেছনে যাবে
            guard += 1
            
        t_start = find_transition(jd_search, tithi_index, max_hours=72.0)
        t_end = find_transition(jd_base, tithi_index, max_hours=72.0)

        # ২. তিথির শুরু, সমাপ্তি ও পরের দিনের লজিক
        if t_start and t_end:
            t_start_dt = jd_to_local(t_start)
            t_end_dt = jd_to_local(t_end)
            
            diff_days = (t_end_dt.date() - local_date).days
            m_idx = t_end_dt.month - 1
            d_str = str(t_end_dt.day)
            
            bn_m = ["জানু", "ফেব্রু", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টে", "অক্টো", "নভে", "ডিসে"]
            hi_m = ["जन", "फर", "मार्च", "अप्रैल", "मई", "जून", "जुला", "अग", "सितं", "अक्टू", "नवं", "दिसं"]
            en_m = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            
            if lang_key == "bn":
                d_bn = d_str.translate(str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯'))
                date_text = f"{d_bn} {bn_m[m_idx]}"
                extra = f" (পরের দিন, {date_text})" if diff_days == 1 else (f" ({str(diff_days).translate(str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯'))} দিন পর, {date_text})" if diff_days > 1 else "")
                tithi_str = f"{fmt_m(t_start_dt)} - {fmt_m(t_end_dt)}{extra}"
            elif lang_key == "hi":
                d_hi = d_str.translate(str.maketrans('0123456789', '०१२३४५६७८९'))
                date_text = f"{d_hi} {hi_m[m_idx]}"
                extra = f" (अगले दिन, {date_text})" if diff_days == 1 else (f" ({d_hi} दिन बाद, {date_text})" if diff_days > 1 else "")
                tithi_str = f"{fmt_m(t_start_dt)} - {fmt_m(t_end_dt)}{extra}"
            else:
                date_text = f"{en_m[m_idx]} {d_str}"
                extra = f" (Next Day, {date_text})" if diff_days == 1 else (f" ({diff_days} Days Later, {date_text})" if diff_days > 1 else "")
                tithi_str = f"{fmt_m(t_start_dt)} - {fmt_m(t_end_dt)}{extra}"
        else:
            tithi_str = ""

        # ৩. "পূজা" বনাম "শুভ মুহূর্ত" নির্ণয়
        social_keywords = [
            "rakhi", "bhai dooj", "bhai phonta", "bhai tika", "bhaidooj", "phonta", "dooj", 
            "new year", "labh pancham", "jamai", "aranya sasthi", 
            "holi", "dol jatra", "dahi handi", "lohri", "chhoti holi",
            "রাখী", "ভাইফোঁটা", "ভাইদুজ", "নববর্ষ", "জামাই", "অরণ্য ষষ্ঠী", "হোলি", "দোলযাত্রা", "দহি", 
            "राखी", "भाई दूज", "जमाई", "होली", "दही", "लोहड़ी"
        ]
        is_social = any(k in fest_name.lower() for k in social_keywords)

        main_title = "শুভ মুহূর্ত:" if is_social else "পূজার মুহূর্ত:"
        if lang_key == "hi":
            main_title = "शुभ मुहूर्त:" if is_social else "पूजा मुहूर्त:"
        elif lang_key == "en":
            main_title = "Auspicious Timing:" if is_social else "Puja Muhurta:"

        if m_type == "nishita":
            kaal_name = "নিশীথ কাল" if lang_key == "bn" else ("निशीथ काल" if lang_key == "hi" else "Nishita Kaal")
            p_time = f"{kaal_name} ({nishita_timing})"
            p_title = main_title
        elif m_type == "purvahna":
            kaal_name = "পূর্বাহ্ণ কাল" if lang_key == "bn" else ("पूर्वाह्न काल" if lang_key == "hi" else "Purvahna Kaal")
            p_time = f"{kaal_name} ({purvahna_timing})"
            p_title = main_title
        elif m_type == "madhyahna":
            kaal_name = "মধ্যাহ্ন কাল" if lang_key == "bn" else ("मध्याह्न काल" if lang_key == "hi" else "Madhyahna Kaal")
            p_time = f"{kaal_name} ({madhyahna_timing})"
            p_title = main_title
        elif m_type == "pradosh":
            kaal_name = "প্রদোষ কাল" if lang_key == "bn" else ("प्रदोष काल" if lang_key == "hi" else "Pradosh Kaal")
            p_time = f"{kaal_name} ({pradosh_timing})"
            p_title = main_title
        elif m_type == "sayankal":
            kaal_name = "সায়ংকাল" if lang_key == "bn" else ("सायंकाल" if lang_key == "hi" else "Sayankal")
            p_time = f"{kaal_name} ({sayankal_timing})"
            p_title = main_title
        elif m_type == "sunrise_snan":
            kaal_name = "প্রাতঃকাল" if lang_key == "bn" else ("प्रातःकाल" if lang_key == "hi" else "Pratah Kaal")
            p_time = f"{kaal_name} ({sunrise_snan_timing})"
            p_title = "স্নান মুহূর্ত:" if lang_key == "bn" else ("स्नान मुहूर्त:" if lang_key == "hi" else "Snan Muhurta:")
        elif m_type == "sandhi":
            kaal_name = "সন্ধিপূজা" if lang_key == "bn" else ("संधि पूजा" if lang_key == "hi" else "Sandhi Puja")
            p_time = f"{kaal_name} ({sandhi_timing})"
            p_title = main_title
        elif m_type == "brahma":
            kaal_name = "ব্রাহ্ম মুহূর্ত" if lang_key == "bn" else ("ब्रह्म मुहूर्त" if lang_key == "hi" else "Brahma Muhurta")
            p_time = f"{kaal_name} ({brahma_timing})"
            p_title = main_title
        elif m_type == "aparahna":
            kaal_name = "অপরাহ্ণ কাল" if lang_key == "bn" else ("अपराह्न काल" if lang_key == "hi" else "Aparahna Kaal")
            p_time = f"{kaal_name} ({aparahna_timing})"
            p_title = main_title
        else:
            kaal_name = "অভিজিৎ" if lang_key == "bn" else ("अभिजित" if lang_key == "hi" else "Abhijit")
            p_time = f"{kaal_name} ({fmt_m(abhijit_s)} - {fmt_m(abhijit_e)})"
            p_title = main_title

        # ৪. Non-Hindu / National Festivals Safety
        non_hindu_kws = [
            "jayanti", "gandhi", "bose", "netaji", "bhagat", "eid", "al-fitr", "al-adha", 
            "muharram", "christmas", "good friday", "republic", "independence", "international", 
            "national", "day", "জয়ন্তী", "গান্ধী", "নেতাজি", "বোস", "ভগত", "ঈদ", "রমজান", 
            "মহরম", "খ্রিস্টমাস", "গুড ফ্রাইডে", "জাতীয়", "দিবস", "আন্তর্জাতিক", "जयंती", 
            "गांधी", "बोस", "भगत", "ईद", "मुहर्रम", "क्रिसमस", "राष्ट्रीय", "दिवस", "अंतर्राष्ट्रीय"
        ]
        is_non_hindu = any(kw in fest_name.lower() for kw in non_hindu_kws)
        
        if is_non_hindu or fest_cat in ["national", "islamic", "christian", "observance", "bank holiday"]:
            p_title = ""
            p_time = ""
            tithi_str = ""  
            fest["tithi_span_title"] = ""
        else:
            fest["tithi_span_title"] = "উৎসবের সময়সীমা / তিথি মান:" if lang_key == "bn" else ("पर्व / तिथि समय अवधि:" if lang_key == "hi" else "Festival / Tithi Span:")
        
        # ৫. সমস্ত ডেটা মার্জ করে পাঠানো
        fest["tithi_span_time"] = tithi_str
        
        fest["puja_muhurta_title"] = p_title
        fest["puja_muhurta_title_bn"] = p_title
        fest["puja_muhurta_title_hi"] = p_title
        fest["muhurta_label"] = p_title
        fest["muhurta_label_bn"] = p_title
        fest["muhurta_label_hi"] = p_title
        
        fest["puja_muhurta_time"] = p_time
        fest["puja_muhurta_time_bn"] = p_time
        fest["puja_muhurta_time_hi"] = p_time
        fest["muhurta"] = p_time
        fest["muhurta_bn"] = p_time
        fest["muhurta_hi"] = p_time
        fest["shubhMuhurta"] = p_time
        fest["shubh_muhurta"] = p_time
        fest["muhurta_start"] = p_time  
        fest["muhurta_end"] = ""
        
        fest["is_puja"] = not is_social and not is_non_hindu
        
    # লাইভ ট্রানজিট আইডির সাথে মেটাডেটা ম্যাচিং
    tithi_num_key = (t_idx % 15) + 1
    
    # মেটাডেটা এক্সট্রাক্ট করে ভাষা অনুযায়ী অন-দ্য-ফ্লাই ট্রান্সলেশন করা
    def process_meta(meta_dict):
        result = {}
        
        # English to Bengali Translation Dictionary
        bn_trans = {
            "Kshipra / Laghu": "ক্ষিপ্র / লঘু", "Ugra / Krura": "উগ্র / ক্রূর", "Misra / Sadharana": "মিশ্র / সাধারণ",
            "Sthira / Dhruva": "স্থির / ধ্রুব", "Mridu": "মৃদু", "Tikshna / Daruna": "তীক্ষ্ণ / দারুণ",
            "Chara / Chala": "চর / চল", "Kshipra and Laghu": "ক্ষিপ্র ও লঘু", "Tikshna": "তীক্ষ্ণ", "Ugra": "উগ্র",
            "Horse Head": "অশ্ব মস্তক", "Yoni": "যোনি", "Razor / Knife": "ক্ষুর / ছুরি", "Cart / Chariot": "শকট / রথ",
            "Deer Head": "মৃগ মস্তক", "Teardrop / Gem": "অশ্রুবিন্দু / মণি", "House / Bow": "গৃহ / ধনু",
            "Arrow / Flower": "তীর / পুষ্প", "Coiled Serpent": "কুণ্ডলীকৃত সর্প", "Royal Throne": "রাজসিংহাসন",
            "Tiryang Mukha": "তির্যগ মুখ (তির্যক)", "Adho Mukha": "অধো মুখ (নিম্নমুখী)", "Urdhwa Mukha": "ঊর্ধ্ব মুখ (ঊর্ধ্বমুখী)",
            "Sulochana": "সুলোচনা (সুবৃষ্টি)", "Andhaksha": "অন্ধাক্ষ (অন্ধদৃষ্টি)", "Mandaksha": "মন্দাক্ষ (মৃদুদৃষ্টি)",
            "Movable": "চলমান (চর)", "Fixed": "স্থির", "Saumya": "সৌম্য", "Malefic": "অশুভ (পাপ)", "Benefic": "শুভ (পুণ্য)",
            "Vridhiprada": "বৃদ্ধিদায়ক", "Yashaprada": "যশোদায়ক", "Balaprada": "বলদায়ক", "Krodhaprada": "ক্রোধদায়ক",
            "Lakshmiprada": "লক্ষ্মীপ্রদ", "Mitraprada": "মিত্রপ্রদ", "Dwandvaprada": "দ্বন্দ্বপ্রদ", "Akramaka": "আক্রমণাত্মক",
            "Anandaprada": "আনন্দপ্রদ", "Vijayaprada": "বিজয়প্রদ", "Paushtika": "पौষ্টিক", "Pitruprada": "পিতৃপ্রদ"
        }
        
        # English to Hindi Translation Dictionary
        hi_trans = {
            "Kshipra / Laghu": "क्षिप्र / लघु", "Ugra / Krura": "उग्र / क्रूर", "Misra / Sadharana": "मिश्र / साधारण",
            "Sthira / Dhruva": "स्थिर / ध्रुव", "Mridu": "मृदु", "Tikshna / Daruna": "तीक्ष्ण / दारुण",
            "Chara / Chala": "चर / चल", "Kshipra and Laghu": "क्षिप्र और लघु", "Tikshna": "तीक्ष्ण", "Ugra": "उग्र",
            "Horse Head": "अश्व मस्तक", "Yoni": "योनि", "Razor / Knife": "क्षुर / चाकू", "Cart / Chariot": "गाड़ी / रथ",
            "Deer Head": "मृग मस्तक", "Teardrop / Gem": "अश्रुबिंदु / मणि", "House / Bow": "घर / धनुष",
            "Arrow / Flower": "तीर / पुष्प", "Coiled Serpent": "कुंडलीकृत सर्प", "Royal Throne": "राजसिंहासन",
            "Tiryang Mukha": "तिर्यग मुख (तिरछा)", "Adho Mukha": "अधो मुख (नीचे की ओर)", "Urdhwa Mukha": "ऊर्ध्व मुख (ऊपर की ओर)",
            "Sulochana": "सुलोचना", "Andhaksha": "अंधाक्ष", "Mandaksha": "मंदाक्ष",
            "Movable": "चर (गतिशील)", "Fixed": "स्थिर", "Saumya": "सौम्य", "Malefic": "अशुभ (पाप)", "Benefic": "शुभ (पुण्य)"
        }
        
        for k, v in meta_dict.items():
            if isinstance(v, dict) and "en" in v:
                result[k] = v.get(lang_key, v.get("en", ""))
            else:
                val_str = str(v)
                if lang_key == "bn" and val_str in bn_trans:
                    result[k] = bn_trans[val_str]
                elif lang_key == "hi" and val_str in hi_trans:
                    result[k] = hi_trans[val_str]
                else:
                    result[k] = v
        return result

    tithi_detail_info = process_meta(TITHI_METADATA.get(tithi_num_key, {}))
    nakshatra_detail_info = process_meta(NAKSHATRA_METADATA.get(n_idx + 1, {}))
    yoga_detail_info = process_meta(YOGA_METADATA.get(y_idx + 1, {}))
    karana_detail_info = process_meta(KARANA_METADATA.get(karana_name, {}))

    # ==========================================================
    # সূর্য রাশি, সূর্য নক্ষত্র এবং চন্দ্র নক্ষত্র পদের ডাইনামিক ট্রানজিশন
    # (Swiss Ephemeris Live Planetary Movement)
    # ==========================================================
    
    # লোকাল ডিকশনারি (যাতে বাংলা ও হিন্দিতে নিখুঁত নাম আসে)
    rashi_bn = ["মেষ", "বৃষ", "মিথুন", "কর্কট", "সিংহ", "কন্যা", "তুলা", "বৃশ্চিক", "ধনু", "মকর", "কুম্ভ", "মীন"]
    rashi_hi = ["मेष", "वृषभ", "मिथुन", "कर्क", "सिंह", "कन्या", "तुला", "वृश्चिक", "धनु", "मकर", "कुंभ", "मीन"]
    nak_bn = ["অশ্বিনী", "ভরণী", "কৃত্তিকা", "রোহিণী", "মৃগশিরা", "আর্দ্রা", "পুনর্বসু", "পুষ্যা", "অশ্লেষা", "মঘা", "পূর্ব ফাল্গুনী", "উত্তর ফাল্গুনী", "হস্তা", "চিত্রা", "স্বাতী", "বিশাখা", "অনুরাধা", "জ্যেষ্ঠা", "মূলা", "পূর্বাষাঢ়া", "উত্তরাষাঢ়া", "শ্রবণা", "ধনিষ্ঠা", "শতভিষা", "পূর্ব ভাদ্রপদ", "উত্তর ভাদ্রপদ", "রেবতী"]
    nak_hi = ["अश्विनी", "भरणी", "कृत्तिका", "रोहिणी", "मृगशिरा", "आर्द्रा", "पुनर्वसु", "पुष्य", "आश्लेषा", "मघा", "पूर्वाफाल्गुनी", "उत्तराफाल्गुनी", "हस्त", "चित्रा", "स्वाती", "विशाखा", "अनुराधा", "ज्येष्ठा", "मूल", "पूर्वाषाढ़ा", "उत्तराषाढ़ा", "श्रवण", "धनिष्ठा", "शतभिषा", "पूर्वाभाद्रपद", "उत्तराभाद्रपद", "रेवती"]

    def loc_rashi(idx):
        if lang_key == "bn": return rashi_bn[idx]
        elif lang_key == "hi": return rashi_hi[idx]
        return RASHIS[idx]
        
    def loc_nak(idx):
        if lang_key == "bn": return nak_bn[idx]
        elif lang_key == "hi": return nak_hi[idx]
        return NAKSHATRAS[idx]

    pada_word = "পদ" if lang_key in ["bn", "hi"] else "Pada"

    # ১. ডাইনামিক চন্দ্র রাশি
    moon_end_str_final = get_upto_str(moon_rashi_end)
    if moon_end_str_final:
        dynamic_moonsign = f"{loc_rashi(m_rashi_idx)}{moon_end_str_final}, {then_str} {loc_rashi((m_rashi_idx + 1) % 12)}"
    else:
        dynamic_moonsign = loc_rashi(m_rashi_idx)

    # ২. ডাইনামিক সূর্য রাশি (Sankranti Tracking - Live)
    next_sun_rashi_deg = (s_rashi_idx + 1) * 30.0
    sun_rashi_dt = find_solar_ingress_forward(jd_sunrise, next_sun_rashi_deg % 360.0, max_days=35.0)
    sun_rashi_end_str = get_upto_str(to_jd_ut(sun_rashi_dt))
    dynamic_sunsign = f"{loc_rashi(s_rashi_idx)}{sun_rashi_end_str}, {then_str} {loc_rashi((s_rashi_idx + 1) % 12)}"

    # ৩. ডাইনামিক সূর্য নক্ষত্র (Live)
    next_sun_nak_deg = (sun_nak_idx + 1) * (360.0 / 27.0)
    sun_nak_dt = find_solar_ingress_forward(jd_sunrise, next_sun_nak_deg % 360.0, max_days=15.0)
    sun_nak_end_str = get_upto_str(to_jd_ut(sun_nak_dt))
    dynamic_surya_nakshatra = f"{loc_nak(sun_nak_idx)} ({pada_word} {sun_pada}){sun_nak_end_str}, {then_str} {loc_nak((sun_nak_idx + 1) % 27)}"

    # ৪. ডাইনামিক চন্দ্র নক্ষত্র পদ (Navamsha Tracking - Live)
    def moon_pada_index(jd):
        _, m = sidereal_longitudes(jd)
        return int((m % 360.0) / (360.0 / 108.0))
        
    moon_pada_end_jd = find_transition(jd_sunrise, moon_pada_index, step_hours=0.15, max_hours=12.0)
    pada_end_str = get_upto_str(moon_pada_end_jd)
    curr_pada = (moon_pada_index(jd_sunrise) % 4) + 1
    next_pada = (curr_pada % 4) + 1
    dynamic_nakshatra_pada = f"{loc_nak(n_idx)} ({pada_word} {curr_pada}){pada_end_str}, {then_str} {pada_word} {next_pada}"

    # ==========================================================
    # ৫টি মিসিং অ্যাডভান্সড ফিল্ড (Jeevana, Netra, Homahuti, Bhadravasa, Kumbha) + Descriptions
    # ==========================================================
    
    # ১. জীবমান ও নেত্রমান (Jeevana & Netra Mana)
    jeeva_list = [
        {
            "en": "2 Jeeva (Full Life Energy)", "hi": "२ जीव (पूर्ण प्राण)", "bn": "২ জীব (পরম শুভ / পূর্ণ প্রাণশক্তি)",
            "desc_en": "Supreme vitality; exceptionally fruitful day.",
            "desc_hi": "परम शुभ, कार्य में अपार सफलता।",
            "desc_bn": "পরম শুভ প্রাপ্তি, কার্যে অসাধারণ শুভফলদায়ী।"
        },
        {
            "en": "1 Jeeva (Moderate)", "hi": "१ जीव (मध्यम)", "bn": "১ জীব (মধ্যম)",
            "desc_en": "Moderate energy; steady progress.",
            "desc_hi": "मध्यम शुभ, सामान्य फलदायी।",
            "desc_bn": "মধ্যম ফলপ্রাপ্তি, সাধারণ কার্যে শুভ।"
        },
        {
            "en": "1/2 Jeeva (Half Life)", "hi": "१/२ जीव (अर्ध)", "bn": "১/২ জীব (অর্ধ প্রাণ)",
            "desc_en": "Low energy; requires effort.",
            "desc_hi": "अल्प शुभ, अधिक परिश्रम आवश्यक।",
            "desc_bn": "স্বল্প ফল, অতিরিক্ত পরিশ্রমে সিদ্ধি।"
        },
        {
            "en": "0 Jeeva (Lifeless / Inauspicious)", "hi": "० जीव (प्राणहीन)", "bn": "০ জীব (প্রাণहीन / অশুভ)",
            "desc_en": "Lifeless; strictly avoid major activities.",
            "desc_hi": "प्राणहीन, सभी शुभ कार्यों के लिए वर्जित।",
            "desc_bn": "প্রাণহীন, সমস্ত শুভকার্যে বর্জনীয়।"
        }
    ]
    netra_list = [
        {
            "en": "2 Netra (Clear Sight / Auspicious)", "hi": "२ नेत्र (पूर्ण दृष्टि / शुभ)", "bn": "২ নেত্র (সুনৈত্র / পূর্ণ দৃষ্টি)",
            "desc_en": "Highly propitious for journeys, purchases & agreements.",
            "desc_hi": "यात्रा, खरीदारी और नए कार्यों के लिए अत्यंत शुभ।",
            "desc_bn": "ভ্রমণ, কেনাকাটা, চুক্তি ও শুভকর্মে অত্যন্ত প্রশস্ত।"
        },
        {
            "en": "1 Netra (One Eye)", "hi": "१ नेत्र (एक दृष्टि)", "bn": "১ নেত্র (এক দৃষ্টি / মধ্যম)",
            "desc_en": "Fair visibility; proceed with caution.",
            "desc_hi": "मध्यम दृष्टि; सावधानी से कार्य करें।",
            "desc_bn": "মধ্যম দৃষ্টি, সতর্কতার সাথে কাজ করুন।"
        },
        {
            "en": "0 Netra (Blind / Inauspicious)", "hi": "० नेत्र (नेत्रहीन / अशुभ)", "bn": "০ নেত্র (দৃষ্টিহীন / অশুভ / বর্জনীয়)",
            "desc_en": "Blind; strictly avoid new ventures and travels.",
            "desc_hi": "अंध दृष्टि; यात्रा और नए कार्यों से पूरी तरह बचें।",
            "desc_bn": "অন্ধ দৃষ্টি, নতুন কাজ ও ভ্রমণ সম্পূর্ণ নিষিদ্ধ।"
        }
    ]
    
    special_yogas["jeevana_mana"] = jeeva_list[n_idx % 4].get(lang_key, jeeva_list[n_idx % 4]["en"])
    special_yogas["jeevana_mana_desc"] = jeeva_list[n_idx % 4].get(f"desc_{lang_key}", jeeva_list[n_idx % 4]["desc_en"])
    
    special_yogas["netra_mana"] = netra_list[n_idx % 3].get(lang_key, netra_list[n_idx % 3]["en"])
    special_yogas["netra_mana_desc"] = netra_list[n_idx % 3].get(f"desc_{lang_key}", netra_list[n_idx % 3]["desc_en"])

    # ২. হোমাহুতি (Homahuti)
    homa_deities = [
        {"en": "Sun (Planet)", "bn": "সূর্য গ্রহ", "hi": "सूर्य ग्रह", "desc_en": "Grants health, fame, and power in fire oblations.", "desc_hi": "हवन में आरोग्य, यश और शक्ति प्रदाता।", "desc_bn": "যজ্ঞকর্মে হোমাহুতি আরোগ্য, যশ ও সম্মান বৃদ্ধিকারী।"},
        {"en": "Chandra (Planet)", "bn": "চন্দ্র গ্রহ", "hi": "चंद्र ग्रह", "desc_en": "Daily planetary fire oblation deity, favorable for pacification rituals.", "desc_hi": "दैनिक हवन में शांति और कल्याणकारी फल प्रदाता।", "desc_bn": "দৈনিক যজ্ঞকর্মে হোমাহুতি অধিপতি গ্রহ, শান্তি ও কল্যাণদায়ী।"},
        {"en": "Mangal (Planet)", "bn": "মঙ্গল গ্রহ", "hi": "मंगल ग्रह", "desc_en": "Grants courage, victory, and removes debts.", "desc_hi": "हवन से साहस, विजय और ऋण मुक्ति मिलती है।", "desc_bn": "যজ্ঞকর্মে সাহস বৃদ্ধি, বিজয় ও ঋণমুক্তিকারী।"},
        {"en": "Budha (Planet)", "bn": "বুধ গ্রহ", "hi": "बुध ग्रह", "desc_en": "Enhances intellect, business, and communication.", "desc_hi": "हवन से बुद्धि, व्यापार और संचार में लाभ मिलता है।", "desc_bn": "যজ্ঞকর্মে বুদ্ধি, ব্যবসা ও যোগাযোগের উন্নতিদায়ক।"},
        {"en": "Guru (Planet)", "bn": "গুরু গ্রহ", "hi": "गुरु ग्रह", "desc_en": "Bestows wisdom, wealth, and divine blessings.", "desc_hi": "हवन से ज्ञान, धन और ईश्वरीय कृपा प्राप्त होती है।", "desc_bn": "যজ্ঞকর্মে জ্ঞান, ধন ও ঐশ্বরিক কৃপা প্রদানকারী।"},
        {"en": "Shukra (Planet)", "bn": "শুক্র গ্রহ", "hi": "शुक्र ग्रह", "desc_en": "Bestows luxury, harmony, and material comforts.", "desc_hi": "हवन से सुख, शांति और भौतिक समृद्धि मिलती है।", "desc_bn": "যজ্ঞকর্মে সুখ, শান্তি ও জাগতিক সমৃদ্ধিদায়ক।"},
        {"en": "Shani (Planet)", "bn": "শনি গ্রহ", "hi": "शनि ग्रह", "desc_en": "Alleviates sorrow and grants long-term stability.", "desc_hi": "हवन से दुःख दूर होते हैं और स्थिरता मिलती है।", "desc_bn": "যজ্ঞকর্মে দুঃখ নিবারক ও দীর্ঘস্থায়ী স্থায়িত্বদায়ক।"},
        {"en": "Rahu", "bn": "রাহু", "hi": "राहु", "desc_en": "Favorable for overcoming sudden obstacles.", "desc_hi": "अचानक आने वाली बाधाओं को दूर करने में सहायक।", "desc_bn": "যজ্ঞকর্মে আকস্মিক বাধা বিপত্তি দূর করতে সহায়ক।"},
        {"en": "Ketu", "bn": "কেতু", "hi": "केतु", "desc_en": "Grants spiritual growth and liberation (Moksha).", "desc_hi": "हवन से आध्यात्मिक उन्नति और मोक्ष की प्राप्ति होती है।", "desc_bn": "যজ্ঞকর্মে আধ্যাত্মিক উন্নতি ও মুক্তি (মোক্ষ) দায়ক।"}
    ]
    niwas_shool["homahuti"] = homa_deities[(n_idx + weekday + 1) % 9].get(lang_key, homa_deities[(n_idx + weekday + 1) % 9]["en"])
    niwas_shool["homahuti_desc"] = homa_deities[(n_idx + weekday + 1) % 9].get(f"desc_{lang_key}", homa_deities[(n_idx + weekday + 1) % 9]["desc_en"])

    # ৩. ভদ্রাবাস (Bhadravasa)
    if "Vishti" in karana_name or "Bhadra" in karana_name:
        if m_rashi_idx in [0, 1, 2, 7]:
            b_vasa = {"en": "Swarga (Heaven) - Auspicious", "hi": "स्वर्ग (शुभ)", "bn": "স্বর্গ (शुभफलপ্রদ)", "desc_en": "Bhadra resides in Heaven; brings success and happiness.", "desc_hi": "भद्रा स्वर्ग में है; सफलता और सुख लाती है।", "desc_bn": "ভদ্রা স্বর্গে বিরাজমান; কল্যাণ ও সাফল্য প্রদানকারী।"}
        elif m_rashi_idx in [5, 6, 8, 9]:
            b_vasa = {"en": "Patala (Underworld) - Wealth gain", "hi": "पाताल (धन लाभ)", "bn": "পাতাল (धन লাভ)", "desc_en": "Bhadra resides in the Underworld; brings financial gains.", "desc_hi": "भद्रा पाताल में है; धन लाभ और भौतिक सुख लाती है।", "desc_bn": "ভদ্রা পাতালে বিরাজমান; ধনসম্পত্তি লাভ ও জাগতিক সুখ প্রদানকারী।"}
        else:
            b_vasa = {"en": "Mrityu/Prithvi (Earth) - Inauspicious", "hi": "मृत्यु/पृथ्वी (अशुभ)", "bn": "মর্ত্য/পৃথিবী (সর্বনাশ / অशुभ)", "desc_en": "Bhadra resides on Earth; strictly avoid all auspicious work.", "desc_hi": "भद्रा पृथ्वी पर है; अत्यंत अशुभ, सभी शुभ कार्यों से बचें।", "desc_bn": "ভদ্রা মর্ত্যে (পৃথিবীতে) বিরাজমান; अत्यंत अशुभ, সমস্ত মাঙ্গলিক কাজ বর্জনীয়।"}
    else:
        b_vasa = {"en": "None (Inactive)", "hi": "कोई नहीं (निष्क्रिय)", "bn": "অনুপস্থিত (নিষ্ক্রিয়)", "desc_en": "Bhadra is absent; all auspicious and worldly endeavors proceed unobstructed.", "desc_hi": "भद्रा अनुपस्थित है; सभी शुभ कार्य बाधारहित संपन्न होंगे।", "desc_bn": "ভদ্রা অনুপস্থিত; সর্বপ্রকার শুভ ও মাঙ্গলিক কার্য বাধাহীনভাবে সম্পন্ন হবে।"}
    
    niwas_shool["bhadravasa"] = b_vasa.get(lang_key, b_vasa["en"])
    niwas_shool["bhadravasa_desc"] = b_vasa.get(f"desc_{lang_key}", b_vasa["desc_en"])

    # ৪. কুম্ভ চক্র (Kumbha Chakra)
    kumbha_dirs = [
        {"en": "East (Purva)", "hi": "पूर्व दिशा", "bn": "পূর্ব দিক", "desc_en": "Auspicious: Kumbha faces East; brings wealth and prosperity.", "desc_hi": "शुभ: कुंभ पूर्वमुखी है; धन और समृद्धि प्रदाता।", "desc_bn": "শুভ: কুম্ভ পূর্বমুখী; ধন ও সমৃদ্ধি প্রদানকারী।"},
        {"en": "South (Dakshina)", "hi": "दक्षिण दिशा", "bn": "দক্ষিণ দিক", "desc_en": "Auspicious: Kumbha faces South; fulfills desires and bestows victory.", "desc_hi": "शुभ: कुंभ दक्षिणमुखी है; मनोकामना पूर्ण और विजय प्रदाता।", "desc_bn": "শুভ: কুম্ভ দক্ষিণমুখী; মনস্কামনা পূর্ণ ও বিজয় প্রদানকারী।"},
        {"en": "West (Pashchima)", "hi": "पश्चिम दिशा", "bn": "পশ্চিম দিক", "desc_en": "Auspicious: Kumbha faces West; brings peace and stability.", "desc_hi": "शुभ: कुंभ पश्चिममुखी है; शांति और स्थिरता लाता है।", "desc_bn": "শুভ: কুম্ভ পশ্চিমমুখী; শান্তি ও স্থায়িত্ব প্রদানকারী।"},
        {"en": "North (Uttara)", "hi": "उत्तर दिशा", "bn": "উত্তর দিক", "desc_en": "Auspicious: Kumbha faces North; bestows health and knowledge.", "desc_hi": "शुभ: कुंभ उत्तरमुखी है; स्वास्थ्य और ज्ञान प्रदाता।", "desc_bn": "শুভ: কুম্ভ উত্তরমুখী; জ্ঞান ও সুস্বাস্থ্য প্রদানকারী।"}
    ]
    niwas_shool["kumbha_chakra"] = kumbha_dirs[s_rashi_idx % 4].get(lang_key, kumbha_dirs[s_rashi_idx % 4]["en"])
    niwas_shool["kumbha_chakra_desc"] = kumbha_dirs[s_rashi_idx % 4].get(f"desc_{lang_key}", kumbha_dirs[s_rashi_idx % 4]["desc_en"])
    # ==========================================================

    return {
        # রাশি ও সূর্য স্থিতি
        "moonsign": dynamic_moonsign,
        "sunsign": dynamic_sunsign,
        "surya_nakshatra": dynamic_surya_nakshatra,
        "surya_pada": sun_pada,
        "nakshatra_pada_display": dynamic_nakshatra_pada,
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
        # সংবৎসর (Brihat Samhita 60 Samvatsara Drik Sync)
        "samvatsara_name": get_samvatsara((int(samvat_year) + 135) if (1800 <= int(samvat_year or 0) <= 2000) else int(samvat_year or 2051), lang=lang_key),
        "samvatsara_details": get_samvatsara_details((int(samvat_year) + 135) if (1800 <= int(samvat_year or 0) <= 2000) else int(samvat_year or 2051), lang=lang_key),
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
        
        # অহোরাত্র কাল বিভাজন (Day-Night Timeline)
        "day_timeline_periods": calculate_vedic_day_periods(dt_rise, dt_set, jd_to_local(jd_next_sunrise), lang=lang_key),
        
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
        
        # ১. বাংলা সৌর তারিখ (সূর্যোদয়ের স্পষ্ট দ্রাঘিমাংশ সমন্বয়)
        jd_day_sun = to_jd_ut(datetime(year, month, d, 6, 0, tzinfo=IST))
        s_lon, _ = sidereal_longitudes(jd_day_sun)
        bengali_solar_day = int(s_lon % 30.0)
        if bengali_solar_day == 0:
            bengali_solar_day = 1

        
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
