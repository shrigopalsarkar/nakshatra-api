from datetime import date
from typing import List, Dict, Any, Optional

# ==============================================================================
# ১. সনাতন/হিন্দু তিথিভিত্তিক সমস্ত পূজা, ব্রত, জয়ন্তী ও নবরাত্রি ডেটাবেজ
#    (Lunar Month, Paksha, Tithi_Number) -> আজীবনের জন্য ১০০% স্বয়ংক্রিয়
# ==============================================================================
HINDU_FESTIVAL_DATABASE = {
    # --------------------------------------------------------------------------
    # চৈত্র মাস (Chaitra)
    # --------------------------------------------------------------------------
    ("Chaitra", "Shukla", 1): {
        "en": "Chaitra Navratri Begins / Gudi Padwa / Basanti Durga Puja Bodhan",
        "hi": "चैत्र नवरात्रि प्रारंभ / गुड़ी पड़वा / वासंतिक दुर्गा पूजा बोधन",
        "bn": "চৈত্র নবরাত্রি আরম্ভ / বাসন্তী দুর্গাপূজা বোধন / গুড়ি পাড়ওয়া",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Maa Shailaputri"
    },
    ("Chaitra", "Shukla", 2): {
        "en": "Sindhara Dooj / Brahmacharini Puja",
        "hi": "सिंधारा दूज / माँ ब्रह्मचारिणी पूजा",
        "bn": "সিন্ধারা দুজ / দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Brahmacharini"
    },
    ("Chaitra", "Shukla", 3): {
        "en": "Gangaur / Matsya Jayanti / Chandraghanta Puja",
        "hi": "गणगौर पूजा / मत्स्य जयंती / माँ चंद्रघंटा पूजा",
        "bn": "গণগৌর পূজা / ভগবান মৎস্য জয়ন্তী / দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🐟", "deity": "Lord Matsya & Maa Gauri"
    },
    ("Chaitra", "Shukla", 5): {
        "en": "Lakshmi Panchami / Sri Panchami (Chaitra)",
        "hi": "लक्ष्मी पंचमी / श्री पंचमी",
        "bn": "শ্রী শ্রী লক্ষ্মী পঞ্চমী ব্রত",
        "category": "hindu", "type": "Vrata", "icon": "🪷", "deity": "Maa Lakshmi"
    },
    ("Chaitra", "Shukla", 8): {
        "en": "Basanti Maha Ashtami / Annapurna Puja / Mahagauri Puja",
        "hi": "माँ अन्नपूर्णा पूजा / बासंती महाष्टमी / महागौरी पूजा",
        "bn": "শ্রী শ্রী অন্নপূর্ণা পূজা / বাসন্তী মহাষ্টমী ও কুমারী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🪷", "deity": "Maa Annapurna & Mahagauri"
    },
    ("Chaitra", "Shukla", 9): {
        "en": "Sri Rama Navami / Siddhidatri Puja / Chaitra Navratri Samapan",
        "hi": "श्री राम नवमी / महानवमी / माँ सिद्धिदात्री पूजा",
        "bn": "শ্রী শ্রী রাম নবমী মহাপর্ব / বাসন্তী নবমী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🏹", "deity": "Lord Sri Rama & Maa Siddhidatri"
    },
    ("Chaitra", "Shukla", 15): {
        "en": "Hanuman Jayanti / Chaitra Purnima (Satyanarayan Puja)",
        "hi": "हनुमान जयंती / चैत्र पूर्णिमा (सत्यनारायण व्रत)",
        "bn": "শ্রী শ্রী হনুমান জয়ন্তী / চৈত্র পূর্ণিমা (শ্রী সত্যনারায়ণ পূজা)",
        "category": "hindu", "type": "Major Festival", "icon": "🚩", "deity": "Lord Hanuman & Sri Satyanarayan"
    },

    # --------------------------------------------------------------------------
    # বৈশাখ মাস (Vaisakha)
    # --------------------------------------------------------------------------
    ("Vaisakha", "Shukla", 3): {
        "en": "Akshaya Tritiya / Parashurama Jayanti / Treta Yugadi",
        "hi": "अक्षय तृतीया / परशुराम जयंती / त्रेता युगादि",
        "bn": "অক্ষয় তৃতীয়া মহাপর্ব / পরশুরাম জয়ন্তী / ত্রেতা যুগাদী",
        "category": "hindu", "type": "Major Festival", "icon": "🪙", "deity": "Lord Vishnu & Maa Lakshmi"
    },
    ("Vaisakha", "Shukla", 5): {
        "en": "Adi Shankaracharya Jayanti / Surdas Jayanti",
        "hi": "आदि शंकराचार्य जयंती / सूरदास जयंती",
        "bn": "আদি শঙ্করাচার্য জয়ন্তী / ভক্ত সুরদাস জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🕉️", "deity": "Jagadguru Adi Shankaracharya"
    },
    ("Vaisakha", "Shukla", 7): {
        "en": "Ganga Saptami / Jahnu Saptami",
        "hi": "गंगा सप्तमी / जाह्नू सप्तमी (गंगा अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা সপ্তমী / জাহ্নু সপ্তমী (গঙ্গা জন্মজয়ন্তী)",
        "category": "hindu", "type": "Major Festival", "icon": "🌊", "deity": "Maa Ganga"
    },
    ("Vaisakha", "Shukla", 9): {
        "en": "Sita Navami / Janaki Jayanti",
        "hi": "सीता नवमी / जानकी जयंती",
        "bn": "শ্রী সীতা নবমী / জানকী জন্মজয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🪷", "deity": "Maa Sita"
    },
    ("Vaisakha", "Shukla", 14): {
        "en": "Sri Narasimha Jayanti / Narasimha Chaturdashi",
        "hi": "श्री नृसिंह जयंती / नृसिंह चतुर्दशी व्रत",
        "bn": "শ্রী শ্রীনৃসিংহ চতুর্দশী / নৃসিংহ জয়ন্তী ব্রত",
        "category": "hindu", "type": "Major Festival", "icon": "🦁", "deity": "Lord Narasimha"
    },
    ("Vaisakha", "Shukla", 15): {
        "en": "Buddha Purnima / Kurma Jayanti / Vaisakhi Snan",
        "hi": "बुद्ध पूर्णिमा / कूर्म जयंती / वैशाखी स्नान",
        "bn": "বুদ্ধ পূর্ণিমা / বৈশাখী পূর্ণিমা / ভগবান কূর্ম জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "☸️", "deity": "Gautama Buddha & Lord Kurma"
    },

    # --------------------------------------------------------------------------
    # জ্যৈষ্ঠ মাস (Jyeshtha)
    # --------------------------------------------------------------------------
    ("Jyeshtha", "Krishna", 15): {
        "en": "Vat Savitri Vrat / Shani Jayanti / Phalaharini Kali Puja",
        "hi": "वट सावित्री व्रत / शनि जयंती / फलहारिणी काली पूजा (अमावस्या)",
        "bn": "বট সাবিত্রী ব্রত / শ্রী শনি জয়ন্তী / ফলহারিণী কালীপূজা (অমাবস্যা)",
        "category": "hindu", "type": "Vrata", "icon": "🌳", "deity": "Shani Deva, Savitri & Maa Kali"
    },
    ("Jyeshtha", "Shukla", 6): {
        "en": "Aranya Sasthi / Jamai Sasthi Vrat",
        "hi": "अरण्य षष्ठी / जमाई षष्ठी व्रत",
        "bn": "অরণ্য ষষ্ঠী / শ্রী শ্রী জামাই ষষ্ঠী ব্রত",
        "category": "hindu", "type": "Major Festival", "icon": "🌿", "deity": "Maa Sasthi"
    },
    ("Jyeshtha", "Shukla", 10): {
        "en": "Ganga Dussehra (Descent of Ganga)",
        "hi": "गंगा दशहरा (माँ गंगा का पृथ्वी पर अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা দশহরা মহোৎসব (মর্ত্যে গঙ্গা অবতরণ)",
        "category": "hindu", "type": "Major Festival", "icon": "🌊", "deity": "Maa Ganga"
    },
    ("Jyeshtha", "Shukla", 11): {
        "en": "Nirjala Ekadashi / Bhim Ekadashi",
        "hi": "निर्जला एकादशी (भीमसेन एकादशी)",
        "bn": "নির্জলা একাদশী ব্রত (ভীম একাদশী)",
        "category": "hindu", "type": "Vrata", "icon": "🕉️", "deity": "Lord Sri Hari Vishnu"
    },
    ("Jyeshtha", "Shukla", 15): {
        "en": "Snan Yatra (Lord Jagannath) / Vat Purnima",
        "hi": "देवस्नान पूर्णिमा / वट पूर्णिमा",
        "bn": "শ্রী জগন্নাথদেবের স্নানযাত্রা / দেবস্নান পূর্ণিমা",
        "category": "hindu", "type": "Major Festival", "icon": "🌸", "deity": "Lord Jagannath"
    },

    # --------------------------------------------------------------------------
    # আষাঢ় মাস (Ashadha - আষাঢ় গুপ্ত নবরাত্রি ও রথযাত্রা)
    # --------------------------------------------------------------------------
    ("Ashadha", "Shukla", 1): {
        "en": "Ashadha Gupt Navratri Begins / Varahi Puja",
        "hi": "आषाढ़ गुप्त नवरात्रि प्रारंभ / वाराही देवी पूजा",
        "bn": "আষাঢ় গুপ্ত নবরাত্রি আরম্ভ / দেবী বারাহী ও দশমহাবিদ্যা পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Das Mahavidya & Maa Varahi"
    },
    ("Ashadha", "Shukla", 2): {
        "en": "Jagannath Ratha Yatra Mahotsav",
        "hi": "श्री जगन्नाथ रथ यात्रा महोत्सव",
        "bn": "শ্রী শ্রী জগন্নাথদেবের রথযাত্রা মহোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "🚩", "deity": "Lord Jagannath, Balabhadra, Subhadra"
    },
    ("Ashadha", "Shukla", 7): {
        "en": "Bipodtarini Vrat & Puja (Sasthi/Saptami)",
        "hi": "विपत्तारीणी व्रत व पूजा",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত ও পূজা",
        "category": "hindu", "type": "Vrata", "icon": "🔱", "deity": "Maa Bipodtarini Durga"
    },
    ("Ashadha", "Shukla", 8): {
        "en": "Bipodtarini Vrat (Shukla Ashtami)",
        "hi": "विपत्तारीणी व्रत (अष्टमी)",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত (অষ্টমী)",
        "category": "hindu", "type": "Vrata", "icon": "🔱", "deity": "Maa Bipodtarini Durga"
    },
    ("Ashadha", "Shukla", 10): {
        "en": "Ulto Rath / Bahuda Yatra",
        "hi": "उल्टा रथ / बहुड़ा यात्रा",
        "bn": "উল্টোরথ যাত্রা মহোৎসব (বাহুড়া যাত্রা)",
        "category": "hindu", "type": "Major Festival", "icon": "🚩", "deity": "Lord Jagannath"
    },
    ("Ashadha", "Shukla", 11): {
        "en": "Devshayani Ekadashi (Chaturmasya Vrata Begins)",
        "hi": "देवशयनी एकादशी (चातुर्मास प्रारंभ)",
        "bn": "দেবশয়নী একাদশী (চাতুর্মাস্য ব্রতারম্ভ)",
        "category": "hindu", "type": "Vrata", "icon": "🕉️", "deity": "Lord Sri Hari Vishnu"
    },
    ("Ashadha", "Shukla", 15): {
        "en": "Guru Purnima / Maharshi Vyasa Puja / Kokila Vrat",
        "hi": "गुरु पूर्णिमा / वेदव्यास पूजा / कोकिला व्रत",
        "bn": "গুরু পূর্ণিমা / মহর্ষি বেদব্যাস পূজা / কোকিলা ব্রত",
        "category": "hindu", "type": "Major Festival", "icon": "🙏", "deity": "Sri Guru & Maharshi Vyasa"
    },

    # --------------------------------------------------------------------------
    # শ্রাবণ মাস (Shravana)
    # --------------------------------------------------------------------------
    ("Shravana", "Shukla", 3): {
        "en": "Hariyali Teej / Madhushrava",
        "hi": "हरियाली तीज / मधुश्रवा",
        "bn": "হরিয়ালী তীজ উৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "🌿", "deity": "Lord Shiva & Maa Parvati"
    },
    ("Shravana", "Shukla", 5): {
        "en": "Nag Panchami / Maa Manasa Puja / Garuda Panchami",
        "hi": "नाग पंचमी / माँ मनसा पूजा / गरुड़ पंचमी",
        "bn": "নাগ পঞ্চমী / মা মনসা পূজা / গরুড় পঞ্চমী",
        "category": "hindu", "type": "Major Festival", "icon": "🐍", "deity": "Maa Manasa & Nag Devata"
    },
    ("Shravana", "Shukla", 6): {
        "en": "Kalki Jayanti",
        "hi": "कल्कि जयंती",
        "bn": "ভগবান কল্কি জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "⚔️", "deity": "Lord Kalki"
    },
    ("Shravana", "Shukla", 15): {
        "en": "Raksha Bandhan / Jhulan Yatra Samapti / Hayagriva Jayanti",
        "hi": "रक्षाबंधन / सावन पूर्णिमा / हयग्रीव जयंती (झूलन यात्रा समापन)",
        "bn": "রাখীবন্ধন উৎসব / ঝুলনযাত্রা সমাপন / ভগবান হয়গ্রীব জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🧵", "deity": "Lord Krishna, Draupadi & Lord Hayagriva"
    },

    # --------------------------------------------------------------------------
    # ভাদ্রপদ মাস (Bhadrapada - জন্মাষ্টমী, গণেশ চতুর্থী ও রাধাষ্টমী)
    # --------------------------------------------------------------------------
    ("Bhadrapada", "Krishna", 8): {
        "en": "Krishna Janmashtami / Gokulashtami",
        "hi": "श्रीकृष्ण जन्माष्टमी / गोकुलाष्टमी",
        "bn": "শ্রী শ্রী কৃষ্ণ জন্মাষ্টমী মহাপর্ব",
        "category": "hindu", "type": "Major Festival", "icon": "🦚", "deity": "Bhagwan Sri Krishna"
    },
    ("Bhadrapada", "Krishna", 9): {
        "en": "Sri Nandotsava",
        "hi": "श्री नंदोत्सव",
        "bn": "শ্রী শ্রী নন্দোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "🍯", "deity": "Bhagwan Sri Krishna & Nanda Baba"
    },
    ("Bhadrapada", "Shukla", 3): {
        "en": "Hartalika Teej / Varaha Jayanti",
        "hi": "हरतालिका तीज / वराह जयंती",
        "bn": "হরতালিকা তীজ / ভগবান বরাহ অবতার জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🌺", "deity": "Lord Shiva, Parvati & Lord Varaha"
    },
    ("Bhadrapada", "Shukla", 4): {
        "en": "Ganesh Chaturthi / Vinayaka Chavithi (Ganeshotsav Begins)",
        "hi": "श्री गणेश चतुर्थी / विनायक पूजा (गणेशोत्सव प्रारंभ)",
        "bn": "শ্রী শ্রী গণেশ চতুর্থী / বিনায়ক পূজা (গণেশোৎসব আরম্ভ)",
        "category": "hindu", "type": "Major Festival", "icon": "🐘", "deity": "Lord Ganesha"
    },
    ("Bhadrapada", "Shukla", 5): {
        "en": "Rishi Panchami Vrat",
        "hi": "ऋषि पंचमी व्रत",
        "bn": "ঋষি পঞ্চমী ব্রত (সপ্তর্ষি পূজা)",
        "category": "hindu", "type": "Vrata", "icon": "🪔", "deity": "Sapta Rishis"
    },
    ("Bhadrapada", "Shukla", 8): {
        "en": "Radhashtami / Mahalakshmi Vrat Begins",
        "hi": "श्री राधाष्टमी / महालक्ष्मी व्रत प्रारंभ",
        "bn": "শ্রী শ্রী রাধাষ্টমী মহাপর্ব / মহালক্ষ্মী ব্রতারম্ভ",
        "category": "hindu", "type": "Major Festival", "icon": "🪷", "deity": "Srimati Radharani & Maa Mahalakshmi"
    },
    ("Bhadrapada", "Shukla", 11): {
        "en": "Parsva Ekadashi / Vamana Jayanti",
        "hi": "परिवर्तिनी एकादशी / वामन जयंती",
        "bn": "পার্শ্ব একাদশী (পরিবর্তিনী) / ভগবান বামন জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🕉️", "deity": "Lord Vamana & Sri Hari"
    },
    ("Bhadrapada", "Shukla", 14): {
        "en": "Anant Chaturdashi / Ganesh Visarjan",
        "hi": "अनंत चतुर्दशी व्रत / गणेश विसर्जन",
        "bn": "অনন্ত চতুর্দশী ব্রত / শ্রী গণেশ বিসর্জন",
        "category": "hindu", "type": "Vrata", "icon": "🕉️", "deity": "Lord Ananta Padmanabha & Ganesha"
    },
    ("Bhadrapada", "Shukla", 15): {
        "en": "Bhadrapada Purnima / Pitru Paksha Shraddha Begins",
        "hi": "भाद्रपद पूर्णिमा / पितृपक्ष प्रारंभ (सत्यनारायण पूजा)",
        "bn": "ভাদ্রপদ পূর্ণিমা / পিতৃপক্ষ শ্রাদ্ধারম্ভ (সত্যনারায়ণ পূজা)",
        "category": "hindu", "type": "Major Festival", "icon": "🙏", "deity": "Lord Satyanarayan & Ancestors"
    },

    # --------------------------------------------------------------------------
    # আশ্বিন মাস (Ashvina - মহালয়া, দুর্গাপূজা ও কোজাগরী লক্ষ্মীপূজা)
    # --------------------------------------------------------------------------
    ("Ashvina", "Krishna", 15): {
        "en": "Mahalaya (Sarvapitri Amavasya / Pitru Tarpan)",
        "hi": "महालया / सर्वपितृ अमावस्या / तर्पण",
        "bn": "মহালয়া / সর্বপিতৃ অমাবস্যা ও পিতৃপক্ষের তর্পণ",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Pitru Devas"
    },
    ("Ashvina", "Shukla", 1): {
        "en": "Sharad Navratri Begins / Ghatasthapana / Shailaputri Puja",
        "hi": "शारदीय नवरात्रि प्रारंभ / घटस्थापना / माँ शैलपुत्री पूजा",
        "bn": "শারদীয়া নবরাত্রি আরম্ভ / ঘটস্থাপন / দেবী শৈলপুত্রী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Shailaputri"
    },
    ("Ashvina", "Shukla", 2): {
        "en": "Navratri Day 2: Brahmacharini Puja",
        "hi": "नवरात्रि दिवस २: माँ ब्रह्मचारिणी पूजा",
        "bn": "শারদ নবরাত্রি ২য় দিন: দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Brahmacharini"
    },
    ("Ashvina", "Shukla", 3): {
        "en": "Navratri Day 3: Chandraghanta Puja",
        "hi": "नवरात्रि दिवस ३: माँ चंद्रघंटा पूजा",
        "bn": "শারদ নবরাত্রি ৩য় দিন: দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Chandraghanta"
    },
    ("Ashvina", "Shukla", 4): {
        "en": "Navratri Day 4: Kushmanda Puja",
        "hi": "नवरात्रि दिवस ४: माँ कूष्मांडा पूजा",
        "bn": "শারদ নবরাত্রি ৪র্থ দিন: দেবী কূষ্মাণ্ডা পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Kushmanda"
    },
    ("Ashvina", "Shukla", 5): {
        "en": "Navratri Day 5: Skandamata Puja / Upang Lalita Vrat",
        "hi": "नवरात्रि दिवस ५: माँ स्कंदमाता पूजा / उपांग ललिता व्रत",
        "bn": "শারদ নবরাত্রি ৫ম দিন: দেবী স্কন্দমাতা পূজা / উপাঙ্গ ললিতা ব্রত",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Skandamata & Lalita"
    },
    ("Ashvina", "Shukla", 6): {
        "en": "Durga Puja: Maha Sashti (Bodhan & Bilva Nimantran)",
        "hi": "दुर्गा षष्ठी (बिल्व निमंत्रण व बोधन / कात्यायनी पूजा)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাষষ্ঠী (বোধন, আমন্ত্রণ ও অধিবাস)",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Katyayani"
    },
    ("Ashvina", "Shukla", 7): {
        "en": "Durga Puja: Maha Saptami (Navapatrika Pravesh Puja)",
        "hi": "दुर्गा सप्तमी (नवपत्रिका प्रवेश पूजा / कालरात्रि पूजा)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাসপ্তমী (নবপত্রিকা প্রবেশ ও মহাস্নান)",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Kalaratri"
    },
    ("Ashvina", "Shukla", 8): {
        "en": "Durga Puja: Maha Ashtami / Sandhi Puja / Kumari Puja",
        "hi": "दुर्गा महाष्टमी / संधि पूजा / कुमारी पूजा (महागौरी)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাঅষ্টমী, সন্ধিপূজা ও কুমারী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Chamunda Durga & Mahagauri"
    },
    ("Ashvina", "Shukla", 9): {
        "en": "Durga Puja: Maha Navami / Ayudha Puja / Navami Homa",
        "hi": "दुर्गा महानवमी पूजा / आयुध पूजा / हवन (सिद्धिदात्री)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহানবমী পূজা ও আয়ুধ পূজা (মহা হোম)",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Siddhidatri Durga"
    },
    ("Ashvina", "Shukla", 10): {
        "en": "Vijaya Dashami / Dussehra / Sindoor Khela & Visarjan",
        "hi": "विजयादशमी / दशहरा / सिंदूर खेला व विसर्जन (अपराजिता पूजा)",
        "bn": "শ্রী শ্রী বিজয়া দশমী / দশহরা / সিঁদুর খেলা ও প্রতিমা বিসর্জন",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Maa Durga & Lord Sri Rama"
    },
    ("Ashvina", "Shukla", 15): {
        "en": "Kojagari Lakshmi Puja / Sharad Purnima / Kumar Purnima",
        "hi": "कोजागरी लक्ष्मी पूजा / शरद पूर्णिमा / कुमार पूर्णिमा",
        "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা / শারদ পূর্ণিমা মহোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "🪷", "deity": "Maa Lakshmi"
    },

    # --------------------------------------------------------------------------
    # কার্তিক মাস (Kartika - শ্যামাপূজা, দীপাবলি, ভাইফোঁটা, জগদ্ধাত্রী ও কার্তিক পূজা)
    # --------------------------------------------------------------------------
    ("Kartika", "Krishna", 4): {
        "en": "Karwa Chauth Vrat",
        "hi": "करवा चौथ व्रत (करक चतुर्थी)",
        "bn": "করবা চৌথ ব্রত",
        "category": "hindu", "type": "Vrata", "icon": "🌙", "deity": "Lord Shiva, Parvati & Chandra Deva"
    },
    ("Kartika", "Krishna", 8): {
        "en": "Ahoi Ashtami Vrat / Radha Kund Snan",
        "hi": "अहोई अष्टमी व्रत / राधा कुंड स्नान",
        "bn": "অহোই অষ্টমী ব্রত / শ্রী রাধাকুণ্ড স্নান",
        "category": "hindu", "type": "Vrata", "icon": "🪔", "deity": "Maa Ahoi"
    },
    ("Kartika", "Krishna", 12): {
        "en": "Govatsa Dwadashi / Bachh Baras / Gau Puja",
        "hi": "गोवत्स द्वादशी (बछ बारस) / गौ माता पूजा",
        "bn": "গোবৎসা দ্বাদশী / বাছুর ও গো-পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🐄", "deity": "Gau Mata & Lord Krishna"
    },
    ("Kartika", "Krishna", 13): {
        "en": "Dhanteras / Dhanvantari Jayanti / Kuber Puja / Yama Deepam",
        "hi": "धनतेरस / धन्वंतरि जयंती / कुबेर पूजा / यम दीपदान",
        "bn": "শ্রী শ্রী ধনতেরাস / ধন্বন্তরি জয়ন্তী / কুবের পূজা (যম দীপদান)",
        "category": "hindu", "type": "Major Festival", "icon": "🪙", "deity": "Lord Dhanvantari & Kuber"
    },
    ("Kartika", "Krishna", 14): {
        "en": "Bhoot Chaturdashi / Naraka Chaturdashi / 14 Pradeep Dan",
        "hi": "नरक चतुर्दशी / छोटी दिवाली / रूप चौदस",
        "bn": "ভূত চতুর্দশী (১৪ প্রদীপ ও ১৪ শাক দান) / নরক চতুর্দশী",
        "category": "hindu", "type": "Major Festival", "icon": "🪔", "deity": "Yamaraja & Ancestors"
    },
    ("Kartika", "Krishna", 15): {
        "en": "Shyama Puja (Kali Puja) / Diwali / Deepawali Maha Lakshmi Puja",
        "hi": "दीपावली / महालक्ष्मी पूजा / माँ काली पूजा (अमावस्या)",
        "bn": "শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / দীপাবলি মহোৎসব ও মহালক্ষ্মী পূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🪔", "deity": "Maa Kali & Maa Mahalakshmi"
    },
    ("Kartika", "Shukla", 1): {
        "en": "Govardhan Puja / Annakut Mahotsav / Bali Pratipada",
        "hi": "गोवर्धन पूजा / अन्नकूट महोत्सव / बलि प्रतिपदा",
        "bn": "শ্রী শ্রী গোবর্ধন পূজা ও অন্নকূট মহোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "⛰️", "deity": "Lord Sri Krishna (Giriraj)"
    },
    ("Kartika", "Shukla", 2): {
        "en": "Bhai Phonta / Bhatri Dwitiya / Yama Dwitiya",
        "hi": "भाई दूज / यम द्वितीया / भ्रातृ द्वितीया",
        "bn": "পবিত্র ভাইফোঁটা (ভ্রাতৃদ্বিতীয়া / যমদ্বিতীয়া)",
        "category": "hindu", "type": "Major Festival", "icon": "🌸", "deity": "Yamuna & Yamaraja"
    },
    ("Kartika", "Shukla", 6): {
        "en": "Chhath Puja (Sandhya Arghya / Surya Sashthi)",
        "hi": "छठ पूजा (संध्या अर्घ्य / सूर्य षष्ठी)",
        "bn": "ছট পূজা (সন্ধ্যার অর্ঘ্যদান ও সূর্য ষষ্ঠী)",
        "category": "hindu", "type": "Major Festival", "icon": "☀️", "deity": "Surya Deva & Chhathi Maiya"
    },
    ("Kartika", "Shukla", 7): {
        "en": "Chhath Puja (Usha Arghya & Paran)",
        "hi": "छठ पूजा (प्रातः अर्घ्य / पारण)",
        "bn": "ছট পূজা (ভোরের অর্ঘ্যদান ও পারণ)",
        "category": "hindu", "type": "Major Festival", "icon": "☀️", "deity": "Surya Deva & Chhathi Maiya"
    },
    ("Kartika", "Shukla", 8): {
        "en": "Gopashtami / Gau Puja Mahotsav",
        "hi": "गोपाष्टमी / कामधेनु गौ पूजा",
        "bn": "শ্রী শ্রী গোপাষ্টমী / কামধেনু গো-পূজা মহোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "🐄", "deity": "Lord Krishna & Gau Mata"
    },
    ("Kartika", "Shukla", 9): {
        "en": "Sri Jagaddhatri Puja / Akshaya Navami / Amla Navami",
        "hi": "जगद्धात्री पूजा / अक्षय नवमी / आँवला नवमी",
        "bn": "শ্রী শ্রী জগদ্ধাত্রী পূজা / অক্ষয় নবমী / আমলকী নবমী",
        "category": "hindu", "type": "Major Festival", "icon": "🦁", "deity": "Maa Jagaddhatri"
    },
    ("Kartika", "Shukla", 11): {
        "en": "Devutthana Ekadashi / Tulsi Vivah / Bhishma Panchaka Begins",
        "hi": "देवउठनी एकादशी / तुलसी विवाह / भीष्म पंचक प्रारंभ",
        "bn": "দেবউত্থান একাদশী / তুলসী বিবাহ / ভীষ্ম পঞ্চক ব্রতারম্ভ",
        "category": "hindu", "type": "Vrata", "icon": "🌿", "deity": "Lord Vishnu & Tulsi Maharani"
    },
    ("Kartika", "Shukla", 14): {
        "en": "Vaikuntha Chaturdashi",
        "hi": "वैकुंठ चतुर्दशी (हरि-हर मिलन)",
        "bn": "শ্রী বৈকুণ্ঠ চতুর্দশী (হরি-হর মিলন)",
        "category": "hindu", "type": "Vrata", "icon": "🕉️", "deity": "Lord Shiva & Lord Vishnu"
    },
    ("Kartika", "Shukla", 15): {
        "en": "Sri Kartik Puja / Rash Yatra / Dev Deepawali / Kartik Purnima",
        "hi": "कार्तिक पूजा / देव दीपावली / रास पूर्णिमा / त्रिपुरारी पूर्णिमा",
        "bn": "শ্রী শ্রী কার্তিক পূজা / শ্রী শ্রী রাসযাত্রা / রাসপূর্ণিমা / দেব দীপাবলি",
        "category": "hindu", "type": "Major Festival", "icon": "🪔", "deity": "Lord Kartikeya, Radha Krishna & Shiva"
    },

    # --------------------------------------------------------------------------
    # মার্গশীর্ষ মাস (Margashirsha / অগ্রহায়ণ)
    # --------------------------------------------------------------------------
    ("Margashirsha", "Shukla", 5): {
        "en": "Vivah Panchami (Sri Rama-Sita Vivah Mahotsav)",
        "hi": "विवाह पंचमी (श्रीराम-जानकी विवाह महोत्सव)",
        "bn": "বিবাহ পঞ্চমী (শ্রীশ্রী সীতারাম শুভ বিবাহ মহোৎসব)",
        "category": "hindu", "type": "Major Festival", "icon": "🏹", "deity": "Lord Sri Rama & Maa Sita"
    },
    ("Margashirsha", "Shukla", 6): {
        "en": "Champa Sasthi / Skanda Sasthi",
        "hi": "चंपा षष्ठी / स्कंद षष्ठी",
        "bn": "চম্পা ষষ্ঠী / স্কন্দ ষষ্ঠী ব্রত",
        "category": "hindu", "type": "Vrata", "icon": "🦚", "deity": "Lord Kartikeya (Khandoba)"
    },
    ("Margashirsha", "Shukla", 11): {
        "en": "Mokshada Ekadashi / Srimad Bhagavad Gita Jayanti",
        "hi": "गीता जयंती / मोक्षदा एकादशी",
        "bn": "শ্রীমদ্ভগবদ্গীতা জয়ন্তী / মোক্ষদা একাদশী",
        "category": "hindu", "type": "Vrata", "icon": "📜", "deity": "Bhagwan Sri Krishna & Srimad Bhagavad Gita"
    },
    ("Margashirsha", "Shukla", 15): {
        "en": "Dattatreya Jayanti / Annapurna Jayanti / Margashirsha Purnima",
        "hi": "दत्तात्रेय जयंती / अन्नपूर्णा जयंती / मार्गशीर्ष पूर्णिमा",
        "bn": "শ্রী দত্তাত্রেয় জয়ন্তী / মা অন্নপূর্ণা আবির্ভাব / মার্গশীর্ষ পূর্ণিমা",
        "category": "hindu", "type": "Major Festival", "icon": "🕉️", "deity": "Lord Dattatreya & Maa Annapurna"
    },

    # --------------------------------------------------------------------------
    # পৌষ মাস (Pausha)
    # --------------------------------------------------------------------------
    ("Pausha", "Shukla", 15): {
        "en": "Pausha Purnima / Shakambhari Jayanti (Shakambhari Navratri Samapan)",
        "hi": "पौष पूर्णिमा / शाकंभरी जयंती (शाकंभरी नवरात्रि समापन)",
        "bn": "পৌষ পূর্ণিমা / মা শাকম্ভরী দেবী জয়ন্তী (শাকম্ভরী নবরাত্রি সমাপন)",
        "category": "hindu", "type": "Major Festival", "icon": "🪷", "deity": "Maa Shakambhari Durga"
    },

    # --------------------------------------------------------------------------
    # মাঘ মাস (Magha - মাঘ গুপ্ত নবরাত্রি, সরস্বতী পূজা ও মহা শিবরাত্রি)
    # --------------------------------------------------------------------------
    ("Magha", "Shukla", 1): {
        "en": "Magha Gupt Navratri Begins",
        "hi": "माघ गुप्त नवरात्रि प्रारंभ / घटस्थापना",
        "bn": "মাঘ গুপ্ত নবরাত্রি আরম্ভ / ঘটস্থাপন ও দশমহাবিদ্যা সাধনা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Das Mahavidya & Maa Durga"
    },
    ("Magha", "Shukla", 4): {
        "en": "Ganesha Jayanti / Varad Vinayaka Chaturthi / Til Kund Chaturthi",
        "hi": "गणेश जयंती / वरद चतुर्थी / तिल कुंद चतुर्थी",
        "bn": "শ্রী গণেশ জন্মজয়ন্তী / বরদ বিনায়ক চতুর্থী (তিল চতুর্থী)",
        "category": "hindu", "type": "Major Festival", "icon": "🐘", "deity": "Lord Ganesha"
    },
    ("Magha", "Shukla", 5): {
        "en": "Sri Saraswati Puja / Vasant Panchami / Sri Panchami",
        "hi": "सरस्वती पूजा / बसंत पंचमी / श्री पंचमी / वाग्देवी आराधना",
        "bn": "শ্রী শ্রী সরস্বতী পূজা / বসন্ত পঞ্চমী / শ্রীপঞ্চমী (বাগদেবী আরাধনা)",
        "category": "hindu", "type": "Major Festival", "icon": "🪕", "deity": "Maa Saraswati (Vagdevi)"
    },
    ("Magha", "Shukla", 7): {
        "en": "Ratha Saptami / Surya Jayanti / Arogya Saptami",
        "hi": "रथ सप्तमी / सूर्य जयंती / आरोग्य सप्तमी / अचला सप्तमी",
        "bn": "রথ সপ্তমী / সূর্য জয়ন্তী / আরোগ্য সপ্তমী মহোৎসব",
        "category": "hindu", "type": "Major Festival", "icon": "☀️", "deity": "Surya Deva"
    },
    ("Magha", "Shukla", 8): {
        "en": "Bhishma Ashtami Vrat & Tarpan",
        "hi": "भीष्म अष्टमी व्रत व तर्पण",
        "bn": "ভীষ্ম অষ্টমী ব্রত ও পিতামহ ভীষ্ম তর্পণ",
        "category": "hindu", "type": "Vrata", "icon": "🏹", "deity": "Bhishma Pitamah"
    },
    ("Magha", "Shukla", 15): {
        "en": "Magha Purnima / Maha Maghi Snan / Lalita Jayanti",
        "hi": "माघ पूर्णिमा / महा माघी स्नान / ललिता जयंती",
        "bn": "মাঘী পূর্ণিমা / মহামাঘী স্নান / মা ললিতা জয়ন্তী",
        "category": "hindu", "type": "Major Festival", "icon": "🌊", "deity": "Lord Vishnu, Ganga & Tripura Sundari"
    },
    ("Magha", "Krishna", 14): {
        "en": "Sri Maha Shivratri Vrat & Mahapuja",
        "hi": "श्री महाशिवरात्रि व्रत व महापूजा / शिव-पार्वती विवाह",
        "bn": "শ্রী শ্রী মহা শিবরাত্রি ব্রত ও চার প্রহর শিবপূজা",
        "category": "hindu", "type": "Major Festival", "icon": "🔱", "deity": "Lord Shiva (Devadhidev) & Maa Parvati"
    },
    ("Magha", "Krishna", 15): {
        "en": "Mauni Amavasya / Magha Amavasya Mahasnan",
        "hi": "मौनी अमावस्या / माघ अमावस्या महास्नान",
        "bn": "মৌনী অমাবস্যা / মাঘী অমাবস্যা মহাতীর্থ স্নান",
        "category": "hindu", "type": "Major Festival", "icon": "🕉️", "deity": "Lord Vishnu & Shiva"
    },

    # --------------------------------------------------------------------------
    # ফাল্গুন মাস (Phalguna - দোলযাত্রা, হোলি ও শ্রীচৈতন্য আবির্ভাব)
    # --------------------------------------------------------------------------
    ("Phalguna", "Krishna", 14): {
        "en": "Maha Shivratri (Purnimanta tradition) / Masik Shivratri",
        "hi": "महाशिवरात्रि / मासिक शिवरात्रि व्रत",
        "bn": "মহা শিবরাত্রি ব্রত / মাসিক শিবরাত্রি",
        "category": "hindu", "type": "Vrata", "icon": "🔱", "deity": "Lord Shiva"
    },
    ("Phalguna", "Shukla", 14): {
        "en": "Holika Dahan / Chhanchar Utsav",
        "hi": "होलिका दहन / कामदहन",
        "bn": "হোলিকা দহন / চাঁচর উৎসব (অগ্নি উৎসব)",
        "category": "hindu", "type": "Major Festival", "icon": "🔥", "deity": "Bhakt Prahlada & Lord Narasimha"
    },
    ("Phalguna", "Shukla", 15): {
        "en": "Dol Jatra / Holi / Sri Gaura Purnima / Lakshmi Jayanti",
        "hi": "होली / डोल पूर्णिमा / गौर पूर्णिमा / लक्ष्मी जयंती",
        "bn": "শ্রী শ্রী দোলযাত্রা / বসন্তোৎসব / শ্রীমন্মহাপ্রভুর শুভ আবির্ভাব / হোলি",
        "category": "hindu", "type": "Major Festival", "icon": "🎨", "deity": "Radha Krishna, Sri Chaitanya & Lakshmi"
    },
}

