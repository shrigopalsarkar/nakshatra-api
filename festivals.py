from datetime import date
from typing import List, Dict, Any

# ১. হিন্দু তিথিভিত্তিক উৎসব ডেটাবেজ
HINDU_FESTIVAL_DATABASE = {
    # চৈত্র মাস
    ("Chaitra", "Shukla", 1): {"en": "Chaitra Navratri / Gudi Padwa", "hi": "चैत्र नवरात्रि / गुड़ी पड़वा", "bn": "চৈত্র নবরাত্রি / গুড়ি পাড়ওয়া"},
    ("Chaitra", "Shukla", 9): {"en": "Rama Navami", "hi": "श्री राम नवमी", "bn": "শ্রী রাম নবমী"},
    ("Chaitra", "Shukla", 15): {"en": "Hanuman Jayanti", "hi": "हनुमान जयंती", "bn": "হনুমান জয়ন্তী"},
    # বৈশাখ মাস
    ("Vaisakha", "Shukla", 3): {"en": "Akshaya Tritiya", "hi": "अक्षय तृतीया", "bn": "অক্ষয় তৃতীয়া"},
    ("Vaisakha", "Shukla", 15): {"en": "Buddha Purnima", "hi": "बुद्ध पूर्णिमा", "bn": "বুদ্ধ পূর্ণিমা"},
    # জ্যৈষ্ঠ মাস
    ("Jyeshtha", "Shukla", 10): {"en": "Ganga Dussehra", "hi": "गंगा दशहरा", "bn": "গঙ্গা দশহরা"},
    ("Jyeshtha", "Shukla", 11): {"en": "Nirjala Ekadashi", "hi": "निर्जला एकादशी", "bn": "নির্জলা একাদশী"},
    # আষাঢ় মাস
    ("Ashadha", "Shukla", 2): {"en": "Jagannath Ratha Yatra", "hi": "जगन्नाथ रथ यात्रा", "bn": "জগন্নাথ রথযাত্রা"},
    ("Ashadha", "Shukla", 15): {"en": "Guru Purnima", "hi": "गुरु पूर्णिमा", "bn": "গুরু পূর্ণিমা"},
    # শ্রাবণ মাস
    ("Shravana", "Shukla", 5): {"en": "Nag Panchami", "hi": "नाग पंचमी", "bn": "নাগ পঞ্চমী"},
    ("Shravana", "Shukla", 15): {"en": "Raksha Bandhan / Jhulan Yatra", "hi": "रक्षाबंधन / झूलन यात्रा", "bn": "রাখীবন্ধন / ঝুলনযাত্রা"},
    # ভাদ্রপদ মাস
    ("Bhadrapada", "Krishna", 8): {"en": "Krishna Janmashtami", "hi": "श्रीकृष्ण जन्माष्टमी", "bn": "শ্রীকৃষ্ণ জন্মাষ্টমী"},
    ("Bhadrapada", "Shukla", 4): {"en": "Ganesh Chaturthi", "hi": "गणेश चतुर्थी", "bn": "গণেশ চতুর্থী"},
    ("Bhadrapada", "Shukla", 8): {"en": "Radhashtami", "hi": "राधाष्टमी", "bn": "রাধাষ্টমী"},
    ("Bhadrapada", "Shukla", 14): {"en": "Anant Chaturdashi", "hi": "अनंत चतुर्दशी", "bn": "অনন্ত চতুর্দশী"},
    # আশ্বিন মাস
    ("Ashvina", "Krishna", 15): {"en": "Mahalaya (Amavasya)", "hi": "सर्वपितृ अमावस्या / महालया", "bn": "মহালয়া"},
    ("Ashvina", "Shukla", 1): {"en": "Sharad Navratri Begins", "hi": "शारदीय नवरात्रि प्रारंभ", "bn": "শারদীয়া নবরাত্রি আরম্ভ"},
    ("Ashvina", "Shukla", 7): {"en": "Maha Saptami (Durga Puja)", "hi": "महा सप्तमी (दुर्गा पूजा)", "bn": "মহা সপ্তমী (দুর্গাপূজা)"},
    ("Ashvina", "Shukla", 8): {"en": "Maha Ashtami / Sandhi Puja", "hi": "महा अष्टमी / संधि पूजा", "bn": "মহা অষ্টমী / সন্ধিপূজা"},
    ("Ashvina", "Shukla", 9): {"en": "Maha Navami", "hi": "महानवमी", "bn": "মহা নবমী"},
    ("Ashvina", "Shukla", 10): {"en": "Vijaya Dashami / Dussehra", "hi": "विजयादशमी / दशहरा", "bn": "বিজয়া দশমী / দশহরা"},
    ("Ashvina", "Shukla", 15): {"en": "Kojagari Lakshmi Puja", "hi": "शरद पूर्णिमा / लक्ष्मी पूजा", "bn": "কোজাগরী লক্ষ্মীপূজা"},
    # কার্তিক মাস
    ("Kartika", "Krishna", 4): {"en": "Karwa Chauth", "hi": "करवा चौथ", "bn": "করবা চৌথ"},
    ("Kartika", "Krishna", 13): {"en": "Dhanteras", "hi": "धनतेरस", "bn": "ধনতেরাস"},
    ("Kartika", "Krishna", 14): {"en": "Naraka Chaturdashi / Bhoot Chaturdashi", "hi": "नरक चतुर्दशी / छोटी दिवाली", "bn": "ভূত চতুর্দশী / চোটি দিওয়ালি"},
    ("Kartika", "Krishna", 15): {"en": "Diwali / Kali Puja / Lakshmi Puja", "hi": "दीपावली / महालक्ष्मी पूजा", "bn": "কালীপূজা / দীপাবলি"},
    ("Kartika", "Shukla", 1): {"en": "Govardhan Puja / Annakut", "hi": "गोवर्धन पूजा / अन्नकूट", "bn": "গোবর্ধন পূজা / অন্নকূট"},
    ("Kartika", "Shukla", 2): {"en": "Bhai Dooj / Bhatri Dwitiya", "hi": "भाई दूज", "bn": "ভ্রাতৃদ্বিতীয়া / ভাইফোঁটা"},
    ("Kartika", "Shukla", 6): {"en": "Chhath Puja (Sandhya Arghya)", "hi": "छठ पूजा", "bn": "ছট পূজা"},
    ("Kartika", "Shukla", 15): {"en": "Dev Deepawali / Rasa Purnima", "hi": "देव दीपावली / रास पूर्णिमा", "bn": "রাস পূর্ণিমা / দেব দীপাবলি"},
    # মার্গশীর্ষ মাস
    ("Margashirsha", "Shukla", 11): {"en": "Mokshada Ekadashi / Gita Jayanti", "hi": "मोक्षदा एकादशी / गीता जयंती", "bn": "মোক্ষদা একাদশী / গীতা জয়ন্তী"},
    # মাঘ মাস
    ("Magha", "Shukla", 5): {"en": "Saraswati Puja / Vasant Panchami", "hi": "सरस्वती पूजा / बसंत पंचमी", "bn": "সরস্বতী পূজা / বসন্ত পঞ্চমী"},
    ("Magha", "Krishna", 14): {"en": "Maha Shivratri", "hi": "महाशिवरात्रि", "bn": "মহা শিবরাত্রি"},
    # ফাল্গুন মাস
    ("Phalguna", "Shukla", 14): {"en": "Holika Dahan", "hi": "होलिका दहन", "bn": "হোলিকা দহন / চাঁচর"},
    ("Phalguna", "Shukla", 15): {"en": "Holi / Dol Jatra / Gaura Purnima", "hi": "होली / डोल यात्रा", "bn": "দোলযাত্রা / হোলি / গৌর পূর্ণিমা"}
}

