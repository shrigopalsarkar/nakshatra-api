from datetime import date
from typing import List, Dict, Any

# ==============================================================================
# ১. হিন্দু তিথিভিত্তিক সমস্ত পূজা, ব্রত ও উৎসব ডেটাবেজ (যেকোনো বছরের জন্য আজীবন ডাইনামিক)
#    (Masa, Paksha, Tithi_Number)
# ==============================================================================
HINDU_FESTIVAL_DATABASE = {
    # --- চৈত্র মাস (Chaitra) ---
    ("Chaitra", "Shukla", 1): {"en": "Chaitra Navratri / Gudi Padwa / Basanti Puja Bodhan", "hi": "चैत्र नवरात्रि / गुड़ी पड़वा / वासंतिक दुर्गा पूजा", "bn": "চৈত্র নবরাত্রি আরম্ভ / বাসন্তী পূজা বোধন / গুড়ি পাড়ওয়া"},
    ("Chaitra", "Shukla", 8): {"en": "Annapurna Puja / Basanti Ashtami", "hi": "अन्नपूर्णा पूजा / बासंती अष्टमी", "bn": "শ্রী শ্রী অন্নপূর্ণা পূজা / বাসন্তী মহাষ্টমী"},
    ("Chaitra", "Shukla", 9): {"en": "Rama Navami", "hi": "श्री राम नवमी", "bn": "শ্রী শ্রী রাম নবমী মহাপর্ব"},
    ("Chaitra", "Shukla", 15): {"en": "Hanuman Jayanti / Chaitra Purnima", "hi": "हनुमान जयंती / चैत्र पूर्णिमा", "bn": "শ্রী শ্রী হনুমান জয়ন্তী / চৈত্র পূর্ণিমা"},

    # --- বৈশাখ মাস (Vaisakha) ---
    ("Vaisakha", "Shukla", 3): {"en": "Akshaya Tritiya / Parashurama Jayanti", "hi": "अक्षय तृतीया / परशुराम जयंती", "bn": "অক্ষয় তৃতীয়া মহাপর্ব / পরশুরাম জয়ন্তী"},
    ("Vaisakha", "Shukla", 5): {"en": "Adi Shankaracharya Jayanti", "hi": "आदि शंकराचार्य जयंती", "bn": "আদি শঙ্করাচার্য জয়ন্তী"},
    ("Vaisakha", "Shukla", 7): {"en": "Ganga Saptami", "hi": "गंगा सप्तमी", "bn": "শ্রী শ্রী গঙ্গা সপ্তমী"},
    ("Vaisakha", "Shukla", 9): {"en": "Sita Navami", "hi": "सीता नवमी", "bn": "শ্রী সীতা নবমী"},
    ("Vaisakha", "Shukla", 14): {"en": "Narasimha Jayanti", "hi": "नृसिंह जयंती", "bn": "শ্রী শ্রীনৃসিংহ জয়ন্তী"},
    ("Vaisakha", "Shukla", 15): {"en": "Buddha Purnima / Kurma Jayanti", "hi": "बुद्ध पूर्णिमा / कूर्म जयंती", "bn": "বুদ্ধ পূর্ণিমা / বৈশাখী পূর্ণিমা"},

    # --- জ্যৈষ্ঠ মাস (Jyeshtha) ---
    ("Jyeshtha", "Krishna", 15): {"en": "Vat Savitri Vrat / Shani Jayanti", "hi": "वट सावित्री व्रत / शनि जयंती", "bn": "বট সাবিত্রী ব্রত / শনি জয়ন্তী (অমাবস্যা)"},
    ("Jyeshtha", "Shukla", 10): {"en": "Ganga Dussehra", "hi": "गंगा दशहरा", "bn": "শ্রী শ্রী গঙ্গা দশহরা মহোৎসব"},
    ("Jyeshtha", "Shukla", 11): {"en": "Nirjala Ekadashi", "hi": "निर्जला एकादशी", "bn": "নির্জলা একাদশী ব্রত"},
    ("Jyeshtha", "Shukla", 15): {"en": "Snan Yatra (Lord Jagannath) / Vat Purnima", "hi": "देवस्नान पूर्णिमा / वट पूर्णिमा", "bn": "শ্রী জগন্নাথদেবের স্নানযাত্রা / দেবস্নান পূর্ণিমা"},

    # --- আষাঢ় মাস (Ashadha) ---
    ("Ashadha", "Shukla", 2): {"en": "Jagannath Ratha Yatra", "hi": "जगन्नाथ रथ यात्रा", "bn": "শ্রী শ্রী জগন্নাথদেবের রথযাত্রা মহোৎসব"},
    ("Ashadha", "Shukla", 10): {"en": "Ulto Rath / Bahuda Yatra", "hi": "उल्टा रथ / बहुड़ा यात्रा", "bn": "উল্টোরথ যাত্রা মহোৎসব"},
    ("Ashadha", "Shukla", 11): {"en": "Devshayani Ekadashi (Chaturmasya Begins)", "hi": "देवशयनी एकादशी (चातुर्मास प्रारंभ)", "bn": "দেবশয়নী একাদশী (চাতুর্মাস্য ব্রতারম্ভ)"},
    ("Ashadha", "Shukla", 15): {"en": "Guru Purnima / Vyasa Puja", "hi": "गुरु पूर्णिमा / व्यास पूजा", "bn": "গুরু পূর্ণিমা / মহর্ষি বেদব্যাস পূজা"},

    # --- শ্রাবণ মাস (Shravana) ---
    ("Shravana", "Shukla", 3): {"en": "Hariyali Teej", "hi": "हरियाली तीज", "bn": "হরিয়ালী তীজ"},
    ("Shravana", "Shukla", 5): {"en": "Nag Panchami / Manasa Puja", "hi": "नाग पंचमी / मनसा पूजा", "bn": "নাগ পঞ্চমী / মা মনসা পূজা"},
    ("Shravana", "Shukla", 15): {"en": "Raksha Bandhan / Jhulan Yatra Samapti", "hi": "रक्षाबंधन / सावन पूर्णिमा", "bn": "রাখীবন্ধন উৎসব / ঝুলনযাত্রা সমাপন"},

    # --- ভাদ্রপদ মাস (Bhadrapada) ---
    ("Bhadrapada", "Krishna", 8): {"en": "Krishna Janmashtami", "hi": "श्रीकृष्ण जन्माष्टमी", "bn": "শ্রী শ্রী কৃষ্ণ জন্মাষ্টমী মহাপর্ব"},
    ("Bhadrapada", "Krishna", 9): {"en": "Nandotsava", "hi": "नंदोत्सव", "bn": "শ্রী শ্রী নন্দোৎসব"},
    ("Bhadrapada", "Shukla", 3): {"en": "Hartalika Teej / Varaha Jayanti", "hi": "हरतालिका तीज / वराह जयंती", "bn": "হরতালিকা তীজ / বরাহ জয়ন্তী"},
    ("Bhadrapada", "Shukla", 4): {"en": "Ganesh Chaturthi / Vinayaka Chaturthi", "hi": "श्री गणेश चतुर्थी / विनायक चतुर्थी", "bn": "শ্রী গণেশ চতুর্থী / বিনায়ক পূজা"},
    ("Bhadrapada", "Shukla", 5): {"en": "Rishi Panchami", "hi": "ऋषि पंचमी", "bn": "ঋষি পঞ্চমী ব্রত"},
    ("Bhadrapada", "Shukla", 8): {"en": "Radhashtami", "hi": "राधाष्टमी", "bn": "শ্রী শ্রী রাধাষ্টমী মহাপর্ব"},
    ("Bhadrapada", "Shukla", 14): {"en": "Anant Chaturdashi / Ganesh Visarjan", "hi": "अनंत चतुर्दशी / गणेश विसर्जन", "bn": "অনন্ত চতুর্দশী ব্রত / গণেশ বিসর্জন"},

    # --- আশ্বিন মাস (Ashvina) - দুর্গাপূজা ও মহোৎসব ---
    ("Ashvina", "Krishna", 15): {"en": "Mahalaya (Amavasya / Pitru Tarpan)", "hi": "महालया / सर्वपितृ अमावस्या", "bn": "মহালয়া / পিতৃপক্ষের তর্পণ ও অমাবস্যা"},
    ("Ashvina", "Shukla", 1): {"en": "Sharad Navratri Begins / Ghatasthapana", "hi": "शारदीय नवरात्रि प्रारंभ / घटस्थापना", "bn": "শারদীয়া নবরাত্রি আরম্ভ ও ঘটস্থাপন"},
    ("Ashvina", "Shukla", 6): {"en": "Durga Sashti (Bodhan & Bilva Nimantran)", "hi": "दुर्गा षष्ठी (बिल्व निमंत्रण)", "bn": "শ্রী শ্রী দুর্গাপূজা: মহাষষ্ঠী (বোধন ও আমন্ত্রণ)"},
    ("Ashvina", "Shukla", 7): {"en": "Durga Saptami (Navapatrika Pravesh)", "hi": "दुर्गा सप्तमी (नवपत्रिका पूजा)", "bn": "শ্রী শ্রী দুর্গাপূজা: মহাসপ্তমী (নবপত্রিকা প্রবেশ)"},
    ("Ashvina", "Shukla", 8): {"en": "Durga Maha Ashtami & Sandhi Puja", "hi": "दुर्गा महाष्टमी / संधि व कुमारी पूजा", "bn": "শ্রী শ্রী দুর্গাপূজা: মহাঅষ্টমী, সন্ধিপূজা ও কুমারী পূজা"},
    ("Ashvina", "Shukla", 9): {"en": "Durga Maha Navami / Ayudha Puja", "hi": "दुर्गा महानवमी पूजा / आयुध पूजा", "bn": "শ্রী শ্রী দুর্গাপূজা: মহানবমী পূজা ও আয়ুধ পূজা"},
    ("Ashvina", "Shukla", 10): {"en": "Vijaya Dashami / Dussehra (Sindoor Khela)", "hi": "विजयादशमी / दशहरा", "bn": "বিজয়া দশমী / সিঁদুর খেলা ও প্রতিমা বিসর্জন"},
    ("Ashvina", "Shukla", 15): {"en": "Kojagari Lakshmi Puja / Sharad Purnima", "hi": "कोजागरी लक्ष्मी पूजा / शरद पूर्णिमा", "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা / শারদ পূর্ণিমা"},

    # --- কার্তিক মাস (Kartika) - শ্যামাপূজা ও দীপাবলি ---
    ("Kartika", "Krishna", 4): {"en": "Karwa Chauth", "hi": "करवा चौथ", "bn": "করবা চৌথ ব্রত"},
    ("Kartika", "Krishna", 8): {"en": "Ahoi Ashtami", "hi": "अहोई अष्टमी", "bn": "অহোই অষ্টমী ব্রত"},
    ("Kartika", "Krishna", 12): {"en": "Govatsa Dwadashi", "hi": "गोवत्स द्वादशी (बछ बारस)", "bn": "গোবৎসা দ্বাদশী / বাছুর পূজা"},
    ("Kartika", "Krishna", 13): {"en": "Dhanteras / Dhanvantari Jayanti", "hi": "धनतेरस / कुबेर पूजा", "bn": "শ্রী শ্রী ধনতেরাস / ধন্বন্তরি জয়ন্তী"},
    ("Kartika", "Krishna", 14): {"en": "Bhoot Chaturdashi / Naraka Chaturdashi", "hi": "नरक चतुर्दशी / छोटी दिवाली", "bn": "ভূত চতুর্দশী (১৪ প্রদীপ ও ১৪ শাক দান)"},
    ("Kartika", "Krishna", 15): {"en": "Shyama Puja (Kali Puja) / Diwali", "hi": "दीपावली / महालक्ष्मी पूजा", "bn": "শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / দীপাবলি"},
    ("Kartika", "Shukla", 1): {"en": "Govardhan Puja / Annakut Mahotsav", "hi": "गोवर्धन पूजा / अन्नकूट", "bn": "শ্রী শ্রী গোবর্ধন পূজা ও অন্নকূট মহোৎসব"},
    ("Kartika", "Shukla", 2): {"en": "Bhai Phonta / Bhatri Dwitiya", "hi": "भाई दूज / यम द्वितीया", "bn": "পবিত্র ভাইফোঁটা (ভ্রাতৃদ্বিতীয়া)"},
    ("Kartika", "Shukla", 6): {"en": "Chhath Puja (Sandhya Arghya)", "hi": "छठ पूजा (संध्या अर्घ्य)", "bn": "ছট পূজা (সন্ধ্যার অর্ঘ্যদান)"},
    ("Kartika", "Shukla", 7): {"en": "Chhath Puja (Usha Arghya)", "hi": "छठ पूजा (प्रातः अर्घ्य / पारण)", "bn": "ছট পূজা (ভোরের অর্ঘ্যদান ও পারণ)"},
    ("Kartika", "Shukla", 8): {"en": "Gopashtami (Go-Puja)", "hi": "गोपाष्टमी / गो-पूजा", "bn": "শ্রী শ্রী গোপাষ্টমী / গো-পূজা"},
    ("Kartika", "Shukla", 9): {"en": "Jagaddhatri Puja / Akshaya Navami", "hi": "जगद्धात्री पूजा / अक्षय नवमी", "bn": "শ্রী শ্রী জগদ্ধাত্রী পূজা / অক্ষয় নবমী"},
    ("Kartika", "Shukla", 11): {"en": "Devutthana Ekadashi / Tulsi Vivah", "hi": "देवउठनी एकादशी / तुलसी विवाह", "bn": "দেবউত্থান একাদশী / তুলসী বিবাহ"},
    ("Kartika", "Shukla", 14): {"en": "Vaikuntha Chaturdashi", "hi": "वैकुंठ चतुर्दशी", "bn": "বৈকুণ্ঠ চতুর্দশী"},
    ("Kartika", "Shukla", 15): {"en": "Rash Yatra / Dev Deepawali / Kartik Purnima", "hi": "देव दीपावली / रास पूर्णिमा", "bn": "শ্রী শ্রী রাসযাত্রা / রাসপূর্ণিমা / দেব দীপাবলি"},

    # --- মার্গশীর্ষ মাস (Margashirsha) ---
    ("Margashirsha", "Shukla", 5): {"en": "Vivah Panchami (Sri Rama-Sita Vivah)", "hi": "विवाह पंचमी (श्रीराम-सीता विवाह)", "bn": "বিবাহ পঞ্চমী (শ্রীশ্রী সীতারাম বিবাহ মহোৎসব)"},
    ("Margashirsha", "Shukla", 11): {"en": "Mokshada Ekadashi / Gita Jayanti", "hi": "गीता जयंती / मोक्षदा एकादशी", "bn": "শ্রীমদ্ভগবদ্গীতা জয়ন্তী / মোক্ষদা একাদশী"},
    ("Margashirsha", "Shukla", 15): {"en": "Dattatreya Jayanti / Annapurna Jayanti", "hi": "दत्तात्रेय जयंती / अन्नपूर्णा जयंती", "bn": "দত্তাত্রেয় জয়ন্তী / অন্নপূর্ণা জয়ন্তী / মার্গশীর্ষ পূর্ণিমা"},

    # --- পৌষ মাস (Pausha) ---
    ("Pausha", "Shukla", 15): {"en": "Pausha Purnima / Shakambhari Jayanti", "hi": "पौष पूर्णिमा / शाकंभरी जयंती", "bn": "পৌষ পূর্ণিমা / শাকম্ভরী জয়ন্তী"},

    # --- মাঘ মাস (Magha) ---
    ("Magha", "Shukla", 5): {"en": "Saraswati Puja / Vasant Panchami", "hi": "सरस्वती पूजा / बसंत पंचमी", "bn": "শ্রী শ্রী সরস্বতী পূজা / বসন্ত পঞ্চমী"},
    ("Magha", "Shukla", 7): {"en": "Ratha Saptami / Surya Jayanti", "hi": "रथ सप्तमी / आरोग्य सप्तमी", "bn": "রথ সপ্তমী / সূর্য জয়ন্তী"},
    ("Magha", "Shukla", 8): {"en": "Bhishma Ashtami", "hi": "भीष्म अष्टमी", "bn": "ভীষ্ম অষ্টমী"},
    ("Magha", "Shukla", 15): {"en": "Magha Purnima (Snan Dan)", "hi": "माघ पूर्णिमा (महा माघी)", "bn": "মাঘী পূর্ণিমা / মহামাঘী স্নান"},
    ("Magha", "Krishna", 14): {"en": "Maha Shivratri Vrat & Puja", "hi": "महाशिवरात्रि व्रत व पूजा", "bn": "শ্রী শ্রী মহা শিবরাত্রি ব্রত ও পূজা"},

    # --- ফাল্গুন মাস (Phalguna) ---
    ("Phalguna", "Shukla", 14): {"en": "Holika Dahan / Chhanchar", "hi": "होलिका दहन", "bn": "হোলিকা দহন / চাঁচর উৎসব"},
    ("Phalguna", "Shukla", 15): {"en": "Dol Jatra / Holi / Gaura Purnima", "hi": "होली / डोल पूर्णिमा / गौर पूर्णिमा", "bn": "শ্রী শ্রী দোলযাত্রা / শ্রী গৌরাঙ্গ মহাপ্রভুর আবির্ভাব / হোলি"},
}