# ==============================================================================
# ২. ভারতীয় জাতীয় ছুটির দিন ও স্মরণীয় দিবস (National Holidays)
# ==============================================================================
INDIAN_NATIONAL_HOLIDAYS = {
    (1, 12): {"en": "National Youth Day (Swami Vivekananda Jayanti)", "hi": "राष्ट्रीय युवा दिवस (स्वामी विवेकानंद जयंती)", "bn": "জাতীয় যুব দিবস (স্বামী বিবেকানন্দ জয়ন্তী)", "category": "national", "icon": "🇮🇳", "deity": "Swami Vivekananda"},
    (1, 23): {"en": "Netaji Subhas Chandra Bose Jayanti (Parakram Diwas)", "hi": "नेताजी सुभाष चंद्र बोस जयंती (पराक्रम दिवस)", "bn": "নেতাজি সুভাষচন্দ্র বসুর জন্মজয়ন্তী (পরাক্রম দিবস)", "category": "national", "icon": "🇮🇳", "deity": "Netaji Subhas Chandra Bose"},
    (1, 26): {"en": "Republic Day of India", "hi": "गणतंत्र दिवस", "bn": "ভারতের প্রজাতন্ত্র দিবস", "category": "national", "icon": "🇮🇳", "deity": "Republic of India"},
    (4, 14): {"en": "Dr. B.R. Ambedkar Jayanti", "hi": "डॉ. बी.आर. आंबेडकर जयंती", "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী", "category": "national", "icon": "🇮🇳", "deity": "Dr. B.R. Ambedkar"},
    (8, 15): {"en": "Independence Day of India", "hi": "स्वतंत्रता दिवस", "bn": "ভারতের স্বাধীনতা দিবস", "category": "national", "icon": "🇮🇳", "deity": "Bharat Mata"},
    (10, 2): {"en": "Mahatma Gandhi Jayanti / Shastri Jayanti", "hi": "गांधी जयंती / लाल बहादुर शास्त्री जयंती", "bn": "গান্ধী জয়ন্তী / লাল বাহাদুর শাস্ত্রী জয়ন্তী", "category": "national", "icon": "🇮🇳", "deity": "Mahatma Gandhi"},
    (10, 31): {"en": "National Unity Day (Sardar Patel Jayanti)", "hi": "राष्ट्रीय एकता दिवस (सरदार पटेल जयंती)", "bn": "জাতীয় একতা দিবস (সর্দার প্যাটেল জয়ন্তী)", "category": "national", "icon": "🇮🇳", "deity": "Sardar Vallabhbhai Patel"},
    (11, 14): {"en": "Children's Day (Jawaharlal Nehru Jayanti)", "hi": "बाल दिवस (जवाहरलाल नेहरू जयंती)", "bn": "শিশু দিবস (জওহরলাল নেহেরু জয়ন্তী)", "category": "national", "icon": "🇮🇳", "deity": "Pt. Jawaharlal Nehru"},
}