# ২. ভারতীয় জাতীয় ছুটির দিন (National Holidays)
INDIAN_NATIONAL_HOLIDAYS = {
    (1, 23): {"en": "Netaji Subhas Chandra Bose Jayanti", "hi": "नेताजी सुभाष चंद्र बोस जयंती", "bn": "নেতাজি সুভাষচন্দ্র বসুর জন্মজয়ন্তী", "category": "national", "icon": "🇮🇳"},
    (1, 26): {"en": "Republic Day", "hi": "गणतंत्र दिवस", "bn": "প্রজাতন্ত্র দিবস", "category": "national", "icon": "🇮🇳"},
    (4, 14): {"en": "Dr. B.R. Ambedkar Jayanti", "hi": "डॉ. बी.आर. आंबेडकर जयंती", "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী", "category": "national", "icon": "🇮🇳"},
    (8, 15): {"en": "Independence Day", "hi": "स्वतंत्रता दिवस", "bn": "স্বাধীনতা দিবস", "category": "national", "icon": "🇮🇳"},
    (10, 2): {"en": "Mahatma Gandhi Jayanti", "hi": "गांधी जयंती", "bn": "গান্ধী জয়ন্তী", "category": "national", "icon": "🇮🇳"},
}

# ৩. খ্রিস্টান ও আন্তর্জাতিক দিবস (Fixed Gregorian)
FIXED_WORLD_CHRISTIAN_DAYS = {
    (1, 1): {"en": "New Year's Day", "hi": "नव वर्ष", "bn": "ইংরেজি নববর্ষ", "category": "world", "icon": "🌍"},
    (3, 8): {"en": "International Women's Day", "hi": "अंतर्राष्ट्रीय महिला दिवस", "bn": "আন্তর্জাতিক নারী দিবস", "category": "world", "icon": "🌍"},
    (4, 22): {"en": "Earth Day", "hi": "पृथ्वी दिवस", "bn": "বিশ্ব বসুন্ধরা দিবস", "category": "world", "icon": "🌍"},
    (5, 1): {"en": "International Workers' Day / May Day", "hi": "अंतर्राष्ट्रीय मजदूर दिवस", "bn": "আন্তর্জাতিক শ্রমিক দিবস / মে দিবস", "category": "world", "icon": "🌍"},
    (6, 5): {"en": "World Environment Day", "hi": "विश्व पर्यावरण दिवस", "bn": "বিশ্ব পরিবেশ দিবস", "category": "world", "icon": "🌍"},
    (6, 21): {"en": "International Yoga Day", "hi": "अंतर्राष्ट्रीय योग दिवस", "bn": "আন্তর্জাতিক যোগ দিবস", "category": "world", "icon": "🌍"},
    (12, 24): {"en": "Christmas Eve", "hi": "क्रिसमस ईव", "bn": "ক্রিসমাস ইভ", "category": "christian", "icon": "✝️"},
    (12, 25): {"en": "Christmas / Merry Christmas", "hi": "क्रिसमस / बड़ा दिन", "bn": "বড়দিন / ক্রিসমাস", "category": "christian", "icon": "✝️"},
    (12, 31): {"en": "New Year's Eve", "hi": "नव वर्ष की पूर्वसंध्या", "bn": "বছরের শেষ দিন", "category": "world", "icon": "🌍"},
}