# ==============================================================================
# ২. ভারতীয় জাতীয় ছুটির দিন ও স্মরণীয় দিবস (National Holidays)
# ==============================================================================
INDIAN_NATIONAL_HOLIDAYS = {
    (1, 12): {"en": "National Youth Day (Swami Vivekananda Jayanti)", "hi": "राष्ट्रीय युवा दिवस (स्वामी विवेकानंद जयंती)", "bn": "জাতীয় যুব দিবস (স্বামী বিবেকানন্দ জয়ন্তী)", "category": "national", "icon": "🇮🇳"},
    (1, 23): {"en": "Netaji Subhas Chandra Bose Jayanti (Parakram Diwas)", "hi": "नेताजी सुभाष चंद्र बोस जयंती (पराक्रम दिवस)", "bn": "নেতাজি সুভাষচন্দ্র বসুর জন্মজয়ন্তী (পরাক্রম দিবস)", "category": "national", "icon": "🇮🇳"},
    (1, 26): {"en": "Republic Day of India", "hi": "गणतंत्र दिवस", "bn": "ভারতের প্রজাতন্ত্র দিবস", "category": "national", "icon": "🇮🇳"},
    (4, 14): {"en": "Dr. B.R. Ambedkar Jayanti", "hi": "डॉ. बी.आर. आंबेडकर जयंती", "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী", "category": "national", "icon": "🇮🇳"},
    (8, 15): {"en": "Independence Day of India", "hi": "स्वतंत्रता दिवस", "bn": "ভারতের স্বাধীনতা দিবস", "category": "national", "icon": "🇮🇳"},
    (10, 2): {"en": "Mahatma Gandhi Jayanti", "hi": "गांधी जयंती / लाल बहादुर शास्त्री जयंती", "bn": "গান্ধী জয়ন্তী / লাল বাহাদুর শাস্ত্রী জয়ন্তী", "category": "national", "icon": "🇮🇳"},
    (10, 31): {"en": "National Unity Day (Sardar Patel Jayanti)", "hi": "राष्ट्रीय एकता दिवस (सरदार पटेल जयंती)", "bn": "জাতীয় একতা দিবস (সর্দার প্যাটেল জয়ন্তী)", "category": "national", "icon": "🇮🇳"},
    (11, 14): {"en": "Children's Day (Jawaharlal Nehru Jayanti)", "hi": "बाल दिवस (जवाहरलाल नेहरू जयंती)", "bn": "শিশু দিবস (জওহরলাল নেহেরু জয়ন্তী)", "category": "national", "icon": "🇮🇳"},
}