# ==============================================================================
# ৩. খ্রিস্টান ও আন্তর্জাতিক ফিক্সড দিবস (Fixed Gregorian / World Observances)
# ==============================================================================
FIXED_WORLD_CHRISTIAN_DAYS = {
    (1, 1): {"en": "New Year's Day", "hi": "नव वर्ष", "bn": "ইংরেজি নববর্ষ", "category": "world", "icon": "🌍", "deity": "Universal"},
    (3, 8): {"en": "International Women's Day", "hi": "अंतर्राष्ट्रीय महिला दिवस", "bn": "আন্তর্জাতিক নারী দিবস", "category": "world", "icon": "🌍", "deity": "Universal"},
    (4, 22): {"en": "Earth Day", "hi": "पृथ्वी दिवस", "bn": "বিশ্ব বসুন্ধরা দিবস", "category": "world", "icon": "🌍", "deity": "Mother Earth"},
    (5, 1): {"en": "International Workers' Day / May Day", "hi": "अंतर्राष्ट्रीय मजदूर दिवस", "bn": "আন্তর্জাতিক শ্রমিক দিবস / মে দিবস", "category": "world", "icon": "🌍", "deity": "Labor & Workers"},
    (6, 5): {"en": "World Environment Day", "hi": "विश्व पर्यावरण दिवस", "bn": "বিশ্ব পরিবেশ দিবস", "category": "world", "icon": "🌍", "deity": "Nature"},
    (6, 21): {"en": "International Yoga Day", "hi": "अंतर्राष्ट्रीय योग दिवस", "bn": "আন্তর্জাতিক যোগ দিবস", "category": "world", "icon": "🌍", "deity": "Yoga & Wellness"},
    (10, 16): {"en": "World Food Day", "hi": "विश्व खाद्य दिवस", "bn": "বিশ্ব খাদ্য দিবস", "category": "world", "icon": "🌍", "deity": "Universal"},
    (12, 24): {"en": "Christmas Eve", "hi": "क्रिसमस ईव", "bn": "ক্রিসমাস ইভ", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (12, 25): {"en": "Christmas / Merry Christmas", "hi": "क्रिसमस / बड़ा दिन", "bn": "শুভ বড়দিন (ক্রিসমাস)", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (12, 31): {"en": "New Year's Eve", "hi": "नव वर्ष की पूर्वसंध्या", "bn": "বছরের শেষ দিন", "category": "world", "icon": "🌍", "deity": "Universal"},
}

# ==============================================================================
# ৪. পরিবর্তনশীল মুসলিম, খ্রিস্টান ও বিশেষ আঞ্চলিক পূজা (Multi-Year 2025-2028)
# ==============================================================================
VARIABLE_RELIGIOUS_DAYS = {
    # --- 2025 ---
    (2025, 3, 31): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2025, 4, 18): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2025, 4, 20): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2025, 6, 7): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2025, 7, 6): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️", "deity": "Imam Hussain"},
    (2025, 9, 5): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️", "deity": "Prophet Muhammad (PBUH)"},

    # --- 2026 ---
    (2026, 3, 20): {"en": "Eid-ul-Fitr (Ramadan Eid)", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2026, 4, 3): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2026, 4, 5): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2026, 5, 27): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2026, 6, 26): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️", "deity": "Imam Hussain"},
    (2026, 7, 21): {"en": "Deodhwani Festival Begins (Kamakhya / Assam)", "hi": "देवध्वनि महोत्सव प्रारंभ (कामाख्या / असम)", "bn": "দেওধ্বনি উৎসব আরম্ভ (কামাখ্যা / আসাম)", "category": "hindu", "type": "Regional Festival", "icon": "🔱", "deity": "Maa Kamakhya & Devi Manasa"},
    (2026, 8, 17): {"en": "Main Manasa Puja (Singha Sankranti)", "hi": "मुख्य मनसा पूजा (सिंह संक्रांति)", "bn": "প্রধান শ্রী শ্রী মনসা পূজা (সিংহ সংক্রান্তি)", "category": "hindu", "type": "Major Festival", "icon": "🐍", "deity": "Maa Manasa"},
    (2026, 8, 26): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️", "deity": "Prophet Muhammad (PBUH)"},
    (2026, 11, 16): {"en": "Kartik Puja (Kartik Sankranti)", "hi": "कार्तिक पूजा (कार्तिक संक्रांति)", "bn": "শ্রী শ্রী কার্তিক পূজা (কার্তিক সংক্রান্তি)", "category": "hindu", "type": "Major Festival", "icon": "🦚", "deity": "Lord Kartikeya"},

    # --- 2027 ---
    (2027, 3, 10): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2027, 3, 26): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2027, 3, 28): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2027, 5, 17): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2027, 6, 16): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️", "deity": "Imam Hussain"},
    (2027, 8, 15): {"en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)", "category": "muslim", "icon": "☪️", "deity": "Prophet Muhammad (PBUH)"},

    # --- 2028 ---
    (2028, 2, 27): {"en": "Eid-ul-Fitr", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2028, 4, 14): {"en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2028, 4, 16): {"en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে", "category": "christian", "icon": "✝️", "deity": "Lord Jesus Christ"},
    (2028, 5, 5): {"en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)", "category": "muslim", "icon": "☪️", "deity": "Allah"},
    (2028, 6, 4): {"en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম", "category": "muslim", "icon": "☪️", "deity": "Imam Hussain"},
}

