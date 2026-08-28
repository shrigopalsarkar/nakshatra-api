from typing import List, Dict, Any

FESTIVAL_DATABASE = {
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
    ("Kartika", "Krishna", 14): {"en": "Naraka Chaturdashi / Choti Diwali", "hi": "नरक चतुर्दशी / छोटी दिवाली", "bn": "ভূত চতুর্দশী / চোটি দিওয়ালি"},
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

def get_festivals_for_day(
    lunar_month: str,
    paksha: str,
    tithi_num: int,
    sankranti_name: str = None,
    lang: str = "en"
) -> List[Dict[str, str]]:
    
    festivals = []
    lang_key = "bn" if "bn" in lang else "hi" if "hi" in lang else "en"
    
    # ১. প্রধান তিথিভিত্তিক উৎসব খোঁজা
    key = (lunar_month, paksha, tithi_num)
    if key in FESTIVAL_DATABASE:
        festivals.append({
            "name": FESTIVAL_DATABASE[key].get(lang_key, FESTIVAL_DATABASE[key]["en"]),
            "type": "Major Festival"
        })
    
    # ২. একাদশী ব্রত (প্রতি মাসের ১১ নম্বর তিথি)
    if tithi_num == 11:
        ekadashi_name = {
            "en": "Ekadashi Vrata",
            "hi": "एकादशी व्रत",
            "bn": "একাদশী ব্রত"
        }
        festivals.append({"name": ekadashi_name.get(lang_key, "Ekadashi"), "type": "Vrata"})
        
    # ৩. প্রদোষ ব্রত (প্রতি মাসের ১৩ নম্বর তিথি)
    if tithi_num == 13:
        pradosh_name = {
            "en": "Pradosh Vrata",
            "hi": "प्रदोष व्रत",
            "bn": "প্রদোষ ব্রত"
        }
        festivals.append({"name": pradosh_name.get(lang_key, "Pradosh"), "type": "Vrata"})
        
    # ৪. সৌর সংক্রান্তি উৎসব (যেমন: মকর সংক্রান্তি / পয়লা বৈশাখ)
    if sankranti_name:
        if "Makara" in sankranti_name:
            sank_names = {"en": "Makar Sankranti / Pongal", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি"}
            festivals.append({"name": sank_names.get(lang_key, "Makar Sankranti"), "type": "Solar"})
        elif "Mesha" in sankranti_name:
            sank_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / बैसाखी", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি"}
            festivals.append({"name": sank_names.get(lang_key, "Poila Boishakh"), "type": "Solar"})

    return festivals