# ==============================================================================
# ৩. খ্রিস্টান ও আন্তর্জাতিক ফিক্সড দিবস (Fixed Gregorian / World Observances)
# ==============================================================================
FIXED_WORLD_CHRISTIAN_DAYS = {
    (1, 1): {"en": "New Year's Day", "hi": "नव वर्ष", "bn": "ইংরেজি নববর্ষ", "category": "world", "icon": "🌍"},
    (3, 8): {"en": "International Women's Day", "hi": "अंतर्राष्ट्रीय महिला दिवस", "bn": "আন্তর্জাতিক নারী দিবস", "category": "world", "icon": "🌍"},
    (4, 22): {"en": "Earth Day", "hi": "पृथ्वी दिवस", "bn": "বিশ্ব বসুন্ধরা দিবস", "category": "world", "icon": "🌍"},
    (5, 1): {"en": "International Workers' Day / May Day", "hi": "अंतर्राष्ट्रीय मजदूर दिवस", "bn": "আন্তর্জাতিক শ্রমিক দিবস / মে দিবস", "category": "world", "icon": "🌍"},
    (6, 5): {"en": "World Environment Day", "hi": "विश्व पर्यावरण दिवस", "bn": "বিশ্ব পরিবেশ দিবস", "category": "world", "icon": "🌍"},
    (6, 21): {"en": "International Yoga Day", "hi": "अंतर्राष्ट्रीय योग दिवस", "bn": "আন্তর্জাতিক যোগ দিবস", "category": "world", "icon": "🌍"},
    (12, 24): {"en": "Christmas Eve", "hi": "क्रिसमस ईव", "bn": "ক্রিসমাস ইভ", "category": "christian", "icon": "✝️"},
    (12, 25): {"en": "Christmas / Merry Christmas", "hi": "क्रिसमस / बड़ा दिन", "bn": "বড়দিন (শুভ ক্রিসমাস)", "category": "christian", "icon": "✝️"},
    (12, 31): {"en": "New Year's Eve", "hi": "नव वर्ष की पूर्वसंध्या", "bn": "বছরের শেষ দিন", "category": "world", "icon": "🌍"},
}