# ==============================================================================
# LANGUAGE NORMALIZATION
# ==============================================================================
def get_language_key(lang: str = "en") -> str:
    value = str(lang or "en").lower().strip()
    if value.startswith("bn") or "বাংলা" in value:
        return "bn"
    if value.startswith("hi") or "हि" in value:
        return "hi"
    return "en"


# ==============================================================================
# SANKRANTI NAME NORMALIZATION
# ==============================================================================
def normalize_sankranti_name(sankranti_name: Optional[str]) -> str:
    if not sankranti_name:
        return ""
    return str(sankranti_name).strip().lower()


# ==============================================================================
# DUPLICATE FESTIVAL PROTECTION
# ==============================================================================
def append_festival_once(
    festivals: List[Dict[str, Any]],
    festival: Dict[str, Any]
) -> None:
    festival_name = festival.get("name", "")
    for existing in festivals:
        if existing.get("name") == festival_name:
            return
    festivals.append(festival)


# ==============================================================================
# MAIN FESTIVAL FUNCTION
# ==============================================================================
def get_festivals_for_day(
    current_date: date,
    lunar_month: str = "",
    paksha: str = "",
    tithi_num: int = 1,
    sankranti_name: Optional[str] = None,
    lang: str = "en"
) -> List[Dict[str, Any]]:
    
    festivals: List[Dict[str, Any]] = []

    # 1. Language & Parameter Sanitization
    l_key = get_language_key(lang)
    lunar_month = str(lunar_month or "").strip()
    paksha = str(paksha or "").strip()

    try:
        tithi_num = int(tithi_num)
    except (TypeError, ValueError):
        tithi_num = 0

    # 2. Hindu Tithi-based Festivals (Database Match)
    h_key = (lunar_month, paksha, tithi_num)
    if h_key in HINDU_FESTIVAL_DATABASE:
        festival_data = HINDU_FESTIVAL_DATABASE[h_key]
        append_festival_once(
            festivals,
            {
                "name": festival_data.get(l_key, festival_data.get("en", "")),
                "category": festival_data.get("category", "hindu"),
                "type": festival_data.get("type", "Major Festival"),
                "icon": festival_data.get("icon", "🕉️"),
                "deity": festival_data.get("deity", "Deity")
            }
        )

    # 3. Ekadashi Vrata (সকল মাসের একাদশী)
    if tithi_num == 11:
        ekadashi_name = {"en": "Ekadashi Vrata / Fast", "hi": "एकादशी व्रत", "bn": "একাদশী ব্রত ও উপবাস"}
        ekadashi_deity = {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"}
        append_festival_once(
            festivals,
            {
                "name": ekadashi_name.get(l_key, ekadashi_name["en"]),
                "category": "hindu",
                "type": "Vrata",
                "icon": "🕉️",
                "deity": ekadashi_deity.get(l_key, ekadashi_deity["en"])
            }
        )

    # 4. Pradosh Vrata (সকল মাসের ত্রয়োদশী প্রদোষ)
    elif tithi_num == 13:
        pradosh_name = {"en": "Pradosh Vrata", "hi": "प्रदोष व्रत", "bn": "প্রদোষ ব্রত"}
        pradosh_deity = {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান দেবাদিদেব মহাদেব"}
        append_festival_once(
            festivals,
            {
                "name": pradosh_name.get(l_key, pradosh_name["en"]),
                "category": "hindu",
                "type": "Vrata",
                "icon": "🔱",
                "deity": pradosh_deity.get(l_key, pradosh_deity["en"])
            }
        )

    # 5. Solar Sankranti & Fixed Solar Puja (পয়লা বৈশাখ, নীল পূজা/চড়ক, মকর সংক্রান্তি, বিশ্বকর্মা)
    m_d = (current_date.month, current_date.day)
    s_name = normalize_sankranti_name(sankranti_name)

    # নীল পূজা ও চড়ক পূজা (চৈত্র সংক্রান্তি - ১৪ই এপ্রিল)
    if m_d == (4, 14):
        nil_names = {"en": "Nil Puja / Charak Puja (Chaitra Sankranti)", "hi": "नील पूजा / चरक पूजा (चैत्र संक्रांति)", "bn": "শ্রী শ্রী নীল পূজা / চড়ক পূজা (চৈত্র সংক্রান্তি)"}
        append_festival_once(festivals, {"name": nil_names.get(l_key, "Nil Puja"), "category": "hindu", "type": "Solar", "icon": "🔱", "deity": "Lord Shiva & Maa Nilavati"})

    # পয়লা বৈশাখ / মেষ সংক্রান্তি (১৫ই এপ্রিল)
    elif m_d == (4, 15) or ("mesha" in s_name or "aries" in s_name):
        mesha_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / पोइला बैशाख", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি (শুভ নববর্ষ)"}
        append_festival_once(festivals, {"name": mesha_names.get(l_key, "Poila Boishakh"), "category": "hindu", "type": "Solar", "icon": "🌾", "deity": "Surya Deva & Ganesha"})

    # পৌষ সংক্রান্তি / মকর সংক্রান্তি (১৪ই জানুয়ারি)
    elif m_d == (1, 14) or ("makar" in s_name or "capricorn" in s_name):
        makar_names = {"en": "Makar Sankranti / Pongal / Poush Parbon", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি / পৌষ পার্বণ ও গঙ্গাসাগর স্নান"}
        append_festival_once(festivals, {"name": makar_names.get(l_key, "Makar Sankranti"), "category": "hindu", "type": "Solar", "icon": "☀️", "deity": "Surya Deva"})

    # বিশ্বকর্মা পূজা / কন্যা সংক্রান্তি (১৭ই সেপ্টেম্বর)
    elif m_d == (9, 17) or ("kanya" in s_name or "virgo" in s_name):
        kanya_names = {"en": "Kanya Sankranti / Vishwakarma Puja", "hi": "कन्या संक्रांति / विश्वकर्मा पूजा", "bn": "কন্যা সংক্রান্তি / শ্রী শ্রী বিশ্বকর্মা পূজা"}
        append_festival_once(festivals, {"name": kanya_names.get(l_key, "Vishwakarma Puja"), "category": "hindu", "type": "Solar", "icon": "⚙️", "deity": "Lord Vishwakarma"})

    # 6. Indian National Holidays
    if m_d in INDIAN_NATIONAL_HOLIDAYS:
        nat = INDIAN_NATIONAL_HOLIDAYS[m_d]
        append_festival_once(
            festivals,
            {
                "name": nat.get(l_key, nat.get("en", "")),
                "category": nat.get("category", "national"),
                "type": "National Holiday",
                "icon": nat.get("icon", "🇮🇳"),
                "deity": nat.get("deity", "National")
            }
        )

    # 7. Fixed World / Christian Days
    if m_d in FIXED_WORLD_CHRISTIAN_DAYS:
        world_day = FIXED_WORLD_CHRISTIAN_DAYS[m_d]
        append_festival_once(
            festivals,
            {
                "name": world_day.get(l_key, world_day.get("en", "")),
                "category": world_day.get("category", "world"),
                "type": "Observance",
                "icon": world_day.get("icon", "🌍"),
                "deity": world_day.get("deity", "Universal")
            }
        )

    # 8. Multi-Year Variable Religious & Regional Days
    full_date_key = (current_date.year, current_date.month, current_date.day)
    if full_date_key in VARIABLE_RELIGIOUS_DAYS:
        rel = VARIABLE_RELIGIOUS_DAYS[full_date_key]
        append_festival_once(
            festivals,
            {
                "name": rel.get(l_key, rel.get("en", "")),
                "category": rel.get("category", "hindu" if "hindu" in rel.get("category", "") else "religious"),
                "type": rel.get("type", "Major Festival"),
                "icon": rel.get("icon", "🕉️"),
                "deity": rel.get("deity", "Deity")
            }
        )

    return festivals