# ৪. মুসলিম ও পরিবর্তনশীল খ্রিস্টান উৎসব (২০২৫ - ২০২৭)
VARIABLE_RELIGIOUS_DAYS = {
    # 2026 সাল
    (2026, 3, 20): {"en": "Eid-ul-Fitr (Ramadan Eid)", "hi": "ईद-उल-फ़ित्र", "bn": "ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2026, 4, 3): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2026, 4, 5): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2026, 5, 27): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "ঈদুল আযহা / বকরি ঈদ", "category": "muslim", "icon": "☪️"},
    (2026, 6, 26): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "মহরম / আশুরা", "category": "muslim", "icon": "☪️"},
    (2026, 8, 26): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "ঈদে মিলাদুন্নবী", "category": "muslim", "icon": "☪️"},
    # 2025 সাল
    (2025, 3, 31): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2025, 4, 18): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2025, 4, 20): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2025, 6, 7): {"en": "Eid-ul-Adha / Bakrid", "hi": "बकरीद", "bn": "বকরি ঈদ", "category": "muslim", "icon": "☪️"},
    (2025, 7, 6): {"en": "Muharram", "hi": "मोहर्रम", "bn": "মহরম", "category": "muslim", "icon": "☪️"},
}

def get_festivals_for_day(
    current_date: date,
    lunar_month: str = "",
    paksha: str = "",
    tithi_num: int = 1,
    sankranti_name: str = None,
    lang: str = "en"
) -> List[Dict[str, Any]]:
    
    festivals = []
    l_key = "bn" if ("bn" in str(lang) or "বাংলা" in str(lang)) else "hi" if ("hi" in str(lang) or "हि" in str(lang)) else "en"
    
    # --- A. হিন্দু তিথিভিত্তিক প্রধান উৎসব ---
    h_key = (lunar_month, paksha, tithi_num)
    if h_key in HINDU_FESTIVAL_DATABASE:
        festivals.append({
            "name": HINDU_FESTIVAL_DATABASE[h_key].get(l_key, HINDU_FESTIVAL_DATABASE[h_key]["en"]),
            "category": "hindu",
            "type": "Major Festival",
            "icon": "🕉️"
        })
    
    # একাদশী ও প্রদোষ ব্রত
    if tithi_num == 11:
        ekadashi = {"en": "Ekadashi Vrata", "hi": "एकादशी व्रत", "bn": "একাদশী ব্রত"}
        festivals.append({"name": ekadashi.get(l_key, "Ekadashi"), "category": "hindu", "type": "Vrata", "icon": "🕉️"})
    elif tithi_num == 13:
        pradosh = {"en": "Pradosh Vrata", "hi": "प्रदोष व्रत", "bn": "প্রদোষ ব্রত"}
        festivals.append({"name": pradosh.get(l_key, "Pradosh"), "category": "hindu", "type": "Vrata", "icon": "🕉️"})
        
    # সৌর সংক্রান্তি
    if sankranti_name:
        if "Makara" in sankranti_name:
            sank_names = {"en": "Makar Sankranti / Pongal", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি"}
            festivals.append({"name": sank_names.get(l_key, "Makar Sankranti"), "category": "hindu", "type": "Solar", "icon": "☀️"})
        elif "Mesha" in sankranti_name:
            sank_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / बैसाखी", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি"}
            festivals.append({"name": sank_names.get(l_key, "Poila Boishakh"), "category": "hindu", "type": "Solar", "icon": "☀️"})

    # --- B. ভারতীয় জাতীয় ছুটির দিন ---
    month_day = (current_date.month, current_date.day)
    if month_day in INDIAN_NATIONAL_HOLIDAYS:
        nat = INDIAN_NATIONAL_HOLIDAYS[month_day]
        festivals.append({
            "name": nat.get(l_key, nat["en"]),
            "category": nat["category"],
            "type": "National Holiday",
            "icon": nat["icon"]
        })

    # --- C. ফিক্সড আন্তর্জাতিক ও খ্রিস্টান উৎসব ---
    if month_day in FIXED_WORLD_CHRISTIAN_DAYS:
        wc = FIXED_WORLD_CHRISTIAN_DAYS[month_day]
        festivals.append({
            "name": wc.get(l_key, wc["en"]),
            "category": wc["category"],
            "type": "Observance",
            "icon": wc["icon"]
        })

    # --- D. পরিবর্তনশীল মুসলিম ও খ্রিস্টান উৎসব ---
    full_date_key = (current_date.year, current_date.month, current_date.day)
    if full_date_key in VARIABLE_RELIGIOUS_DAYS:
        rel = VARIABLE_RELIGIOUS_DAYS[full_date_key]
        festivals.append({
            "name": rel.get(l_key, rel["en"]),
            "category": rel["category"],
            "type": "Religious Festival",
            "icon": rel["icon"]
        })

    return festivals