# ==============================================================================
# ৪. মুসলিম ও পরিবর্তনশীল খ্রিস্টান উৎসব (Multi-Year: 2025, 2026, 2027, 2028)
# ==============================================================================
VARIABLE_RELIGIOUS_DAYS = {
    # --- 2025 ---
    (2025, 3, 31): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2025, 4, 18): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2025, 4, 20): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2025, 6, 7): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️"},
    (2025, 7, 6): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️"},
    (2025, 9, 5): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️"},

    # --- 2026 ---
    (2026, 3, 20): {"en": "Eid-ul-Fitr (Ramadan Eid)", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2026, 4, 3): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2026, 4, 5): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2026, 5, 27): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️"},
    (2026, 6, 26): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️"},
    (2026, 8, 26): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️"},

    # --- 2027 ---
    (2027, 3, 10): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2027, 3, 26): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2027, 3, 28): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2027, 5, 17): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️"},
    (2027, 6, 16): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️"},
    (2027, 8, 15): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️"},

    # --- 2028 ---
    (2028, 2, 27): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️"},
    (2028, 4, 14): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️"},
    (2028, 4, 16): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️"},
    (2028, 5, 5): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️"},
    (2028, 6, 4): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️"},
}

# ==============================================================================
# ৫. উৎসব ও ব্রত রিটার্ন করার মূল ফাংশন (All Integrations)
# ==============================================================================
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
    
    # --- A. হিন্দু তিথিভিত্তিক সমস্ত পূজা ও উৎসব ---
    h_key = (lunar_month, paksha, tithi_num)
    if h_key in HINDU_FESTIVAL_DATABASE:
        festivals.append({
            "name": HINDU_FESTIVAL_DATABASE[h_key].get(l_key, HINDU_FESTIVAL_DATABASE[h_key]["en"]),
            "category": "hindu",
            "type": "Major Festival",
            "icon": "🕉️"
        })
    
    # একাদশী ও প্রদোষ ব্রত (বাংলা, হিন্দি ও ইংরেজি অনুবাদসহ)
    if tithi_num == 11:
        ekadashi_name = {"en": "Ekadashi Vrata / Fast", "hi": "एकादशी व्रत", "bn": "একাদশী ব্রত ও উপবাস"}
        ekadashi_deity = {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"}
        festivals.append({
            "name": ekadashi_name.get(l_key, "Ekadashi"),
            "category": "hindu",
            "type": "Vrata",
            "icon": "🕉️",
            "deity": ekadashi_deity.get(l_key, "Lord Sri Hari Vishnu")
        })
    elif tithi_num == 13:
        pradosh_name = {"en": "Pradosh Vrata", "hi": "प्रदोष व्रत", "bn": "প্রদোষ ব্রত"}
        pradosh_deity = {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান দেবাদিদেব মহাদেব"}
        festivals.append({
            "name": pradosh_name.get(l_key, "Pradosh"),
            "category": "hindu",
            "type": "Vrata",
            "icon": "🔱",
            "deity": pradosh_deity.get(l_key, "Lord Shiva")
        })
        
    # সৌর সংক্রান্তি ও ফিক্সড পূজা (পয়লা বৈশাখ, মকর সংক্রান্তি, বিশ্বকর্মা পূজা)
    m_d = (current_date.month, current_date.day)
    if m_d == (4, 15) or (sankranti_name and "Mesha" in sankranti_name):
        sank_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / पोइला बैशाख", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি"}
        festivals.append({"name": sank_names.get(l_key, "Poila Boishakh"), "category": "hindu", "type": "Solar", "icon": "🌾"})
    elif m_d == (1, 14) or (sankranti_name and "Makara" in sankranti_name):
        sank_names = {"en": "Makar Sankranti / Pongal", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি"}
        festivals.append({"name": sank_names.get(l_key, "Makar Sankranti"), "category": "hindu", "type": "Solar", "icon": "☀️"})
    elif m_d == (9, 17):
        vis_names = {"en": "Vishwakarma Puja", "hi": "विश्वकर्मा पूजा", "bn": "শ্রী শ্রী বিশ্বকর্মা পূজা"}
        festivals.append({"name": vis_names.get(l_key, "Vishwakarma Puja"), "category": "hindu", "type": "Major Festival", "icon": "⚙️"})

    # --- B. ভারতীয় জাতীয় ছুটির দিন ---
    if m_d in INDIAN_NATIONAL_HOLIDAYS:
        nat = INDIAN_NATIONAL_HOLIDAYS[m_d]
        festivals.append({
            "name": nat.get(l_key, nat["en"]),
            "category": nat["category"],
            "type": "National Holiday",
            "icon": nat["icon"]
        })

    # --- C. খ্রিস্টান ও আন্তর্জাতিক ফিক্সড দিবস ---
    if m_d in FIXED_WORLD_CHRISTIAN_DAYS:
        wc = FIXED_WORLD_CHRISTIAN_DAYS[m_d]
        festivals.append({
            "name": wc.get(l_key, wc["en"]),
            "category": wc["category"],
            "type": "Observance",
            "icon": wc["icon"]
        })

    # --- D. মুসলিম ও পরিবর্তনশীল খ্রিস্টান উৎসব ---
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
