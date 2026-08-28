from datetime import date
from typing import List, Dict, Any, Optional

# ==============================================================================
# ১. সনাতন/হিন্দু তিথিভিত্তিক সমস্ত পূজা, ব্রত, তাৎপর্য ও শাস্ত্রীয় পূজার মুহূর্ত
# ==============================================================================
HINDU_FESTIVAL_DATABASE = {
    # --------------------------------------------------------------------------
    # চৈত্র মাস (Chaitra)
    # --------------------------------------------------------------------------
    ("Chaitra", "Shukla", 1): {
        "en": "Chaitra Navratri Begins / Gudi Padwa / Basanti Durga Puja Bodhan",
        "hi": "चैत्र नवरात्रि प्रारंभ / गुड़ी पड़वा / वासंतिक दुर्गा पूजा बोधन",
        "bn": "চৈত্র নবরাত্রি আরম্ভ / বাসন্তী দুর্গাপূজা বোধন / গুড়ি পাড়ওয়া",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Maa Shailaputri", "hi": "माँ दुर्गा व माँ शैलपुत्री", "bn": "মা দুর্গা ও দেবী শৈলপুত্রী"},
        "description": {
            "en": "Sacred beginning of Chaitra Vasantik Navratri with Ghatasthapana and invocation of Maa Durga.",
            "hi": "घटस्थापना व माँ शैलपुत्री आराधना के साथ चैत्र वासंतिक नवरात्रि का पावन शुभारंभ।",
            "bn": "ঘটস্থাপন ও মা দুর্গার বোধন পূজার মাধ্যমে চৈত্র বাসন্তী নবরাত্রির শুভ সূচনা।"
        },
        "muhurta": {"en": "Ghatasthapana & Morning Muhurta (06:15 - 10:20 AM)", "hi": "घटस्थापना व प्रातःकाल मुहूर्त (प्रातः ०६:१५ - १०:२०)", "bn": "ঘটস্থাপন ও প্রাতঃকাল মুহূর্ত (সকাল ০৬:১৫ - ১০:২০)"}
    },
    ("Chaitra", "Shukla", 2): {
        "en": "Sindhara Dooj / Brahmacharini Puja",
        "hi": "सिंधारा दूज / माँ ब्रह्मचारिणी पूजा",
        "bn": "সিন্ধারা দুজ / দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Brahmacharini", "hi": "माँ ब्रह्मचारिणी", "bn": "দেবী ব্রহ্মচারিণী"},
        "description": {
            "en": "Worship of Maa Brahmacharini for penance, wisdom, and spiritual restraint on the 2nd day of Navratri.",
            "hi": "तप, त्याग, वैराग्य एवं संयम की वृद्धि हेतु नवरात्रि के दूसरे दिन माँ ब्रह्मचारिणी का पूजन।",
            "bn": "তপস্যা, ত্যাগ ও সংযম বৃদ্ধির উদ্দেশ্যে নবরাত্রির দ্বিতীয় দিনে দেবী ব্রহ্মচারিণীর বিশেষ পূজা।"
        },
        "muhurta": {"en": "Purvahna Kaal (Morning 07:00 - 10:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Chaitra", "Shukla", 3): {
        "en": "Gangaur / Matsya Jayanti / Chandraghanta Puja",
        "hi": "गणगौर पूजा / मत्स्य जयंती / माँ चंद्रघंटा पूजा",
        "bn": "গণগৌর পূজা / ভগবান মৎস্য জয়ন্তী / দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐟",
        "deity": {"en": "Lord Matsya & Maa Gauri", "hi": "भगवान मत्स्य व माँ गौरी", "bn": "ভগবান মৎস্য ও দেবী গৌরী"},
        "description": {
            "en": "Celebration of marital harmony via Gangaur Gauri worship and invocation of Lord Vishnu's fish incarnation (Matsya).",
            "hi": "अखंड सौभाग्य प्राप्ति हेतु गणगौर गौरी पूजन एवं भगवान विष्णु के प्रथम मत्स्य अवतार का जन्मोत्सव।",
            "bn": "অখণ্ড দাম্পত্য সৌভাগ্যে দেবী গৌরী পূজা এবং শ্রীহরি বিষ্ণুর প্রথম মৎস্য অবতারের আবির্ভাব মহোৎসব।"
        },
        "muhurta": {"en": "Pradosh Kaal & Morning Muhurta", "hi": "प्रदोष काल व प्रातःकाल मुहूर्त", "bn": "প্রদোষ কাল ও প্রাতঃকাল মুহূর্ত"}
    },
    ("Chaitra", "Shukla", 5): {
        "en": "Lakshmi Panchami / Sri Panchami (Chaitra)",
        "hi": "लक्ष्मी पंचमी / श्री पंचमी",
        "bn": "শ্রী শ্রী লক্ষ্মী পঞ্চমী ব্রত",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪷",
        "deity": {"en": "Maa Lakshmi", "hi": "माँ महालक्ष्मी", "bn": "মা মহালক্ষ্মী"},
        "description": {
            "en": "Sacred fasting and offerings dedicated to Goddess Lakshmi to attract prosperity, wisdom, and wealth.",
            "hi": "धन-धान्य, ऐश्वर्य एवं सौभाग्य की प्राप्ति हेतु चैत्र शुक्ल पंचमी पर माँ लक्ष्मी की विशेष आराधना।",
            "bn": "ধনধান্য ও সৌভাগ্য বৃদ্ধির কামনায় চৈত্র মাসের শুক্ল পঞ্চমীতে দেবী লক্ষ্মীর চরণে বিশেষ পূজা ও উপবাস।"
        },
        "muhurta": {"en": "Pradosh Kaal (Evening 05:45 - 08:00 PM)", "hi": "प्रदोष काल (संध्या ०५:४५ - ०८:००)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যা ০৫:৪৫ - ০৮:০০)"}
    },
    ("Chaitra", "Shukla", 8): {
        "en": "Basanti Maha Ashtami / Annapurna Puja / Mahagauri Puja",
        "hi": "माँ अन्नपूर्णा पूजा / बासंती महाष्टमी / महागौरी पूजा",
        "bn": "শ্রী শ্রী অন্নপূর্ণা পূজা / বাসন্তী মহাষ্টমী ও কুমারী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪷",
        "deity": {"en": "Maa Annapurna & Mahagauri", "hi": "माँ अन्नपूर्णा व महागौरी", "bn": "মা অন্নপূর্ণা ও দেবী মহাগৌরী"},
        "description": {
            "en": "Worship of Maa Annapurna for food and abundance, alongside Basanti Maha Ashtami Kumari Puja.",
            "hi": "धन-धान्य अधिष्ठात्री माँ अन्नपूर्णा एवं बासंती महाष्टमी पर कन्या (कुमारी) पूजन।",
            "bn": "অন্নদাত্রী মা অন্নপূর্ণার বিশেষ আরাধনা এবং বাসন্তী মহাষ্টমীতে পবিত্র কুমারী পূজা।"
        },
        "muhurta": {"en": "Sandhi Puja & Ashtami Purvahna", "hi": "संधि पूजा व महाष्टमी पूर्वाह्न", "bn": "মহাষ্টমী ও সন্ধিপূজা মুহূর্ত (৪৮ মিনিট)"}
    },
    ("Chaitra", "Shukla", 9): {
        "en": "Sri Rama Navami / Siddhidatri Puja",
        "hi": "श्री राम नवमी / माँ सिद्धिदात्री पूजा",
        "bn": "শ্রী শ্রী রাম নবমী মহাপর্ব / বাসন্তী নবমী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🏹",
        "deity": {"en": "Lord Sri Rama & Maa Siddhidatri", "hi": "भगवान श्रीराम व माँ सिद्धिदात्री", "bn": "ভগবান শ্রীরামচন্দ্র ও দেবী সিদ্ধিদাত্রী"},
        "description": {
            "en": "Divine appearance day of Maryada Purushottam Lord Sri Rama at noon in Ayodhya.",
            "hi": "अयोध्या में मर्यादा पुरुषोत्तम भगवान श्रीराम का पावन प्राकट्य दिवस व जन्मोत्सव।",
            "bn": "অযোধ্যাধামে পরম পুরুষোত্তম ভগবান শ্রীরামচন্দ্রের শুভ আবির্ভাব ও জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Madhyahna Kaal Muhurta (11:00 AM - 01:30 PM)", "hi": "मध्याह्न काल मुहूर्त (दोपहर ११:०० - ०१:३०)", "bn": "মধ্যাহ্ন কাল মুহূর্ত (দুপুর ১১:০০ - ০১:৩০)"}
    },
    ("Chaitra", "Shukla", 15): {
        "en": "Hanuman Jayanti / Chaitra Purnima (Satyanarayan Puja)",
        "hi": "हनुमान जयंती / चैत्र पूर्णिमा (सत्यनारायण व्रत)",
        "bn": "শ্রী শ্রী হনুমান জয়ন্তী / চৈত্র পূর্ণিমা (শ্রী সত্যনারায়ণ পূজা)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🚩",
        "deity": {"en": "Lord Hanuman & Sri Satyanarayan", "hi": "श्री हनुमान जी व श्री सत्यनारायण", "bn": "শ্রী হনুমানজী ও শ্রী সত্যনারায়ণ"},
        "description": {
            "en": "Celebration of the birth of Lord Hanuman, the epitome of devotion and strength, along with Chaitra Satyanarayan Puja.",
            "hi": "भक्ति व शक्ति के प्रतीक पवनपुत्र श्री हनुमान जी का जन्मोत्सव एवं पूर्णिमा सत्यनारायण पूजन।",
            "bn": "পরম ভক্ত ও শক্তির প্রতীক শ্রী হনুমানজীর জন্মজয়ন্তী এবং চৈত্র পূর্ণিমার সত্যনারায়ণ পূজা।"
        },
        "muhurta": {"en": "Brahma Muhurta & Pradosh Kaal", "hi": "ब्रह्म मुहूर्त व प्रदोष काल", "bn": "ব্রাহ্ম মুহূর্ত ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # বৈশাখ মাস (Vaisakha)
    # --------------------------------------------------------------------------
    ("Vaisakha", "Shukla", 3): {
        "en": "Akshaya Tritiya / Parashurama Jayanti / Treta Yugadi",
        "hi": "अक्षय तृतीया / परशुराम जयंती / त्रेता युगादि",
        "bn": "অক্ষয় তৃতীয়া মহাপর্ব / পরশুরাম জয়ন্তী / ত্রেতা যুগাদী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪙",
        "deity": {"en": "Lord Vishnu & Maa Lakshmi", "hi": "भगवान विष्णु व माँ लक्ष्मी", "bn": "ভগবান বিষ্ণু ও মা লক্ষ্মী"},
        "description": {
            "en": "Highly auspicious day where merits of charity and new beginnings never diminish.",
            "hi": "दान, जप, स्वर्ण क्रय एवं शुभ कार्यों के लिए अक्षय पुण्य फलदायी पावन दिवस।",
            "bn": "দান, জপ, গৃহপ্রবেশ ও শুভ কাজের জন্য অক্ষয় পুণ্যদায়ী পরম পবিত্র মহাপর্ব।"
        },
        "muhurta": {"en": "Abhijit & Purvahna (All-day Auspicious)", "hi": "अभिजित व पूर्वाह्न मुहूर्त (सर्वसिद्धि मुहूर्त)", "bn": "অভিজিৎ ও পূর্বাহ্ন মুহূর্ত (সারাদিন অক্ষয় লগ্ন)"}
    },
    ("Vaisakha", "Shukla", 5): {
        "en": "Adi Shankaracharya Jayanti / Surdas Jayanti",
        "hi": "आदि शंकराचार्य जयंती / सूरदास जयंती",
        "bn": "আদি শঙ্করাচার্য জয়ন্তী / ভক্ত সুরদাস জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "जयंती पर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️",
        "deity": {"en": "Jagadguru Adi Shankaracharya", "hi": "जगद्गुरु आदि शंकराचार्य", "bn": "জগদ্গুরু আদি শঙ্করাচার্য"},
        "description": {
            "en": "Advent of Jagadguru Adi Shankaracharya, who revived Sanatana Dharma and Advaita philosophy.",
            "hi": "अद्वैत वेदांत के प्रणेता एवं सनातन धर्म के पुनरुद्धारक जगद्गुरु आदि शंकराचार्य का पावन प्राकट्य दिवस।",
            "bn": "অদ্বৈত বেদান্তের প্রবক্তা ও সনাতন ধর্মের রক্ষাকর্তা জগদ্গুরু আদি শঙ্করাচার্যের আবির্ভাব তিথি।"
        },
        "muhurta": {"en": "Madhyahna Kaal (11:15 AM - 01:45 PM)", "hi": "मध्याह्न काल (दोपहर ११:१५ - ०१:४५)", "bn": "মধ্যাহ্ন কাল (দুপুর ১১:১৫ - ০১:৪৫)"}
    },
    ("Vaisakha", "Shukla", 7): {
        "en": "Ganga Saptami / Jahnu Saptami",
        "hi": "गंगा सप्तमी / जाह्नू सप्तमी (गंगा अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা সপ্তমী / জাহ্নু সপ্তমী (গঙ্গা জন্মজয়ন্তী)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌊",
        "deity": {"en": "Maa Ganga", "hi": "माँ गंगा", "bn": "মা গঙ্গা"},
        "description": {
            "en": "Commemoration of the day Sage Jahnu released sacred River Ganga from his ear as Jahnavi.",
            "hi": "महर्षि जाह्नू द्वारा माँ गंगा को अपनी जंघा/कर्ण से पुनः मुक्त करने पर जाह्नवी प्राकट्य उत्सव।",
            "bn": "মহর্ষি জাহ্নুর কর্ণ থেকে দেবী গঙ্গার পুনরায় মুক্তির মাধ্যমে ‘জাহ্নবী’ রূপে আবির্ভাবের শুভ তিথি।"
        },
        "muhurta": {"en": "Madhyahna Mahasnan Muhurta (10:45 AM - 01:15 PM)", "hi": "मध्याह्न महास्नान मुहूर्त (प्रातः १०:४५ - ०१:१५)", "bn": "মধ্যাহ্ন মহাস্নান মুহূর্ত (সকাল ১০:৪৫ - ০১:১৫)"}
    },
    ("Vaisakha", "Shukla", 9): {
        "en": "Sita Navami / Janaki Jayanti",
        "hi": "सीता नवमी / जानकी जयंती",
        "bn": "শ্রী সীতা নবমী / জানকী জন্মজয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪷",
        "deity": {"en": "Maa Sita", "hi": "माँ जानकी सीता", "bn": "মা জানকী সীতা"},
        "description": {
            "en": "Appearance day of Maa Sita, discovered by King Janaka while plowing the sacred field.",
            "hi": "महाराज जनक द्वारा हल जोतते समय भूमि से प्रकट हुईं जगज्जननी माँ सीता का पावन प्राकट्य दिवस।",
            "bn": "মহারাজ জনক কর্তৃক যজ্ঞভূমি কর্ষণকালে ভূগর্ভ থেকে জগৎজননী মা সীতার পরম আবির্ভাব তিথি।"
        },
        "muhurta": {"en": "Madhyahna Kaal Muhurta (11:00 AM - 01:30 PM)", "hi": "मध्याह्न काल मुहूर्त (दोपहर ११:०० - ०१:३०)", "bn": "মধ্যাহ্ন কাল মুহূর্ত (দুপুর ১১:০০ - ০১:৩০)"}
    },
    ("Vaisakha", "Shukla", 14): {
        "en": "Sri Narasimha Jayanti / Narasimha Chaturdashi",
        "hi": "श्री नृसिंह जयंती / नृसिंह चतुर्दशी व्रत",
        "bn": "শ্রী শ্রীনৃসিংহ চতুর্দশী / নৃসিংহ জয়ন্তী ব্রত",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🦁",
        "deity": {"en": "Lord Narasimha", "hi": "भगवान नृसिंह देव", "bn": "ভগবান শ্রীনৃসিংহ দেব"},
        "description": {
            "en": "Lord Vishnu assumed the half-lion incarnation at dusk to protect Bhakta Prahlada and destroy Hiranyakashipu.",
            "hi": "भक्त प्रह्लाद की रक्षा एवं हिरण्यकशिपु के संहार हेतु गोधूलि वेला में भगवान नृसिंह का प्राकट्य।",
            "bn": "ভক্ত প্রহ্লাদকে রক্ষা ও হিরণ্যকশিপু নিধনে গোধূলি লগ্নে স্তম্ভ বিদীর্ণ করে শ্রীনৃসিংহদেবের প্রকাশ।"
        },
        "muhurta": {"en": "Sayankal / Sandhya Muhurta (Sunset 05:30 - 07:15 PM)", "hi": "सायंकाल / संध्या मुहूर्त (सूर्यास्त ०५:३० - ०७:१५)", "bn": "সায়ংকাল / সন্ধ্যা মুহূর্ত (সূর্যাস্ত ০৫:৩০ - ০৭:১৫)"}
    },
    ("Vaisakha", "Shukla", 15): {
        "en": "Buddha Purnima / Kurma Jayanti / Vaisakhi Snan",
        "hi": "बुद्ध पूर्णिमा / कूर्म जयंती / वैशाखी स्नान",
        "bn": "বুদ্ধ পূর্ণিমা / বৈশাখী পূর্ণিমা / ভগবান কূর্ম জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "☸️",
        "deity": {"en": "Gautama Buddha & Lord Kurma", "hi": "गौतम बुद्ध व भगवान कूर्म", "bn": "গৌতম বুদ্ধ ও ভগবান কূর্ম"},
        "description": {
            "en": "Triple celebration of Buddha's birth, enlightenment, and parinirvana, alongside Lord Kurma's advent.",
            "hi": "भगवान बुद्ध का जन्म, ज्ञान प्राप्ति व महापरिनिर्वाण दिवस तथा समुद्र मंथन हेतु कूर्म अवतार दिवस।",
            "bn": "ভগবান বুদ্ধের ত্রি-স্মৃতিবিজড়িত পুণ্যতিথি এবং সমুদ্র মন্থন সহায়তাকারী কূর্ম অবতারের আবির্ভাব।"
        },
        "muhurta": {"en": "Brahma Muhurta & Pradosh Kaal", "hi": "ब्रह्म मुहूर्त व प्रदोष काल", "bn": "ব্রাহ্ম মুহূর্ত ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # জ্যৈষ্ঠ মাস (Jyeshtha)
    # --------------------------------------------------------------------------
    ("Jyeshtha", "Krishna", 15): {
        "en": "Vat Savitri Vrat / Shani Jayanti / Phalaharini Kali Puja",
        "hi": "वट सावित्री व्रत / शनि जयंती / फलहारिणी काली पूजा",
        "bn": "বট সাবিত্রী ব্রত / শ্রী শনি জয়ন্তী / ফলহারिणी কালীপূজা",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌳",
        "deity": {"en": "Shani Deva, Savitri & Maa Kali", "hi": "शनि देव, माता सावित्री व माँ काली", "bn": "শ্রী শনি দেব, সতী সাবিত্রী ও মা কালী"},
        "description": {
            "en": "Fast for marital longevity, Shani Deva's birth observance, and Phalaharini Kali Puja at night.",
            "hi": "अखंड सौभाग्य हेतु वट वृक्ष पूजन, शनि देव जयंती व मध्यरात्रि फलहारिणी काली पूजा।",
            "bn": "অখণ্ড সৌভাগ্যের জন্য বটবৃক্ষ পূজা, শনিদেবের আবির্ভাব তিথি ও ফলহারিণী কালীপূজা।"
        },
        "muhurta": {"en": "Nishita Kaal (Kali Puja) & Purvahna (Vat Puja)", "hi": "निशीथ काल (काली पूजा) व पूर्वाह्न (वट पूजा)", "bn": "নিশীথ কাল (কালীপূজা) ও পূর্বাহ্ন (বট পূজা)"}
    },
    ("Jyeshtha", "Shukla", 6): {
        "en": "Aranya Sasthi / Jamai Sasthi Vrat",
        "hi": "अरण्य षष्ठी / जमाई षष्ठी व्रत",
        "bn": "অরণ্য ষষ্ঠী / শ্রী শ্রী জামাই ষষ্ঠী ব্রত",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🌿",
        "deity": {"en": "Maa Sasthi", "hi": "माँ षष्ठी", "bn": "মা ষষ্ঠী দেবী"},
        "description": {
            "en": "Traditional festival invoking Maa Sasthi's blessings for offspring and welcoming sons-in-law.",
            "hi": "संतान की दीर्घायु व कल्याण हेतु माँ षष्ठी का पूजन एवं जामाता सत्कार पर्व।",
            "bn": "সন্তানের মঙ্গল কামনায় মা ষষ্ঠীর আশীর্বাদ গ্রহণ ও জামাতাকে বরণ করার মধুর সামাজিক মহাপর্ব।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:30 - 11:00 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:३० - ११:००)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:৩০ - ১১:০০)"}
    },
    ("Jyeshtha", "Shukla", 10): {
        "en": "Ganga Dussehra (Descent of Ganga)",
        "hi": "गंगा दशहरा (माँ गंगा का पृथ्वी पर अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা দশহরা মহোৎসব (মর্ত্যে গঙ্গা অবতরণ)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌊",
        "deity": {"en": "Maa Ganga", "hi": "माँ गंगा", "bn": "মা গঙ্গা"},
        "description": {
            "en": "Celebration of the day sacred River Ganga descended to Earth through Bhagiratha's penance.",
            "hi": "महाराज भगीरथ के कठोर तप से माँ गंगा के स्वर्ग से मर्तलोक पर पावन अवतरण का महापर्व।",
            "bn": "রাজর্ষি ভগীরথের কঠোর তপস্যায় সন্তুষ্ট হয়ে পতিতপাবনী মা গঙ্গার মর্ত্যে অবতরণ মহোৎসব।"
        },
        "muhurta": {"en": "Hasta Nakshatra & Madhyahna Snan", "hi": "हस्त नक्षत्र व मध्याह्न स्नान काल", "bn": "হস্তা নক্ষত্র ও মধ্যাহ্ন স্নান সময়"}
    },
    ("Jyeshtha", "Shukla", 11): {
        "en": "Nirjala Ekadashi / Bhim Ekadashi",
        "hi": "निर्जला एकादशी (भीमसेन एकादशी)",
        "bn": "নির্জলা একাদশী ব্রত (ভীম একাদশী)",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "महाव्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️",
        "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "The most rigorous Ekadashi fast observed without food and water to attain the merits of all 24 Ekadashis.",
            "hi": "जल की एक बूँद भी ग्रहण किए बिना समस्त २४ एकादशियों का पुण्य फल देने वाला महाव्रत।",
            "bn": "জলস্পর্শ না করে ২৪টি একাদশীর সমতুল্য পুণ্যফলদায়ী সর্বশ্রেষ্ঠ ও পরম পবিত্র নির্জলা ব্রত।"
        },
        "muhurta": {"en": "Brahma Muhurta & Morning Fast (05:00 - 08:30 AM)", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा (०५:०० - ०८:३०)", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃ পূজা (ভোর ০৫:০০ - ০৮:৩০)"}
    },
    ("Jyeshtha", "Shukla", 15): {
        "en": "Snan Yatra (Lord Jagannath) / Vat Purnima",
        "hi": "देवस्नान पूर्णिमा / वट पूर्णिमा",
        "bn": "শ্রী জগন্নাথদেবের স্নানযাত্রা / দেবস্নান পূর্ণিমা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌸",
        "deity": {"en": "Lord Jagannath", "hi": "भगवान श्री जगन्नाथ", "bn": "ভগবান শ্রী জগন্নাথদেব"},
        "description": {
            "en": "Auspicious bathing ceremony of Lord Jagannath with 108 pots of herbal water on His appearance day.",
            "hi": "भगवान जगन्नाथ, बलभद्र व सुभद्रा का १०८ सुवासित कलशों से दिव्य स्नान एवं गजानन वेश दर्शन।",
            "bn": "১০৮টি সুগন্ধি তীর্থ বারি দ্বারা শ্রীজগন্নাথ, বলভদ্র ও সুভদ্রার মহাজলাভিষেক ও গজানন বেশ দর্শন।"
        },
        "muhurta": {"en": "Jyeshtha Purnima Snan Muhurta (Purvahna)", "hi": "पूर्णिमा महास्नान मुहूर्त (पूर्वाह्न)", "bn": "পূর্ণিমা দেবস্নান মুহূর্ত (পূর্বাহ্ন)"}
    },

    # --------------------------------------------------------------------------
    # আষাঢ় মাস (Ashadha)
    # --------------------------------------------------------------------------
    ("Ashadha", "Shukla", 1): {
        "en": "Ashadha Gupt Navratri Begins / Varahi Puja",
        "hi": "आषाढ़ गुप्त नवरात्रि प्रारंभ / वाराही देवी पूजा",
        "bn": "আষাঢ় গুপ্ত নবরাত্রি আরম্ভ / দেবী বারাহী ও দশমহাবিদ্যা পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "साधना पर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Das Mahavidya & Maa Varahi", "hi": "दस महाविद्या व माँ वाराही", "bn": "দশমহাবিদ্যা ও দেবী বারাহী"},
        "description": {
            "en": "Nine nights of esoteric Shakta sadhana invoking the Das Mahavidyas and Matrikas.",
            "hi": "दस महाविद्याओं एवं तांत्रिक साधनाओं की गुप्त सिद्धि हेतु पावन नौ दिवसीय अनुष्ठान।",
            "bn": "দশমহাবিদ্যা ও তন্ত্রসাধনার সিদ্ধিলাভের জন্য ৯ দিনব্যাপী পবিত্র আষাঢ় গুপ্ত নবরাত্রি আরম্ভ।"
        },
        "muhurta": {"en": "Ghatasthapana & Abhijit Muhurta", "hi": "घटस्थापना व अभिजित मुहूर्त", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত"}
    },
    ("Ashadha", "Shukla", 2): {
        "en": "Jagannath Ratha Yatra Mahotsav",
        "hi": "श्री जगन्नाथ रथ यात्रा महोत्सव",
        "bn": "শ্রী শ্রী জগন্নাথদেবের রথযাত্রা মহোৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🚩",
        "deity": {"en": "Lord Jagannath, Balabhadra & Subhadra", "hi": "भगवान जगन्नाथ, बलभद्र व सुभद्रा", "bn": "ভগবান জগন্নাথ, বলভদ্র ও দেবী সুভদ্রা"},
        "description": {
            "en": "Grand chariot procession of Lord Jagannath, Balabhadra, and Subhadra to the Gundicha Temple.",
            "hi": "भगवान जगन्नाथ, भाई बलभद्र व बहन सुभद्रा का दिव्य रथों पर गुंडिचा मंदिर प्रस्थान।",
            "bn": "শ্রী শ্রী জগন্নাথদেব, বলভদ্র ও দেবী সুভদ্রার রথে চড়ে গুণ্ডিচা মাসির বাড়ি গমনাগমন মহোৎসব।"
        },
        "muhurta": {"en": "Ratha Pratistha & Yatra Muhurta", "hi": "रथ प्रतिष्ठा व यात्रा मुहूर्त", "bn": "রথ প্রতিষ্ঠা ও রথযাত্রা শুভ লগ্ন"}
    },
    ("Ashadha", "Shukla", 7): {
        "en": "Bipodtarini Vrat & Puja (Sasthi/Saptami)",
        "hi": "विपत्तारीणी व्रत व पूजा",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত ও পূজা",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🔱",
        "deity": {"en": "Maa Bipodtarini Durga", "hi": "माँ विपत्तारीणी दुर्गा", "bn": "মা বিপদতারিণী দুর্গা"},
        "description": {
            "en": "Fasting and worship of Maa Durga with 13 offerings to dispel all worldly perils.",
            "hi": "परिवार को समस्त संकटों व विपदाओं से मुक्त रखने हेतु १३ प्रकार के फल-उपचार से माँ का पूजन।",
            "bn": "পরিবারকে সর্ববিপদ থেকে মুক্ত রাখতে ১৩ প্রকার ফল ও লাল ডোর সহযোগে দেবী বিপদতারিণীর ব্রত।"
        },
        "muhurta": {"en": "Purvahna & Madhyahna Kaal", "hi": "पूर्वाह्न व मध्याह्न काल", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ব্রত সময়"}
    },
    ("Ashadha", "Shukla", 8): {
        "en": "Bipodtarini Vrat (Shukla Ashtami)",
        "hi": "विपत्तारीणी व्रत (अष्टमी)",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত (অষ্টমী)",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🔱",
        "deity": {"en": "Maa Bipodtarini Durga", "hi": "माँ विपत्तारीणी दुर्गा", "bn": "মা বিপদতারিণী দুর্গা"},
        "description": {
            "en": "Saturday/Tuesday Shukla Ashtami worship of Maa Bipodtarini for protection.",
            "hi": "शनिवार/मंगलवार युक्त आषाढ़ शुक्ल अष्टमी पर माँ विपत्तारीणी की संकटमोचनी पूजा।",
            "bn": "শনিবার/মঙ্গলবার যুক্ত আষাঢ় শুক্ল অষ্টমীতে বিপদহারিণী দেবীর পরম নিষ্ঠাসহ পূজা ও ব্রতপালন।"
        },
        "muhurta": {"en": "Purvahna & Madhyahna Kaal", "hi": "पूर्वाह्न व मध्याह्न काल", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ব্রত সময়"}
    },
    ("Ashadha", "Shukla", 10): {
        "en": "Ulto Rath / Bahuda Yatra",
        "hi": "उल्टा रथ / बहुड़ा यात्रा",
        "bn": "উল্টোরথ যাত্রা মহোৎসব (বাহুড়া যাত্রা)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🚩",
        "deity": {"en": "Lord Jagannath", "hi": "भगवान जगन्नाथ", "bn": "ভগবান জগন্নাথদেব"},
        "description": {
            "en": "Return journey of Lord Jagannath, Balabhadra, and Subhadra to the main temple (Srimandir).",
            "hi": "गुंडिचा मंदिर से भगवान जगन्नाथ, बलभद्र व सुभद्रा का मुख्य श्रीमंदिर में पुनरागमन।",
            "bn": "গুণ্ডিচা মাসির বাড়ি থেকে শ্রী শ্রী জগন্নাথদেবের নিজ শ্রীমন্দিরে শুভ প্রত্যাবর্তন যাত্রা।"
        },
        "muhurta": {"en": "Aparahna Kaal (Afternoon Return 01:30 - 04:30 PM)", "hi": "अपराह्न काल (दोपहर ०१:३० - ०४:३०)", "bn": "অপরাহ্ন কাল (দুপুর ০১:৩০ - ০৪:৩০)"}
    },
    ("Ashadha", "Shukla", 11): {
        "en": "Devshayani Ekadashi (Chaturmasya Vrata Begins)",
        "hi": "देवशयनी एकादशी (चातुर्मास प्रारंभ)",
        "bn": "দেবশয়নী একাদশী (চাতুর্মাস্য ব্রতারম্ভ)",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️",
        "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Lord Vishnu enters cosmic yoga-nidra for four months on the cosmic serpent Shesha.",
            "hi": "क्षीरसागर में शेषनाग की शैय्या पर भगवान विष्णु का चार मास के लिए योगनिद्रा में शयन।",
            "bn": "ক্ষীরসমুদ্রে শেষনাগের অনন্ত শয্যায় শ্রীহরি বিষ্ণুর চার মাসের জন্য যোগনিদ্রায় গমন ও চাতুর্মাস্যারম্ভ।"
        },
        "muhurta": {"en": "Purvahna & Sayankal Shayana Puja", "hi": "पूर्वाह्न व देव शयन पूजा काल", "bn": "পূর্বাহ্ন ও দেব শয়ন পূজা কাল"}
    },
    ("Ashadha", "Shukla", 15): {
        "en": "Guru Purnima / Maharshi Vyasa Puja / Kokila Vrat",
        "hi": "गुरु पूर्णिमा / वेदव्यास पूजा / कोकिला व्रत",
        "bn": "গুরু পূর্ণিমা / মহর্ষি বেদব্যাস পূজা / কোকিলা ব্রত",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🙏",
        "deity": {"en": "Sri Guru & Maharshi Vyasa", "hi": "सद्गुरु देव व महर्षि वेदव्यास", "bn": "শ্রী গুরু ও মহর্ষি বেদব্যাস"},
        "description": {
            "en": "Paying reverent homage to spiritual teachers and celebrating the birth of Veda Vyasa.",
            "hi": "अज्ञान रूपी अंधकार को दूर करने वाले गुरुदेव एवं चारों वेदों के रचयिता महर्षि व्यास का वंदन।",
            "bn": "অজ্ঞানতার অন্ধকার দূরকারী সদগুরুদেবের পাদপদ্মে প্রণতি ও মহর্ষি বেদব্যাসের শুভ জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Purvahna Kaal & Abhijit Muhurta (08:00 - 11:30 AM)", "hi": "पूर्वाह्न काल व अभिजित मुहूर्त (०८:०० - ११:३०)", "bn": "পূর্বাহ্ন কাল ও অভিজিৎ মুহূর্ত (সকাল ০৮:০০ - ১১:৩০)"}
    },

    # --------------------------------------------------------------------------
    # শ্রাবণ মাস (Shravana)
    # --------------------------------------------------------------------------
    ("Shravana", "Shukla", 3): {
        "en": "Hariyali Teej / Madhushrava",
        "hi": "हरियाली तीज / मधुश्रवा",
        "bn": "হরিয়ালী তীজ উৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌿",
        "deity": {"en": "Lord Shiva & Maa Parvati", "hi": "भगवान शिव व माँ पार्वती", "bn": "দেবাদিদেব শিব ও মা পার্বতী"},
        "description": {
            "en": "Celebration of the divine reunion of Shiva and Parvati amidst the greenery of monsoon.",
            "hi": "माँ पार्वती के कठोर तप के पश्चात भगवान शिव से पुनर्मिलन की स्मृति में सुहाग का पावन पर्व।",
            "bn": "কঠোর তপস্যার পর মা পার্বতীর সঙ্গে মহাদেবের পুণ্য মিলনের স্মৃতিতে সৌভাগ্যবর্ধক হরিয়ালী তীজ।"
        },
        "muhurta": {"en": "Pradosh Kaal (Evening 05:30 - 07:45 PM)", "hi": "प्रदोष काल (संध्या ०५:३० - ०७:४५)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যা ০৫:৩০ - ০৭:৪৫)"}
    },
    ("Shravana", "Shukla", 5): {
        "en": "Nag Panchami / Maa Manasa Puja",
        "hi": "नाग पंचमी / माँ मनसा पूजा",
        "bn": "নাগ পঞ্চমী / মা মনসা পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐍",
        "deity": {"en": "Maa Manasa & Nag Devata", "hi": "माँ मनसा व नाग देवता", "bn": "মা মনসা দেবী ও নাগ দেবতা"},
        "description": {
            "en": "Worship of serpent deities and Maa Manasa for protection against obstacles and poisons.",
            "hi": "सर्पभय निवारण, सुख-शांति एवं माँ मनसा व अष्टनागों की विशेष पूजा आराधना।",
            "bn": "সর্পভয় নিবারণ ও পারিবারিক সুরক্ষার জন্য দেবী মনসা ও অষ্টনাগের বিশেষ পূজা।"
        },
        "muhurta": {"en": "Purvahna Kaal (06:00 - 09:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०६:०० - ०९:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৬:০০ - ০৯:৩০)"}
    },
    ("Shravana", "Shukla", 6): {
        "en": "Kalki Jayanti",
        "hi": "कल्कि जयंती",
        "bn": "ভগবান কল্কি জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "जयंती पर्व", "bn": "মহাপর্ব"},
        "icon": "⚔️",
        "deity": {"en": "Lord Kalki", "hi": "भगवान कल्कि देव", "bn": "ভগবান কল্কি দেব"},
        "description": {
            "en": "Prophesied future advent of Lord Vishnu's tenth incarnation to establish Satya Yuga.",
            "hi": "कलयुग के अंत में अधर्म का विनाश कर पुनः सत्ययुग स्थापित करने वाले भगवान कल्कि का प्राकट्य पर्व।",
            "bn": "কলিযুগের শেষে পাপক্ষয় করে সত্যযুগ পুনঃপ্রতিষ্ঠার উদ্দেশ্যে দশম কল্কি অবতারের আগমন স্মরণ।"
        },
        "muhurta": {"en": "Sayankal / Pradosh Kaal (05:45 - 08:00 PM)", "hi": "सायंकाल / प्रदोष काल (०५:४५ - ०८:००)", "bn": "সায়ংকাল / প্রদোষ কাল (সন্ধ্যা ০৫:৪৫ - ০৮:০০)"}
    },
    ("Shravana", "Shukla", 15): {
        "en": "Raksha Bandhan / Jhulan Yatra Samapti",
        "hi": "रक्षाबंधन / सावन पूर्णिमा / झूलन यात्रा समापन",
        "bn": "রাখীবন্ধন উৎসব / ঝুলনযাত্রা সমাপন / ভগবান হয়গ্রীব জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🧵",
        "deity": {"en": "Lord Krishna, Draupadi & Lord Hayagriva", "hi": "भगवान श्रीकृष्ण, द्रौपदी व हयग्रीव", "bn": "শ্রীকৃষ্ণ, দ্রৌপদী ও ভগবান হয়গ্রীব"},
        "description": {
            "en": "Sacred bond of protection and affection between brothers and sisters, marking the conclusion of Jhulan Yatra.",
            "hi": "भाई-बहन के अटूट स्नेह ও रक्षा का पावन पर्व तथा श्रीराधा-कृष्ण झूलन यात्रा का समापन।",
            "bn": "ভাই-বোনের স্নেহ ও প্রীতির পবিত্র রাখী বন্ধন মহোৎসব এবং শ্রীশ্রী ঝুলনযাত্রা সমাপন।"
        },
        "muhurta": {"en": "Aparahna & Pradosh (Bhadra Free Time)", "hi": "अपराह्न व प्रदोष काल (भद्रा रहित)", "bn": "অপরাহ্ন ও প্রদোষ কাল (ভদ্রামুক্ত শুভ লগ্ন)"}
    },

    # --------------------------------------------------------------------------
    # ভাদ্রপদ মাস (Bhadrapada)
    # --------------------------------------------------------------------------
    ("Bhadrapada", "Krishna", 8): {
        "en": "Krishna Janmashtami / Gokulashtami",
        "hi": "श्रीकृष्ण जन्माष्टमी / गोकुलाष्टमी",
        "bn": "শ্রী শ্রী কৃষ্ণ জন্মাষ্টমী মহাপর্ব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🦚",
        "deity": {"en": "Bhagwan Sri Krishna", "hi": "भगवान श्रीकृष्ण", "bn": "ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Divine midnight advent of Lord Sri Krishna to eradicate injustice and protect Dharma.",
            "hi": "अधर्म के नाश एवं धर्म की स्थापना हेतु मध्यरात्रि में भगवान श्रीकृष्ण का दिव्य जन्मोत्सव।",
            "bn": "ধরাধামে ধর্মের পুনঃপ্রতিষ্ঠা ও অসুর নিধনে মধ্যরাত্রিতে ভগবান শ্রীকৃষ্ণের পরম শুভ আবির্ভাব।"
        },
        "muhurta": {"en": "Nishita Kaal Muhurta (Midnight 11:45 PM - 12:45 AM)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि ११:४५ - १२:४५)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি ১১:৪৫ - ১২:৪৫)"}
    },
    ("Bhadrapada", "Krishna", 9): {
        "en": "Sri Nandotsava",
        "hi": "श्री नंदोत्सव",
        "bn": "শ্রী শ্রী নন্দোৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🍯",
        "deity": {"en": "Bhagwan Sri Krishna & Nanda Baba", "hi": "बालकृष्ण व नन्द बाबा", "bn": "বালগোপাল ও নন্দ বাবা"},
        "description": {
            "en": "Joyous celebration in Gokula on the day after Janmashtami, distributing sweets, curd, and butter.",
            "hi": "नंदबाबा के भवन में आनंद भयो, जय कन्हैया लाल की - गोकुल में माखन-मिश्री वितरण का उल्लाস।",
            "bn": "গোকুলে নন্দভবনে ননী ও মিষ্টান্ন বিতরণের মাধ্যমে গোপাল জন্মের আনন্দোৎসব উদযাপন।"
        },
        "muhurta": {"en": "Pratah Kaal / Morning Utsav (07:00 - 10:30 AM)", "hi": "प्रातःकाल उत्सव मुहूर्त (०७:०० - १०:३०)", "bn": "প্রাতঃকাল মহোৎসব লগ্ন (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Bhadrapada", "Shukla", 3): {
        "en": "Hartalika Teej / Varaha Jayanti",
        "hi": "हरतालिका तीज / वराह जयंती",
        "bn": "হরতালিকা তীজ / ভগবান বরাহ অবতার জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌺",
        "deity": {"en": "Lord Shiva, Parvati & Lord Varaha", "hi": "शिव-पार्वती व भगवान वराह", "bn": "শিব-পার্বতী ও ভগবান বরাহ দেব"},
        "description": {
            "en": "Strict fast observed for marital bliss, commemorating Parvati's penance to attain Lord Shiva.",
            "hi": "अखंड सौभाग्य प्राप्ति हेतु बालू के शिवलिंग बनाकर माता पार्वती व शिव जी की रात्रि जागरण पूजा।",
            "bn": "অখণ্ড সৌভাগ্যের কামনায় বালুকার শিবলিঙ্গ নির্মাণ করে পার্বতী-মহাদেবের নির্জলা আরাধনা।"
        },
        "muhurta": {"en": "Pratah Kaal & Pradosh Kaal", "hi": "प्रातःकाल व प्रदोष काल", "bn": "প্রাতঃকাল ও প্রদোষ কাল"}
    },
    ("Bhadrapada", "Shukla", 4): {
        "en": "Ganesh Chaturthi / Vinayaka Chavithi",
        "hi": "श्री गणेश चतुर्थी / विनायक पूजा",
        "bn": "শ্রী শ্রী গণেশ চতুর্থী / বিনায়ক পূজা (গণেশোৎসব আরম্ভ)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐘",
        "deity": {"en": "Lord Ganesha", "hi": "भगवान श्री गणेश", "bn": "ভগবান শ্রী গণেশ"},
        "description": {
            "en": "Festive commencement of Ganeshotsav welcoming the remover of obstacles, Lord Ganesha.",
            "hi": "विघ्नहर्ता भगवान श्री गणेश के पावन प्राकट्य पर रिद्धि-सिद्धि युक्त गणेशोत्सव का शुभारंभ।",
            "bn": "বিঘ্নবিনাশক ও সর্বসিদ্ধিদাতা ভগবান শ্রী গণেশের শুভ আরাধনা ও গণেশোৎসব আরম্ভ।"
        },
        "muhurta": {"en": "Madhyahna Kaal Muhurta (11:00 AM - 01:30 PM)", "hi": "मध्याह्न काल मुहूर्त (दोपहर ११:०० - ०१:३०)", "bn": "মধ্যাহ্ন কাল মুহূর্ত (দুপুর ১১:০০ - ০১:৩০)"}
    },
    ("Bhadrapada", "Shukla", 5): {
        "en": "Rishi Panchami Vrat",
        "hi": "ऋषि पंचमी व्रत",
        "bn": "ঋষি পঞ্চমী ব্রত (সপ্তর্ষি পূজা)",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪔",
        "deity": {"en": "Sapta Rishis", "hi": "सप्तर्षि गण", "bn": "পবিত্র সপ্তর্ষি মণ্ডল"},
        "description": {
            "en": "Veneration of the Seven Great Sages (Sapta Rishis) to atone for accidental transgressions.",
            "hi": "जाने-अनजाने में हुए दोषों के निवारण हेतु कश्यपादि सप्त ऋषियों का विशेष पूजन व व्रत।",
            "bn": "অনিচ্ছাকৃত পাপক্ষয় ও পবিত্রতার জন্য কশ্যপাদি সপ্ত ঋষির উদ্দেশ্যে নিষ্ঠাপূর্ণ ব্রত ও অর্চনা।"
        },
        "muhurta": {"en": "Madhyahna Kaal (10:45 AM - 01:15 PM)", "hi": "मध्याह्न काल (१०:४५ - ०१:१५)", "bn": "মধ্যাহ্ন কাল (সকাল ১০:৪৫ - ০১:১৫)"}
    },
    ("Bhadrapada", "Shukla", 8): {
        "en": "Radhashtami / Mahalakshmi Vrat Begins",
        "hi": "श्री राधाष्टमी / महालक्ष्मी व्रत प्रारंभ",
        "bn": "শ্রী শ্রী রাধাষ্টমী মহাপর্ব / মহালক্ষ্মী ব্রতারম্ভ",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪷",
        "deity": {"en": "Srimati Radharani & Maa Mahalakshmi", "hi": "श्रीमती राधारानी व माँ महालक्ष्मी", "bn": "শ্রীমতী রাধারাণী ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Divine noon advent of Srimati Radharani at Barsana, the personification of pure devotion.",
            "hi": "बरसाना में दोपहर के समय प्रेम ও भक्ति की अधिष्ठात्री श्रीमती राधारानी का पावन प्राकट्य।",
            "bn": "পরমভক্তি ও প্রেমের মূর্ত প্রতীক শ্রীমতী রাধারাণীর বৃষভানুপুরে শুভ দ্বিপ্রহরে আবির্ভাব তিথি।"
        },
        "muhurta": {"en": "Madhyahna Kaal Muhurta (11:00 AM - 01:30 PM)", "hi": "मध्याह्न काल मुहूर्त (दोपहर ११:०० - ०१:३०)", "bn": "মধ্যাহ্ন কাল মুহূর্ত (দুপুর ১১:০০ - ০১:৩০)"}
    },
    ("Bhadrapada", "Shukla", 11): {
        "en": "Parsva Ekadashi / Vamana Jayanti",
        "hi": "परिवर्तिनी एकादशी / वामन जयंती",
        "bn": "পার্শ্ব একাদশী (পরিবর্তিনী) / ভগবান বামন জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️",
        "deity": {"en": "Lord Vamana & Sri Hari", "hi": "भगवान वामन व श्री हरि", "bn": "ভগবান বামন দেব ও শ্রীহরি"},
        "description": {
            "en": "Lord Vishnu shifts side in cosmic slumber, and appearance of Vamana Deva to redeem King Bali.",
            "hi": "शयन करते हुए भगवान विष्णु करवट बदलते हैं एवं राजा बलि का उद्धार करने वाले वामन देव का प्राकट्य।",
            "bn": "যোগনিদ্রায় শ্রীহরির পার্শ্ব পরিবর্তন এবং দানবীর বলিকে উদ্ধারকারী ভগবান বামনের আবির্ভাব।"
        },
        "muhurta": {"en": "Madhyahna Kaal (Vamana Puja 11:15 AM - 01:45 PM)", "hi": "मध्याह्न काल (११:१५ - ०१:४५)", "bn": "মধ্যাহ্ন কাল (বামন পূজা ১১:১৫ - ০১:৪৫)"}
    },
    ("Bhadrapada", "Shukla", 14): {
        "en": "Anant Chaturdashi / Ganesh Visarjan",
        "hi": "अनंत चतुर्दशी व्रत / गणेश विसर्जन",
        "bn": "অনন্ত চতুর্দশী ব্রত / শ্রী গণেশ বিসর্জন",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️",
        "deity": {"en": "Lord Ananta Padmanabha & Ganesha", "hi": "भगवान अनंत पद्मनाभ व श्री गणेश", "bn": "ভগবান অনন্ত পদ্মনাভ ও শ্রী গণেশ"},
        "description": {
            "en": "Tying the 14-knot sacred Ananta thread and concluding the 10-day Ganeshotsav with immersion.",
            "hi": "चौदह गांठों वाले अनंत सूत्र का धारण एवं १० दिवसीय गणेशोत्सव का विसर्जन व विदाई।",
            "bn": "১৪টি গ্রন্থিযুক্ত অনন্ত সূত্র ধারণ এবং ১০ দিনব্যাপী গণেশোৎসবের প্রতিমা বিসর্জন।"
        },
        "muhurta": {"en": "Purvahna (Anant Puja) & Day-long Visarjan", "hi": "पूर्वाह्न (अनंत पूजा) व दिनभर विसर्जन", "bn": "পূর্বাহ্ন (অনন্ত পূজা) ও সারাদিন বিসর্জন"}
    },
    ("Bhadrapada", "Shukla", 15): {
        "en": "Bhadrapada Purnima / Pitru Paksha Shraddha Begins",
        "hi": "भाद्रपद पूर्णिमा / पितृपक्ष प्रारंभ (सत्यनारायण पूजा)",
        "bn": "ভাদ্রপদ পূর্ণিমা / পিতৃপক্ষ শ্রাদ্ধারম্ভ (সত্যনারায়ণ পূজা)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🙏",
        "deity": {"en": "Lord Satyanarayan & Ancestors", "hi": "सत्यनारायण देव व पितृ गण", "bn": "শ্রী সত্যনারায়ণ ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Full moon observance and initiation of Mahalaya Pitru Paksha fortnight for ancestor shraddha.",
            "hi": "सत्यनारायण पूर्णिमा पूजन एवं पूर्वजों की तृप्ति हेतु १६ दिवसीय महालय श्राद्ध पक्ष का आरंभ।",
            "bn": "সত্যনারায়ণ পূজা এবং পরলোকগত পিতৃপুরুষের আত্মার তৃপ্তির উদ্দেশ্যে ১৬ দিনের পিতৃপক্ষ শ্রাদ্ধারম্ভ।"
        },
        "muhurta": {"en": "Kutapa & Aparahna (Tarpan) & Pradosh", "hi": "कुतप व अपराह्न (तर्पण) व प्रदोष", "bn": "কুতপ কাল (তর্পণ) ও প্রদোষ সত্যনারায়ণ"}
    },

    # --------------------------------------------------------------------------
    # আশ্বিন মাস (Ashvina - দুর্গাপূজা)
    # --------------------------------------------------------------------------
    ("Ashvina", "Krishna", 15): {
        "en": "Mahalaya (Sarvapitri Amavasya / Pitru Tarpan)",
        "hi": "महालया / सर्वपितृ अमावस्या / तर्पण",
        "bn": "মহালয়া / সর্বপিতৃ অমাবস্যা ও পিতৃপক্ষের তর্পণ",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Pitru Devas", "hi": "माँ दुर्गा व पितृ देव", "bn": "মা দুর্গা ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Grand invocation of Maa Durga and sacred water offerings (tarpan) to departed ancestors.",
            "hi": "देवी दुर्गा का पावन आवाहन एवं पूर्वजों के प्रति श्रद्धा सुमन व पितृ तर्पण का पवित्र दिन।",
            "bn": "দেবী দুর্গার আবাহনী লগ্ন এবং পরলোকগত পিতৃপুরুষের উদ্দেশ্যে তর্পণ নিবেদনের পবিত্র ক্ষণ।"
        },
        "muhurta": {"en": "Kutapa & Rauhina Muhurta (Tarpan Time)", "hi": "कुतप व रौहिण मुहूर्त (तर्पण काल)", "bn": "কুতপ ও রৌহিণ মুহূর্ত (তর্পণ সময়)"}
    },
    ("Ashvina", "Shukla", 1): {
        "en": "Sharad Navratri Begins / Ghatasthapana / Shailaputri Puja",
        "hi": "शारदीय नवरात्रि प्रारंभ / घटस्थापना / माँ शैलपुत्री पूजा",
        "bn": "শারদীয়া নবরাত্রি আরম্ভ / ঘটস্থাপন / দেবী শৈলপুত্রী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Shailaputri", "hi": "माँ दुर्गा व शैलपुत्री", "bn": "মা দুর্গা ও দেবী শৈলপুত্রী"},
        "description": {
            "en": "Commencement of the 9-day Sharad Navratri festival by establishing the sacred urn.",
            "hi": "कलश स्थापना व माँ शैलपुत्री के पूजन के साथ नौ दिवसीय पावन शारदीय दुर्गोत्सव का शुभारंभ।",
            "bn": "পবিত্র ঘটস্থাপন ও দেবী শৈলপুত্রীর আরাধনার মাধ্যমে ৯ দিনব্যাপী শারদীয়া দুর্গোৎসবের আরম্ভ।"
        },
        "muhurta": {"en": "Ghatasthapana & Abhijit Muhurta (06:15 - 10:15 AM)", "hi": "घटस्थापना व अभिजित मुहूर्त (प्रातः ०६:१५ - १०:१५)", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত (সকাল ০৬:১৫ - ১০:১৫)"}
    },
    ("Ashvina", "Shukla", 2): {
        "en": "Navratri Day 2: Brahmacharini Puja",
        "hi": "नवरात्रि दिवस २: माँ ब्रह्मचारिणी पूजा",
        "bn": "শারদ নবরাত্রি ২য় দিন: দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Brahmacharini", "hi": "माँ ब्रह्मचारिणी", "bn": "দেবী ব্রহ্মচারিণী"},
        "description": {
            "en": "Second day of Navratri dedicated to the goddess of austerity and divine asceticism.",
            "hi": "तपस्या ও ज्ञान की प्रदाता देवी ब्रह्मचारिणी का नवरात्रि के द्वितीय दिवस पर पावन पूजन।",
            "bn": "তপোনিষ্ঠা ও দিব্য প্রজ্ঞার দেবী ব্রহ্মচারিণীর চরণে নবরাত্রির দ্বিতীয় দিনে ভক্তিপূর্ণ নিবেদন।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:00 - 10:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Ashvina", "Shukla", 3): {
        "en": "Navratri Day 3: Chandraghanta Puja",
        "hi": "नवरात्रि दिवस ३: माँ चंद्रघंटा पूजा",
        "bn": "শারদ নবরাত্রি ৩য় দিন: দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Chandraghanta", "hi": "माँ चंद्रघंटा", "bn": "দেবী চন্দ্রঘণ্টা"},
        "description": {
            "en": "Worship of the ten-armed warrior form bearing a crescent bell for courage and inner peace.",
            "hi": "साहस, निर्भयता व शांति की दात्री माँ चंद्रघंटा का नवरात्रि के तृतीय दिवस पर अर्चन।",
            "bn": "বীরত্ব, নির্ভীকতা ও শান্তির বরদাত্রী দশভুজা দেবী চন্দ্রঘণ্টার নবরাত্রির তৃতীয় দিনের পূজা।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:00 - 10:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Ashvina", "Shukla", 4): {
        "en": "Navratri Day 4: Kushmanda Puja",
        "hi": "नवरात्रि दिवस ४: माँ कूष्मांडा पूजा",
        "bn": "শারদ নবরাত্রি ৪র্থ দিন: দেবী কূষ্মাণ্ডা পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Kushmanda", "hi": "माँ कूष्मांडा", "bn": "দেবী কূষ্মাণ্ডা"},
        "description": {
            "en": "Invoking the creator of the cosmic universe with Her radiant divine smile.",
            "hi": "अपनी मंद मुस्कान से ब्रह्मांड की रचना करने वाली देवी कूष्मांडा का पावन पूजन।",
            "bn": "মন্দ মধুর হাস্যে অণ্ড বা ব্রহ্মাণ্ডের সৃষ্টিকর্ত্রী অষ্টভুজা দেবী কূষ্মাণ্ডার বিশেষ পূজা।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:00 - 10:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Ashvina", "Shukla", 5): {
        "en": "Navratri Day 5: Skandamata Puja / Upang Lalita Vrat",
        "hi": "नवरात्रि दिवस ५: माँ स्कंदमाता पूजा / उपांग ललिता व्रत",
        "bn": "শারদ নবরাত্রি ৫ম দিন: দেবী স্কন্দমাতা পূজা / উপাঙ্গ ললিতা ব্রত",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Skandamata & Lalita", "hi": "माँ स्कंदमाता व ललिता", "bn": "দেবী স্কন্দমাতা ও ললিতা"},
        "description": {
            "en": "Worship of the mother of Lord Kartikeya (Skanda), bestowing salvation and prosperity.",
            "hi": "देवसेनापति भगवान स्कंद (कार्तिकेय) की माता माँ स्कंदमाता की भक्तिमयी आराधना।",
            "bn": "দেব সেনাপতি কার্তিকেয়ের জননী দেবী স্কন্দমাতা ও শ্রী ললিতা দেবীর বাৎসল্যপূর্ণ আরাধনা।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:00 - 10:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:০০ - ১০:৩০)"}
    },
    ("Ashvina", "Shukla", 6): {
        "en": "Durga Puja: Maha Sashti (Bodhan & Bilva Nimantran)",
        "hi": "दुर्गा षष्ठी (बिल्व निमंत्रण व बोधन)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাষষ্ঠী (বোধন, আমন্ত্রণ ও অধিবাস)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Katyayani", "hi": "माँ दुर्गा व माँ कात्यायनी", "bn": "মা দুর্গা ও দেবী কাত্যায়নী"},
        "description": {
            "en": "Awakening of Maa Durga through Bilva tree rituals, Kalparambha, and sacred invocation.",
            "hi": "बिल्व वृक्ष के नीचे माँ दुर्गा का पावन बोधन, आमंत्रण एवं कल्पारंभ अनुष्ठान।",
            "bn": "বিল্ববৃক্ষমূলে দেবীর বোধন, আমন্ত্রণ ও অধিবাসের মাধ্যমে শারদীয়া দুর্গোৎসবের শুভ সূচনা।"
        },
        "muhurta": {"en": "Sayankal Bilva Nimantran & Adhivas", "hi": "सायंकाल बिल्व निमंत्रण व अधिवास", "bn": "সায়ংকালে বিল্ব নিমন্ত্রণ, বোধন ও অধিবাস"}
    },
    ("Ashvina", "Shukla", 7): {
        "en": "Durga Puja: Maha Saptami (Navapatrika Pravesh)",
        "hi": "दुर्गा सप्तमी (नवपत्रिका प्रवेश पूजा)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাসপ্তমী (নবপত্রিকা প্রবেশ ও মহাস্নান)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Kalaratri", "hi": "माँ दुर्गा व माँ कालरात्रि", "bn": "মা দুর্গা ও দেবী কালরাত্রি"},
        "description": {
            "en": "Bathing and entry of Navapatrika (Kola Bou) representing 9 forms of Mother Nature.",
            "hi": "प्रकृति के नौ रूपों की प्रतीक नवपत्रिका (केला बहू) का पावन प्रवेश व प्राण प्रतिष्ठा।",
            "bn": "প্রকৃতির ৯টি ঔষধি রূপ নবপত্রিকা (কলাবউ) স্নান, মণ্ডপে প্রবেশ ও মহাসপ্তমী বিহিত পূজা।"
        },
        "muhurta": {"en": "Pratah Kaal Navapatrika Entry & Snan", "hi": "प्रातःकाल नवपत्रिका प्रवेश व स्नान", "bn": "প্রাতঃকালে নবপত্রিকা প্রবেশ ও মহাস্নান"}
    },
    ("Ashvina", "Shukla", 8): {
        "en": "Durga Puja: Maha Ashtami / Sandhi Puja / Kumari Puja",
        "hi": "दुर्गा महाष्टमी / संधि पूजा / कुमारी पूजा",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাঅষ্টমী, সন্ধিপূজা ও কুমারী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Chamunda Durga & Mahagauri", "hi": "माँ चामुंडा दुर्गा व महागौरी", "bn": "দেবী চামুণ্ডা দুর্গা ও মহাগৌরী"},
        "description": {
            "en": "Supreme worship of Chamunda Durga at the juncture of Ashtami and Navami with 108 lamps.",
            "hi": "अष्टमी-नवमी के संधि काल में १०८ दीपों से माँ चामुंडा की विशेष संधि पूजा व कन्या पूजन।",
            "bn": "অষ্টমী ও নবমীর সন্ধিক্ষণে চণ্ড-মুণ্ড বিনাশিনী দেবী চামুণ্ডার ১০৮ প্রদীপ প্রজ্বলনে মহা সন্ধিপূজা।"
        },
        "muhurta": {"en": "Exact Sandhi Puja 48-Minute Span", "hi": "संधि पूजा मुहूर्त (४८ मिनट संधि काल)", "bn": "সন্ধিপূজা মুহূর্ত (৪৮ মিনিট ব্যপ্তিকাল)"}
    },
    ("Ashvina", "Shukla", 9): {
        "en": "Durga Puja: Maha Navami / Navami Homa",
        "hi": "दुर्गा महानवमी पूजा / नवमी हवन",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহানবমী পূজা ও মহাহোম",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Siddhidatri Durga", "hi": "माँ सिद्धिदात्री दुर्गा", "bn": "দেবী সিদ্ধিদাত্রী দুর্গা"},
        "description": {
            "en": "Completion of Durga Puja rituals with grand sacrificial fire (Maha Yagya) and Ayudha Puja.",
            "hi": "माँ दुर्गा की पूर्ण विधि-विधान से महानवमी पूजा, आयुध पूजन एवं महाहवन अनुष्ठान।",
            "bn": "মহা আহুতির মাধ্যমে মহাহোম, আয়ুধ পূজা ও নবমীর বিহিত পূজার মাধ্যমে বিজয়ের সংকল্প গ্রহণ।"
        },
        "muhurta": {"en": "Madhyahna Maha Homa Muhurta", "hi": "मध्याह्न महाहवन मुहूर्त", "bn": "মধ্যাহ্ন মহাহোম ও নবমী যজ্ঞ সময়"}
    },
    ("Ashvina", "Shukla", 10): {
        "en": "Vijaya Dashami / Dussehra / Visarjan",
        "hi": "विजयादशमी / दशहरा / विसर्जन",
        "bn": "শ্রী শ্রী বিজয়া দশমী / দশহরা / সিঁদুর খেলা ও বিসর্জন",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Maa Durga & Lord Sri Rama", "hi": "माँ दुर्गा व भगवान श्रीराम", "bn": "মা দুর্গা ও ভগবান শ্রীরামচন্দ্র"},
        "description": {
            "en": "Triumph of good over evil, Sindoor Khela, and farewell immersion of Maa Durga.",
            "hi": "बुराई पर अच्छाई की विजय, रावण दहन, सिंदूर खेला एवं माँ दुर्गा का भावभीना विसर्जन।",
            "bn": "অসুরের বিনাশে শুভর জয়, মা দুর্গাকে বিদায় সম্ভাষণ, সিঁদুর খেলা ও পবিত্র অপরাজিতা পূজা।"
        },
        "muhurta": {"en": "Aparajita Puja & Vijaya Muhurta (02:00 - 02:45 PM)", "hi": "अपराजिता पूजा व विजय मुहूर्त (दोपहर ०२:०० - ०२:४५)", "bn": "অপরাজিতা পূজা ও বিজয় মুহূর্ত (দুপুর ০২:০০ - ০২:৪৫)"}
    },
    ("Ashvina", "Shukla", 15): {
        "en": "Kojagari Lakshmi Puja / Sharad Purnima",
        "hi": "कोजागरी लक्ष्मी पूजा / शरद पूर्णिमा",
        "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা / শারদ পূর্ণিমা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "icon": "🪷",
        "deity": {"en": "Maa Lakshmi & Sri Hari", "hi": "माँ महालक्ष्मी व श्रीहरि", "bn": "মা লক্ষ্মী ও শ্রীহরি নারায়ণ"},
        "description": {
            "en": "Worship of Maa Lakshmi on full moon night to bestow wealth, prosperity, and peace.",
            "hi": "शरद पूर्णिमा की धवल रात्रि में धन-समृद्धि की देवी माँ महालक्ष्मी की रात्रि जागरण पूजा।",
            "bn": "শারদ পূর্ণিমার অমল জ্যোৎস্নায় ধন-ধান্য ও সমৃদ্ধির অধিষ্ঠাত্রী মা লক্ষ্মীর কোজাগরী জাগরণ ও পূজা।"
        },
        "muhurta": {"en": "Nishita Kaal & Pradosh Kaal Muhurta", "hi": "निशीथ काल व प्रदोष काल मुहूर्त", "bn": "নিশীথ কাল ও প্রদোষ কাল মুহূর্ত (রাত্রিকাল)"}
    },

    # --------------------------------------------------------------------------
    # কার্তিক মাস (Kartika)
    # --------------------------------------------------------------------------
    ("Kartika", "Krishna", 4): {
        "en": "Karwa Chauth Vrat",
        "hi": "करवा चौथ व्रत (करक चतुर्थी)",
        "bn": "করবা চৌথ ব্রত",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌙",
        "deity": {"en": "Lord Shiva, Parvati & Chandra Deva", "hi": "शिव-पार्वती व चन्द्र देव", "bn": "শিব-পার্বতী ও চন্দ্র দেব"},
        "description": {
            "en": "Rigorous fast observed by married women from sunrise till moonrise for their husband's longevity.",
            "hi": "सुहागिन महिलाओं द्वारा पति की दीर्घायु ও स्वास्थ्य हेतु सूर्योदय से चंद्रोदय तक निर्जला व्रत।",
            "bn": "স্বামীর দীর্ঘায়ু ও কল্যাণে সূর্যোদয় থেকে চন্দ্রোদয় পর্যন্ত সৌভাগ্যবতী নারীদের নিষ্ঠাপূর্ণ নির্জলা ব্রত।"
        },
        "muhurta": {"en": "Moonrise & Pradosh Kaal (After 07:45 PM)", "hi": "चन्द्रोदय व प्रदोष काल (रात्रि ०७:४५ के उपरांत)", "bn": "চন্দ্রোদয় ও প্রদোষ কাল (রাত ০৭:৪৫ এর পর)"}
    },
    ("Kartika", "Krishna", 8): {
        "en": "Ahoi Ashtami Vrat / Radha Kund Snan",
        "hi": "अहोई अष्टमी व्रत / राधा कुंड स्नान",
        "bn": "অহোই অষ্টমী ব্রত / শ্রী রাধাকুণ্ড স্নান",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪔",
        "deity": {"en": "Maa Ahoi", "hi": "माँ अहोई", "bn": "মা অহোই দেবী"},
        "description": {
            "en": "Mothers fast for the well-being and long life of their children, breaking the fast after star sighting.",
            "hi": "माताएं अपनी संतानों की दीर्घायु, स्वास्थ्य व सुखद भविष्य के लिए तारा दर्शन तक व्रत रखती हैं।",
            "bn": "মাতা কর্তৃক সন্তানের মঙ্গল ও দীর্ঘ জীবনের কামনায় সায়ংকালে নক্ষত্র দর্শন পর্যন্ত উপবাস ব্রত।"
        },
        "muhurta": {"en": "Sayankal Star Gazing & Pradosh (05:40 - 07:00 PM)", "hi": "सायंकाल तारा दर्शन व प्रदोष (०५:४० - ०७:००)", "bn": "সায়ংকালে তারা দর্শন ও প্রদোষ (সন্ধ্যা ০৫:৪০ - ০৭:০০)"}
    },
    ("Kartika", "Krishna", 12): {
        "en": "Govatsa Dwadashi / Bachh Baras / Gau Puja",
        "hi": "गोवत्स द्वादशी (बछ बारस) / गौ माता पूजा",
        "bn": "গোবৎসা দ্বাদশী / বাছুর ও গো-পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🐄",
        "deity": {"en": "Gau Mata & Lord Krishna", "hi": "गौ माता व भगवान श्रीकृष्ण", "bn": "গো-মাতা ও ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Veneration of cows and their calves before Diwali, thanking Kamadhenu for nourishing humanity.",
            "hi": "दीपावली से पूर्व कामधेनु स्वरूपा गौ माता एवं बछड़े का कृतज्ञतापूर्वक पूजन व वंदन।",
            "bn": "দীপাবলির প্রাক্কালে কামধেনু রূপিণী গো-মাতা ও বাছুরের প্রতি শ্রদ্ধা ও কৃতজ্ঞতা জ্ঞাপন পূজা।"
        },
        "muhurta": {"en": "Pradosh Kaal (05:30 - 07:45 PM)", "hi": "प्रदोष काल (संध्या ०५:३० - ०৭:४५)", "bn": "প্রদোষ কাল (সন্ধ্যা ০৫:৩০ - ০৭:৪৫)"}
    },
    ("Kartika", "Krishna", 13): {
        "en": "Dhanteras / Dhanvantari Jayanti / Kuber Puja",
        "hi": "धनतेरस / धन्वंतरि जयंती / कुबेर पूजा",
        "bn": "শ্রী শ্রী ধনতেরাস / ধন্বন্তরি জয়ন্তী / কুবের পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापর্ব", "bn": "মহাপর্ব"},
        "icon": "🪙",
        "deity": {"en": "Lord Dhanvantari & Kuber", "hi": "भगवान धन्वंतरि व कुबेर देव", "bn": "ভগবান ধন্বন্তরি ও কুবের দেব"},
        "description": {
            "en": "Worship of Dhanvantari for health and Lord Kuber for wealth, with evening Yama Deepam.",
            "hi": "आरोग्य हेतु धन्वंतरि, समृद्धि हेतु कुबेर पूजन एवं अकाल मृत्यु निवारण हेतु यम दीपदान।",
            "bn": "সুস্বাস্থ্যের জন্য ধন্বন্তরি ও সমৃদ্ধির জন্য কুবের পূজা এবং যমরাজের উদ্দেশ্যে প্রদীপ দান।"
        },
        "muhurta": {"en": "Pradosh Kaal & Vrishabha Lagna (05:45 - 08:15 PM)", "hi": "प्रदोष काल व वृषभ लग्न (संध्या ०५:४৫ - ०৮:১৫)", "bn": "প্রদোষ কাল ও বৃষ লগ্ন (সন্ধ্যা ০৫:৪৫ - ০৮:১৫)"}
    },
    ("Kartika", "Krishna", 14): {
        "en": "Bhoot Chaturdashi / Naraka Chaturdashi / 14 Pradeep Dan",
        "hi": "नरक चतुर्दशी / छोटी दिवाली / रूप चौदस",
        "bn": "ভূত চতুর্দশী (১৪ প্রদীপ ও ১৪ শাক দান) / নরক চতুর্দশী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "icon": "🪔",
        "deity": {"en": "Yamaraja & Ancestors", "hi": "यमराज व पितृ गण", "bn": "যমরাজ ও চোদ্দ পুরুষ"},
        "description": {
            "en": "Lighting 14 lamps to dispel dark energies and honour the 14 ancestors prior to Kali Puja.",
            "hi": "चौदह यमदीप प्रज्वलित कर नकारात्मकता दूर करना एवं रूप निखार हेतु अभ्यंग स्नान।",
            "bn": "চোদ্দ প্রদীপ প্রজ্বলন ও চোদ্দ শাক গ্রহণের মাধ্যমে অশুভ শক্তি দূরীকরণ ও চোদ্দ পুরুষের স্মরণ।"
        },
        "muhurta": {"en": "Sayankal 14 Deepam & Abhyanga Snan", "hi": "सायंकाल यम दीपदान व अभ्यंग स्नान", "bn": "সায়ংকালে ১৪ প্রদীপ দান ও তৈলাভ্যঙ্গ স্নান"}
    },
    ("Kartika", "Krishna", 15): {
        "en": "Shyama Puja (Kali Puja) / Diwali / Lakshmi Puja",
        "hi": "दीपावली / महालक्ष्मी पूजा / माँ काली पूजा",
        "bn": "শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / দীপাবলি মহোৎসব ও মহালক্ষ্মী পূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪔",
        "deity": {"en": "Maa Kali & Maa Mahalakshmi", "hi": "माँ काली व माँ महालक्ष्मी", "bn": "মা শ্যামা কালী ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Victory of light over darkness with earthen lamps and midnight worship of Maa Kali.",
            "hi": "अंधकार पर प्रकाश की विजय का दीपोत्सव एवं मध्यरात्रि में माँ काली की तांत्रिक व वैदिक पूजा।",
            "bn": "অন্ধকার দূর করে আলোর দীপাবলি উৎসব এবং অমাবস্যার নিশীথ রাতে মা শ্যামা কালীর আরাধনা।"
        },
        "muhurta": {"en": "Nishita Kaal (Kali Puja) & Pradosh (Diwali)", "hi": "निशीथ काल (काली पूजा) व प्रदोष (लक्ष्मी पूजा)", "bn": "নিশীথ কাল (কালীপূজা) ও প্রদোষ লগ্ন (দীপাবলি)"}
    },
    ("Kartika", "Shukla", 1): {
        "en": "Govardhan Puja / Annakut Mahotsav / Bali Pratipada",
        "hi": "गोवर्धन पूजा / अन्नकूट महोत्सव / बलि प्रतिपदा",
        "bn": "শ্রী শ্রী গোবর্ধন পূজা ও অন্নকূট মহোৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "⛰️",
        "deity": {"en": "Lord Sri Krishna (Giriraj)", "hi": "गिरिराज भगवान श्रीकृष्ण", "bn": "গিরিরাজ ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Commemorating Lord Krishna lifting the Govardhan Hill with offerings of 56 delicacies (Chhappan Bhog).",
            "hi": "इंद्र के मानमर्दन हेतु भगवान श्रीकृष्ण द्वारा गोवर्धन पर्वत धारण एवं ५६ भोग अन्नकूट समर्पण।",
            "bn": "ইন্দ্রের দর্পচূর্ণ করে শ্রীকৃষ্ণ কর্তৃক গোবর্ধন পর্বত ধারণ এবং ছাপ্পান্ন ভোগ নিবেদনে অন্নকূট উৎসব।"
        },
        "muhurta": {"en": "Pratah Kaal & Sayankal Annakut", "hi": "प्रातःकाल व सायंकाल अन्नकूट", "bn": "প্রাতঃকাল ও সায়ংকালে অন্নকূট ভোগ"}
    },
    ("Kartika", "Shukla", 2): {
        "en": "Bhai Phonta / Bhatri Dwitiya / Yama Dwitiya",
        "hi": "भाई दूज / यम द्वितीया / भ्रातृ द्वितीया",
        "bn": "পবিত্র ভাইফোঁটা (ভ্রাতৃদ্বিতীয়া / যমদ্বিতীয়া)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌸",
        "deity": {"en": "Yamuna & Yamaraja", "hi": "यमुना जी व यमराज", "bn": "যমুনা দেবী ও যমরাজ"},
        "description": {
            "en": "Sisters pray for their brothers' long life and protection from harm on Yama Dwitiya.",
            "hi": "बहनें अपने भाई की दीर्घायु, यश ও आरोग्यता के लिए तिलक लगाकर मंगल कामना करती हैं।",
            "bn": "যমের দুয়ারে কাঁটা দিয়ে ভাইয়ের দীর্ঘায়ু ও সর্ববিপদমুক্তির জন্য ভগিনীর পবিত্র আশীর্বাদ লগ্ন।"
        },
        "muhurta": {"en": "Aparahna Kaal Muhurta (01:15 - 03:30 PM)", "hi": "अपराह्न काल मुहूर्त (दोपहर ०१:१५ - ०३:३०)", "bn": "অপরাহ্ন কাল মুহূর্ত (দুপুর ০১:১৫ - ০৩:৩০)"}
    },
    ("Kartika", "Shukla", 6): {
        "en": "Chhath Puja (Sandhya Arghya / Surya Sashthi)",
        "hi": "छठ पूजा (संध्या अर्घ्य / सूर्य षष्ठी)",
        "bn": "ছট পূজা (সন্ধ্যার অর্ঘ্যদান ও সূর্য ষষ্ঠী)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "☀️",
        "deity": {"en": "Surya Deva & Chhathi Maiya", "hi": "भगवान सूर्य व छठी मइया", "bn": "ভগবান সূর্য দেব ও ছটি মাইয়া"},
        "description": {
            "en": "Offering sacred evening oblation (Arghya) in water bodies to the setting Sun God.",
            "hi": "जल में खड़े होकर अस्ताचलगामी भगवान सूर्य एवं छठी मइया को प्रथम संध्या अर्घ्य अर्पण।",
            "bn": "জলে দাঁড়িয়ে অস্তগামী ভগবান সূর্য দেব ও পরমাপ্রকৃতি ছটি মাইয়ার উদ্দেশ্যে পবিত্র সায়ং অর্ঘ্যদান।"
        },
        "muhurta": {"en": "Sunset / Sandhya Arghya Muhurta (05:05 - 05:40 PM)", "hi": "सूर्यास्त संध्या अर्घ्य मुहूर्त (०५:०५ - ०५:४०)", "bn": "সূর্যাস্ত সায়ং অর্ঘ্যদান মুহূর্ত (বিকাল ০৫:০৫ - ০৫:৪০)"}
    },
    ("Kartika", "Shukla", 7): {
        "en": "Chhath Puja (Usha Arghya & Paran)",
        "hi": "छठ पूजा (प्रातः अर्घ्य / पारण)",
        "bn": "ছট পূজা (ভোরের অর্ঘ্যদান ও পারণ)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "☀️",
        "deity": {"en": "Surya Deva & Chhathi Maiya", "hi": "भगवान सूर्य व छठी मइया", "bn": "ভগবান সূর্য দেব ও ছটি মাইয়া"},
        "description": {
            "en": "Offering dawn oblation to the rising Sun God, successfully concluding the 36-hour nirjala fast.",
            "hi": "उदीयमान भगवान सूर्य को प्रातः अर्घ्य समर्पण के साथ ३६ घंटे के निर्जला महाव्रत का पारण।",
            "bn": "উদীয়মান সূর্য দেবতাকে ভোরের অর্ঘ্য নিবেদনের মাধ্যমে ৩৬ ঘণ্টার নির্জলা মহাব্রতের সমাপন ও পারণ।"
        },
        "muhurta": {"en": "Sunrise / Usha Arghya Muhurta (05:55 - 06:40 AM)", "hi": "सूर्योदय उषा अर्घ्य मुहूर्त (०५:५५ - ०६:४०)", "bn": "সূর্যোদয় ঊষা অর্ঘ্যদান মুহূর্ত (ভোর ০৫:৫৫ - ০৬:৪০)"}
    },
    ("Kartika", "Shukla", 8): {
        "en": "Gopashtami / Gau Puja Mahotsav",
        "hi": "गोपाष्टमी / कामधेनु गौ पूजा",
        "bn": "শ্রী শ্রী গোপাষ্টমী / কামধেনু গো-পূজা মহোৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐄",
        "deity": {"en": "Lord Krishna & Gau Mata", "hi": "भगवान श्रीकृष्ण व कामधेनु", "bn": "শ্রীকৃষ্ণ ও কামধেনু গো-মাতা"},
        "description": {
            "en": "The auspicious day when Lord Krishna officially graduated from tending calves to herding cows.",
            "hi": "भगवान श्रीकृष्ण द्वारा बछड़ों की जगह गौ चारण की दीक्षा लेने का पावन गोपाष्टमी उत्सव।",
            "bn": "শ্রীকৃষ্ণ কর্তৃক বাছুরের পরিবর্তে স্বয়ং ধেনু চারণের দায়িত্ব গ্রহণের পুণ্যময় গোপাষ্টমী তিথি।"
        },
        "muhurta": {"en": "Pratah Kaal (Morning 07:30 - 10:30 AM)", "hi": "प्रातःकाल मुहूर्त (०७:३० - १०:३०)", "bn": "প্রাতঃকাল মুহূর্ত (সকাল ০৭:৩০ - ১০:৩০)"}
    },
    ("Kartika", "Shukla", 9): {
        "en": "Sri Jagaddhatri Puja / Akshaya Navami / Amla Navami",
        "hi": "जगद्धात्री पूजा / अक्षय नवमी / आँवला नवमी",
        "bn": "শ্রী শ্রী জগদ্ধাত্রী পূজা / অক্ষয় নবমী / আমলকী নবমী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🦁",
        "deity": {"en": "Maa Jagaddhatri", "hi": "माँ जगद्धात्री", "bn": "মা জগদ্ধাত্রী দেবী"},
        "description": {
            "en": "Worship of Maa Jagaddhatri, the sustainer of the world, and sacred sitting beneath Amla trees.",
            "hi": "संसार का भरण-पोषण करने वाली माँ जगद्धात्री की पूजा एवं आँवला वृक्ष के नीचे पूजन व भोजन।",
            "bn": "জগতের ধাত্রী দেবী জগদ্ধাত্রীর ত্রিকাল পূজা এবং পুণ্যফলদায়ী অক্ষয় আমলকী নবমী ব্রত।"
        },
        "muhurta": {"en": "Purvahna & Madhyahna (Triple Prahar Puja)", "hi": "पूर्वाह्न व मध्याह्न त्रिकाल पूजा", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ত্রিকাল পূজা"}
    },
    ("Kartika", "Shukla", 11): {
        "en": "Devutthana Ekadashi / Tulsi Vivah / Bhishma Panchaka Begins",
        "hi": "देवउठनी एकादशी / तुलसी विवाह / भीष्म पंचक प्रारंभ",
        "bn": "দেবউত্থান একাদশী / তুলসী বিবাহ / ভীষ্ম পঞ্চক ব্রতারম্ভ",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌿",
        "deity": {"en": "Lord Vishnu & Tulsi Maharani", "hi": "भगवान शालिग्राम व तुलसी जी", "bn": "ভগবান শালগ্রাম ও তুলসী মহারাণী"},
        "description": {
            "en": "Lord Vishnu awakens from four-month cosmic slumber, resuming all auspicious ceremonies and Tulsi Vivah.",
            "hi": "चातुर्मास की समाप्ति पर भगवान विष्णु का जागृत होना एवं शालिग्राम-तुलसी विवाह से शुभ कार्यों का आरंभ।",
            "bn": "চাতুর্মাস্য শেষে শ্রীহরির যোগনিদ্রা ভঙ্গ এবং শালগ্রাম-তুলসী বিবাহের মাধ্যমে সর্ব শুভকার্য আরম্ভ।"
        },
        "muhurta": {"en": "Pradosh Kaal (Tulsi Vivah 05:30 - 08:00 PM)", "hi": "प्रदोष काल (तुलसी विवाह ०५:३० - ०८:००)", "bn": "প্রদোষ কাল (তুলসী বিবাহ সন্ধ্যা ০৫:৩০ - ০৮:০০)"}
    },
    ("Kartika", "Shukla", 14): {
        "en": "Vaikuntha Chaturdashi",
        "hi": "वैकुंठ चतुर्दशी (हरि-हर मिलन)",
        "bn": "শ্রী বৈকুণ্ঠ চতুর্দশী (হরি-হর মিলন)",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️",
        "deity": {"en": "Lord Shiva & Lord Vishnu", "hi": "भगवान शिव व भगवान विष्णु", "bn": "দেবাদিদেব শিব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Divine union of Shiva and Vishnu where Lord Shiva worshipped Vishnu with 1000 lotus blossoms.",
            "hi": "भगवान शिव व विष्णु का पावन मिलन, जिसमें शिव जी ने भगवान विष्णु को सहस्र कमल अर्पित किए थे।",
            "bn": "ভগবান শিব ও শ্রীহরি বিষ্ণুর পরম পবিত্র মিলন তিথি এবং সহস্র পদ্ম নিবেদনের পূজা।"
        },
        "muhurta": {"en": "Nishita Kaal Muhurta (Midnight 11:40 PM - 12:35 AM)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि ११:४० - १२:३५)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি ১১:৪০ - ১২:৩৫)"}
    },
    ("Kartika", "Shukla", 15): {
        "en": "Sri Kartik Puja / Rash Yatra / Dev Deepawali / Kartik Purnima",
        "hi": "कार्तिक पूजा / देव दीपावली / रास पूर्णिमा / त्रिपुरारी पूर्णिमा",
        "bn": "শ্রী শ্রী কার্তিক পূজা / শ্রী শ্রী রাসযাত্রা / রাসপূর্ণিমা / দেব দীপাবলি",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪔",
        "deity": {"en": "Lord Kartikeya, Radha Krishna & Shiva", "hi": "कार्तिकेय, राधा-कृष्ण व शिव जी", "bn": "দেব সেনাপতি কার্তিক, রাধাকৃষ্ণ ও শিব"},
        "description": {
            "en": "Vrindavan Maha Raas, Lord Shiva slaying Tripurasura (Dev Deepawali in Varanasi), and Kartik Puja.",
            "hi": "काशी में देवताओं की देव दीपावली, श्रीराधा-कृष्ण की महारास पूर्णिमा एवं कार्तिकेय पूजन।",
            "bn": "বৃন্দাবনে শ্রীশ্রী রাধাকৃষ্ণের রাসযাত্রা মহোৎসব, কাশীতে দেব দীপাবলি এবং শ্রী কার্তিক পূজা।"
        },
        "muhurta": {"en": "Pradosh Kaal & Full Moon Night", "hi": "प्रदोष काल व दीपदान मुहूर्त", "bn": "প্রদোষ কাল ও দেব দীপাবলি লগ্ন"}
    },

    # --------------------------------------------------------------------------
    # মার্গশীর্ষ মাস (Margashirsha)
    # --------------------------------------------------------------------------
    ("Margashirsha", "Shukla", 5): {
        "en": "Vivah Panchami (Sri Rama-Sita Vivah Mahotsav)",
        "hi": "विवाह पंचमी (श्रीराम-जानकी विवाह महोत्सव)",
        "bn": "বিবাহ পঞ্চমী (শ্রীশ্রী সীতারাম শুভ বিবাহ মহোৎসব)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महाপর্ব", "bn": "মহাপর্ব"},
        "icon": "🏹",
        "deity": {"en": "Lord Sri Rama & Maa Sita", "hi": "भगवान श्रीराम व माँ सीता", "bn": "ভগবান শ্রীরামচন্দ্র ও মা জানকী"},
        "description": {
            "en": "Celebration of the celestial wedding anniversary of Lord Sri Rama and Maa Sita in Janakpur.",
            "hi": "जनकपुर में मर्यादा पुरुषोत्तम भगवान श्रीराम एवं जगज्जननी जानकी जी के पावन विवाह का उत्सव।",
            "bn": "জনকপুরধামে ভগবান শ্রীরামচন্দ্র ও মা জানকীর পবিত্র স্বর্গীয় শুভ বিবাহ বার্ষিকী মহোৎসব।"
        },
        "muhurta": {"en": "Abhijit & Godhuli Muhurta (11:45 AM - 01:15 PM)", "hi": "अभिजित व गोधूलि मुहूर्त (११:४५ - ०१:१५)", "bn": "অভিজিৎ ও গোধূলি শুভ লগ্ন (সকাল ১১:৪৫ - ০১:১৫)"}
    },
    ("Margashirsha", "Shukla", 6): {
        "en": "Champa Sasthi / Skanda Sasthi",
        "hi": "चंपा षष्ठी / स्कंद षष्ठी",
        "bn": "চম্পা ষষ্ঠী / স্কন্দ ষষ্ঠী ব্রত",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🦚",
        "deity": {"en": "Lord Kartikeya (Khandoba)", "hi": "भगवान कार्तिकेय (खंडोबा)", "bn": "ভগবান কার্তিকেয়"},
        "description": {
            "en": "Veneration of Lord Kartikeya (Khandoba) offering Champa flowers, brinjal, and millet bread.",
            "hi": "भगवान कार्तिकेय (मल्हारी मार्तंड) को चंपा पुष्प व बाजरा-बैंगन भोग समर्पण कर व्रत।",
            "bn": "দেব সেনাপতি কার্তিকেয়কে চাঁপা ফুল নিবেদন এবং শারীরিক সুস্থতার কামনায় বিশেষ ষষ্ঠী ব্রত।"
        },
        "muhurta": {"en": "Purvahna Kaal (07:30 - 10:30 AM)", "hi": "पूर्वाह्न काल (०७:३० - १०:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৭:৩০ - ১০:৩০)"}
    },
    ("Margashirsha", "Shukla", 11): {
        "en": "Mokshada Ekadashi / Srimad Bhagavad Gita Jayanti",
        "hi": "गीता जयंती / मोक्षदा एकादशी",
        "bn": "শ্রীমদ্ভগবদ্গীতা জয়ন্তী / মোক্ষদা একাদশী",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "📜",
        "deity": {"en": "Bhagwan Sri Krishna & Srimad Bhagavad Gita", "hi": "भगवान श्रीकृष्ण व श्रीमद्भगवद्गीता", "bn": "ভগবান শ্রীকৃষ্ণ ও শ্রীমদ্ভগবদ্গীতা"},
        "description": {
            "en": "The day Lord Krishna delivered the immortal song of Gita to Arjuna on the battlefield of Kurukshetra.",
            "hi": "कुरुक्षेत्र की रणभूमि में भगवान श्रीकृष्ण द्वारा अर्जुन को दिए गए अमर गीता उपदेश का पावन दिवस।",
            "bn": "কুরুক্ষেত্রের পুণ্য রণাঙ্গনে অর্জুনের মোহ দূর করতে ভগবান শ্রীকৃষ্ণ কর্তৃক উচ্চারিত গীতার জন্মতিথি।"
        },
        "muhurta": {"en": "Purvahna Kaal (Gita Path 07:00 - 11:30 AM)", "hi": "पूर्वाह्न काल (गीता पाठ ०७:०० - ११:३०)", "bn": "পূর্বাহ্ন কাল (গীতা পাঠ ও পূজা ০৭:০০ - ১১:৩০)"}
    },
    ("Margashirsha", "Shukla", 15): {
        "en": "Dattatreya Jayanti / Annapurna Jayanti / Margashirsha Purnima",
        "hi": "दत्तात्रेय जयंती / अन्नपूर्णा जयंती / मार्गशीर्ष पूर्णिमा",
        "bn": "শ্রী দত্তাত্রেয় জয়ন্তী / মা অন্নপূর্ণা আবির্ভাব / মার্গশীর্ষ পূর্ণিমা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️",
        "deity": {"en": "Lord Dattatreya & Maa Annapurna", "hi": "भगवान दत्तात्रेय व माँ अन्नपूर्णा", "bn": "ভগবান দত্তাত্রেয় ও মা অন্নপূর্ণা"},
        "description": {
            "en": "Appearance of Lord Dattatreya (the composite trimurti of Brahma, Vishnu, Shiva) and Maa Annapurna.",
            "hi": "ब्रह्मा, विष्णु, महेश के संयुक्त त्रिदेव रूप भगवान दत्तात्रेय एवं माँ अन्नपूर्णा का प्राकट्योत्सव।",
            "bn": "ব্রহ্মা, বিষ্ণু ও শিবের সমন্বিত রূপ ভগবান দত্তাত্রেয় এবং মা অন্নপূর্ণার শুভ আবির্ভাব তিথি।"
        },
        "muhurta": {"en": "Pradosh Kaal (Evening 05:30 - 07:45 PM)", "hi": "प्रदोष काल (संध्या ०५:३० - ०७:४५)", "bn": "প্রদোষ কাল (সন্ধ্যাবেলা ০৫:৩০ - ০৭:৪৫)"}
    },

    # --------------------------------------------------------------------------
    # পৌষ মাস (Pausha)
    # --------------------------------------------------------------------------
    ("Pausha", "Shukla", 15): {
        "en": "Pausha Purnima / Shakambhari Jayanti",
        "hi": "पौष पूर्णिमा / शाकंभरी जयंती (शाकंभरी नवरात्रि समापन)",
        "bn": "পৌষ পূর্ণিমা / মা শাকম্ভরী দেবী জয়ন্তী (শাকম্ভরী নবরাত্রি সমাপন)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪷",
        "deity": {"en": "Maa Shakambhari Durga", "hi": "माँ शाकंभरी देवी", "bn": "মা শাকম্ভরী দুর্গা"},
        "description": {
            "en": "Worship of Maa Shakambhari, who alleviated famine and drought with green vegetables and water.",
            "hi": "अकाल व सूखे से पृथ्वी की रक्षा हेतु वनस्पतियों ও जल को प्रकट करने वाली देवी शाकंभरी की पूजा।",
            "bn": "অনাবৃষ্টি ও দুর্ভিক্ষ দূর করে সবুজ শস্য-শাকসবজি দানকারিণী মা শাকম্ভরীর বিশেষ আবির্ভাব পূজা।"
        },
        "muhurta": {"en": "Purvahna & Pradosh Kaal", "hi": "पूर्वाह्न व प्रदोष काल", "bn": "পূর্বাহ্ন ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # মাঘ মাস (Magha)
    # --------------------------------------------------------------------------
    ("Magha", "Shukla", 1): {
        "en": "Magha Gupt Navratri Begins",
        "hi": "माघ गुप्त नवरात्रि प्रारंभ / घटस्थापना",
        "bn": "মাঘ গুপ্ত নবরাত্রি আরম্ভ / ঘটস্থাপন ও দশমহাবিদ্যা সাধনা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "साधना पर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Das Mahavidya & Maa Durga", "hi": "दस महाविद्या व माँ दुर्गा", "bn": "দশমহাবিদ্যা ও মা দুর্গা"},
        "description": {
            "en": "Auspicious commencement of winter Gupt Navratri for spiritual austerities and Tantric sadhana.",
            "hi": "शिशिर ऋतु में आत्मिक शक्ति व महाविद्याओं की कृपा प्राप्ति हेतु गुप्त नवरात्रि घटस्थापना।",
            "bn": "শীতকালীন গুপ্ত নবরাত্রিতে ঘটস্থাপন ও আত্মশুদ্ধি এবং দশমহাবিদ্যার নিগূঢ় সাধনার শুভ সূচনা।"
        },
        "muhurta": {"en": "Ghatasthapana & Abhijit Muhurta (06:45 - 10:15 AM)", "hi": "घटस्थापना व अभिजित मुहूर्त (प्रातः ०६:४५ - १०:१५)", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত (সকাল ০৬:৪৫ - ১০:১৫)"}
    },
    ("Magha", "Shukla", 4): {
        "en": "Ganesha Jayanti / Varad Vinayaka Chaturthi / Til Kund Chaturthi",
        "hi": "गणेश जयंती / वरद चतुर्थी / तिल कुंद चतुर्थी",
        "bn": "শ্রী গণেশ জন্মজয়ন্তী / বরদ বিনায়ক চতুর্থী (তিল চতুর্থী)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐘",
        "deity": {"en": "Lord Ganesha", "hi": "भगवान श्री गणेश", "bn": "ভগবান শ্রী গণেশ"},
        "description": {
            "en": "Traditional appearance day of Lord Ganesha in Magha, offering sesame (til) laddus.",
            "hi": "माघ मास में भगवान श्री गणेश का पावन जन्मोत्सव, तिल-गुड़ के लड्डुओं से विशेष पूजा।",
            "bn": "মাঘ মাসের শুক্ল চতুর্থীতে সিদ্ধিদাতা শ্রী গণেশের জন্মজয়ন্তী এবং তিলের লাড্ডু নিবেদন পূজা।"
        },
        "muhurta": {"en": "Madhyahna Kaal Muhurta (11:00 AM - 01:30 PM)", "hi": "मध्याह्न काल मुहूर्त (दोपहर ११:०० - ०१:३०)", "bn": "মধ্যাহ্ন কাল মুহূর্ত (দুপুর ১১:০০ - ০১:৩০)"}
    },
    ("Magha", "Shukla", 5): {
        "en": "Sri Saraswati Puja / Vasant Panchami / Sri Panchami",
        "hi": "सरस्वती पूजा / बसंत पंचमी / श्री पंचमी / वाग्देवी आराधना",
        "bn": "শ্রী শ্রী সরস্বতী পূজা / বসন্ত পঞ্চমী / শ্রীপঞ্চমী (বাগদেবী আরাধনা)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪕",
        "deity": {"en": "Maa Saraswati (Vagdevi)", "hi": "वाग्देवी माँ सरस्वती", "bn": "বাগদেবী মা সরস্বতী"},
        "description": {
            "en": "Worship of the Goddess of knowledge, music, and arts, marking the arrival of spring.",
            "hi": "विद्या, बुद्धि, ज्ञान व संगीत की अधिष्ठात्री देवी माँ सरस्वती की आराधना व वसंत ऋतु आगमन।",
            "bn": "বিদ্যা, বুদ্ধি ও জ্ঞানের বরদাত্রী মা সরস্বতীর শ্রীচরণে অঞ্জলি প্রদান ও বসন্তের শুভ আবাহন।"
        },
        "muhurta": {"en": "Purvahna Kaal Muhurta (07:00 AM - 12:30 PM)", "hi": "पूर्वाह्न काल मुहूर्त (प्रातः ०७:०० - दोपहर १२:३०)", "bn": "পূর্বাহ্ন কাল মুহূর্ত (সকাল ০৭:০০ - দুপুর ১২:৩০)"}
    },
    ("Magha", "Shukla", 7): {
        "en": "Ratha Saptami / Surya Jayanti / Arogya Saptami",
        "hi": "रथ सप्तमी / सूर्य जयंती / आरोग्य सप्तमी / अचला सप्तमी",
        "bn": "রথ সপ্তমী / সূর্য জয়ন্তী / আরোগ্য সপ্তমী মহোৎসব",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "☀️",
        "deity": {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"},
        "description": {
            "en": "The day Lord Surya mounted His golden chariot driven by Aruna with seven green horses.",
            "hi": "भगवान सूर्य देव द्वारा अपने सात घोड़ों वाले दिव्य रथ पर आरूढ़ होकर ज्ञान प्रकाश फैलाने का दिन।",
            "bn": "সপ্তরথী ঘোটকবাহী রথে ভগবান সূর্যদেবের আরোহণ ও আরোগ্যলাভের পুণ্য সূর্য জয়ন্তী স্নান।"
        },
        "muhurta": {"en": "Sunrise & Arunodaya Snan Muhurta (05:45 - 07:15 AM)", "hi": "सूर्योदय व अरुणोदय स्नान मुहूर्त (०५:४५ - ०७:१৫)", "bn": "সূর্যোদয় ও অরুণোদয় স্নান মুহূর্ত (ভোর ০৫:৪৫ - ০৭:১৫)"}
    },
    ("Magha", "Shukla", 8): {
        "en": "Bhishma Ashtami Vrat & Tarpan",
        "hi": "भीष्म अष्टमी व्रत व तर्पण",
        "bn": "ভীষ্ম অষ্টমী ব্রত ও পিতামহ ভীষ্ম তর্পণ",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "तर्पण पर्व", "bn": "উপবাস ব্রত"},
        "icon": "🏹",
        "deity": {"en": "Bhishma Pitamah", "hi": "पितामह भीष्म", "bn": "পিতামহ ভীষ্ম"},
        "description": {
            "en": "Commemorating the departure of Grandsire Bhishma on Uttarayana and offering him water tarpan.",
            "hi": "सूर्य के उत्तरायण होने पर इच्छामृत्यु प्राप्त पितामह भीष्म के मोक्ष गमन पर श्राद्ध ও तर्पण।",
            "bn": "সূর্যের উত্তরায়ণে পিতামহ ভীষ্মের মোক্ষলাভ স্মরণে সর্ববর্ণের ভক্তগণের তৃপ্তিদায়ক ভীষ্ম তর্পণ।"
        },
        "muhurta": {"en": "Madhyahna Tarpan Kaal (11:15 AM - 01:30 PM)", "hi": "मध्याह्न तर्पण काल (११:१५ - ०१:३०)", "bn": "মধ্যাহ্ন তর্পণ সময় (সকাল ১১:১৫ - ০১:৩০)"}
    },
    ("Magha", "Shukla", 15): {
        "en": "Magha Purnima / Maha Maghi Snan / Lalita Jayanti",
        "hi": "माघ पूर्णिमा / महा माघी स्नान / ललिता जयंती",
        "bn": "মাঘী পূর্ণিমা / মহামাঘী স্নান / মা ললিতা জয়ন্তী",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌊",
        "deity": {"en": "Lord Vishnu, Ganga & Tripura Sundari", "hi": "विष्णु जी, गंगा व माँ ललिता", "bn": "শ্রীহরি বিষ্ণু, গঙ্গা ও মা ললিতা ত্রিপুরাসুন্দরী"},
        "description": {
            "en": "Confluence of deities in sacred rivers, highly praised for Prayag Triveni Sangam snan.",
            "hi": "प्रयागराज त्रिवेणी संगम में समस्त तीर्थों के वास पर पवित्र स्नान एवं माँ ललिता जयंती।",
            "bn": "প্রয়াগরাজ ও সর্বতীর্থে পুণ্যস্নান, দান এবং দেবী ললিতা ত্রিপুরাসুন্দরীর শুভ আবির্ভাব তিথি।"
        },
        "muhurta": {"en": "Brahma Muhurta & Sunrise Snan (05:00 - 07:30 AM)", "hi": "ब्रह्म मुहूर्त व सूर्योदय स्नान (०५:०० - ०७:३०)", "bn": "ব্রাহ্ম মুহূর্ত ও সূর্যোদয় মহাতীর্থ স্নান (ভোর ০৫:০০ - ০৭:৩০)"}
    },
    ("Magha", "Krishna", 14): {
        "en": "Sri Maha Shivratri Vrat & Mahapuja",
        "hi": "श्री महाशिवरात्रि व्रत व महापूजा / शिव-पार्वती विवाह",
        "bn": "শ্রী শ্রী মহা শিবরাত্রি ব্রত ও চার প্রহর শিবপূজা",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱",
        "deity": {"en": "Lord Shiva & Maa Parvati", "hi": "देवाधिदेव महादेव व माँ पार्वती", "bn": "দেবাদিদেব মহাদেব ও মা পার্বতী"},
        "description": {
            "en": "Great night of Shiva observing day-long fast and four-prahar lingam abhishek.",
            "hi": "भगवान शिव-पार्वती के पावन विवाह एवं लिंगोद्भव की महानिशा, चार प्रहर जलाभिषेक व व्रत।",
            "bn": "শিব-পার্বতীর বিবাহ ও জ্যোতির্লিঙ্গ প্রকাশের মহাপর্ব; দিবারাত্র উপবাস ও চার প্রহর রুদ্রাভিষেক।"
        },
        "muhurta": {"en": "Nishita Kaal Muhurta (Midnight) & 4 Prahar", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि) व चार प्रहर", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি) ও চার প্রহর পূজা"}
    },
    ("Magha", "Krishna", 15): {
        "en": "Mauni Amavasya / Magha Amavasya Mahasnan",
        "hi": "मौनी अमावस्या / माघ अमावस्या महास्नान",
        "bn": "মৌনী অমাবস্যা / মাঘী অমাবস্যা মহাতীর্থ স্নান",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️",
        "deity": {"en": "Lord Vishnu & Shiva", "hi": "भगवान विष्णु व शिव जी", "bn": "ভগবান বিষ্ণু ও শিব"},
        "description": {
            "en": "Observing silence (Mauna Vrata) and sacred holy dipping in the Ganges for inner peace.",
            "hi": "मन के संयम हेतु मौन व्रत धारण एवं त्रिवेणी संगम में अमृत स्नान का सर्वोत्कृष्ट दिन।",
            "bn": "মনঃসংযমের জন্য মৌনব্রত পালন এবং পবিত্র গঙ্গাবারি ও ত্রিবেণী সঙ্গমে মহাস্নান।"
        },
        "muhurta": {"en": "Brahma Muhurta & Dawn Snan (05:00 - 08:00 AM)", "hi": "ब्रह्म मुहूर्त व प्रातःकाल (०५:०० - ०८:००)", "bn": "ব্রাহ্ম মুহূর্ত ও ভোরবেলা (সকাল ০৫:০০ - ০৮:০০)"}
    },

    # --------------------------------------------------------------------------
    # ফাল্গুন মাস (Phalguna)
    # --------------------------------------------------------------------------
    ("Phalguna", "Krishna", 14): {
        "en": "Maha Shivratri (Purnimanta tradition) / Masik Shivratri",
        "hi": "महाशिवरात्रि / मासिक शिवरात्रि व्रत",
        "bn": "মহা শিবরাত্রি ব্রত / মাসিক শিবরাত্রি",
        "category": "hindu",
        "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🔱",
        "deity": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান শিব"},
        "description": {
            "en": "Monthly Shivratri worship of the Shiva Linga at midnight for liberation from sins.",
            "hi": "मनोकामना पूर्ति एवं कष्टों के निवारण हेतु मध्यरात्रि में भगवान शिव का जलाभिषेक।",
            "bn": "মনোবাঞ্ছা পূরণ ও সর্বক্লেশ মুক্তির উদ্দেশ্যে নিশীথ কালে শিবলিঙ্গে জলাভিষেক ও উপবাস।"
        },
        "muhurta": {"en": "Nishita Kaal (Midnight 11:45 PM - 12:40 AM)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि ११:४५ - १२:४०)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি ১১:৪৫ - ১২:৪০)"}
    },
    ("Phalguna", "Shukla", 14): {
        "en": "Holika Dahan / Chhanchar Utsav",
        "hi": "होलिका दहन / कामदहन",
        "bn": "হোলিকা দহন / চাঁচর উৎসব (অগ্নি উৎসব)",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔥",
        "deity": {"en": "Bhakt Prahlada & Lord Narasimha", "hi": "भक्त प्रह्लाद व भगवान नृसिंह", "bn": "ভক্ত প্রহ্লাদ ও ভগবান শ্রীনৃসিংহ"},
        "description": {
            "en": "Burning of Holika symbolizing the triumph of devotion (Prahlada) over evil arrogance.",
            "hi": "अहंकार रूपी होलिका का भस्म होना एवं भक्त प्रह्लाद की रक्षा की स्मृति में पावन अग्नि पूजन।",
            "bn": "অহংকারের প্রতীক অসুরিকা হোলিকার দহন এবং অটল হরিভক্তির জয় উদযাপনে চাঁচর বহ্ন্যুৎসব।"
        },
        "muhurta": {"en": "Pradosh Kaal (Bhadra Free Evening)", "hi": "प्रदोष काल (भद्रा रहित संध्याकाल)", "bn": "প্রদোষ কাল (ভদ্রামুক্ত সন্ধ্যাবেলা)"}
    },
    ("Phalguna", "Shukla", 15): {
        "en": "Dol Jatra / Holi / Sri Gaura Purnima / Lakshmi Jayanti",
        "hi": "होली / डोल पूर्णिमा / गौर पूर्णिमा / लक्ष्मी जयंती",
        "bn": "শ্রী শ্রী দোলযাত্রা / বসন্তোৎসব / শ্রীমন্মহাপ্রভুর শুভ আবির্ভাব / হোলি",
        "category": "hindu",
        "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🎨",
        "deity": {"en": "Radha Krishna, Sri Chaitanya & Lakshmi", "hi": "राधा-कृष्ण, श्री चैतन्य व लक्ष्मी जी", "bn": "রাধাকৃষ্ণ, শ্রীচৈতন্য মহাপ্রভু ও মা লক্ষ্মী"},
        "description": {
            "en": "Festival of colors, Dolotsav of Radha-Krishna, and divine advent of Sri Chaitanya Mahaprabhu.",
            "hi": "रंगोत्सव होली, श्रीराधा-कृष्ण का डोल उत्सव एवं श्री चैतन्य महाप्रभु का पावन प्राकट्योत्सव।",
            "bn": "রাধাকৃষ্ণের প্রেমময় দোল মহোৎসব, রঙের বসন্তোৎসব এবং শ্রী শ্রী গৌরাঙ্গ মহাপ্রভুর শুভ আবির্ভাব।"
        },
        "muhurta": {"en": "Purvahna Dolotsav & Pradosh Gaura Arati", "hi": "पूर्वाह्न डोल उत्सव व संध्याकाल", "bn": "পূর্বাহ্ন দোলোৎসব ও সায়ংকালীন আবির্ভাব আরতি"}
    }
}

# ==============================================================================
# ২. ভারতীয় জাতীয় ছুটির দিন, বিপ্লবী ও স্বাধীনতা সংগ্রামীদের স্মরণীয় দিবস
# ==============================================================================
INDIAN_NATIONAL_HOLIDAYS = {
    # --------------------------------------------------------------------------
    # জানুয়ারি (January)
    # --------------------------------------------------------------------------
    (1, 12): {
        "en": "National Youth Day (Swami Vivekananda Jayanti) & Masterda Surya Sen Martyrdom Day",
        "hi": "राष्ट्रीय युवा दिवस (स्वामी विवेकानंद जयंती) व मास्टरदा सूर्य सेन बलिदान दिवस",
        "bn": "জাতীয় যুব দিবস (স্বামী বিবেকানন্দ জয়ন্তী) ও মাস্টারদা সূর্য সেনের আত্মোৎসর্গ দিবস",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Swami Vivekananda & Surya Sen", "hi": "स्वामी विवेकानंद व मास्टरदा सूर्य सेन", "bn": "স্বামী বিবেকানন্দ ও মাস্টারদা সূর্য সেন"},
        "description": {
            "en": "Birth anniversary of Swami Vivekananda and supreme martyrdom of Chittagong armoury raid hero Masterda Surya Sen.",
            "hi": "युवा शक्ति के प्रेरणास्रोत स्वामी विवेकानंद की जयंती एवं चटगांव शस्त्रागार क्रांति के महानायक सूर्य सेन का बलिदान।",
            "bn": "যুব প্রেরণা স্বামী বিবেকানন্দের জন্মজয়ন্তী এবং চট্টগ্রাম অস্ত্রাগার আক্রমণের মহানায়ক মাস্টারদা সূর্য সেনের ফাঁসি দিবস।"
        },
        "muhurta": {"en": "Morning Commemoration (08:00 - 11:00 AM)", "hi": "प्रातः वंदन सभा (०८:०० - ११:००)", "bn": "প্রাতঃকালীন স্মরণ সভা (সকাল ০৮:০০ - ১১:০০)"}
    },
    (1, 23): {
        "en": "Parakram Diwas (Netaji Subhas Chandra Bose Jayanti)",
        "hi": "पराक्रम दिवस (नेताजी सुभाष चंद्र बोस जयंती)",
        "bn": "পরাক্রম দিবস (নেতাজি সুভাষচন্দ্র বসুর জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय पर्व", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Netaji Subhas Chandra Bose", "hi": "नेताजी सुभाष चंद्र बोस", "bn": "নেতাজি সুভাষচন্দ্র বসু"},
        "description": {
            "en": "Birth anniversary of the supreme commander of the Azad Hind Fauj, Netaji Subhas Chandra Bose.",
            "hi": "आजाद हिंद फौज के सर्वोच्च सेनापति एवं स्वाधीनता संग्राम के महानायक नेताजी का पावन जन्मोत्सव।",
            "bn": "আজাদ হিন্দ ফৌজের সর্বাধিনায়ক ও ভারতের স্বাধীনতার মহানায়ক দেশনায়ক নেতাজির শুভ জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (1, 26): {
        "en": "Republic Day of India",
        "hi": "गणतंत्र दिवस",
        "bn": "ভারতের প্রজাতন্ত্র দিবস",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Holiday", "hi": "राष्ट्रीय पर्व", "bn": "জাতীয় উৎসব"},
        "deity": {"en": "Republic of India & Dr. B.R. Ambedkar", "hi": "भारत गणराज्य व डॉ. आंबेडकर", "bn": "ভারত প্রজাতন্ত্র ও ডঃ বি. আর. আম্বেদকর"},
        "description": {
            "en": "Commemorating the enactment of the Constitution of India in 1950.",
            "hi": "१९५० में भारत के संप्रभु लोकतांत्रिक संविधान के लागू होने का राष्ट्रीय गौरव दिवस।",
            "bn": "১৯৫০ সালের ২৬শে জানুয়ারি ভারতীয় সংবিধান আনুষ্ঠানিকভাবে কার্যকর হওয়ার ঐতিহাসিক জাতীয় দিবস।"
        },
        "muhurta": {"en": "Morning Flag Hoisting (08:00 - 10:30 AM)", "hi": "प्रातः ध्वजारोहण (०८:०० - १०:३०)", "bn": "সকালবেলা জাতীয় পতাকা উত্তোলন (০৮:০০ - ১০:৩০)"}
    },
    (1, 28): {
        "en": "Lala Lajpat Rai Jayanti (Punjab Kesari)",
        "hi": "लाला लाजपत राय जयंती (पंजाब केसरी)",
        "bn": "লালা লাজপত রায় জয়ন্তী (পাঞ্জাব কেশরী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "जयंती पर्व", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Lala Lajpat Rai", "hi": "पंजाब केसरी लाला लाजपत राय", "bn": "পাঞ্জাব কেশরী লালা লাজপত রায়"},
        "description": {
            "en": "Birth anniversary of prominent nationalist leader of the Lal-Bal-Pal trio, Lala Lajpat Rai.",
            "hi": "लाल-बाल-पाल त्रिमूर्ति के प्रमुख स्तंभ एवं महान स्वतंत्रता सेनानी लाला लाजपत राय की जयंती।",
            "bn": "লাল-বাল-পাল ত্রয়ীর অন্যতম পুরোধা ও নির্ভীক স্বাধীনতা সংগ্রামী লালা লাজপত রায়ের জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Morning Remembrance", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (1, 30): {
        "en": "Martyrs' Day (Shaheed Diwas / Mahatma Gandhi Punyatithi)",
        "hi": "शहीद दिवस (महात्मा गांधी पुण्यतिथि)",
        "bn": "শহীদ দিবস (মহাত্মা গান্ধীর প্রয়াণ দিবস)",
        "category": "national", "icon": "🕯️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "জাতীয় শোক ও শ্রদ্ধা দিবস"},
        "deity": {"en": "Mahatma Gandhi & Freedom Martyrs", "hi": "महात्मा गांधी व समस्त अमर शहीद", "bn": "মহাত্মা গান্ধী ও অমর শহীদগণ"},
        "description": {
            "en": "Nationwide 2-minute silence observing the supreme sacrifices of all freedom fighters.",
            "hi": "राष्ट्रपिता महात्मा गांधी की पुण्यतिथि पर देश के समस्त अमर शहीदों की पावन स्मृति में मौन व श्रद्धांजलि।",
            "bn": "মহাত্মা গান্ধীর প্রয়াণ দিবসে দেশের সমস্ত বীর শহীদ ও বিপ্লবীদের প্রতি ২ মিনিটের নীরব শ্রদ্ধাঞ্জলি।"
        },
        "muhurta": {"en": "11:00 AM (2-Minute National Silence)", "hi": "पूर्वाह्न ११:०० (२ मिनट मौन श्रद्धांजलि)", "bn": "সকাল ১১:০০ (২ মিনিট জাতীয় নীরবতা পালন)"}
    },

    # --------------------------------------------------------------------------
    # ফেব্রুয়ারি (February)
    # --------------------------------------------------------------------------
    (2, 13): {
        "en": "National Women's Day (Sarojini Naidu Jayanti)",
        "hi": "राष्ट्रीय महिला दिवस (सरोजिनी नायडू जयंती)",
        "bn": "জাতীয় নারী দিবস (সরোজিনী নাইডু জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Sarojini Naidu (Nightingale of India)", "hi": "भारत कोकिला सरोजिनी नायडू", "bn": "ভারত কোকিলা সরোজিনী নাইডু"},
        "description": {
            "en": "Birth anniversary of the Nightingale of India and iconic freedom fighter Sarojini Naidu.",
            "hi": "भारत कोकिला एवं स्वतंत्रता संग्राम सेनानी सरोजिनी नायडू के जन्मोत्सव पर राष्ट्रीय महिला दिवस।",
            "bn": "ভারত কোকিলা ও স্বাধীনতা সংগ্রামের অগ্রণী নারী নেত্রী সরোজিনী নাইডুর জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (2, 27): {
        "en": "Chandrashekhar Azad Martyrdom Day (Balidan Diwas)",
        "hi": "चंद्रशेखर आजाद बलिदान दिवस",
        "bn": "চন্দ্রশেখর আজাদের আত্মবলিদান দিবস",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Chandrashekhar Azad", "hi": "अमर शहीद चंद्रशेखर आजाद", "bn": "অমর বিপ্লবী চন্দ্রশেখর আজাদ"},
        "description": {
            "en": "Remembering the supreme sacrifice of revolutionary leader Azad at Alfred Park, Prayagraj.",
            "hi": "प्रयागराज के अल्फ्रेड पार्क में मातृभूमि की रक्षा हेतु हंसते-हंसते प्राण न्यौछावर करने वाले आजाद का नमन।",
            "bn": "প্রয়াগরাজের আলফ্রেড পার্কে মাতৃভূমির জন্য আজীবন স্বাধীন থাকার সংকল্প রক্ষা করে আত্মোৎসর্গের দিন।"
        },
        "muhurta": {"en": "Morning Remembrance (09:00 - 11:30 AM)", "hi": "प्रातः स्मरण (०९:०० - ११:३०)", "bn": "প্রাতঃকালীন স্মরণ (সকাল ০৯:০০ - ১১:৩০)"}
    },
    (2, 28): {
        "en": "National Science Day (Raman Effect Discovery)",
        "hi": "राष्ट्रीय विज्ञान दिवस (रमन प्रभाव खोज)",
        "bn": "জাতীয় বিজ্ঞান দিবস (রমন এফেক্ট আবিষ্কার)",
        "category": "national", "icon": "🔬",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Sir C.V. Raman", "hi": "सर सी.वी. रमन", "bn": "নোবেলজয়ী স্যার সি. ভি. রমন"},
        "description": {
            "en": "Marking the discovery of the Raman Effect by Nobel Laureate Sir C.V. Raman in 1928.",
            "hi": "१९२८ में रमन प्रभाव की ऐतिहासिक खोज एवं भारत के वैज्ञानिक गौरव का पावन उत्सव।",
            "bn": "১৯২৮ সালের ২৮শে ফেব্রুয়ারি পদার্থবিজ্ঞানী সি. ভি. রমনের ঐতিহাসিক 'রমন এফেক্ট' আবিষ্কারের স্মরণ।"
        },
        "muhurta": {"en": "All Day Science Sessions", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },

    # --------------------------------------------------------------------------
    # মার্চ (March)
    # --------------------------------------------------------------------------
    (3, 23): {
        "en": "Shaheed Diwas (Bhagat Singh, Rajguru, Sukhdev Martyrdom Day)",
        "hi": "शहीद दिवस (भगत सिंह, राजगुरु व सुखदेव बलिदान दिवस)",
        "bn": "শহীদ দিবস (ভগত সিং, রাজগুরু ও সুখদেবের ফাঁসি দিবস)",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "अमर बलिदान दिवस", "bn": "অমর আত্মবলিদান দিবস"},
        "deity": {"en": "Bhagat Singh, Sukhdev & Rajguru", "hi": "शहीद-ए-आजम भगत सिंह, राजगुरु व सुखदेव", "bn": "শহীদ-ই-আজম ভগত সিং, রাজগুরু ও সুখদেব"},
        "description": {
            "en": "Supreme martyrdom day of young revolutionaries Bhagat Singh, Rajguru, and Sukhdev in Lahore Central Jail.",
            "hi": "लाहौर जेल में मातृभूमि के लिए फांसी के फंदे को चूमने वाले अमर क्रांतिकारियों का पावन स्मरण।",
            "bn": "লাহোর সেন্ট্রাল জেলে দেশের স্বাধীনতার জন্য হাসিমুখে ফাঁসির মঞ্চে ওঠা অমর তিন বীর বিপ্লবীর আত্মত্যাগ।"
        },
        "muhurta": {"en": "Evening Tributes & Candlelight Vigil", "hi": "सायंकाल दीप श्रद्धांजलि", "bn": "সন্ধ্যায় প্রদীপ প্রজ্বলন ও শ্রদ্ধাঞ্জলি"}
    },

    # --------------------------------------------------------------------------
    # এপ্রিল (April)
    # --------------------------------------------------------------------------
    (4, 8): {
        "en": "Mangal Pandey Martyrdom Day",
        "hi": "मंगल पांडे बलिदान दिवस (१८५७ क्रांति)",
        "bn": "মঙ্গল পাণ্ডের ফাঁসি দিবস (১৮৫৭ মহাবিদ্রোহ)",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Shaheed Mangal Pandey", "hi": "अमर शहीद मंगल पांडे", "bn": "প্রথম শহীদ মঙ্গল পাণ্ডে"},
        "description": {
            "en": "Remembering the hero who sparked India's First War of Independence in 1857 at Barrackpore.",
            "hi": "१८५७ के प्रथम स्वाधीनता संग्राम की ज्वाला प्रज्वलित करने वाले बैरकपुर के अमर नायक का स्मरण।",
            "bn": "১৮৫৭ সালে ব্যারাকপুর সেনাছাউনিতে ব্রিটিশদের বিরুদ্ধে প্রথম বিদ্রোহের সূচনা করা বীর শহীদ।"
        },
        "muhurta": {"en": "Morning Remembrance", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (4, 14): {
        "en": "Dr. B.R. Ambedkar Jayanti (Equality Day)",
        "hi": "डॉ. बी.आर. आंबेडकर जयंती (समानता दिवस)",
        "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী (সাম্য দিবস)",
        "category": "national", "icon": "📜",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Babasaheb Dr. B.R. Ambedkar", "hi": "बाबासाहेब डॉ. भीमराव आंबेडकर", "bn": "বাবাসাহেব ডঃ বি. আর. আম্বেদকর"},
        "description": {
            "en": "Birth anniversary of the chief architect of the Indian Constitution and crusader of social equality.",
            "hi": "संविधान निर्माता एवं वंचितों के उत्थान के मसीहा भारत रत्न बाबासाहेब आंबेडकर की जयंती।",
            "bn": "ভারতীয় সংবিধানের প্রধান স্থপতি ও সমাজ সংস্কারক ভারতরত্ন বাবাসাহেব আম্বেদকরের জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (4, 23): {
        "en": "Veer Kunwar Singh Jayanti (Vijay Utsav)",
        "hi": "वीर कुंवर सिंह विजयोत्सव",
        "bn": "বীর কুঁয়ার সিংহ বিজয়োৎসব জয়ন্তী",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Commemorative Day", "hi": "विजयोत्सव", "bn": "বিজয়োৎসব দিবস"},
        "deity": {"en": "Veer Kunwar Singh of Jagdishpur", "hi": "वीर बाबू कुंवर सिंह", "bn": "১৮৫৭-র বীর যোদ্ধা কুঁয়ার সিংহ"},
        "description": {
            "en": "Honouring the octogenarian hero of the 1857 War of Independence from Bihar.",
            "hi": "१८५७ के संग्राम में अदम्य साहस का परिचय देने वाले बिहार जगदीशपुर के वीर योद्धा का उत्सव।",
            "bn": "১৮৫৭ সালের মহাবিদ্রোহে ৮০ বছর বয়সে ব্রিটিশদের পরাস্তকারী বিহারের অদম্য যোদ্ধা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },

    # --------------------------------------------------------------------------
    # মে (May)
    # --------------------------------------------------------------------------
    (5, 9): {
        "en": "Gopal Krishna Gokhale Jayanti",
        "hi": "गोपाल कृष्ण गोखले जयंती",
        "bn": "গোপাল কৃষ্ণ গোখলে জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Gopal Krishna Gokhale", "hi": "गोपाल कृष्ण गोखले", "bn": "গোপাল কৃষ্ণ গোখলে"},
        "description": {
            "en": "Birth anniversary of the revered mentor of Mahatma Gandhi and founder of Servants of India Society.",
            "hi": "सर्वेंट्स ऑफ इंडिया सोसायटी के संस्थापक एवं महात्मा गांधी के राजनीतिक गुरु का जयंती स्मरण।",
            "bn": "সার্ভেন্টস অফ ইন্ডিয়া সোসাইটির প্রতিষ্ঠাতা ও মহাত্মা গান্ধীর রাজনৈতিক গুরু হিসেবে খ্যাত মনীষী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (5, 28): {
        "en": "Veer Savarkar Jayanti",
        "hi": "वीर सावरकर जयंती",
        "bn": "বীর সাভারকার জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "जयंती पर्व", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Vinayak Damodar Savarkar", "hi": "विनायक दामोदर सावरकर", "bn": "বিনায়ক দামোদর সাভারকার"},
        "description": {
            "en": "Birth anniversary of revolutionary freedom fighter and writer Veer Savarkar.",
            "hi": "१८५७ के स्वातंत्र्य समर के प्रखर लेखक एवं कालापानी की यातनाएं सहने वाले क्रांतिवीर का स्मरण।",
            "bn": "সেলুলার জেলের অমানুষিক নির্যাতন সহ্যকারী স্বাধীনতা সংগ্রামী ও ঐতিহাসিক লেখক বীর সাভারকার।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः वंदन", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },

    # --------------------------------------------------------------------------
    # জুন (June)
    # --------------------------------------------------------------------------
    (6, 9): {
        "en": "Bhagwan Birsa Munda Martyrdom Day",
        "hi": "भगवान बिरसा मुंडा बलिदान दिवस",
        "bn": "ভগবান বিরসা মুণ্ডার আত্মবলিদান দিবস",
        "category": "national", "icon": "🏹",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Bhagwan Birsa Munda (Dharti Aaba)", "hi": "धरती आबा भगवान बिरसा मुंडा", "bn": "ধরিত্রী আবা ভগবান বিরসা মুণ্ডা"},
        "description": {
            "en": "Remembering the tribal freedom fighter and folk hero who led the Ulgulan movement against British oppression.",
            "hi": "उलगुलान महाक्रांति के जनक एवं जनजातीय अधिकारों के रक्षक धरती आबा का पावन बलिदान दिवस।",
            "bn": "ব্রিটিশ বিরোধী উলগুলান আন্দোলনের পুরোধা ও আদিবাসী সমাজের মুক্তিদূত বিরসা মুণ্ডার প্রয়াণ তিথি।"
        },
        "muhurta": {"en": "Morning Commemoration", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },
    (6, 11): {
        "en": "Ram Prasad Bismil Jayanti",
        "hi": "पंडित राम प्रसाद बिस्मिल जयंती",
        "bn": "পণ্ডিত রাম প্রসাদ বিসমিল জন্মজয়ন্তী",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Ram Prasad Bismil", "hi": "अमर क्रांतिकारी राम प्रसाद बिस्मिल", "bn": "অমর বিপ্লবী রাম প্রসাদ বিসমিল"},
        "description": {
            "en": "Birth anniversary of revolutionary poet and HRA founder who penned 'Sarfaroshi Ki Tamanna'.",
            "hi": "'सरफरोशी की तमन्ना' के अमर रचयिता एवं काकोरी क्रांति के मुख्य महानायक की पावन जयंती।",
            "bn": "'সরফরোশী কি তামান্না' গানের অমর রচয়িতা ও কাকোরি বিপ্লবের অবিসংবাদিত নেতা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (6, 18): {
        "en": "Rani Lakshmibai Martyrdom Day (Jhansi Ki Rani)",
        "hi": "झांसी की रानी लक्ष्मीबाई बलिदान दिवस",
        "bn": "ঝাঁসির রানি লক্ষ্মীবাঈয়ের আত্মবলিদান দিবস",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Rani Lakshmibai of Jhansi", "hi": "वीरांगना महारानी लक्ष्मीबाई", "bn": "বীরাঙ্গনা রানি লক্ষ্মীবাঈ"},
        "description": {
            "en": "Supreme martyrdom of the fierce warrior Queen of Jhansi on the battlefield of Gwalior in 1858.",
            "hi": "ग्वालियर के युद्ध में 'मैं अपनी झांसी नहीं दूंगी' का सिंहनाद कर वीरगति पाने वाली वीरांगना का नमन।",
            "bn": "গোয়ালিয়রের রণক্ষেত্রে ব্রিটিশদের বিরুদ্ধে অসীম বিক্রমে যুদ্ধ করে রানি লক্ষ্মীবাঈয়ের অমর আত্মত্যাগ।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः वंदन", "bn": "প্রাতঃকালীন বন্দনা"}
    },

    # --------------------------------------------------------------------------
    # জুলাই (July)
    # --------------------------------------------------------------------------
    (7, 4): {
        "en": "Alluri Sitarama Raju Jayanti (Manyam Veerudu)",
        "hi": "अल्लूरी सीताराम राजू जयंती",
        "bn": "আল্লুরি সীতারাম রাজু জন্মজয়ন্তী",
        "category": "national", "icon": "🏹",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Alluri Sitarama Raju", "hi": "मान्यम वीरुडु अल्लूरी सीताराम राजू", "bn": "মান্যম বীরুড়ু আল্লুরি সীতারাম রাজু"},
        "description": {
            "en": "Birth anniversary of the leader of the Rampa Rebellion of 1922 in the Eastern Ghats.",
            "hi": "आंध्र प्रदेश में रम्पा आदिवासी क्रांति के महानायक एवं ब्रिटिश हुकूमत को दहलाने वाले वीर।",
            "bn": "অন্ধ্রপ্রদেশে আদিবাসী রামপা বিদ্রোহের মহানায়ক ও নির্ভীক স্বাধীনতা যোদ্ধা।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (7, 23): {
        "en": "Lokmanya Tilak Jayanti & Chandrashekhar Azad Jayanti",
        "hi": "लोकमान्य बाल गंगाधर तिलक जयंती व चंद्रशेखर आजाद जयंती",
        "bn": "লোকমান্য বাল গঙ্গাধর তিলক জয়ন্তী ও চন্দ্রশেখর আজাদের জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "संयुक्त जयंती पर्व", "bn": "যুগ্ম জন্মজয়ন্তী দিবস"},
        "deity": {"en": "Lokmanya Tilak & Chandrashekhar Azad", "hi": "लोकमान्य तिलक व चंद्रशेखर आजाद", "bn": "লোকমান্য তিলক ও চন্দ্রশেখর আজাদ"},
        "description": {
            "en": "Joint birth anniversary of Lokmanya Tilak ('Swaraj is my birthright') and revolutionary Azad.",
            "hi": "'स्वराज मेरा जन्मसिद्ध अधिकार है' का उद्घोषक तिलक एवं अजेय क्रांतिकारी आजाद की पावन जयंती।",
            "bn": "'স্বরাজ আমার জন্মগত অধিকার' প্রবক্তা লোকমান্য তিলক এবং অমর বিপ্লবী আজাদের যুগ্ম জন্মতিথি।"
        },
        "muhurta": {"en": "Morning Commemoration (08:30 - 11:30 AM)", "hi": "प्रातः स्मरण (०৮:३० - ११:३०)", "bn": "প্রাতঃকালীন স্মরণ সভা (সকাল ০৮:৩০ - ১১:৩০)"}
    },
    (7, 31): {
        "en": "Shaheed Udham Singh Martyrdom Day",
        "hi": "शहीद उधम सिंह बलिदान दिवस",
        "bn": "শহীদ উধম সিং-এর আত্মবলিদান দিবস",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Shaheed Udham Singh (Ram Mohammad Singh Azad)", "hi": "अमर शहीद उधम सिंह", "bn": "অমর বিপ্লবী উধম সিং"},
        "description": {
            "en": "Remembering the patriot who avenged the Jallianwala Bagh massacre by executing Michael O'Dwyer in London.",
            "hi": "जलियांवाला बाग नरसंहार का प्रतिशोध लंदन में जाकर लेने वाले अमर बलिदानी उधम सिंह का स्मरण।",
            "bn": "জালিয়ানওয়ালাবাগ হত্যাকাণ্ডের প্রতিশোধ নিতে লন্ডনে গিয়ে মাইকেল ও'ডায়ারকে নিধনকারী বীর শহীদ।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },

    # --------------------------------------------------------------------------
    # আগস্ট (August)
    # --------------------------------------------------------------------------
    (8, 1): {
        "en": "Lokmanya Bal Gangadhar Tilak Death Anniversary",
        "hi": "लोकमान्य बाल गंगाधर तिलक पुण्यतिथि",
        "bn": "লোকমান্য বাল গঙ্গাধর তিলকের প্রয়াণ দিবস",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "पुण्यतिथि", "bn": "প্রয়াণ দিবস"},
        "deity": {"en": "Lokmanya Bal Gangadhar Tilak", "hi": "लोकमान्य बाल गंगाधर तिलक", "bn": "লোকমান্য বাল গঙ্গাধর তিলক"},
        "description": {
            "en": "Remembering the Father of the Indian Unrest and nationalist leader.",
            "hi": "गणेशोत्सव व शिवाजी उत्सव के माध्यम से राष्ट्रीय चेतना जगाने वाले लोकमान्य की पुण्यतिथि।",
            "bn": "সার্বজনীন গণেশোৎসব ও শিবাজী উৎসবের মাধ্যমে স্বাধীনতা আন্দোলনের জাগরণকারী জননেতা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (8, 11): {
        "en": "Khudiram Bose Martyrdom Day",
        "hi": "अमर शहीद खुदीराम बोस बलिदान दिवस",
        "bn": "অমর বিপ্লবী ক্ষুদিরাম বসুর আত্মবলিদান দিবস",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Shaheed Khudiram Bose", "hi": "अमर शहीद खुदीराम बोस", "bn": "অমর বিপ্লবী ক্ষুদিরাম বসু"},
        "description": {
            "en": "Remembering the youngest revolutionary martyr who went to the gallows at age 18 with a smile in Muzaffarpur.",
            "hi": "मात्र १८ वर्ष की आयु में मुजफ्फरपुर जेल में मुस्कुराते हुए फांसी का फंदा चूमने वाले अमर वीर।",
            "bn": "'একবার বিদায় দে মা ঘুরে আসি' - মাত্র ১৮ বছর বয়সে মুজফফরপুর জেলে ফাঁসির মঞ্চে ওঠা অমর শহীদ।"
        },
        "muhurta": {"en": "Morning Tributes (08:00 - 10:30 AM)", "hi": "प्रातः स्मरण (०८:०० - १०:३०)", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি (সকাল ০৮:০০ - ১০:৩০)"}
    },
    (8, 15): {
        "en": "Independence Day of India",
        "hi": "स्वतंत्रता दिवस",
        "bn": "ভারতের স্বাধীনতা দিবস",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Holiday", "hi": "राष्ट्रीय महापर्व", "bn": "জাতীয় মহোৎসব"},
        "deity": {"en": "Bharat Mata & All Freedom Fighters", "hi": "भारत माता व समस्त अमर बलिदानी", "bn": "ভারত মাতা ও সমস্ত স্বাধীনতা সংগ্রামী"},
        "description": {
            "en": "Celebration of India achieving freedom from British colonial rule on August 15, 1947.",
            "hi": "१५ अगस्त १९४७ को प्राप्त भारत की स्वाधीनता का पावन राष्ट्रीय स्वतंत्रता उत्सव।",
            "bn": "১৯৪৭ সালের ১৫ই আগস্ট পরাধীনতার শৃঙ্খল ভেঙে স্বাধীনতা অর্জনের মহান ও গৌরবময় দিন।"
        },
        "muhurta": {"en": "Morning Flag Hoisting (07:30 - 10:00 AM)", "hi": "प्रातः ध्वजारोहण (०७:३० - १०:००)", "bn": "প্রাতঃকালে জাতীয় পতাকা উত্তোলন (সকাল ০৭:৩০ - ১০:০০)"}
    },
    (8, 29): {
        "en": "National Sports Day (Major Dhyan Chand Jayanti)",
        "hi": "राष्ट्रीय खेल दिवस (मेजर ध्यानचंद जयंती)",
        "bn": "জাতীয় ক্রীড়া দিবস (মেজর ধ্যানচাঁদ জন্মজয়ন্তী)",
        "category": "national", "icon": "🏑",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Major Dhyan Chand (Hockey Wizard)", "hi": "हॉकी के जादूगर मेजर ध्यानचंद", "bn": "হকির জাদুকর মেজর ধ্যানচাঁদ"},
        "description": {
            "en": "Birth anniversary of the legendary Indian hockey wizard Major Dhyan Chand.",
            "hi": "भारत को तीन ओलंपिक स्वर्ण पदक दिलाने वाले हॉकी के महानायक मेजर ध्यानचंद की जयंती।",
            "bn": "ভারতকে অলিম্পিকে সোনা এনে দেওয়া মহান কিংবদন্তি জাদুকর ধ্যানচাঁদের জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Sporting Events", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন ক্রীড়া প্রতিযোগিতা"}
    },

    # --------------------------------------------------------------------------
    # সেপ্টেম্বর (September)
    # --------------------------------------------------------------------------
    (9, 4): {
        "en": "Dadabhai Naoroji Jayanti (Grand Old Man of India)",
        "hi": "दादाभाई नौरोजी जयंती (ग्रैंड ओल्ड मैन ऑफ इंडिया)",
        "bn": "দাদাভাই নওরোজি জন্মজয়ন্তী (ভারতের গ্র্যান্ড ওল্ড ম্যান)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Dadabhai Naoroji", "hi": "दादाभाई नौरोजी", "bn": "দাদাভাই নওরোজি"},
        "description": {
            "en": "Birth anniversary of the pioneer nationalist who exposed the economic 'Drain of Wealth' theory.",
            "hi": "ब्रिटिश शासन द्वारा भारत के आर्थिक दोहन (ड्रेन ऑफ वेल्थ) को उजागर करने वाले महान अर्थशास्त्री।",
            "bn": "ব্রিটিশ শাসনের অর্থনৈতিক শোষণ ফাঁসকারী ব্রিটিশ পার্লামেন্টের প্রথম ভারতীয় সদস্য।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (9, 5): {
        "en": "Teachers' Day (Dr. Sarvepalli Radhakrishnan Jayanti)",
        "hi": "शिक्षक दिवस (डॉ. सर्वपल्ली राधाकृष्णन जयंती)",
        "bn": "শিক্ষক দিবস (ডঃ সর্বপল্লী রাধাকৃষ্ণণ জন্মজয়ন্তী)",
        "category": "national", "icon": "📚",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Dr. Sarvepalli Radhakrishnan & Gurus", "hi": "डॉ. राधाकृष्णन व समस्त गुरुजन", "bn": "ডঃ রাধাকৃষ্ণণ ও শ্রদ্ধেয় শিক্ষকবৃন্দ"},
        "description": {
            "en": "Honouring all educators on the birth anniversary of great philosopher and President Dr. Radhakrishnan.",
            "hi": "महान दार्शनिक व भारत के पूर्व राष्ट्रपति डॉ. राधाकृष्णन के जन्मोत्सव पर गुरु-वंदन दिवस।",
            "bn": "দার্শনিক রাষ্ট্রনায়ক ডঃ সর্বপল্লী রাধাকৃষ্ণণের জন্মজয়ন্তীতে গুরু ও শিক্ষকদের প্রতি শ্রদ্ধা নিবেদন।"
        },
        "muhurta": {"en": "Morning Guru Vandana (08:30 - 11:30 AM)", "hi": "प्रातः गुरु वंदन (०८:३० - ११:३०)", "bn": "প্রাতঃকালীন গুরু বন্দনা (সকাল ০৮:৩০ - ১১:৩০)"}
    },
    (9, 10): {
        "en": "Bagha Jatin Martyrdom Day (Jatindranath Mukherjee)",
        "hi": "बाघा जतिन बलिदान दिवस (यतींद्रनाथ मुखर्जी)",
        "bn": "বাঘা যতীনের আত্মবলিদান দিবস (যতীন্দ্রনাথ মুখোপাধ্যায়)",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Bagha Jatin (Jatindranath Mukherjee)", "hi": "क्रांतिकारी बाघा जतिन", "bn": "অমর বিপ্লবী বাঘা যতীন"},
        "description": {
            "en": "Hero of the Battle of Buribalam (1915), fighting valiantly against British forces in Odisha.",
            "hi": "बालासोर में बूढ़ीबालंग नदी के तट पर ब्रिटिश सेना से आमने-सामने युद्ध लड़ने वाले क्रांतिवीर।",
            "bn": "উড়িষ্যার বুড়িবালামের তীরে ব্রিটিশ বাহিনীর বিরুদ্ধে সম্মুখ সমরে যুদ্ধ করা অকুতোভয় বিপ্লবী।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },
    (9, 13): {
        "en": "Jatin Das Martyrdom Day (63-Day Hunger Strike Hero)",
        "hi": "यतींद्रनाथ दास (जतिन दास) बलिदान दिवस",
        "bn": "বিপ্লবী যতীন দাসের আত্মবলিদান দিবস (৬৩ দিনের অনশন)",
        "category": "national", "icon": "🕯️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Jatindra Nath Das", "hi": "अमर बलिदानी जतिन दास", "bn": "অমর বিপ্লবী যতীন দাস"},
        "description": {
            "en": "Martyrdom after a heroic 63-day hunger strike in Lahore Jail demanding human rights for political prisoners.",
            "hi": "लाहौर जेल में कैदियों के अधिकारों हेतु ६३ दिनों के ऐतिहासिक अनशन के उपरांत प्राण त्यागने वाले वीर।",
            "bn": "লাহোর সেন্ট্রাল জেলে রাজনৈতিক বন্দিদের অধিকারের দাবিতে ঐতিহাসিক ৬৩ দিনের অনশনে আত্মোৎসর্গ।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },
    (9, 14): {
        "en": "Hindi Diwas (Adoption of Hindi as Official Language)",
        "hi": "हिन्दी दिवस (राजभाषा हिंदी स्वीकृति दिवस)",
        "bn": "হিন্দি দিবস (সরকারি ভাষা স্বীকৃতি দিবস)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Matribhasha & Rashtrabhasha Hindi", "hi": "मातृभाषा व राजभाषा हिन्दी", "bn": "মাতৃভাষা ও সরকারি ভাষা হিন্দি"},
        "description": {
            "en": "Commemorating the adoption of Hindi in Devanagari script as the Official Language of the Union in 1949.",
            "hi": "१४ सितंबर १९४९ को संविधान सभा द्वारा देवनागरी लिपि में हिंदी को राजभाषा स्वीकार करने का उत्सव।",
            "bn": "১৯৪৯ সালের ১৪ই সেপ্টেম্বর ভারতীয় সংবিধান সভা কর্তৃক হিন্দিকে সরকারি ভাষার মর্যাদা দেওয়ার দিন।"
        },
        "muhurta": {"en": "All Day Literary Programs", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন সাহিত্য অনুষ্ঠান"}
    },
    (9, 20): {
        "en": "Kanaklata Barua Martyrdom Day (Birbala of Assam)",
        "hi": "कनकलता बरुआ बलिदान दिवस (असम की वीरबाला)",
        "bn": "কনকলতা বড়ুয়ার আত্মবলিদান দিবস (আসামের বীরবালা)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Kanaklata Barua & Mukunda Kakati", "hi": "वीरबाला कनकलता बरुआ", "bn": "বীরবালা কনকলতা বড়ুয়া"},
        "description": {
            "en": "17-year-old martyr shot while hoisting the Tricolour during Quit India Movement at Gohpur, Assam.",
            "hi": "भारत छोड़ो आंदोलन में तिरंगा फहराते हुए मात्र १७ वर्ष की आयु में सीने पर गोली खाने वाली वीरांगना।",
            "bn": "ভারত ছাড়ো আন্দোলনে জাতীয় পতাকা উত্তোলন করতে গিয়ে মাত্র ১৭ বছর বয়সে শহীদ হওয়া অসমীয়া কন্যা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },
    (9, 23): {
        "en": "Pritilata Waddedar Martyrdom Day (Pahartali Heroine)",
        "hi": "प्रीतिलता वाद्देदार बलिदान दिवस",
        "bn": "প্রীতিলতা ওয়াদ্দেদারের আত্মবলিদান দিবস",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Veerangana Pritilata Waddedar", "hi": "वीरांगना प्रीतिलता वाद्देदार", "bn": "অগ্নিযুগের বীরাঙ্গনা প্রীতিলতা ওয়াদ্দেদার"},
        "description": {
            "en": "Led the successful raid on Pahartali European Club (1932) and consumed potassium cyanide to avoid capture.",
            "hi": "पहाड़तली यूरोपीय क्लब पर साहसी आक्रमण का नेतृत्व कर गिरफ्तारी से बचने हेतु विषपान करने वाली वीरांगना।",
            "bn": "পাহাড়তলী ইউরোপিয়ান ক্লাব আক্রমণ সফল করে ব্রিটিশদের হাতে ধরা না দিয়ে সায়ানাইড খেয়ে আত্মাহুতি।"
        },
        "muhurta": {"en": "Morning Remembrance", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (9, 28): {
        "en": "Shaheed Bhagat Singh Jayanti",
        "hi": "शहीद-ए-आजम भगत सिंह जयंती",
        "bn": "শহীদ-ই-আজম ভগত সিং জন্মজয়ন্তী",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Commemorative Day", "hi": "जयंती पर्व", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Shaheed Bhagat Singh", "hi": "शहीद भगत सिंह", "bn": "শহীদ ভগত সিং"},
        "description": {
            "en": "Birth anniversary of the iconic revolutionary martyr who energized India's youth with 'Inquilab Zindabad'.",
            "hi": "'इंकलाब जिंदाबाद' के उद्घोष से स्वाधीनता संग्राम में नवीन ऊर्जा भरने वाले भगत सिंह का जन्मोत्सव।",
            "bn": "'ইনকিলাব জিন্দাবাদ' ধ্বনিতে দেশের যুবসমাজকে উদ্বুদ্ধকারী মহান বিপ্লবী ভগত সিং-এর জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Morning Tributes (08:30 - 11:30 AM)", "hi": "प्रातः स्मरण (०৮:३० - ११:३०)", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি (সকাল ০৮:৩০ - ১১:৩০)"}
    },
    (9, 29): {
        "en": "Matangini Hazra Martyrdom Day (Gandhi Buri of Tamluk)",
        "hi": "मातंगिनी हाजरा बलिदान दिवस (गांधी बूढ़ी)",
        "bn": "মাতঙ্গিনী হাজরার আত্মবলিদান দিবস (গান্ধী বুড়ি)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Matangini Hazra (Gandhi Buri)", "hi": "वीरांगना मातंगिनी हाजरा", "bn": "বীরাঙ্গনা মাতঙ্গিনী হাজরা"},
        "description": {
            "en": "72-year-old patriot shot repeatedly while keeping the National Flag flying during the 1942 Quit India march in Tamluk.",
            "hi": "तमलुक में ७३ वर्ष की आयु में गोलियां खाकर भी तिरंगे को झुकने न देने वाली अदम्य वीरांगना।",
            "bn": "তমলুকে ভারত ছাড়ো আন্দোলনে ব্রিটিশদের বুলেটের মুখে বন্দে মাতরম বলে জাতীয় পতাকা উঁচিয়ে রাখা বীরাঙ্গনা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },

    # --------------------------------------------------------------------------
    # অক্টোবর (October)
    # --------------------------------------------------------------------------
    (10, 2): {
        "en": "Mahatma Gandhi Jayanti & Lal Bahadur Shastri Jayanti",
        "hi": "गांधी जयंती व लाल बहादुर शास्त्री जयंती",
        "bn": "গান্ধী জয়ন্তী ও লাল বাহাদুর শাস্ত্রী জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Holiday", "hi": "राष्ट्रीय महापर्व", "bn": "জাতীয় মহোৎসব"},
        "deity": {"en": "Mahatma Gandhi & Lal Bahadur Shastri", "hi": "महात्मा गांधी व लाल बहादुर शास्त्री", "bn": "মহাত্মা গান্ধী ও লাল বাহাদুর শাস্ত্রী"},
        "description": {
            "en": "Birth anniversaries of Father of the Nation Mahatma Gandhi (Ahimsa) and Prime Minister Shastri ('Jai Jawan Jai Kisan').",
            "hi": "सत्य-अहिंसा के प्रणेता महात्मा गांधी एवं 'जय जवान जय किसान' के उद्घोषक शास्त्री जी की पावन जयंती।",
            "bn": "অহিংসার দূত মহাত্মা গান্ধী এবং 'জয় জওয়ান জয় কিষাণ' স্লোগানের রূপকার লাল বাহাদুর শাস্ত্রীর জন্মতিথি।"
        },
        "muhurta": {"en": "Morning Prayer Assembly (08:00 - 10:30 AM)", "hi": "प्रातः सर्वधर्म प्रार्थना (०८:०० - १०:३०)", "bn": "প্রাতঃকালীন সর্বধর্ম প্রার্থনা সভা (সকাল ০৮:০০ - ১০:৩০)"}
    },
    (10, 22): {
        "en": "Ashfaqulla Khan Jayanti (Kakori Hero)",
        "hi": "अमर क्रांतिकारी अशफाक उल्ला खां जयंती",
        "bn": "অমর বিপ্লবী আশফাকউল্লা খান জন্মজয়ন্তী",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Shaheed Ashfaqulla Khan", "hi": "शहीद अशफाक उल्ला खां", "bn": "শহীদ আশফাকউল্লা খান"},
        "description": {
            "en": "Birth anniversary of prominent HRA revolutionary and key organizer of the Kakori Action.",
            "hi": "काकोरी ट्रेन एक्शन के अमर महानायक एवं गंगा-जमुनी तहजीब के प्रतीक क्रांतिकारी का जन्मोत्सव।",
            "bn": "কাকোরি ট্রেন অভিযানের অমর বিপ্লবী এবং রামপ্রসাদ বিসমিলের অভিন্নহৃদয় বন্ধু আশফাকউল্লা খানের জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Morning Remembrance", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (10, 31): {
        "en": "National Unity Day (Rashtriya Ekta Diwas / Sardar Patel Jayanti)",
        "hi": "राष्ट्रीय एकता दिवस (सरदार वल्लभभाई पटेल जयंती)",
        "bn": "জাতীয় একতা দিবস (সর্দার বল্লভভাই প্যাটেল জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Sardar Vallabhbhai Patel (Iron Man of India)", "hi": "लौह पुरुष सरदार वल्लभभाई पटेल", "bn": "লৌহমানব সর্দার বল্লভভাই প্যাটেল"},
        "description": {
            "en": "Honouring the Iron Man of India for integrating over 560 princely states into one united republic.",
            "hi": "५६० से अधिक रियासतों का विलय कर अखंड भारत का निर्माण करने वाले लौह पुरुष का पावन जन्मोत्सव।",
            "bn": "৫৬০-র বেশি দেশীয় রাজ্যকে এক করে অখণ্ড ভারত গড়ার রূপকার লৌহমানব সর্দার প্যাটেলের জন্মতিথি।"
        },
        "muhurta": {"en": "Morning Unity Run (06:30 - 09:00 AM)", "hi": "प्रातः एकता दौड़ (०६:३० - ०९:००)", "bn": "প্রাতঃকালীন একতা পদযাত্রা (সকাল ০৬:৩০ - ০৯:০০)"}
    },

    # --------------------------------------------------------------------------
    # নভেম্বর (November)
    # --------------------------------------------------------------------------
    (11, 7): {
        "en": "Bipin Chandra Pal Jayanti (Father of Revolutionary Thoughts)",
        "hi": "बिपिन चंद्र पाल जयंती",
        "bn": "বিপিন চন্দ্র পাল জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Bipin Chandra Pal", "hi": "क्रांतिकारी बिपिन चंद्र पाल", "bn": "বিপ্লবী চিন্তার জনক বিপিন চন্দ্র পাল"},
        "description": {
            "en": "Birth anniversary of the fiery orator and one of the main leaders of the Lal-Bal-Pal triumvirate.",
            "hi": "लाल-बाल-पाल त्रिमूर्ति के प्रखर राष्ट्रभक्त व स्वदेशी आंदोलन के प्रमुख नेता की पावन जयंती।",
            "bn": "স্বদেশী আন্দোলনের পুরোধা ব্যক্তিত্ব এবং লাল-বাল-পাল ত্রয়ীর অন্যতম মহান জাতীয়তাবাদী নেতা।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (11, 11): {
        "en": "National Education Day (Maulana Abul Kalam Azad Jayanti)",
        "hi": "राष्ट्रीय शिक्षा दिवस (मौलाना अबुल कलाम आजाद जयंती)",
        "bn": "জাতীয় শিক্ষা দিবস (মৌলানা আবুল কালাম আজাদ জন্মজয়ন্তী)",
        "category": "national", "icon": "📚",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Maulana Abul Kalam Azad", "hi": "मौलाना अबुल कलाम आजाद", "bn": "মৌলানা আবুল কালাম আজাদ"},
        "description": {
            "en": "Birth anniversary of India's first Minister of Education and founder of IITs and UGC.",
            "hi": "स्वतंत्र भारत के प्रथम शिक्षा मंत्री एवं आईआईटी व यूजीसी के संस्थापक का जयंती स्मरण।",
            "bn": "স্বাধীন ভারতের প্রথম শিক্ষামন্ত্রী এবং আইআইটি ও ইউজিসির দূরদর্শী প্রতিষ্ঠাতা।"
        },
        "muhurta": {"en": "All Day Educational Sessions", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন শিক্ষামূলক আলোচনা"}
    },
    (11, 14): {
        "en": "Children's Day (Jawaharlal Nehru Jayanti)",
        "hi": "बाल दिवस (जवाहरलाल नेहरू जयंती)",
        "bn": "শিশু দিবস (পণ্ডিত জওহরলাল নেহেরু জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Pt. Jawaharlal Nehru (Chacha Nehru)", "hi": "पं. जवाहरलाल नेहरू (चाचा नेहरू)", "bn": "পণ্ডিত জওহরলাল নেহরু (চাচা নেহরু)"},
        "description": {
            "en": "Birth anniversary of India's first Prime Minister, dedicated to child welfare and development.",
            "hi": "बच्चों के प्यारे 'चाचा नेहरू' के जन्मोत्सव पर बाल कल्याण ও शिक्षा संवर्धन दिवस।",
            "bn": "স্বাধীন ভারতের প্রথম প্রধানমন্ত্রী পণ্ডিত নেহরুর শিশুদের প্রতি স্নেহের স্মরণে শিশু কল্যাণ দিবস।"
        },
        "muhurta": {"en": "All Day School Celebrations", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন বিদ্যালয়ভিত্তিক উৎসব"}
    },
    (11, 15): {
        "en": "Janjatiya Gaurav Diwas (Bhagwan Birsa Munda Jayanti)",
        "hi": "जनजातीय गौरव दिवस (भगवान बिरसा मुंडा जयंती)",
        "bn": "জনজাতীয় গৌরব দিবস (ভগবান বিরসা মুণ্ডা জন্মজয়ন্তী)",
        "category": "national", "icon": "🏹",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय गौरव दिवस", "bn": "জাতীয় গৌরব দিবস"},
        "deity": {"en": "Bhagwan Birsa Munda", "hi": "भगवान बिरसा मुंडा", "bn": "ভগবান বিরসা মুণ্ডা"},
        "description": {
            "en": "Birth anniversary of Bhagwan Birsa Munda celebrating tribal culture and their contribution to freedom.",
            "hi": "जनजातीय अस्मिता, संस्कृति एवं स्वाधीनता में आदिवासी नायकों के योगदान का राष्ट्रीय गौरव पर्व।",
            "bn": "ভারতের স্বাধীনতা সংগ্রামে আদিবাসী সমাজের অবদান ও ভগবান বিরসা মুণ্ডার শুভ জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Morning Tributes (08:30 - 11:30 AM)", "hi": "प्रातः वंदन (०৮:३० - ११:३०)", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি (সকাল ০৮:৩০ - ১১:৩০)"}
    },
    (11, 19): {
        "en": "Rani Lakshmibai Jayanti (Jhansi Ki Rani)",
        "hi": "झांसी की रानी लक्ष्मीबाई जयंती",
        "bn": "ঝাঁসির রানি লক্ষ্মীবাঈ জন্মজয়ন্তী",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Rani Lakshmibai", "hi": "महारानी लक्ष्मीबाई (छबीली)", "bn": "বীরাঙ্গনা রানি লক্ষ্মীবাঈ"},
        "description": {
            "en": "Birth anniversary of the legendary Queen of Jhansi, an immortal symbol of Indian womanhood and bravery.",
            "hi": "भारतीय नारी के शौर्य, स्वाभिमान व वीरता की अमर प्रतीक वीरांगना लक्ष्मीबाई का जन्मोत्सव।",
            "bn": "ভারতীয় নারীর বীরত্ব, আত্মমর্যাদা ও স্বাধীনতার প্রতীক ঝাঁসির রানি লক্ষ্মীবাঈয়ের জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "Morning Remembrance", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (11, 26): {
        "en": "National Constitution Day (Samvidhan Diwas)",
        "hi": "संविधान दिवस (राष्ट्रीय विधि दिवस)",
        "bn": "জাতীয় সংবিধান দিবস (আইন দিবস)",
        "category": "national", "icon": "📜",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Constitution of India & Dr. Ambedkar", "hi": "भारतीय संविधान व डॉ. आंबेडकर", "bn": "ভারতীয় সংবিধান ও ডঃ আম্বেদকর"},
        "description": {
            "en": "Commemorating the adoption of the Constitution of India by the Constituent Assembly on 26 Nov 1949.",
            "hi": "२६ नवंबर १९४९ को संविधान सभा द्वारा भारत के संविधान को अंगीकृत करने का ऐतिहासिक दिवस।",
            "bn": "১৯৪৯ সালের ২৬শে নভেম্বর গণপরিষদ কর্তৃক আনুষ্ঠানিকভাবে ভারতীয় সংবিধান গ্রহণের পুণ্য দিবস।"
        },
        "muhurta": {"en": "Preamble Reading at 11:00 AM", "hi": "पूर्वाह्न ११:०० (प्रस्तावना पाठ)", "bn": "সকাল ১১:০০ (সংবিধানের প্রস্তাবনা পাঠ)"}
    },

    # --------------------------------------------------------------------------
    # ডিসেম্বর (December)
    # --------------------------------------------------------------------------
    (12, 3): {
        "en": "Dr. Rajendra Prasad Jayanti & Khudiram Bose Jayanti",
        "hi": "डॉ. राजेंद्र प्रसाद जयंती व अमर शहीद खुदीराम बोस जयंती",
        "bn": "ডঃ রাজেন্দ্র প্রসাদ জন্মজয়ন্তী ও অমর বিপ্লবী ক্ষুদিরাম বসু জয়ন্তী",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "Commemorative Day", "hi": "संयुक्त जयंती दिवस", "bn": "যুগ্ম জন্মজয়ন্তী দিবস"},
        "deity": {"en": "Dr. Rajendra Prasad & Khudiram Bose", "hi": "देशरत्न डॉ. राजेंद्र प्रसाद व खुदीराम बोस", "bn": "দেশরত্ন ডঃ রাজেন্দ্র প্রসাদ ও ক্ষুদিরাম বসু"},
        "description": {
            "en": "Birth anniversary of India's first President Dr. Rajendra Prasad and Bengal's young martyr Khudiram Bose.",
            "hi": "भारत के प्रथम राष्ट्रपति देशरत्न डॉ. राजेंद्र प्रसाद एवं क्रांतिकारी खुदीराम बोस का पावन जन्मोत्सव।",
            "bn": "ভারতের প্রথম রাষ্ট্রপতি ডঃ রাজেন্দ্র প্রসাদ এবং মেদিনীপুরের কিশোর বিপ্লবী ক্ষুদিরাম বসুর জন্মতিথি।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন স্মরণ"}
    },
    (12, 11): {
        "en": "Subramania Bharati Jayanti (Mahakavi)",
        "hi": "महाकवि सुब्रह्मण्य भारती जयंती (भारतीय भाषा दिवस)",
        "bn": "মহাকবি সুব্রহ্মণ্যম ভারতী জন্মজয়ন্তী",
        "category": "national", "icon": "📜",
        "type": {"en": "Commemorative Day", "hi": "जयंती दिवस", "bn": "স্মরণীয় দিবস"},
        "deity": {"en": "Mahakavi Subramania Bharati", "hi": "महाकवि सुब्रह्मण्य भारती", "bn": "তামিল মহাকবি সুব্রহ্মণ্যম ভারতী"},
        "description": {
            "en": "Birth anniversary of pioneering Tamil poet and freedom fighter, celebrated as Indian Language Day.",
            "hi": "तमिल राष्ट्रकवि एवं समाज सुधारक भारती की जयंती, जो भारतीय भाषा उत्सव के रूप में मान्य है।",
            "bn": "তামিল জাতীয়তাবাদী কবি ও সমাজ সংস্কারক সুব্রহ্মণ্যম ভারতীর জন্মজয়ন্তী (ভারতীয় ভাষা দিবস)।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন সাহিত্য চর্চা"}
    },
    (12, 19): {
        "en": "Kakori Martyrs' Day (Ram Prasad Bismil & Ashfaqulla Khan Balidan Diwas)",
        "hi": "काकोरी शहीद दिवस (बिस्मिल, अशफाक उल्ला व रोशन सिंह बलिदान दिवस)",
        "bn": "কাকোরি শহীদ দিবস (রাম প্রসাদ বিসমিল ও আশফাকউল্লা খান ফাঁসি দিবস)",
        "category": "national", "icon": "⚔️",
        "type": {"en": "Martyrdom Day", "hi": "अमर बलिदान दिवस", "bn": "আত্মবলিদান দিবস"},
        "deity": {"en": "Bismil, Ashfaqulla & Roshan Singh", "hi": "अमर शहीद बिस्मिल, अशफाक व रोशन सिंह", "bn": "শহীদ বিসমিল, আশফাকউল্লা ও রোশন সিংহ"},
        "description": {
            "en": "Supreme sacrifice of Kakori Train Action revolutionaries who were hanged by the British regime in 1927.",
            "hi": "मातृभूमि की स्वतंत्रता के लिए १९२७ में फांसी के फंदे पर झूलने वाले काकोरी के अमर नायकों का नमन।",
            "bn": "১৯২৭ সালের ১৯শে ডিসেম্বর কাকোরি বিপ্লবের মহান শহীদদের ফাঁসির মঞ্চে অমর আত্মত্যাগ।"
        },
        "muhurta": {"en": "Morning Tributes", "hi": "प्रातः स्मरण", "bn": "প্রাতঃকালীন শ্রদ্ধাঞ্জলি"}
    },
    (12, 25): {
        "en": "Good Governance Day (Atal Bihari Vajpayee & Madan Mohan Malaviya Jayanti)",
        "hi": "सुशासन दिवस (अटल बिहारी वाजपेयी व मदन मोहन मालवीय जयंती)",
        "bn": "সুশাসন দিবস (অটল বিহারী বাজপেয়ী ও মদন মোহন মালব্য জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳",
        "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Atal Bihari Vajpayee & Pt. Malaviya", "hi": "अटल बिहारी वाजपेयी व महामना मालवीय जी", "bn": "অটল বিহারী বাজপেয়ী ও মহামনা মালব্য"},
        "description": {
            "en": "Birth anniversaries of former Prime Minister Atal Bihari Vajpayee and BHU founder Mahamana Malaviya.",
            "hi": "पूर्व प्रधानमंत्री भारत रत्न वाजपेयी जी एवं काशी हिंदू विश्वविद्यालय के संस्थापक मालवीय जी का जन्मोत्सव।",
            "bn": "প্রাক্তন প্রধানমন্ত্রী অটল বিহারী বাজপেয়ী এবং বেনারস হিন্দু বিশ্ববিদ্যালয়ের প্রতিষ্ঠাতা মহামনা মালব্যের জন্মতিথি।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    }
}

# ==============================================================================
# ৩. খ্রিস্টান ও আন্তর্জাতিক ফিক্সড দিবস
# ==============================================================================
FIXED_WORLD_CHRISTIAN_DAYS = {
    (1, 1): {
        "en": "New Year's Day", "hi": "नव वर्ष", "bn": "ইংরেজি নববর্ষ",
        "category": "world", "icon": "🌍", "type": {"en": "Global Celebration", "hi": "अंतर्राष्ट्रीय पर्व", "bn": "আন্তর্জাতিক উৎসব"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {"en": "Welcoming the Gregorian New Year with joy, peace, and new resolutions.", "hi": "नवीन आशाओं, संकल्पों एवं हर्षोल्लास के साथ नव वर्ष का स्वागत।", "bn": "নতুন আশা, সংকল্প ও আনন্দ-উচ্ছ্বাসের সাথে ইংরেজি নববর্ষ বরণ।"},
        "muhurta": {"en": "All Day Celebration", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিনব্যাপী উৎসব"}
    },
    (3, 8): {
        "en": "International Women's Day", "hi": "अंतर्राष्ट्रीय महिला दिवस", "bn": "আন্তর্জাতিক নারী দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {"en": "Honouring women's social, economic, cultural, and political achievements worldwide.", "hi": "नारी शक्ति के अधिकारों, समानता ও उपलब्धियों के सम्मान का पावन दिवस।", "bn": "নারীর অধিকার, মর্যাদা ও সমাজে তাদের গৌরবময় অবদানের স্বীকৃতি উদযাপনের দিন।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (4, 22): {
        "en": "Earth Day", "hi": "पृथ्वी दिवस", "bn": "বিশ্ব বসুন্ধরা দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "पर्यावरण दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Mother Earth", "hi": "धरती माता", "bn": "ধরিত্রী মাতা"},
        "description": {"en": "Demonstrating support for environmental protection and conservation of our planet.", "hi": "प्रकृति के संरक्षण, वृक्षारोपण एवं धरती माता के प्रति कृतज्ञता समर्पण का दिन।", "bn": "পরিবেশ সুরক্ষা, বৃক্ষরোপণ ও ধরিত্রী মাতাকে রক্ষার অঙ্গীকার গ্রহণের দিবস।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (5, 1): {
        "en": "International Workers' Day / May Day", "hi": "अंतर्राष्ट्रीय मजदूर दिवस", "bn": "আন্তর্জাতিক শ্রমিক দিবস / মে দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "श्रमिक दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Labor & Workers", "hi": "श्रमिक वर्ग", "bn": "শ্রমজীবী মানুষ"},
        "description": {"en": "Celebrating the historic struggles and triumphs of working-class laborers.", "hi": "समाज निर्माण में अमूल्य योगदान देने वाले श्रमजीवियों व कामगारों का सम्मान दिवस।", "bn": "বিশ্বের শ্রমজীবী ও মেহনতী মানুষের অধিকার আদায়ের ঐতিহাসিক সংকল্প দিবস।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (6, 5): {
        "en": "World Environment Day", "hi": "विश्व पर्यावरण दिवस", "bn": "বিশ্ব পরিবেশ দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "पर्यावरण दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Nature", "hi": "प्रकृति", "bn": "প্রকৃতি মাতা"},
        "description": {"en": "Promoting worldwide awareness and action for the protection of our environment.", "hi": "प्रकृति, नदियाँ एवं जंगलों को प्रदूषण मुक्त रखने हेतु जन-जागरूकता का दिवस।", "bn": "দূষণমুক্ত সবুজ পৃথিবী গড়ে তোলার লক্ষ্যে বিশ্বব্যাপী পরিবেশ সচেতনতার দিন।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (6, 21): {
        "en": "International Yoga Day", "hi": "अंतर्राष्ट्रीय योग दिवस", "bn": "আন্তর্জাতিক যোগ দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "योग दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Yoga & Wellness", "hi": "योग व स्वास्थ्य", "bn": "যোগ ও সুস্বাস্থ্য"},
        "description": {"en": "Promoting the physical, mental, and spiritual benefits of ancient Indian yoga practice.", "hi": "शारीरिक, मानसिक एवं आध्यात्मिक आरोग्यता हेतु प्राचीन भारतीय योग का वैश्विक दिवस।", "bn": "দেহ, মন ও আত্মার সুস্থতার জন্য প্রাচীন ভারতীয় যোগবিদ্যার আন্তর্জাতিক উদযাপন।"},
        "muhurta": {"en": "Morning Yoga Session (06:00 - 08:30 AM)", "hi": "प्रातः योगाभ्यास (०६:०० - ०८:३०)", "bn": "প্রাতঃকালীন যোগাভ্যাস (সকাল ০৬:০০ - ০৮:৩০)"}
    },
    (10, 16): {
        "en": "World Food Day", "hi": "विश्व खाद्य दिवस", "bn": "বিশ্ব খাদ্য দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "खाद्य दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {"en": "Marking the creation of the Food and Agriculture Organization to eliminate global hunger.", "hi": "वैश्विक भुखमरी उन्मूलन एवं अन्न के सम्मान हेतु विश्व खाद्य सुरक्षा दिवस।", "bn": "বিশ্ব ক্ষুধা মুক্তি ও খাদ্য নিরাপত্তার বার্তা ছড়িয়ে দেওয়ার আন্তর্জাতিক দিবস।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (12, 24): {
        "en": "Christmas Eve", "hi": "क्रिसमस ईव", "bn": "ক্রিসমাস ইভ",
        "category": "christian", "icon": "✝️", "type": {"en": "Christian Festival", "hi": "ईसाई पर्व", "bn": "খ্রিস্টীয় উৎসব"},
        "deity": {"en": "Lord Jesus Christ", "hi": "प्रभु यीशु मसीह", "bn": "প্রভু যীশু খ্রীষ্ট"},
        "description": {"en": "Evening preceding the Nativity of Jesus, observed with candlelight vigil and carols.", "hi": "प्रभु यीशु के जन्म की पूर्व संध्या पर गिरजाघरों में मोमबत्ती व कैरोल प्रार्थना।", "bn": "প্রভু যীশুর জন্মতিথির পূর্বসন্ধ্যায় গির্জায় মোমবাতি প্রজ্বলন ও মধ্যরাত্রির প্রার্থনা।"},
        "muhurta": {"en": "Midnight Mass (11:30 PM - 12:30 AM)", "hi": "मध्यरात्रि प्रार्थना (११:३० - १२:३०)", "bn": "মধ্যরাত্রিকালীন বিশেষ প্রার্থনা (১১:৩০ - ১২:৩০)"}
    },
    (12, 25): {
        "en": "Christmas / Merry Christmas", "hi": "क्रिसमस / बड़ा दिन", "bn": "শুভ বড়দিন (ক্রিসমাস)",
        "category": "christian", "icon": "✝️", "type": {"en": "Christian Festival", "hi": "ईसाई पर्व", "bn": "খ্রিস্টীয় উৎসব"},
        "deity": {"en": "Lord Jesus Christ", "hi": "प्रभु यीशु मसीह", "bn": "প্রভু যীশু খ্রীষ্ট"},
        "description": {"en": "Celebration of the birth of Jesus Christ, sharing love, gifts, and peace.", "hi": "प्रेम, शांति एवं करुणा के संदेशवाहक प्रभु यीशु मसीह का पावन जन्मोत्सव।", "bn": "প্রেম, ক্ষমা ও মানবতার পথপ্রদর্শক প্রভু যীশু খ্রীষ্টের শুভ জন্মোৎসব।"},
        "muhurta": {"en": "Morning Church Mass (08:30 - 11:00 AM)", "hi": "प्रातः चर्च प्रार्थना (०८:३० - ११:००)", "bn": "প্রাতঃকালীন বিশেষ প্রার্থনা সভা (সকাল ০৮:৩০ - ১১:০০)"}
    },
    (12, 31): {
        "en": "New Year's Eve", "hi": "नव वर्ष की पूर्वसंध्या", "bn": "বছরের শেষ দিন",
        "category": "world", "icon": "🌍", "type": {"en": "Global Celebration", "hi": "अंतर्राष्ट्रीय पर्व", "bn": "আন্তর্জাতিক উৎসব"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {"en": "Bidding farewell to the departing year and counting down to welcome the new year.", "hi": "बीते वर्ष को विदाई देकर मध्यरात्रि में नवीन वर्ष का स्वागत करने का उत्सव।", "bn": "অতিক্রান্ত বছরকে বিদায় জানিয়ে মধ্যরাতে নতুন বছরকে বরণ করে নেওয়ার আনন্দক্ষণ।"},
        "muhurta": {"en": "Midnight Countdown (11:59 PM)", "hi": "मध्यरात्रि स्वागत (११:५९)", "bn": "মধ্যরাত্রি বর্ষবরণ কাউন্টডাউন"}
    }
}

# ==============================================================================
# ৪. পরিবর্তনশীল মুসলিম, খ্রিস্টান ও বিশেষ আঞ্চলিক পূজা
# ==============================================================================
VARIABLE_RELIGIOUS_DAYS = {
    # --- 2026 ---
    (2026, 3, 20): {
        "en": "Eid-ul-Fitr (Ramadan Eid)", "hi": "ईद-उल-फ़ित्र", "bn": "পবিত্র ঈদুল ফিতর",
        "category": "muslim", "icon": "☪️", "type": {"en": "Islamic Festival", "hi": "इस्लामी महापर्व", "bn": "ইসলামিক উৎসব"},
        "deity": {"en": "Allah", "hi": "अल्लाह", "bn": "আল্লাহ তায়ালা"},
        "description": {"en": "Festival marking the end of the sacred month of Ramadan fasting.", "hi": "रमजान के पवित्र माह के उपवासों (रोज़े) की पूर्णता पर खुशी ও भाईचारे का महापर्व।", "bn": "পবিত্র মাহে রমজানের মাসব্যাপী সিয়াম সাধনার শেষে আনন্দ ও ভাতৃত্বের মহাপর্ব।"},
        "muhurta": {"en": "Morning Eid Namaz (07:30 - 09:30 AM)", "hi": "प्रातः ईद नमाज़ (०७:३० - ०९:३०)", "bn": "সকালের ঈদের জামাত (০৭:৩০ - ০৯:৩০)"}
    },
    (2026, 4, 3): {
        "en": "Good Friday", "hi": "गुड फ्राइडे", "bn": "পবিত্র গুড ফ্রাইডে",
        "category": "christian", "icon": "✝️", "type": {"en": "Christian Observance", "hi": "ईसाई पर्व", "bn": "খ্রিস্টীয় উৎসব"},
        "deity": {"en": "Lord Jesus Christ", "hi": "प्रभु यीशु मसीह", "bn": "প্রভু যীশু খ্রীষ্ট"},
        "description": {"en": "Solemn commemoration of the crucifixion and supreme sacrifice of Jesus Christ on Calvary.", "hi": "मानवता के पापों के निवारण हेतु प्रभु यीशु के क्रूस बलिदान का शोक व प्रार्थना दिवस।", "bn": "মানবজাতির মুক্তির জন্য ক্রুশবিদ্ধ প্রভু যীশুর আত্মত্যাগের গম্ভীর প্রার্থনা দিবস।"},
        "muhurta": {"en": "Afternoon Service (01:30 - 03:30 PM)", "hi": "दोपहर प्रार्थना (०१:३० - ०३:३०)", "bn": "দুপুরের বিশেষ প্রার্থনা (০১:৩০ - ০৩:৩০)"}
    },
    (2026, 4, 5): {
        "en": "Easter Sunday", "hi": "ईस्टर संडे", "bn": "ইস্টার সানডে",
        "category": "christian", "icon": "✝️", "type": {"en": "Christian Festival", "hi": "ईसाई महापर्व", "bn": "খ্রিস্টীয় উৎসব"},
        "deity": {"en": "Lord Jesus Christ", "hi": "प्रभु यीशु मसीह", "bn": "প্রভু যীশু খ্রীষ্ট"},
        "description": {"en": "Joyous celebration of the resurrection of Jesus Christ from the dead on the third day.", "hi": "मृत्यु पर विजय प्राप्त कर प्रभु यीशु के पुनरुत्थान का पावन विजय पर्व।", "bn": "মৃত্যুকে জয় করে প্রভু যীশু খ্রীষ্টের পুনরুত্থানের পরম আনন্দময় বিজয়ের দিন।"},
        "muhurta": {"en": "Sunrise Easter Service (05:30 - 08:30 AM)", "hi": "सूर्योदय ईस्टर प्रार्थना (०५:३० - ०८:३०)", "bn": "সূর্যোদয় বিশেষ প্রার্থনা (ভোর ০৫:৩০ - ০৮:৩০)"}
    },
    (2026, 5, 27): {
        "en": "Eid-ul-Adha / Bakrid", "hi": "ईद-उल-अज़हा / बकरीद", "bn": "পবিত্র ঈদুল আযহা (বকরি ঈদ)",
        "category": "muslim", "icon": "☪️", "type": {"en": "Islamic Festival", "hi": "इस्लामी महापर्व", "bn": "ইসলামিক উৎসব"},
        "deity": {"en": "Allah", "hi": "अल्लाह", "bn": "আল্লাহ তায়ালা"},
        "description": {"en": "Commemorating Prophet Ibrahim's supreme willingness to sacrifice for devotion to God.", "hi": "हजरत इब्राहिम के अद्वितीय समर्पण एवं ईश-भक्ति की स्मृति में कुर्बानी का महापर्व।", "bn": "হযরত ইব্রাহীম (আঃ)-এর মহান ত্যাগের স্মরণে আত্মোৎসর্গের কুরবানি ঈদ।"},
        "muhurta": {"en": "Morning Bakrid Namaz (07:00 - 09:30 AM)", "hi": "प्रातः बकरीद नमाज़ (०७:०० - ०९:३०)", "bn": "ভোরের ঈদের নামাজ ও কুরবানি (০৭:০০ - ০৯:৩০)"}
    },
    (2026, 6, 26): {
        "en": "Muharram / Ashura", "hi": "मोहर्रम / आशूरा", "bn": "পবিত্র মহরম",
        "category": "muslim", "icon": "☪️", "type": {"en": "Islamic Observance", "hi": "शोक दिवस", "bn": "ইসলামিক দিবস"},
        "deity": {"en": "Imam Hussain", "hi": "इमाम हुसैन", "bn": "হযরত ইমাম হুসাইন (রাঃ)"},
        "description": {"en": "Mourning the martyrdom of Imam Hussain and his companions at the Battle of Karbala.", "hi": "कर्बला के मैदान में सत्य व न्याय के लिए हजरत इमाम हुसैन की शहादत का शोक दिवस।", "bn": "কারবালার প্রান্তরে সত্য ও ন্যায়ের পক্ষে হযরত ইমাম হুসাইনের শাহাদাতের শোক দিবস।"},
        "muhurta": {"en": "Day of Fast & Mourning", "hi": "रोज़ा व मातम काल", "bn": "রোজা ও শোক দিবস"}
    },
    (2026, 7, 21): {
        "en": "Deodhwani Festival Begins (Kamakhya / Assam)", "hi": "देवध्वनि महोत्सव प्रारंभ (कामाख्या / असम)", "bn": "দেওধ্বনি উৎসব আরম্ভ (কামাখ্যা / আসাম)",
        "category": "hindu", "icon": "🔱", "type": {"en": "Regional Festival", "hi": "क्षेत्रीय पर्व", "bn": "আঞ্চলিক উৎসব"},
        "deity": {"en": "Maa Kamakhya & Devi Manasa", "hi": "माँ कामाख्या व मनसा देवी", "bn": "মা কামাখ্যা ও মা মনসা দেবী"},
        "description": {"en": "Sacred shamanic trance-dance festival celebrated at the Kamakhya Temple in Assam.", "hi": "असम के कामाख्या शक्तिपीठ में देवधनी नृत्य व देवी मनसा की तांत्रिक आराधना।", "bn": "আসামের কামাখ্যা ধামে দেবী মনসা ও পদ্মার উদ্দেশ্যে দেবনর্তকদের বিশেষ দেওধ্বনি নৃত্য।"},
        "muhurta": {"en": "Purvahna Kaal (08:00 - 11:30 AM)", "hi": "पूर्वाह्न काल (०८:०० - ११:३०)", "bn": "পূর্বাহ্ন কাল (সকাল ০৮:০০ - ১১:৩০)"}
    },
    (2026, 8, 17): {
        "en": "Main Manasa Puja (Singha Sankranti)", "hi": "मुख्य मनसा पूजा (सिंह संक्रांति)", "bn": "প্রধান শ্রী শ্রী মনসা পূজা (সিংহ সংক্রান্তি)",
        "category": "hindu", "icon": "🐍", "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "deity": {"en": "Maa Manasa", "hi": "माँ मनसा देवी", "bn": "মা মনসা দেবী"},
        "description": {"en": "Grand annual worship of Goddess Manasa across Bengal and Assam on Singha Sankranti.",
        "hi": "सिंह संक्रांति पर बंगाल व असम में विष निवारक माँ मनसा की प्रधान वार्षिक महापूजा।",
        "bn": "সিংহ সংক্রান্তির পুণ্যলগ্নে সর্পভয়নাশিনী মা মনসার বার্ষিক মহোৎসব ও পূজা সমাপন।"},
        "muhurta": {"en": "Purvahna & Madhyahna Kaal", "hi": "पूर्वाह्न व मध्याह्न काल", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন কাল"}
    },
    (2026, 8, 26): {
        "en": "Milad-un-Nabi (Mawlid)", "hi": "ईद-ए-मिलाद", "bn": "পবিত্র ঈদে মিলাদুন্নবী (সাঃ)",
        "category": "muslim", "icon": "☪️", "type": {"en": "Islamic Festival", "hi": "इस्लामी महापर्व", "bn": "ইসলামিক উৎসব"},
        "deity": {"en": "Prophet Muhammad (PBUH)", "hi": "पैगंबर मुहम्मद (स.अ.व.)", "bn": "মহানবী হযরত মুহাম্মদ (সাঃ)"},
        "description": {"en": "Observing the blessed birth anniversary of the Islamic Prophet Muhammad.", "hi": "इस्लाम के अंतिम संदेशवाहक पैगंबर हजरत मुहम्मद के पावन जन्मोत्सव पर दुआ व तकरीर।", "bn": "মানবতার দিশারী আখেরি নবী হযরত মুহাম্মদ (সাঃ)-এর শুভ জন্ম ও ওফাত দিবস।"},
        "muhurta": {"en": "All Day Blessings", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিনব্যাপী মিলাদ মাহফিল"}
    },
    (2026, 11, 16): {
        "en": "Kartik Puja (Kartik Sankranti)", "hi": "कार्तिक पूजा (कार्तिक संक्रांति)", "bn": "শ্রী শ্রী কার্তিক পূজা (কার্তিক সংক্রান্তি)",
        "category": "hindu", "icon": "🦚", "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "deity": {"en": "Lord Kartikeya", "hi": "भगवान कार्तिकेय", "bn": "দেব সেনাপতি কার্তিক"},
        "description": {"en": "Worship of commander-in-chief Lord Kartikeya on Kartik Sankranti for beauty, courage, and offspring.",
        "hi": "कार्तिक संक्रांति पर सुयोग्य संतान व साहस प्राप्ति हेतु देवसेनापति कार्तिकेय का पूजन।",
        "bn": "কার্তিক সংক্রান্তির রাতে রূপবান সন্তান ও বীর্যবত্তার কামনায় দেব সেনাপতি কার্তিকের আরাধনা।"},
        "muhurta": {"en": "Pradosh Kaal (Evening 05:15 - 08:30 PM)", "hi": "प्रदोष काल (संध्या ०५:१५ - ०८:३०)", "bn": "প্রদোষ কাল (সন্ধ্যা ০৫:১৫ - ০৮:৩০)"}
    }
}

def get_language_key(lang: str = "en") -> str:
    value = str(lang or "en").lower().strip()
    if value.startswith("bn") or "বাংলা" in value:
        return "bn"
    if value.startswith("hi") or "हि" in value:
        return "hi"
    return "en"

def normalize_sankranti_name(sankranti_name: Optional[str]) -> str:
    return str(sankranti_name or "").strip().lower()

def append_festival_once(festivals: List[Dict[str, Any]], festival: Dict[str, Any]) -> None:
    festival_name = festival.get("name", "")
    for existing in festivals:
        if existing.get("name") == festival_name:
            return
    festivals.append(festival)

def resolve_field(obj: Any, l_key: str) -> str:
    if isinstance(obj, dict):
        return obj.get(l_key, obj.get("en", ""))
    return str(obj or "")

# ==============================================================================
# MAIN FESTIVAL EXTRACTOR
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
    l_key = get_language_key(lang)
    lunar_month = str(lunar_month or "").strip()
    paksha = str(paksha or "").strip()

    try:
        tithi_num = int(tithi_num)
    except (TypeError, ValueError):
        tithi_num = 0

    # 1. তিথিভিত্তিক সনাতন উৎসব (HINDU_FESTIVAL_DATABASE)
    h_key = (lunar_month, paksha, tithi_num)
    if h_key in HINDU_FESTIVAL_DATABASE:
        item = HINDU_FESTIVAL_DATABASE[h_key]
        append_festival_once(
            festivals,
            {
                "name": item.get(l_key, item.get("en", "")),
                "category": item.get("category", "hindu"),
                "type": resolve_field(item.get("type"), l_key),
                "icon": item.get("icon", "🕉️"),
                "deity": resolve_field(item.get("deity"), l_key),
                "description": resolve_field(item.get("description"), l_key),
                "muhurta": resolve_field(item.get("muhurta"), l_key)
            }
        )

    # 2. সর্বভারতীয় একাদশী ব্রত (Ekadashi Vrata)
    if tithi_num == 11:
        ekadashi_name = {"en": "Ekadashi Vrata / Fast", "hi": "एकादशी व्रत", "bn": "একাদশী ব্রত ও উপবাস"}
        ekadashi_deity = {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"}
        ekadashi_desc = {
            "en": "Sacred fasting day dedicated to Lord Vishnu to cleanse sins and attain spiritual devotion.",
            "hi": "समस्त पापों के नाश एवं भगवान विष्णु की कृपा प्राप्ति हेतु पावन निर्जला/फलाहार व्रत।",
            "bn": "ভগবান শ্রীহরি বিষ্ণুর প্রীত্যর্থে পাপক্ষয় ও আধ্যাত্মিক কল্যাণ কামনায় পরম পবিত্র উপবাস ব্রত।"
        }
        ekadashi_muhurta = {"en": "Brahma Muhurta & Morning Fast", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃকালীন সঙ্কল্প"}
        append_festival_once(
            festivals,
            {
                "name": ekadashi_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🕉️",
                "deity": ekadashi_deity[l_key],
                "description": ekadashi_desc[l_key],
                "muhurta": ekadashi_muhurta[l_key]
            }
        )

    # 3. প্রদোষ ব্রত (Pradosh Vrata)
    elif tithi_num == 13:
        pradosh_name = {"en": "Pradosh Vrata", "hi": "प्रदोष व्रत", "bn": "প্রদোষ ব্রত"}
        pradosh_deity = {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান দেবাদিদেব মহাদেব"}
        pradosh_desc = {
            "en": "Twilight worship of Lord Shiva to attain peace, health, and freedom from distress.",
            "hi": "संध्याकाल (प्रदोष काल) में भगवान शिव की आराधना से सुख, आरोग्य एवं संकट मुक्ति।",
            "bn": "সন্ধ্যাবেলায় দেবাদিদেব মহাদেবের আরাধনা করে সর্বসংকট মুক্তি ও মানসিক শান্তি লাভের ব্রত।"
        }
        pradosh_muhurta = {"en": "Pradosh Kaal Muhurta (Evening 05:40 - 08:00 PM)", "hi": "प्रदोष काल मुहूर्त (संध्या ०५:४० - ०८:००)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যা ০৫:৪০ - ০৮:০০)"}
        append_festival_once(
            festivals,
            {
                "name": pradosh_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🔱",
                "deity": pradosh_deity[l_key],
                "description": pradosh_desc[l_key],
                "muhurta": pradosh_muhurta[l_key]
            }
        )

    # 4. সত্যনারায়ণ পূজা (Purnima Vrata)
    elif tithi_num == 15 and paksha == "Shukla":
        purnima_name = {"en": "Purnima Vrata / Sri Satyanarayan Puja", "hi": "पूर्णिमा व्रत / श्री सत्यनारायण पूजा", "bn": "পূর্ণিমা ব্রত / শ্রী সত্যনারায়ণ পূজা"}
        purnima_deity = {"en": "Lord Sri Satyanarayan (Vishnu)", "hi": "भगवान श्री सत्यनारायण", "bn": "শ্রী সত্যনারায়ণ নারায়ণ"}
        purnima_desc = {
            "en": "Offering Panchamrit, Shinni bhog, and Katha to Lord Satyanarayan on full moon.",
            "hi": "श्री सत्यनारायण भगवान का पंचामृत भोग, कथा श्रवण एवं पूर्णिमा चंद्र दर्शन।",
            "bn": "শ্রীশ্রী সত্যনারায়ণ দেবের পঞ্চামৃত সিন্নি ভোগ, মাহাত্ম্য কথা শ্রবণ ও পূর্ণিমা উপবাস।"
        }
        purnima_muhurta = {"en": "Pradosh Kaal (Evening Katha 05:45 - 08:15 PM)", "hi": "प्रदोष काल (संध्या कथा ०५:४५ - ०८:१५)", "bn": "প্রদোষ কাল (সন্ধ্যায় কথা শ্রবণ ০৫:৪৫ - ০৮:১৫)"}
        append_festival_once(
            festivals,
            {
                "name": purnima_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🌕",
                "deity": purnima_deity[l_key],
                "description": purnima_desc[l_key],
                "muhurta": purnima_muhurta[l_key]
            }
        )

    # 5. সৌর সংক্রান্তি ও নির্দিষ্ট পূজা (Solar Festivals)
    m_d = (current_date.month, current_date.day)
    s_name = normalize_sankranti_name(sankranti_name)

    if m_d == (4, 14):
        nil_names = {"en": "Nil Puja / Charak Puja (Chaitra Sankranti)", "hi": "नील पूजा / चरक पूजा (चैत्र संक्रांति)", "bn": "শ্রী শ্রী নীল পূজা / চড়ক পূজা (চৈত্র সংক্রান্তি)"}
        nil_deity = {"en": "Lord Shiva & Maa Nilavati", "hi": "भगवान शिव व माँ लीलावती", "bn": "দেবাদিদেব শিব ও নীলবতী মাতা"}
        nil_desc = {
            "en": "Worship of Lord Shiva and Maa Nilavati on the last day of the Bengali solar year.",
            "hi": "वर्ष के अंतिम दिन संक्रांति पर भगवान शिव एवं माँ नीलावती की कठिन तपस्या व चरक पूजन।",
            "bn": "চৈত্র সংক্রান্তিতে সন্তানের মঙ্গল কামনায় নীলবতী দেবী ও শিবের উপবাস এবং চড়কের বহ্নিপূজা।"
        }
        nil_muhurta = {"en": "Pradosh Kaal (Evening 05:45 - 08:00 PM)", "hi": "प्रदोष काल", "bn": "প্রদোষ কাল (সন্ধ্যাবেলা)"}
        append_festival_once(festivals, {"name": nil_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key], "icon": "🔱", "deity": nil_deity[l_key], "description": nil_desc[l_key], "muhurta": nil_muhurta[l_key]})

    elif m_d == (4, 15) or ("mesha" in s_name or "aries" in s_name):
        mesha_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / पोइला बैशाख", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি (শুভ নববর্ষ)"}
        mesha_deity = {"en": "Surya Deva & Ganesha", "hi": "सूर्य देव व गणेश जी", "bn": "ভগবান সূর্য দেব ও শ্রী গণেশ"}
        mesha_desc = {
            "en": "Solar New Year marking Sun's entry into Aries, opening new business ledgers (Hal Khata).",
            "hi": "सूर्य का मेष राशि में प्रवेश, सौर नववर्षारंभ एवं नए व्यापारिक बहीखातों का पूजन।",
            "bn": "মেষ রাশিতে সূর্যের শুভ প্রবেশ, বাংলা সৌর নববর্ষ উদযাপন ও ব্যবসায়িক শুভ হালখাতা পূজা।"
        }
        mesha_muhurta = {"en": "Purvahna Kaal (Morning Puja 07:00 - 11:30 AM)", "hi": "पूर्वाह्न काल (प्रातः ०७:०० - ११:३०)", "bn": "পূর্বাহ্ন কাল (সকালবেলা ০৭:০০ - ১১:৩০)"}
        append_festival_once(festivals, {"name": mesha_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key], "icon": "🌾", "deity": mesha_deity[l_key], "description": mesha_desc[l_key], "muhurta": mesha_muhurta[l_key]})

    elif m_d == (1, 14) or ("makar" in s_name or "capricorn" in s_name):
        makar_names = {"en": "Makar Sankranti / Pongal / Poush Parbon", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি / পৌষ পার্বণ ও গঙ্গাসাগর স্নান"}
        makar_deity = {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"}
        makar_desc = {
            "en": "Sun transits into Capricorn (Makara) marking the auspicious Uttarayana, observed with Gangasagar snan and sesame charity.",
            "hi": "सूर्य का मकर राशि में प्रवेश, उत्तरायण आरंभ एवं गंगासागर महास्नान व तिल-गुड़ दान का महापर्व।",
            "bn": "সূর্যের মকর রাশিতে উত্তরায়ণ গমন, গঙ্গাসাগর তীর্থে পুণ্যস্নান ও নতুন শস্যের পিঠেপুলির পৌষ পার্বণ।"
        }
        makar_muhurta = {"en": "Makara Sankranti Punya Kaal (07:15 AM - 05:45 PM)", "hi": "मकर संक्रांति पुण्य काल (प्रातः ०७:१५ - ०५:४५)", "bn": "মকর সংক্রান্তি পুণ্যকাল স্নান ও দান (সকাল ০৭:১৫ - বিকাল ০৫:৪৫)"}
        append_festival_once(festivals, {"name": makar_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key], "icon": "☀️", "deity": makar_deity[l_key], "description": makar_desc[l_key], "muhurta": makar_muhurta[l_key]})

    elif m_d == (9, 17) or ("kanya" in s_name or "virgo" in s_name):
        kanya_names = {"en": "Kanya Sankranti / Vishwakarma Puja", "hi": "कन्या संक्रांति / विश्वकर्मा पूजा", "bn": "কন্যা সংক্রান্তি / শ্রী শ্রী বিশ্বকর্মা পূজা"}
        kanya_deity = {"en": "Lord Vishwakarma", "hi": "भगवान विश्वकर्मा", "bn": "দেবশিল্পী শ্রী শ্রী বিশ্বকর্মা"}
        kanya_desc = {
            "en": "Worship of the divine celestial architect and craftsman, Lord Vishwakarma, in factories and workshops.",
            "hi": "दिव्य वास्तुकार भगवान विश्वकर्मा का यंत्रों, कारखानों व शिल्प संस्थानों में विधिपूर्वक पूजन।",
            "bn": "দেবশিল্পী বিশ্বকর্মার চরণে শিল্প, কলকারখানা ও যন্ত্রপাতির সমৃদ্ধির কামনায় বিশেষ অর্ঘ্য নিবেদন।"
        }
        kanya_muhurta = {"en": "Purvahna & Abhijit Muhurta (07:00 AM - 12:30 PM)", "hi": "पूर्वाह्न व अभिजित मुहूर्त (०७:०० - १२:३०)", "bn": "পূর্বাহ্ন ও অভিজিৎ মুহূর্ত (সকাল ০৭:০০ - দুপুর ১২:৩০)"}
        append_festival_once(festivals, {"name": kanya_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key], "icon": "⚙️", "deity": kanya_deity[l_key], "description": kanya_desc[l_key], "muhurta": kanya_muhurta[l_key]})

    # 6. ভারতীয় জাতীয় দিবস (National Holidays)
    if m_d in INDIAN_NATIONAL_HOLIDAYS:
        nat = INDIAN_NATIONAL_HOLIDAYS[m_d]
        append_festival_once(
            festivals,
            {
                "name": nat[l_key],
                "category": nat.get("category", "national"),
                "type": resolve_field(nat.get("type"), l_key),
                "icon": nat.get("icon", "🇮🇳"),
                "deity": resolve_field(nat.get("deity"), l_key),
                "description": resolve_field(nat.get("description"), l_key),
                "muhurta": resolve_field(nat.get("muhurta"), l_key)
            }
        )

    # 7. আন্তর্জাতিক দিবস (Fixed World Days)
    if m_d in FIXED_WORLD_CHRISTIAN_DAYS:
        world_day = FIXED_WORLD_CHRISTIAN_DAYS[m_d]
        append_festival_once(
            festivals,
            {
                "name": world_day[l_key],
                "category": world_day.get("category", "world"),
                "type": resolve_field(world_day.get("type"), l_key),
                "icon": world_day.get("icon", "🌍"),
                "deity": resolve_field(world_day.get("deity"), l_key),
                "description": resolve_field(world_day.get("description"), l_key),
                "muhurta": resolve_field(world_day.get("muhurta"), l_key)
            }
        )

    # 8. পরিবর্তনশীল দিবস (Variable Religious Days)
    full_date_key = (current_date.year, current_date.month, current_date.day)
    if full_date_key in VARIABLE_RELIGIOUS_DAYS:
        rel = VARIABLE_RELIGIOUS_DAYS[full_date_key]
        append_festival_once(
            festivals,
            {
                "name": rel[l_key],
                "category": rel.get("category", "hindu" if "hindu" in rel.get("category", "") else "religious"),
                "type": resolve_field(rel.get("type"), l_key),
                "icon": rel.get("icon", "🕉️"),
                "deity": resolve_field(rel.get("deity"), l_key),
                "description": resolve_field(rel.get("description"), l_key),
                "muhurta": resolve_field(rel.get("muhurta"), l_key)
            }
        )

    return festivals
