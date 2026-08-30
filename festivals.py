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
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Maa Shailaputri", "hi": "माँ दुर्गा व माँ शैलपुत्री", "bn": "মা দুর্গা ও দেবী শৈলপুত্রী"},
        "description": {
            "en": "Sacred beginning of Chaitra Vasantik Navratri with Ghatasthapana and invocation of Maa Durga.",
            "hi": "घटस्थापना व माँ शैलपुत्री आराधना के साथ चैत्र वासंतिक नवरात्रि का पावन शुभारंभ।",
            "bn": "ঘটস্থাপন ও মা দুর্গার বোধন পূজার মাধ্যমে চৈত্র বাসন্তী নবরাত্রির শুভ সূচনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Morning Muhurta", "hi": "घटस्थापना व प्रातः मुहूर्त", "bn": "ঘটস্থাপন ও প্রাতঃকাল মুহূর্ত"}
    },
    ("Chaitra", "Shukla", 2): {
        "en": "Sindhara Dooj / Brahmacharini Puja",
        "hi": "सिंधारा दूज / माँ ब्रह्मचारिणी पूजा",
        "bn": "সিন্ধারা দুজ / দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Brahmacharini", "hi": "माँ ब्रह्मचारिणी", "bn": "দেবী ব্রহ্মচারিণী"},
        "description": {
            "en": "Worship of Maa Brahmacharini for penance, wisdom, and spiritual restraint on the 2nd day of Navratri.",
            "hi": "तप, त्याग, वैराग्य एवं संयम की वृद्धि हेतु नवरात्रि के दूसरे दिन माँ ब्रह्मचारिणी का पूजन।",
            "bn": "তপস্যা, ত্যাগ ও সংযম বৃদ্ধির উদ্দেশ্যে নবরাত্রির দ্বিতীয় দিনে দেবী ব্রহ্মচারিণীর বিশেষ পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Chaitra", "Shukla", 3): {
        "en": "Gangaur / Matsya Jayanti / Chandraghanta Puja",
        "hi": "गणगौर पूजा / मत्स्य जयंती / माँ चंद्रघंटा पूजा",
        "bn": "গণগৌর পূজা / ভগবান মৎস্য জয়ন্তী / দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐟", "deity": {"en": "Lord Matsya & Maa Gauri", "hi": "भगवान मत्स्य व माँ गौरी", "bn": "ভগবান মৎস্য ও দেবী গৌরী"},
        "description": {
            "en": "Celebration of marital harmony via Gangaur Gauri worship and invocation of Lord Vishnu's fish incarnation (Matsya).",
            "hi": "अखंड सौभाग्य प्राप्ति हेतु गणगौर गौरी पूजन एवं भगवान विष्णु के प्रथम मत्स्य अवतार का जन्मोत्सव।",
            "bn": "অখণ্ড দাম্পত্য সৌভাগ্যে দেবী গৌরী পূজা এবং শ্রীহরি বিষ্ণুর প্রথম মৎস্য অবতারের আবির্ভাব মহোৎসব।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal Muhurta", "hi": "प्रदोष काल मुहूर्त", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যাবেলা)"}
    },
    ("Chaitra", "Shukla", 5): {
        "en": "Lakshmi Panchami / Sri Panchami (Chaitra)",
        "hi": "लक्ष्मी पंचमी / श्री पंचमी",
        "bn": "শ্রী শ্রী লক্ষ্মী পঞ্চমী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪷", "deity": {"en": "Maa Lakshmi", "hi": "माँ महालक्ष्मी", "bn": "মা মহালক্ষ্মী"},
        "description": {
            "en": "Sacred fasting and offerings dedicated to Goddess Lakshmi to attract prosperity, wisdom, and wealth.",
            "hi": "धन-धान्य, ऐश्वर्य एवं सौभाग्य की प्राप्ति हेतु चैत्र शुक्ल पंचमी पर माँ लक्ष्मी की विशेष आराधना।",
            "bn": "ধনধান্য ও সৌভাগ্য বৃদ্ধির কামনায় চৈত্র মাসের শুক্ল পঞ্চমীতে দেবী লক্ষ্মীর চরণে বিশেষ পূজা ও উপবাস।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल (संध्याकाल)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যাবেলা)"}
    },
    ("Chaitra", "Shukla", 8): {
        "en": "Basanti Maha Ashtami / Annapurna Puja / Mahagauri Puja",
        "hi": "माँ अन्नपूर्णा पूजा / बासंती महाष्टमी / महागौरी पूजा",
        "bn": "শ্রী শ্রী অন্নপূর্ণা পূজা / বাসন্তী মহাষ্টমী ও কুমারী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Annapurna & Mahagauri", "hi": "माँ अन्नपूर्णा व महागौरी", "bn": "মা অন্নপূর্ণা ও দেবী মহাগৌরী"},
        "description": {
            "en": "Worship of Maa Annapurna for food and abundance, alongside Basanti Maha Ashtami Kumari Puja.",
            "hi": "धन-धान्य अधिष्ठात्री माँ अन्नपूर्णा एवं बासंती महाष्टमी पर कन्या (कुमारी) पूजन।",
            "bn": "অন্নদাত্রী মা অন্নপূর্ণার বিশেষ আরাধনা এবং বাসন্তী মহাষ্টমীতে পবিত্র কুমারী পূজা।"
        },
        "muhurta_type": "sandhi",
        "muhurta_label": {"en": "Sandhi Puja Muhurta (48 mins)", "hi": "संधि पूजा मुहूर्त (४८ मिनट)", "bn": "সন্ধিপূজা মুহূর্ত (৪৮ মিনিট)"}
    },
    ("Chaitra", "Shukla", 9): {
        "en": "Sri Rama Navami / Siddhidatri Puja",
        "hi": "श्री राम नवमी / माँ सिद्धिदात्री पूजा",
        "bn": "শ্রী শ্রী রাম নবমী মহাপর্ব / বাসন্তী নবমী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🏹", "deity": {"en": "Lord Sri Rama & Maa Siddhidatri", "hi": "भगवान श्रीराम व माँ सिद्धिदात्री", "bn": "ভগবান শ্রীরামচন্দ্র ও দেবী সিদ্ধিদাত্রী"},
        "description": {
            "en": "Divine appearance day of Maryada Purushottam Lord Sri Rama at noon in Ayodhya.",
            "hi": "अयोध्या में मर्यादा पुरुषोत्तम भगवान श्रीराम का पावन प्राकट्य दिवस व जन्मोत्सव।",
            "bn": "অযোধ্যাধামে পরম পুরুষোত্তম ভগবান শ্রীরামচন্দ্রের শুভ আবির্ভাব ও জন্মজয়ন্তী।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত (শ্রীরাম আবির্ভাব)"}
    },
    ("Chaitra", "Shukla", 15): {
        "en": "Hanuman Jayanti / Chaitra Purnima (Satyanarayan Puja)",
        "hi": "हनुमान जयंती / चैत्र पूर्णिमा (सत्यनारायण व्रत)",
        "bn": "শ্রী শ্রী হনুমান জয়ন্তী / চৈত্র পূর্ণিমা (শ্রী সত্যনারায়ণ পূজা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🚩", "deity": {"en": "Lord Hanuman & Sri Satyanarayan", "hi": "श्री हनुमान जी व श्री सत्यनारायण", "bn": "শ্রী হনুমানজী ও শ্রী সত্যনারায়ণ"},
        "description": {
            "en": "Celebration of the birth of Lord Hanuman, the epitome of devotion and strength, along with Chaitra Satyanarayan Puja.",
            "hi": "भक्ति व शक्ति के प्रतीक पवनपुत्र श्री हनुमान जी का जन्मोत्सव एवं पूर्णिमा सत्यनारायण पूजन।",
            "bn": "পরম ভক্ত ও শক্তির প্রতীক শ্রী হনুমানজীর জন্মজয়ন্তী এবং চৈত্র পূর্ণিমার সত্যনারায়ণ পূজা।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Morning Worship", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃকাল"}
    },

    # --------------------------------------------------------------------------
    # বৈশাখ মাস (Vaisakha)
    # --------------------------------------------------------------------------
    ("Vaisakha", "Shukla", 3): {
        "en": "Akshaya Tritiya / Parashurama Jayanti / Treta Yugadi",
        "hi": "अक्षय तृतीया / परशुराम जयंती / त्रेता युगादि",
        "bn": "অক্ষয় তৃতীয়া মহাপর্ব / পরশুরাম জয়ন্তী / ত্রেতা যুগাদী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪙", "deity": {"en": "Lord Vishnu & Maa Lakshmi", "hi": "भगवान विष्णु व माँ लक्ष्मी", "bn": "ভগবান বিষ্ণু ও মা লক্ষ্মী"},
        "description": {
            "en": "Highly auspicious day where merits of charity and new beginnings never diminish.",
            "hi": "दान, जप, स्वर्ण क्रय एवं शुभ कार्यों के लिए अक्षय पुण्य फलदायी पावन दिवस।",
            "bn": "দান, জপ, গৃহপ্রবেশ ও শুভ কাজের জন্য অক্ষয় পুণ্যদায়ী পরম পবিত্র মহাপর্ব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Abhijit & Purvahna Muhurta", "hi": "अभिजित व पूर्वाह्न मुहूर्त", "bn": "অভিজিৎ ও পূর্বাহ্ন মুহূর্ত"}
    },
    ("Vaisakha", "Shukla", 5): {
        "en": "Adi Shankaracharya Jayanti / Surdas Jayanti",
        "hi": "आदि शंकराचार्य जयंती / सूरदास जयंती",
        "bn": "আদি শঙ্করাচার্য জয়ন্তী / ভক্ত সুরদাস জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "जयंती पर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Jagadguru Adi Shankaracharya", "hi": "जगद्गुरु आदि शंकराचार्य", "bn": "জগদ্গুরু আদি শঙ্করাচার্য"},
        "description": {
            "en": "Advent of Jagadguru Adi Shankaracharya, who revived Sanatana Dharma and Advaita philosophy.",
            "hi": "अद्वैत वेदांत के प्रणेता एवं सनातन धर्म के पुनरुद्धारक जगद्गुरु आदि शंकराचार्य का पावन प्राकट्य दिवस।",
            "bn": "অদ্বৈত বেদান্তের প্রবক্তা ও সনাতন ধর্মের রক্ষাকর্তা জগদ্গুরু আদি শঙ্করাচার্যের আবির্ভাব তিথি।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত"}
    },
    ("Vaisakha", "Shukla", 7): {
        "en": "Ganga Saptami / Jahnu Saptami",
        "hi": "गंगा सप्तमी / जाह्नू सप्तमी (गंगा अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা সপ্তমী / জাহ্নু সপ্তমী (গঙ্গা জন্মজয়ন্তী)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌊", "deity": {"en": "Maa Ganga", "hi": "माँ गंगा", "bn": "মা গঙ্গা"},
        "description": {
            "en": "Commemoration of the day Sage Jahnu released sacred River Ganga from his ear as Jahnavi.",
            "hi": "महर्षि जाह्नू द्वारा माँ गंगा को अपनी जंघा/कर्ण से पुनः मुक्त करने पर जाह्नवी प्राकट्य उत्सव।",
            "bn": "মহর্ষি জাহ্নুর কর্ণ থেকে দেবী গঙ্গার পুনরায় মুক্তির মাধ্যমে ‘জাহ্নবী’ রূপে আবির্ভাবের শুভ তিথি।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Mahasnan Muhurta", "hi": "मध्याह्न महास्नान मुहूर्त", "bn": "মধ্যাহ্ন মহাস্নান মুহূর্ত"}
    },
    ("Vaisakha", "Shukla", 9): {
        "en": "Sita Navami / Janaki Jayanti",
        "hi": "सीता नवमी / जानकी जयंती",
        "bn": "শ্রী সীতা নবমী / জানকী জন্মজয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Sita", "hi": "माँ जानकी सीता", "bn": "মা জানকী সীতা"},
        "description": {
            "en": "Appearance day of Maa Sita, discovered by King Janaka while plowing the sacred field.",
            "hi": "महाराज जनक द्वारा हल जोतते समय भूमि से प्रकट हुईं जगज्जननी माँ सीता का पावन प्राकट्य दिवस।",
            "bn": "মহারাজ জনক কর্তৃক যজ্ঞভূমি কর্ষণকালে ভূগর্ভ থেকে জগৎজননী মা সীতার পরম আবির্ভাব তিথি।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত"}
    },
    ("Vaisakha", "Shukla", 14): {
        "en": "Sri Narasimha Jayanti / Narasimha Chaturdashi",
        "hi": "श्री नृसिंह जयंती / नृसिंह चतुर्दशी व्रत",
        "bn": "শ্রী শ্রীনৃসিংহ চতুর্দশী / নৃসিংহ জয়ন্তী ব্রত",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🦁", "deity": {"en": "Lord Narasimha", "hi": "भगवान नृसिंह देव", "bn": "ভগবান শ্রীনৃসিংহ দেব"},
        "description": {
            "en": "Lord Vishnu assumed the half-lion incarnation at dusk to protect Bhakta Prahlada and destroy Hiranyakashipu.",
            "hi": "भक्त प्रह्लाद की रक्षा एवं हिरण्यकशिपु के संहार हेतु गोधूलि वेला में भगवान नृसिंह का प्राकट्य।",
            "bn": "ভক্ত প্রহ্লাদকে রক্ষা ও হিরণ্যকশিপু নিধনে গোধূলি লগ্নে স্তম্ভ বিদীর্ণ করে শ্রীনৃসিংহদেবের প্রকাশ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal / Sandhya Muhurta (Sunset)", "hi": "सायंकाल / संध्या मुहूर्त (सूर्यास्त)", "bn": "সায়ংকাল / সন্ধ্যা মুহূর্ত (সূর্যাস্ত)"}
    },
    ("Vaisakha", "Shukla", 15): {
        "en": "Buddha Purnima / Kurma Jayanti / Vaisakhi Snan",
        "hi": "बुद्ध पूर्णिमा / कूर्म जयंती / वैशाखी स्नान",
        "bn": "বুদ্ধ পূর্ণিমা / বৈশাখী পূর্ণিমা / ভগবান কূর্ম জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☸️", "deity": {"en": "Gautama Buddha & Lord Kurma", "hi": "गौतम बुद्ध व भगवान कूर्म", "bn": "গৌতম বুদ্ধ ও ভগবান কূর্ম"},
        "description": {
            "en": "Triple celebration of Buddha's birth, enlightenment, and parinirvana, alongside Lord Kurma's advent.",
            "hi": "भगवान बुद्ध का जन्म, ज्ञान प्राप्ति व महापरिनिर्वाण दिवस तथा समुद्र मंथन हेतु कूर्म अवतार दिवस।",
            "bn": "ভগবান বুদ্ধের ত্রি-স্মৃতিবিজড়িত পুণ্যতিথি এবং সমুদ্র মন্থন সহায়তাকারী কূর্ম অবতারের আবির্ভাব।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Pradosh Kaal", "hi": "ब्रह्म मुहूर्त व प्रदोष काल", "bn": "ব্রাহ্ম মুহূর্ত ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # জ্যৈষ্ঠ মাস (Jyeshtha)
    # --------------------------------------------------------------------------
    ("Jyeshtha", "Krishna", 15): {
        "en": "Vat Savitri Vrat / Shani Jayanti / Phalaharini Kali Puja",
        "hi": "वट सावित्री व्रत / शनि जयंती / फलहारिणी काली पूजा",
        "bn": "বট সাবিত্রী ব্রত / শ্রী শনি জয়ন্তী / ফলহারিণী কালীপূজা",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌳", "deity": {"en": "Shani Deva, Savitri & Maa Kali", "hi": "शनि देव, माता सावित्री व माँ काली", "bn": "শ্রী শনি দেব, সতী সাবিত্রী ও মা কালী"},
        "description": {
            "en": "Fast for marital longevity, Shani Deva's birth observance, and Phalaharini Kali Puja at night.",
            "hi": "अखंड सौभाग्य हेतु वट वृक्ष पूजन, शनि देव जयंती व मध्यरात्रि फलहारिणी काली पूजा।",
            "bn": "অখণ্ড সৌভাগ্যের জন্য বটবৃক্ষ পূজা, শনিদেবের আবির্ভাব তিথি ও ফলহারিণী কালীপূজা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal (Kali Puja) & Purvahna (Vat)", "hi": "निशीथ काल (काली पूजा) व पूर्वाह्न (वट)", "bn": "নিশীথ কাল (কালীপূজা) ও পূর্বাহ্ন (বট পূজা)"}
    },
    ("Jyeshtha", "Shukla", 6): {
        "en": "Aranya Sasthi / Jamai Sasthi Vrat",
        "hi": "अरण्य षष्ठी / जमाई षष्ठी व्रत",
        "bn": "অরণ্য ষষ্ঠী / শ্রী শ্রী জামাই ষষ্ঠী ব্রত",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🌿", "deity": {"en": "Maa Sasthi", "hi": "माँ षष्ठी", "bn": "মা ষষ্ঠী দেবী"},
        "description": {
            "en": "Traditional festival invoking Maa Sasthi's blessings for offspring and welcoming sons-in-law.",
            "hi": "संतान की दीर्घायु व कल्याण हेतु माँ षष्ठी का पूजन एवं जामाता सत्कार पर्व।",
            "bn": "সন্তানের মঙ্গল কামনায় মা ষষ্ঠীর আশীর্বাদ গ্রহণ ও জামাতাকে বরণ করার মধুর সামাজিক মহাপর্ব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Jyeshtha", "Shukla", 10): {
        "en": "Ganga Dussehra (Descent of Ganga)",
        "hi": "गंगा दशहरा (माँ गंगा का पृथ्वी पर अवतरण)",
        "bn": "শ্রী শ্রী গঙ্গা দশহরা মহোৎসব (মর্ত্যে গঙ্গা অবতরণ)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌊", "deity": {"en": "Maa Ganga", "hi": "माँ गंगा", "bn": "মা গঙ্গা"},
        "description": {
            "en": "Celebration of the day sacred River Ganga descended to Earth through Bhagiratha's penance.",
            "hi": "महाराज भगीरथ के कठोर तप से माँ गंगा के स्वर्ग से मर्तलोक पर पावन अवतरण का महापर्व।",
            "bn": "রাজর্ষি ভগীরথের কঠোর তপস্যায় সন্তুষ্ট হয়ে পতিতপাবনী মা গঙ্গার মর্ত্যে অবতরণ মহোৎসব।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Hasta Nakshatra & Madhyahna Snan", "hi": "हस्त नक्षत्र व मध्याह्न स्नान काल", "bn": "হস্তা নক্ষত্র ও মধ্যাহ্ন স্নান সময়"}
    },
    ("Jyeshtha", "Shukla", 11): {
        "en": "Nirjala Ekadashi / Bhim Ekadashi",
        "hi": "निर्जला एकादशी (भीमसेन एकादशी)",
        "bn": "নির্জলা একাদশী ব্রত (ভীম একাদশী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "महाव्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "The most rigorous Ekadashi fast observed without food and water to attain the merits of all 24 Ekadashis.",
            "hi": "जल की एक बूँद भी ग्रहण किए बिना समस्त २४ एकादशियों का पुण्य फल देने वाला महाव्रत।",
            "bn": "জলস্পর্শ না করে ২৪টি একাদশীর সমতুল্য পুণ্যফলদায়ী সর্বশ্রেষ্ঠ ও পরম পবিত্র নির্জলা ব্রত।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Morning Fast", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃ পূজা"}
    },
    ("Jyeshtha", "Shukla", 15): {
        "en": "Snan Yatra (Lord Jagannath) / Vat Purnima",
        "hi": "देवस्नान पूर्णिमा / वट पूर्णिमा",
        "bn": "শ্রী জগন্নাথদেবের স্নানযাত্রা / দেবস্নান পূর্ণিমা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Lord Jagannath", "hi": "भगवान श्री जगन्नाथ", "bn": "ভগবান শ্রী জগন্নাথদেব"},
        "description": {
            "en": "Auspicious bathing ceremony of Lord Jagannath with 108 pots of herbal water on His appearance day.",
            "hi": "भगवान जगन्नाथ, बलभद्र व सुभद्रा का १०८ सुवासित कलशों से दिव्य स्नान एवं गजानन वेश दर्शन।",
            "bn": "১০৮টি সুগন্ধি তীর্থ বারি দ্বারা শ্রীজগন্নাথ, বলভদ্র ও সুভদ্রার মহাজলাভিষেক ও গজানন বেশ দর্শন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Jyeshtha Purnima Snan Muhurta", "hi": "पूर्णिमा महास्नान मुहूर्त", "bn": "পূর্ণিমা দেবস্নান মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # আষাঢ় মাস (Ashadha)
    # --------------------------------------------------------------------------
    ("Ashadha", "Shukla", 1): {
        "en": "Ashadha Gupt Navratri Begins / Varahi Puja",
        "hi": "आषाढ़ गुप्त नवरात्रि प्रारंभ / वाराही देवी पूजा",
        "bn": "আষাঢ় গুপ্ত নবরাত্রি আরম্ভ / দেবী বারাহী ও দশমহাবিদ্যা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "साधना पर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Das Mahavidya & Maa Varahi", "hi": "दस महाविद्या व माँ वाराही", "bn": "দশমহাবিদ্যা ও দেবী বারাহী"},
        "description": {
            "en": "Nine nights of esoteric Shakta sadhana invoking the Das Mahavidyas and Matrikas.",
            "hi": "दस महाविद्याओं एवं तांत्रिक साधनाओं की गुप्त सिद्धि हेतु पावन नौ दिवसीय अनुष्ठान।",
            "bn": "দশমহাবিদ্যা ও তন্ত্রসাধনার সিদ্ধিলাভের জন্য ৯ দিনব্যাপী পবিত্র আষাঢ় গুপ্ত নবরাত্রি আরম্ভ।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Abhijit Muhurta", "hi": "घटस्थापना व अभिजित मुहूर्त", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত"}
    },
    ("Ashadha", "Shukla", 2): {
        "en": "Jagannath Ratha Yatra Mahotsav",
        "hi": "श्री जगन्नाथ रथ यात्रा महोत्सव",
        "bn": "শ্রী শ্রী জগন্নাথদেবের রথযাত্রা মহোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🚩", "deity": {"en": "Lord Jagannath, Balabhadra & Subhadra", "hi": "भगवान जगन्नाथ, बलभद्र व सुभद्रा", "bn": "ভগবান জগন্নাথ, বলভদ্র ও দেবী সুভদ্রা"},
        "description": {
            "en": "Grand chariot procession of Lord Jagannath, Balabhadra, and Subhadra to the Gundicha Temple.",
            "hi": "भगवान जगन्नाथ, भाई बलभद्र व बहन सुभद्रा का दिव्य रथों पर गुंडिचा मंदिर प्रस्थान।",
            "bn": "শ্রী শ্রী জগন্নাথদেব, বলভদ্র ও দেবী সুভদ্রার রথে চড়ে গুণ্ডিচা মাসির বাড়ি গমনাগমন মহোৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ratha Pratistha & Yatra Muhurta", "hi": "रथ प्रतिष्ठा व यात्रा मुहूर्त", "bn": "রথ প্রতিষ্ঠা ও রথযাত্রা শুভ লগ্ন"}
    },
    ("Ashadha", "Shukla", 7): {
        "en": "Bipodtarini Vrat & Puja (Sasthi/Saptami)",
        "hi": "विपत्तारीणी व्रत व पूजा",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত ও পূজা",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Maa Bipodtarini Durga", "hi": "माँ विपत्तारीणी दुर्गा", "bn": "মা বিপদতারিণী দুর্গা"},
        "description": {
            "en": "Fasting and worship of Maa Durga with 13 offerings to dispel all worldly perils.",
            "hi": "परिवार को समस्त संकटों व विपदाओं से मुक्त रखने हेतु १३ प्रकार के फल-उपचार से माँ का पूजन।",
            "bn": "পরিবারকে সর্ববিপদ থেকে মুক্ত রাখতে ১৩ প্রকার ফল ও লাল ডোর সহযোগে দেবী বিপদতারিণীর ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna & Madhyahna Kaal", "hi": "पूर्वाह्न व मध्याह्न काल", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ব্রত সময়"}
    },
    ("Ashadha", "Shukla", 8): {
        "en": "Bipodtarini Vrat (Shukla Ashtami)",
        "hi": "विपत्तारीणी व्रत (अष्टमी)",
        "bn": "শ্রী শ্রী বিপদতারিণী ব্রত (অষ্টমী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Maa Bipodtarini Durga", "hi": "माँ विपत्तारीणी दुर्गा", "bn": "মা বিপদতারিণী দুর্গা"},
        "description": {
            "en": "Saturday/Tuesday Shukla Ashtami worship of Maa Bipodtarini for protection.",
            "hi": "शनिवार/मंगलवार युक्त आषाढ़ शुक्ल अष्टमी पर माँ विपत्तारीणी की संकटमोचनी पूजा।",
            "bn": "শনিবার/মঙ্গলবার যুক্ত আষাঢ় শুক্ল অষ্টমীতে বিপদহারিণী দেবীর পরম নিষ্ঠাসহ পূজা ও ব্রতপালন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna & Madhyahna Kaal", "hi": "पूर्वाह्न व मध्याह्न काल", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ব্রত সময়"}
    },
    ("Ashadha", "Shukla", 10): {
        "en": "Ulto Rath / Bahuda Yatra",
        "hi": "उल्टा रथ / बहुड़ा यात्रा",
        "bn": "উল্টোরথ যাত্রা মহোৎসব (বাহুড়া যাত্রা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🚩", "deity": {"en": "Lord Jagannath", "hi": "भगवान जगन्नाथ", "bn": "ভগবান জগন্নাথদেব"},
        "description": {
            "en": "Return journey of Lord Jagannath, Balabhadra, and Subhadra to the main temple (Srimandir).",
            "hi": "गुंडिचा मंदिर से भगवान जगन्नाथ, बलभद्र व सुभद्रा का मुख्य श्रीमंदिर में पुनरागमन।",
            "bn": "গুণ্ডিচা মাসির বাড়ি থেকে শ্রী শ্রী জগন্নাথদেবের নিজ শ্রীমন্দিরে শুভ প্রত্যাবর্তন যাত্রা।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Kaal (Afternoon Return)", "hi": "अपराह्न काल (प्रत्यागमन)", "bn": "অপরাহ্ন কাল (প্রত্যাবর্তন যাত্রা)"}
    },
    ("Ashadha", "Shukla", 11): {
        "en": "Devshayani Ekadashi (Chaturmasya Vrata Begins)",
        "hi": "देवशयनी एकादशी (चातुर्मास प्रारंभ)",
        "bn": "দেবশয়নী একাদশী (চাতুর্মাস্য ব্রতারম্ভ)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Lord Vishnu enters cosmic yoga-nidra for four months on the cosmic serpent Shesha.",
            "hi": "क्षीरसागर में शेषनाग की शैय्या पर भगवान विष्णु का चार मास के लिए योगनिद्रा में शयन।",
            "bn": "ক্ষীরসমুদ্রে শেষনাগের অনন্ত শয্যায় শ্রীহরি বিষ্ণুর চার মাসের জন্য যোগনিদ্রায় গমন ও চাতুর্মাস্যারম্ভ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Dev Shayana Puja", "hi": "सायंकाल देव शयन पूजा", "bn": "সায়ংকালে দেব শয়ন পূজা কাল"}
    },
    ("Ashadha", "Shukla", 15): {
        "en": "Guru Purnima / Maharshi Vyasa Puja / Kokila Vrat",
        "hi": "गुरु पूर्णिमा / वेदव्यास पूजा / कोकिला व्रत",
        "bn": "গুরু পূর্ণিমা / মহর্ষি বেদব্যাস পূজা / কোকিলা ব্রত",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🙏", "deity": {"en": "Sri Guru & Maharshi Vyasa", "hi": "सद्गुरु देव व महर्षि वेदव्यास", "bn": "শ্রী গুরু ও মহর্ষি বেদব্যাস"},
        "description": {
            "en": "Paying reverent homage to spiritual teachers and celebrating the birth of Veda Vyasa.",
            "hi": "अज्ञान रूपी अंधकार को दूर करने वाले गुरुदेव एवं चारों वेदों के रचयिता महर्षि व्यास का वंदन।",
            "bn": "অজ্ঞানতার অন্ধকার দূরকারী সদগুরুদেবের পাদপদ্মে প্রণতি ও মহর্ষি বেদব্যাসের শুভ জন্মজয়ন্তী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal & Abhijit Muhurta", "hi": "पूर्वाह्न काल व अभिजित मुहूर्त", "bn": "পূর্বাহ্ন কাল ও অভিজিৎ মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # শ্রাবণ মাস (Shravana)
    # --------------------------------------------------------------------------
    ("Shravana", "Shukla", 3): {
        "en": "Hariyali Teej / Madhushrava",
        "hi": "हरियाली तीज / मधुश्रवा",
        "bn": "হরিয়ালী তীজ উৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌿", "deity": {"en": "Lord Shiva & Maa Parvati", "hi": "भगवान शिव व माँ पार्वती", "bn": "দেবাদিদেব শিব ও মা পার্বতী"},
        "description": {
            "en": "Celebration of the divine reunion of Shiva and Parvati amidst the greenery of monsoon.",
            "hi": "माँ पार्वती के कठोर तप के पश्चात भगवान शिव से पुनर्मिलन की स्मृति में सुहाग का पावन पर्व।",
            "bn": "কঠোর তপস্যার পর মা পার্বতীর সঙ্গে মহাদেবের পুণ্য মিলনের স্মৃতিতে সৌভাগ্যবর্ধক হরিয়ালী তীজ।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल (संध्याकाल)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যাবেলা)"}
    },
    ("Shravana", "Shukla", 5): {
        "en": "Nag Panchami / Maa Manasa Puja",
        "hi": "नाग पंचमी / माँ मनसा पूजा",
        "bn": "নাগ পঞ্চমী / মা মনসা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🐍", "deity": {"en": "Maa Manasa & Nag Devata", "hi": "माँ मनसा व नाग देवता", "bn": "মা মনসা দেবী ও নাগ দেবতা"},
        "description": {
            "en": "Worship of serpent deities and Maa Manasa for protection against obstacles and poisons.",
            "hi": "सर्पभय निवारण, सुख-शांति एवं माँ मनसा व अष्टनागों की विशेष पूजा आराधना।",
            "bn": "সর্পভয় নিবারণ ও পারিবারিক সুরক্ষার জন্য দেবী মনসা ও অষ্টনাগের বিশেষ পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকালবেলা)"}
    },
    ("Shravana", "Shukla", 6): {
        "en": "Kalki Jayanti",
        "hi": "कल्कि जयंती",
        "bn": "ভগবান কল্কি জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "জয়ন্তী পর্ব", "bn": "মহাপর্ব"},
        "icon": "⚔️", "deity": {"en": "Lord Kalki", "hi": "भगवान कल्कि देव", "bn": "ভগবান কল্কি দেব"},
        "description": {
            "en": "Prophesied future advent of Lord Vishnu's tenth incarnation to establish Satya Yuga.",
            "hi": "कलयुग के अंत में अधर्म का विनाश कर पुनः सत्ययुग स्थापित करने वाले भगवान कल्कि का प्राकट्य पर्व।",
            "bn": "কলিযুগের শেষে পাপক্ষয় করে সত্যযুগ পুনঃপ্রতিষ্ঠার উদ্দেশ্যে দশম কল্কি অবতারের আগমন স্মরণ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal / Pradosh Kaal", "hi": "सायंकाल / प्रदोष काल", "bn": "সায়ংকাল / প্রদোষ কাল"}
    },
    ("Shravana", "Shukla", 15): {
        "en": "Raksha Bandhan / Jhulan Yatra Samapti",
        "hi": "रक्षाबंधन / सावन पूर्णिमा / झूलन यात्रा समापन",
        "bn": "রাখীবন্ধন উৎসব / ঝুলনযাত্রা সমাপন / ভগবান হয়গ্রীব জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🧵", "deity": {"en": "Lord Krishna, Draupadi & Lord Hayagriva", "hi": "भगवान श्रीकृष्ण, द्रौपदी व हयग्रीव", "bn": "শ্রীকৃষ্ণ, দ্রৌপদী ও ভগবান হয়গ্রীব"},
        "description": {
            "en": "Sacred bond of protection and affection between brothers and sisters, marking the conclusion of Jhulan Yatra.",
            "hi": "भाई-बहन के अटूट स्नेह व रक्षा का पावन पर्व तथा श्रीराधा-कृष्ण झूलन यात्रा का समापन।",
            "bn": "ভাই-বোনের স্নেহ ও প্রীতির পবিত্র রাখী বন্ধন মহোৎসব এবং শ্রীশ্রী ঝুলনযাত্রা সমাপন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna & Pradosh (Bhadra Free)", "hi": "अपराह्न व प्रदोष काल (भद्रा रहित)", "bn": "অপরাহ্ন ও প্রদোষ কাল (ভদ্রামুক্ত শুভ লগ্ন)"}
    },

    # --------------------------------------------------------------------------
    # ভাদ্রপদ মাস (Bhadrapada)
    # --------------------------------------------------------------------------
    ("Bhadrapada", "Krishna", 8): {
        "en": "Krishna Janmashtami / Gokulashtami",
        "hi": "श्रीकृष्ण जन्माष्टमी / गोकुलाष्टमी",
        "bn": "শ্রী শ্রী কৃষ্ণ জন্মাষ্টমী মহাপর্ব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🦚", "deity": {"en": "Bhagwan Sri Krishna", "hi": "भगवान श्रीकृष्ण", "bn": "ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Divine midnight advent of Lord Sri Krishna to eradicate injustice and protect Dharma.",
            "hi": "अधर्म के नाश एवं धर्म की स्थापना हेतु मध्यरात्रि में भगवान श्रीकृष्ण का दिव्य जन्मोत्सव।",
            "bn": "ধরাধামে ধর্মের পুনঃপ্রতিষ্ঠা ও অসুর নিধনে মধ্যরাত্রিতে ভগবান শ্রীকৃষ্ণের পরম শুভ আবির্ভাব।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Muhurta (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি)"}
    },
    ("Bhadrapada", "Krishna", 9): {
        "en": "Sri Nandotsava",
        "hi": "श्री नंदोत्सव",
        "bn": "শ্রী শ্রী নন্দোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🍯", "deity": {"en": "Bhagwan Sri Krishna & Nanda Baba", "hi": "बालकृष्ण व नन्द बाबा", "bn": "বালগোপাল ও নন্দ বাবা"},
        "description": {
            "en": "Joyous celebration in Gokula on the day after Janmashtami, distributing sweets, curd, and butter.",
            "hi": "नंदबाबा के भवन में आनंद भयो, जय कन्हैया लाल की - गोकुल में माखन-मिश्री वितरण का उल्लास।",
            "bn": "গোকুলে নন্দভবনে ননী ও মিষ্টান্ন বিতরণের মাধ্যমে গোপাল জন্মের আনন্দোৎসব উদযাপন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal / Morning Utsav", "hi": "प्रातःकाल उत्सव मुहूर्त", "bn": "প্রাতঃকাল মহোৎসব লগ্ন"}
    },
    ("Bhadrapada", "Shukla", 3): {
        "en": "Hartalika Teej / Varaha Jayanti",
        "hi": "हरतालिका तीज / वराह जयंती",
        "bn": "হরতালিকা তীজ / ভগবান বরাহ অবতার জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌺", "deity": {"en": "Lord Shiva, Parvati & Lord Varaha", "hi": "शिव-पार्वती व भगवान वराह", "bn": "শিব-পার্বতী ও ভগবান বরাহ দেব"},
        "description": {
            "en": "Strict fast observed for marital bliss, commemorating Parvati's penance to attain Lord Shiva.",
            "hi": "अखंड सौभाग्य प्राप्ति हेतु बालू के शिवलिंग बनाकर माता पार्वती व शिव जी की रात्रि जागरण पूजा।",
            "bn": "অখণ্ড সৌভাগ্যের কামনায় বালুকার শিবলিঙ্গ নির্মাণ করে পার্বতী-মহাদেবের নির্জলা আরাধনা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal Muhurta", "hi": "प्रदोष काल मुहूर्त", "bn": "প্রদোষ কাল মুহূর্ত"}
    },
    ("Bhadrapada", "Shukla", 4): {
        "en": "Ganesh Chaturthi / Vinayaka Chavithi",
        "hi": "श्री गणेश चतुर्थी / विनायक पूजा",
        "bn": "শ্রী শ্রী গণেশ চতুর্থী / বিনায়ক পূজা (গণেশোৎসব আরম্ভ)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha", "hi": "भगवान श्री गणेश", "bn": "ভগবান শ্রী গণেশ"},
        "description": {
            "en": "Festive commencement of Ganeshotsav welcoming the remover of obstacles, Lord Ganesha.",
            "hi": "विघ्नहर्ता भगवान श्री गणेश के पावन प्राकट्य पर रिद्धि-सिद्धि युक्त गणेशोत्सव का शुभारंभ।",
            "bn": "বিঘ্নবিনাশক ও সর্বসিদ্ধিদাতা ভগবান শ্রী গণেশের শুভ আরাধনা ও গণেশোৎসব আরম্ভ।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত (গণেশ পূজা)"}
    },
    ("Bhadrapada", "Shukla", 5): {
        "en": "Rishi Panchami Vrat",
        "hi": "ऋषि पंचमी व्रत",
        "bn": "ঋষি পঞ্চমী ব্রত (সপ্তর্ষি পূজা)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🪔", "deity": {"en": "Sapta Rishis", "hi": "सप्तर्षि गण", "bn": "পবিত্র সপ্তর্ষি মণ্ডল"},
        "description": {
            "en": "Veneration of the Seven Great Sages (Sapta Rishis) to atone for accidental transgressions.",
            "hi": "जाने-अनजाने में हुए दोषों के निवारण हेतु कश्यपादि सप्त ऋषियों का विशेष पूजन व व्रत।",
            "bn": "অনিচ্ছাকৃত পাপক্ষয় ও পবিত্রতার জন্য কশ্যপাদি সপ্ত ঋষির উদ্দেশ্যে নিষ্ঠাপূর্ণ ব্রত ও অর্চনা।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal (Noon)", "hi": "मध्याह्न काल", "bn": "মধ্যাহ্ন কাল ব্রত সময়"}
    },
    ("Bhadrapada", "Shukla", 8): {
        "en": "Radhashtami / Mahalakshmi Vrat Begins",
        "hi": "श्री राधाष्टमी / महालक्ष्मी व्रत प्रारंभ",
        "bn": "শ্রী শ্রী রাধাষ্টমী মহাপর্ব / মহালক্ষ্মী ব্রতারম্ভ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Srimati Radharani & Maa Mahalakshmi", "hi": "श्रीमती राधारानी व माँ महालक्ष्मी", "bn": "শ্রীমতী রাধারাণী ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Divine noon advent of Srimati Radharani at Barsana, the personification of pure devotion.",
            "hi": "बरसाना में दोपहर के समय प्रेम व भक्ति की अधिष्ठात्री श्रीमती राधारानी का पावन प्राकट्य।",
            "bn": "পরমভক্তি ও প্রেমের মূর্ত প্রতীক শ্রীমতী রাধারাণীর বৃষভানুপুরে শুভ দ্বিপ্রহরে আবির্ভাব তিথি।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত"}
    },
    ("Bhadrapada", "Shukla", 11): {
        "en": "Parsva Ekadashi / Vamana Jayanti",
        "hi": "परिवर्तिनी एकादशी / वामन जयंती",
        "bn": "পার্শ্ব একাদশী (পরিবর্তিনী) / ভগবান বামন জয়ন্তী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Vamana & Sri Hari", "hi": "भगवान वामन व श्री हरि", "bn": "ভগবান বামন দেব ও শ্রীহরি"},
        "description": {
            "en": "Lord Vishnu shifts side in cosmic slumber, and appearance of Vamana Deva to redeem King Bali.",
            "hi": "शयन करते हुए भगवान विष्णु करवट बदलते हैं एवं राजा बलि का उद्धार करने वाले वामन देव का प्राकट्य।",
            "bn": "যোগনিদ্রায় শ্রীহরির পার্শ্ব পরিবর্তন এবং দানবীর বলিকে উদ্ধারকারী ভগবান বামনের আবির্ভাব।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal (Vamana Puja)", "hi": "मध्याह्न काल (वामन पूजा)", "bn": "মধ্যাহ্ন কাল (বামন পূজা)"}
    },
    ("Bhadrapada", "Shukla", 14): {
        "en": "Anant Chaturdashi / Ganesh Visarjan",
        "hi": "अनंत चतुर्दशी व्रत / गणेश विसर्जन",
        "bn": "অনন্ত চতুর্দশী ব্রত / শ্রী গণেশ বিসর্জন",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Ananta Padmanabha & Ganesha", "hi": "भगवान अनंत पद्मनाभ व श्री गणेश", "bn": "ভগবান অনন্ত পদ্মনাভ ও শ্রী গণেশ"},
        "description": {
            "en": "Tying the 14-knot sacred Ananta thread and concluding the 10-day Ganeshotsav with immersion.",
            "hi": "चौदह गांठों वाले अनंत सूत्र का धारण एवं १० दिवसीय गणेशोत्सव का विसर्जन व विदाई।",
            "bn": "১৪টি গ্রন্থিযুক্ত অনন্ত সূত্র ধারণ এবং ১০ দিনব্যাপী গণেশোৎসবের প্রতিমা বিসর্জন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Anant Puja Muhurta", "hi": "पूर्वाह्न अनंत पूजा मुहूर्त", "bn": "পূর্বাহ্ন অনন্ত পূজা মুহূর্ত"}
    },
    ("Bhadrapada", "Shukla", 15): {
        "en": "Bhadrapada Purnima / Pitru Paksha Shraddha Begins",
        "hi": "भाद्रपद पूर्णिमा / पितृपक्ष प्रारंभ (सत्यनारायण पूजा)",
        "bn": "ভাদ্রপদ পূর্ণিমা / পিতৃপক্ষ শ্রাদ্ধারম্ভ (সত্যনারায়ণ পূজা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🙏", "deity": {"en": "Lord Satyanarayan & Ancestors", "hi": "सत्यनारायण देव व पितृ गण", "bn": "শ্রী সত্যনারায়ণ ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Full moon observance and initiation of Mahalaya Pitru Paksha fortnight for ancestor shraddha.",
            "hi": "सत्यनारायण पूर्णिमा पूजन एवं पूर्वजों की तृप्ति हेतु १६ दिवसीय महालय श्राद्ध पक्ष का आरंभ।",
            "bn": "সত্যনারায়ণ পূজা এবং পরলোকগত পিতৃপুরুষের আত্মার তৃপ্তির উদ্দেশ্যে ১৬ দিনের পিতৃপক্ষ শ্রাদ্ধারম্ভ।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Kutapa & Aparahna (Tarpan)", "hi": "कुतप व अपराह्न (तर्पण)", "bn": "কুতপ ও অপরাহ্ন কাল (তর্পণ সময়)"}
    },

    # --------------------------------------------------------------------------
    # আশ্বিন মাস (Ashvina - দুর্গাপূজা)
    # --------------------------------------------------------------------------
    ("Ashvina", "Krishna", 15): {
        "en": "Mahalaya (Sarvapitri Amavasya / Pitru Tarpan)",
        "hi": "महालया / सर्वपितृ अमावस्या / तर्पण",
        "bn": "মহালয়া / সর্বপিতৃ অমাবস্যা ও পিতৃপক্ষের তর্পণ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Pitru Devas", "hi": "माँ दुर्गा व पितृ देव", "bn": "মা দুর্গা ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Grand invocation of Maa Durga and sacred water offerings (tarpan) to departed ancestors.",
            "hi": "देवी दुर्गा का पावन आवाहन एवं पूर्वजों के प्रति श्रद्धा सुमन व पितृ तर्पण का पवित्र दिन।",
            "bn": "দেবী দুর্গার আবাহনী লগ্ন এবং পরলোকগত পিতৃপুরুষের উদ্দেশ্যে তর্পণ নিবেদনের পবিত্র ক্ষণ।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Kutapa & Rauhina Muhurta (Tarpan)", "hi": "कुतप व रौहिण मुहूर्त (तर्पण काल)", "bn": "কুতপ ও রৌহিণ মুহূর্ত (তর্পণ সময়)"}
    },
    ("Ashvina", "Shukla", 1): {
        "en": "Sharad Navratri Begins / Ghatasthapana / Shailaputri Puja",
        "hi": "शारदीय नवरात्रि प्रारंभ / घटस्थापना / माँ शैलपुत्री पूजा",
        "bn": "শারদীয়া নবরাত্রি আরম্ভ / ঘটস্থাপন / দেবী শৈলপুত্রী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Shailaputri", "hi": "माँ दुर्गा व शैलपुत्री", "bn": "মা দুর্গা ও দেবী শৈলপুত্রী"},
        "description": {
            "en": "Commencement of the 9-day Sharad Navratri festival by establishing the sacred urn.",
            "hi": "कलश स्थापना व माँ शैलपुत्री के पूजन के साथ नौ दिवसीय पावन शारदीय दुर्गोत्सव का शुभारंभ।",
            "bn": "পবিত্র ঘটস্থাপন ও দেবী শৈলপুত্রীর আরাধনার মাধ্যমে ৯ দিনব্যাপী শারদীয়া দুর্গোৎসবের আরম্ভ।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Abhijit Muhurta", "hi": "घटस्थापना व अभिजित मुहूर्त", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত"}
    },
    ("Ashvina", "Shukla", 2): {
        "en": "Navratri Day 2: Brahmacharini Puja",
        "hi": "नवरात्रि दिवस २: माँ ब्रह्मचारिणी पूजा",
        "bn": "শারদ নবরাত্রি ২য় দিন: দেবী ব্রহ্মচারিণী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Brahmacharini", "hi": "माँ ब्रह्मचारिणी", "bn": "দেবী ব্রহ্মচারিণী"},
        "description": {
            "en": "Second day of Navratri dedicated to the goddess of austerity and divine asceticism.",
            "hi": "तपस्या व ज्ञान की प्रदाता देवी ब्रह्मचारिणी का नवरात्रि के द्वितीय दिवस पर पावन पूजन।",
            "bn": "তপোনিষ্ঠা ও দিব্য প্রজ্ঞার দেবী ব্রহ্মচারিণীর চরণে নবরাত্রির দ্বিতীয় দিনে ভক্তিপূর্ণ নিবেদন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Ashvina", "Shukla", 3): {
        "en": "Navratri Day 3: Chandraghanta Puja",
        "hi": "नवरात्रि दिवस ३: माँ चंद्रघंटा पूजा",
        "bn": "শারদ নবরাত্রি ৩য় দিন: দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Chandraghanta", "hi": "माँ चंद्रघंटा", "bn": "দেবী চন্দ্রঘণ্টা"},
        "description": {
            "en": "Worship of the ten-armed warrior form bearing a crescent bell for courage and inner peace.",
            "hi": "साहस, निर्भयता व शांति की दात्री माँ चंद्रघंटा का नवरात्रि के तृतीय दिवस पर अर्चन।",
            "bn": "বীরত্ব, নির্ভীকতা ও শান্তির বরদাত্রী দশভুজা দেবী চন্দ্রঘণ্টার নবরাত্রির তৃতীয় দিনের পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Ashvina", "Shukla", 4): {
        "en": "Navratri Day 4: Kushmanda Puja",
        "hi": "नवरात्रि दिवस ४: माँ कूष्मांडा पूजा",
        "bn": "শারদ নবরাত্রি ৪র্থ দিন: দেবী কূষ্মাণ্ডা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Kushmanda", "hi": "माँ कूष्मांडा", "bn": "দেবী কূষ্মাণ্ডা"},
        "description": {
            "en": "Invoking the creator of the cosmic universe with Her radiant divine smile.",
            "hi": "अपनी मंद मुस्कान से ब्रह्मांड की रचना करने वाली देवी कूष्मांडा का पावन पूजन।",
            "bn": "মন্দ মধুর হাস্যে অণ্ড বা ব্রহ্মাণ্ডের সৃষ্টিকর্ত্রী অষ্টভুজা দেবী কূষ্মাণ্ডার বিশেষ পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Ashvina", "Shukla", 5): {
        "en": "Navratri Day 5: Skandamata Puja / Upang Lalita Vrat",
        "hi": "नवरात्रि दिवस ५: माँ स्कंदमाता पूजा / उपांग ललिता व्रत",
        "bn": "শারদ নবরাত্রি ৫ম দিন: দেবী স্কন্দমাতা পূজা / উপাঙ্গ ললিতা ব্রত",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Skandamata & Lalita", "hi": "माँ स्कंदमाता व ललिता", "bn": "দেবী স্কন্দমাতা ও ললিতা"},
        "description": {
            "en": "Worship of the mother of Lord Kartikeya (Skanda), bestowing salvation and prosperity.",
            "hi": "देवसेनापति भगवान स्कंद (कार्तिकेय) की माता माँ स्कंदमाता की भक्तिमयी आराधना।",
            "bn": "দেব সেনাপতি কার্তিকেয়ের জননী দেবী স্কন্দমাতা ও শ্রী ললিতা দেবীর বাৎসল্যপূর্ণ আরাধনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल (प्रातःकाल)", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Ashvina", "Shukla", 6): {
        "en": "Durga Puja: Maha Sashti (Bodhan & Bilva Nimantran)",
        "hi": "दुर्गा षष्ठी (बिल्व निमंत्रण व बोधन)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাষষ্ঠী (বোধন, আমন্ত্রণ ও অধিবাস)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Katyayani", "hi": "माँ दुर्गा व माँ कात्यायनी", "bn": "মা দুর্গা ও দেবী কাত্যায়নী"},
        "description": {
            "en": "Awakening of Maa Durga through Bilva tree rituals, Kalparambha, and sacred invocation.",
            "hi": "बिल्व वृक्ष के नीचे माँ दुर्गा का पावन बोधन, आमंत्रण एवं कल्पारंभ अनुष्ठान।",
            "bn": "বিল্ববৃক্ষমূলে দেবীর বোধন, আমন্ত্রণ ও অধিবাসের মাধ্যমে শারদীয়া দুর্গোৎসবের শুভ সূচনা।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Bilva Nimantran & Adhivas", "hi": "सायंकाल बिल्व निमंत्रण व अधिवास", "bn": "সায়ংকালে বিল্ব নিমন্ত্রণ, বোধন ও অধিবাস"}
    },
    ("Ashvina", "Shukla", 7): {
        "en": "Durga Puja: Maha Saptami (Navapatrika Pravesh)",
        "hi": "दुर्गा सप्तमी (नवपत्रिका प्रवेश पूजा)",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাসপ্তমী (নবপত্রিকা প্রবেশ ও মহাস্নান)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Kalaratri", "hi": "माँ दुर्गा व माँ कालरात्रि", "bn": "মা দুর্গা ও দেবী কালরাত্রি"},
        "description": {
            "en": "Bathing and entry of Navapatrika (Kola Bou) representing 9 forms of Mother Nature.",
            "hi": "प्रकृति के नौ रूपों की प्रतीक नवपत्रिका (केला बहू) का पावन प्रवेश व प्राण प्रतिष्ठा।",
            "bn": "প্রকৃতির ৯টি ঔষধি রূপ নবপত্রিকা (কলাবউ) স্নান, মণ্ডপে প্রবেশ ও মহাসপ্তমী বিহিত পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal Navapatrika Entry & Snan", "hi": "प्रातःकाल नवपत्रिका प्रवेश व स्नान", "bn": "প্রাতঃকালে নবপত্রিকা প্রবেশ ও মহাস্নান"}
    },
    ("Ashvina", "Shukla", 8): {
        "en": "Durga Puja: Maha Ashtami / Sandhi Puja / Kumari Puja",
        "hi": "दुर्गा महाष्टमी / संधि पूजा / कुमारी पूजा",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাঅষ্টমী, সন্ধিপূজা ও কুমারী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Chamunda Durga & Mahagauri", "hi": "माँ चामुंडा दुर्गा व महागौरी", "bn": "দেবী চামুণ্ডা দুর্গা ও মহাগৌরী"},
        "description": {
            "en": "Supreme worship of Chamunda Durga at the juncture of Ashtami and Navami with 108 lamps.",
            "hi": "अष्टमी-नवमी के संधि काल में १०८ दीपों से माँ चामुंडा की विशेष संधि पूजा व कन्या पूजन।",
            "bn": "অষ্টমী ও নবমীর সন্ধিক্ষণে চণ্ড-মুণ্ড বিনাশিনী দেবী চামুণ্ডার ১০৮ প্রদীপ প্রজ্বলনে মহা সন্ধিপূজা।"
        },
        "muhurta_type": "sandhi",
        "muhurta_label": {"en": "Sandhi Puja Muhurta (48-min span)", "hi": "सटीक संधि पूजा मुहूर्त (४८ मिनट)", "bn": "শাস্ত্রীয় সন্ধিপূজা মুহূর্ত (৪৮ মিনিট)"}
    },
    ("Ashvina", "Shukla", 9): {
        "en": "Durga Puja: Maha Navami / Navami Homa",
        "hi": "दुर्गा महानवमी पूजा / नवमी हवन",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহানবমী পূজা ও মহাহোম",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Siddhidatri Durga", "hi": "माँ सिद्धिदात्री दुर्गा", "bn": "দেবী সিদ্ধিদাত্রী দুর্গা"},
        "description": {
            "en": "Completion of Durga Puja rituals with grand sacrificial fire (Maha Yagya) and Ayudha Puja.",
            "hi": "माँ दुर्गा की पूर्ण विधि-विधान से महानवमी पूजा, आयुध पूजन एवं महाहवन अनुष्ठान।",
            "bn": "মহা আহুতির মাধ্যমে মহাহোম, আয়ুধ পূজা ও নবমীর বিহিত পূজার মাধ্যমে বিজয়ের সংকল্প গ্রহণ।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Maha Homa Muhurta", "hi": "मध्याह्न महाहवन मुहूर्त", "bn": "মধ্যাহ্ন মহাহোম ও নবমী যজ্ঞ সময়"}
    },
    ("Ashvina", "Shukla", 10): {
        "en": "Vijaya Dashami / Dussehra / Visarjan",
        "hi": "विजयादशमी / दशहरा / विसर्जन",
        "bn": "শ্রী শ্রী বিজয়া দশমী / দশহরা / সিঁদুর খেলা ও বিসর্জন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Lord Sri Rama", "hi": "माँ दुर्गा व भगवान श्रीराम", "bn": "মা দুর্গা ও ভগবান শ্রীরামচন্দ্র"},
        "description": {
            "en": "Triumph of good over evil, Sindoor Khela, and farewell immersion of Maa Durga.",
            "hi": "बुराई पर अच्छाई की विजय, रावण दहन, सिंदूर खेला एवं माँ दुर्गा का भावभीना विसर्जन।",
            "bn": "অসুরের বিনাশে শুভর জয়, মা দুর্গাকে বিদায় সম্ভাষণ, সিঁদুর খেলা ও পবিত্র অপরাজিতা পূজা।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparajita Puja & Vijaya Muhurta", "hi": "अपराजिता पूजा व विजय मुहूर्त", "bn": "অপরাজিতা পূজা ও বিজয় মুহূর্ত"}
    },
    ("Ashvina", "Shukla", 15): {
        "en": "Kojagari Lakshmi Puja / Sharad Purnima",
        "hi": "कोजागरी लक्ष्मी पूजा / शरद पूर्णिमा",
        "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা / শারদ পূর্ণিমা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Lakshmi & Sri Hari", "hi": "माँ महालक्ष्मी व श्रीहरि", "bn": "মা লক্ষ্মী ও শ্রীহরি নারায়ণ"},
        "description": {
            "en": "Worship of Maa Lakshmi on full moon night to bestow wealth, prosperity, and peace.",
            "hi": "शरद पूर्णिमा की धवल रात्रि में धन-समृद्धि की देवी माँ महालक्ष्मी की रात्रि जागरण पूजा।",
            "bn": "শারদ পূর্ণিমার অমল জ্যোৎস্নায় ধন-ধান্য ও সমৃদ্ধির অধিষ্ঠাত্রী মা লক্ষ্মীর কোজাগরী জাগরণ ও পূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh & Nishita Kaal", "hi": "प्रदोष व निशीथ काल", "bn": "প্রদোষ ও নিশীথ কাল মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # কার্তিক মাস (Kartika)
    # --------------------------------------------------------------------------
    ("Kartika", "Krishna", 4): {
        "en": "Karwa Chauth Vrat",
        "hi": "करवा चौथ व्रत (करक चतुर्थी)",
        "bn": "করবা চৌথ ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌙", "deity": {"en": "Lord Shiva, Parvati & Chandra Deva", "hi": "शिव-पार्वती व चन्द्र देव", "bn": "শিব-পার্বতী ও চন্দ্র দেব"},
        "description": {
            "en": "Rigorous fast observed by married women from sunrise till moonrise for their husband's longevity.",
            "hi": "सुहागिन महिलाओं द्वारा पति की दीर्घायु व स्वास्थ्य हेतु सूर्योदय से चंद्रोदय तक निर्जला व्रत।",
            "bn": "স্বামীর দীর্ঘায়ু ও কল্যাণে সূর্যোদয় থেকে চন্দ্রোদয় পর্যন্ত সৌভাগ্যবতী নারীদের নিষ্ঠাপূর্ণ নির্জলা ব্রত।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Moonrise & Pradosh Kaal", "hi": "चन्द्रोदय व प्रदोष काल", "bn": "চন্দ্রোদয় ও প্রদোষ কাল"}
    },
    ("Kartika", "Krishna", 8): {
        "en": "Ahoi Ashtami Vrat / Radha Kund Snan",
        "hi": "अहोई अष्टमी व्रत / राधा कुंड स्नान",
        "bn": "অহোই অষ্টমী ব্রত / শ্রী রাধাকুণ্ড স্নান",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🪔", "deity": {"en": "Maa Ahoi", "hi": "माँ अहोई", "bn": "মা অহোই দেবী"},
        "description": {
            "en": "Mothers fast for the well-being and long life of their children, breaking the fast after star sighting.",
            "hi": "माताएं अपनी संतानों की दीर्घायु, स्वास्थ्य व सुखद भविष्य के लिए तारा दर्शन तक व्रत रखती हैं।",
            "bn": "মাতা কর্তৃক সন্তানের মঙ্গল ও দীর্ঘ জীবনের কামনায় সায়ংকালে নক্ষত্র দর্শন পর্যন্ত উপবাস ব্রত।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Star Gazing & Pradosh", "hi": "सायंकाल तारा दर्शन व प्रदोष", "bn": "সায়ংকালে তারা দর্শন ও প্রদোষ"}
    },
    ("Kartika", "Krishna", 12): {
        "en": "Govatsa Dwadashi / Bachh Baras / Gau Puja",
        "hi": "गोवत्स द्वादशी (बछ बारस) / गौ माता पूजा",
        "bn": "গোবৎসা দ্বাদশী / বাছুর ও গো-পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🐄", "deity": {"en": "Gau Mata & Lord Krishna", "hi": "गौ माता व भगवान श्रीकृष्ण", "bn": "গো-মাতা ও ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Veneration of cows and their calves before Diwali, thanking Kamadhenu for nourishing humanity.",
            "hi": "दीपावली से पूर्व कामधेनु स्वरूपा गौ माता एवं बछड़े का कृतज्ञतापूर्वक पूजन व वंदन।",
            "bn": "দীপাবলির প্রাক্কালে কামধেনু রূপিণী গো-মাতা ও বাছুরের প্রতি শ্রদ্ধা ও কৃতজ্ঞতা জ্ঞাপন পূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल", "bn": "প্রদোষ কাল (সন্ধ্যাবেলা)"}
    },
    ("Kartika", "Krishna", 13): {
        "en": "Dhanteras / Dhanvantari Jayanti / Kuber Puja",
        "hi": "धनतेरस / धन्वंतरि जयंती / कुबेर पूजा",
        "bn": "শ্রী শ্রী ধনতেরাস / ধন্বন্তরি জয়ন্তী / কুবের পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪙", "deity": {"en": "Lord Dhanvantari & Kuber", "hi": "भगवान धन्वंतरि व कुबेर देव", "bn": "ভগবান ধন্বন্তরি ও কুবের দেব"},
        "description": {
            "en": "Worship of Dhanvantari for health and Lord Kuber for wealth, with evening Yama Deepam.",
            "hi": "आरोग्य हेतु धन्वंतरि, समृद्धि हेतु कुबेर पूजन एवं अकाल मृत्यु निवारण हेतु यम दीपदान।",
            "bn": "সুস্বাস্থ্যের জন্য ধন্বন্তরি ও সমৃদ্ধির জন্য কুবের পূজা এবং যমরাজের উদ্দেশ্যে প্রদীপ দান।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal & Vrishabha Lagna", "hi": "प्रदोष काल व वृषभ लग्न", "bn": "প্রদোষ কাল ও বৃষ লগ্ন"}
    },
    ("Kartika", "Krishna", 14): {
        "en": "Bhoot Chaturdashi / Naraka Chaturdashi / 14 Pradeep Dan",
        "hi": "नरक चतुर्दशी / छोटी दिवाली / रूप चौदस",
        "bn": "ভূত চতুর্দশী (১৪ প্রদীপ ও ১৪ শাক দান) / নরক চতুর্দশী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Yamaraja & Ancestors", "hi": "यमराज व पितृ गण", "bn": "যমরাজ ও চোদ্দ পুরুষ"},
        "description": {
            "en": "Lighting 14 lamps to dispel dark energies and honour the 14 ancestors prior to Kali Puja.",
            "hi": "चौदह यमदीप प्रज्वलित कर नकारात्मकता दूर करना एवं रूप निखार हेतु अभ्यंग स्नान।",
            "bn": "চোদ্দ প্রদীপ প্রজ্বলন ও চোদ্দ শাক গ্রহণের মাধ্যমে অশুভ শক্তি দূরীকরণ ও চোদ্দ পুরুষের স্মরণ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal 14 Deepam & Abhyanga Snan", "hi": "सायंकाल यम दीपदान व अभ्यंग स्नान", "bn": "সায়ংকালে ১৪ প্রদীপ দান ও তৈলাভ্যঙ্গ স্নান"}
    },
    ("Kartika", "Krishna", 15): {
        "en": "Shyama Puja (Kali Puja) / Diwali / Lakshmi Puja",
        "hi": "दीपावली / महालक्ष्मी पूजा / माँ काली पूजा",
        "bn": "শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / দীপাবলি মহোৎসব ও মহালক্ষ্মী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Maa Kali & Maa Mahalakshmi", "hi": "माँ काली व माँ महालक्ष्मी", "bn": "মা শ্যামা কালী ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Victory of light over darkness with earthen lamps and midnight worship of Maa Kali.",
            "hi": "अंधकार पर प्रकाश की विजय का दीपोत्सव एवं मध्यरात्रि में माँ काली की तांत्रिक व वैदिक पूजा।",
            "bn": "অন্ধকার দূর করে আলোর দীপাবলি উৎসব এবং অমাবস্যার নিশীথ রাতে মা শ্যামা কালীর আরাধনা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal (Kali Puja) & Pradosh", "hi": "निशीथ काल (काली पूजा) व प्रदोष", "bn": "নিশীথ কাল (কালীপূজা) ও প্রদোষ লগ্ন"}
    },
    ("Kartika", "Shukla", 1): {
        "en": "Govardhan Puja / Annakut Mahotsav / Bali Pratipada",
        "hi": "गोवर्धन पूजा / अन्नकूट महोत्सव / बलि प्रतिपदा",
        "bn": "শ্রী শ্রী গোবর্ধন পূজা ও অন্নকূট মহোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "⛰️", "deity": {"en": "Lord Sri Krishna (Giriraj)", "hi": "गिरिराज भगवान श्रीकृष्ण", "bn": "গিরিরাজ ভগবান শ্রীকৃষ্ণ"},
        "description": {
            "en": "Commemorating Lord Krishna lifting the Govardhan Hill with offerings of 56 delicacies (Chhappan Bhog).",
            "hi": "इंद्र के मानमर्दन हेतु भगवान श्रीकृष्ण द्वारा गोवर्धन पर्वत धारण एवं ५६ भोग अन्नकूट समर्पण।",
            "bn": "ইন্দ্রের দর্পচূর্ণ করে শ্রীকৃষ্ণ কর্তৃক গোবর্ধন পর্বত ধারণ এবং ছাপ্পান্ন ভোগ নিবেদনে অন্নকূট উৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal & Sayankal Annakut", "hi": "प्रातःकाल व सायंकाल अन्नकूट", "bn": "প্রাতঃকাল ও সায়ংকালে অন্নকূট ভোগ"}
    },
    ("Kartika", "Shukla", 2): {
        "en": "Bhai Phonta / Bhatri Dwitiya / Yama Dwitiya",
        "hi": "भाई दूज / यम द्वितीया / भ्रातृ द्वितीया",
        "bn": "পবিত্র ভাইফোঁটা (ভ্রাতৃদ্বিতীয়া / যমদ্বিতীয়া)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Yamuna & Yamaraja", "hi": "यमुना जी व यमराज", "bn": "যমুনা দেবী ও যমরাজ"},
        "description": {
            "en": "Sisters pray for their brothers' long life and protection from harm on Yama Dwitiya.",
            "hi": "बहनें अपने भाई की दीर्घायु, यश व आरोग्यता के लिए तिलक लगाकर मंगल कामना करती हैं।",
            "bn": "যমের দুয়ারে কাঁটা দিয়ে ভাইয়ের দীর্ঘায়ু ও সর্ববিপদমুক্তির জন্য ভগিনীর পবিত্র আশীর্বাদ লগ্ন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Kaal Muhurta", "hi": "अपराह्न काल मुहूर्त", "bn": "অপরাহ্ন কাল মুহূর্ত (ভ্রাতৃদ্বিতীয়া)"}
    },
    ("Kartika", "Shukla", 6): {
        "en": "Chhath Puja (Sandhya Arghya / Surya Sashthi)",
        "hi": "छठ पूजा (संध्या अर्घ्य / सूर्य षष्ठी)",
        "bn": "ছট পূজা (সন্ধ্যার অর্ঘ্যদান ও সূর্য ষষ্ঠী)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☀️", "deity": {"en": "Surya Deva & Chhathi Maiya", "hi": "भगवान सूर्य व छठी मइया", "bn": "ভগবান সূর্য দেব ও ছটি মাইয়া"},
        "description": {
            "en": "Offering sacred evening oblation (Arghya) in water bodies to the setting Sun God.",
            "hi": "जल में खड़े होकर अस्ताचलगामी भगवान सूर्य एवं छठी मइया को प्रथम संध्या अर्घ्य अर्पण।",
            "bn": "জলে দাঁড়িয়ে অস্তগামী ভগবান সূর্য দেব ও পরমাপ্রকৃতি ছটি মাইয়ার উদ্দেশ্যে পবিত্র সায়ং অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sunset / Sandhya Arghya Muhurta", "hi": "सूर्यास्त संध्या अर्घ्य मुहूर्त", "bn": "সূর্যাস্ত সায়ং অর্ঘ্যদান মুহূর্ত"}
    },
    ("Kartika", "Shukla", 7): {
        "en": "Chhath Puja (Usha Arghya & Paran)",
        "hi": "छठ पूजा (प्रातः अर्घ्य / पारण)",
        "bn": "ছট পূজা (ভোরের অর্ঘ্যদান ও পারণ)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☀️", "deity": {"en": "Surya Deva & Chhathi Maiya", "hi": "भगवान सूर्य व छठी मइया", "bn": "ভগবান সূর্য দেব ও ছটি মাইয়া"},
        "description": {
            "en": "Offering dawn oblation to the rising Sun God, successfully concluding the 36-hour nirjala fast.",
            "hi": "उदीयमान भगवान सूर्य को प्रातः अर्घ्य समर्पण के साथ ३६ घंटे के निर्जला महाव्रत का पारण।",
            "bn": "উদীয়মান সূর্য দেবতাকে ভোরের অর্ঘ্য নিবেদনের মাধ্যমে ৩৬ ঘণ্টার নির্জলা মহাব্রতের সমাপন ও পারণ।"
        },
        "muhurta_type": "sunrise_snan",
        "muhurta_label": {"en": "Sunrise / Usha Arghya Muhurta", "hi": "सूर्योदय उषा अर्घ्य मुहूर्त", "bn": "সূর্যোদয় ঊষা অর্ঘ্যদান মুহূর্ত"}
    },
    ("Kartika", "Shukla", 8): {
        "en": "Gopashtami / Gau Puja Mahotsav",
        "hi": "गोपाष्टमी / कामधेनु गौ पूजा",
        "bn": "শ্রী শ্রী গোপাষ্টমী / কামধেনু গো-পূজা মহোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🐄", "deity": {"en": "Lord Krishna & Gau Mata", "hi": "भगवान श्रीकृष्ण व कामधेनु", "bn": "শ্রীকৃষ্ণ ও কামধেনু গো-মাতা"},
        "description": {
            "en": "The auspicious day when Lord Krishna officially graduated from tending calves to herding cows.",
            "hi": "भगवान श्रीकृष्ण द्वारा बछड़ों की जगह गौ चारण की दीक्षा लेने का पावन गोपाष्टमी उत्सव।",
            "bn": "শ্রীকৃষ্ণ কর্তৃক বাছুরের পরিবর্তে স্বয়ং ধেনু চারণের দায়িত্ব গ্রহণের পুণ্যময় গোপাষ্টমী তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal (Morning)", "hi": "प्रातःकाल मुहूर्त", "bn": "প্রাতঃকাল মুহূর্ত"}
    },
    ("Kartika", "Shukla", 9): {
        "en": "Sri Jagaddhatri Puja / Akshaya Navami / Amla Navami",
        "hi": "जगद्धात्री पूजा / अक्षय नवमी / आँवला नवमी",
        "bn": "শ্রী শ্রী জগদ্ধাত্রী পূজা / অক্ষয় নবমী / আমলকী নবমী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🦁", "deity": {"en": "Maa Jagaddhatri", "hi": "माँ जगद्धात्री", "bn": "মা জগদ্ধাত্রী দেবী"},
        "description": {
            "en": "Worship of Maa Jagaddhatri, the sustainer of the world, and sacred sitting beneath Amla trees.",
            "hi": "संसार का भरण-पोषण करने वाली माँ जगद्धात्री की पूजा एवं आँवला वृक्ष के नीचे पूजन व भोजन।",
            "bn": "জগতের ধাত্রী দেবী জগদ্ধাত্রীর ত্রিকাল পূজা এবং পুণ্যফলদায়ী অক্ষয় আমলকী নবমী ব্রত।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Purvahna & Madhyahna Puja", "hi": "पूर्वाह्न व मध्याह्न त्रिकाल पूजा", "bn": "পূর্বাহ্ন ও মধ্যাহ্ন ত্রিকাল পূজা"}
    },
    ("Kartika", "Shukla", 11): {
        "en": "Devutthana Ekadashi / Tulsi Vivah / Bhishma Panchaka Begins",
        "hi": "देवउठनी एकादशी / तुलसी विवाह / भीष्म पंचक प्रारंभ",
        "bn": "দেবউত্থান একাদশী / তুলসী বিবাহ / ভীষ্ম পঞ্চক ব্রতারম্ভ",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌿", "deity": {"en": "Lord Vishnu & Tulsi Maharani", "hi": "भगवान शालिग्राम व तुलसी जी", "bn": "ভগবান শালগ্রাম ও তুলসী মহারাণী"},
        "description": {
            "en": "Lord Vishnu awakens from four-month cosmic slumber, resuming all auspicious ceremonies and Tulsi Vivah.",
            "hi": "चातुर्मास की समाप्ति पर भगवान विष्णु का जागृत होना एवं शालिग्राम-तुलसी विवाह से शुभ कार्यों का आरंभ।",
            "bn": "চাতুর্মাস্য শেষে শ্রীহরির যোগনিদ্রা ভঙ্গ এবং শালগ্রাম-তুলসী বিবাহের মাধ্যমে সর্ব শুভকার্য আরম্ভ।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Tulsi Vivah)", "hi": "प्रदोष काल (तुलसी विवाह)", "bn": "প্রদোষ কাল (তুলসী বিবাহ সময়)"}
    },
    ("Kartika", "Shukla", 14): {
        "en": "Vaikuntha Chaturdashi",
        "hi": "वैकुंठ चतुर्दशी (हरि-हर मिलन)",
        "bn": "শ্রী বৈকুণ্ঠ চতুর্দশী (হরি-হর মিলন)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Shiva & Lord Vishnu", "hi": "भगवान शिव व भगवान विष्णु", "bn": "দেবাদিদেব শিব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Divine union of Shiva and Vishnu where Lord Shiva worshipped Vishnu with 1000 lotus blossoms.",
            "hi": "भगवान शिव व विष्णु का पावन मिलन, जिसमें शिव जी ने भगवान विष्णु को सहस्र कमल अर्पित किए थे।",
            "bn": "ভগবান শিব ও শ্রীহরি বিষ্ণুর পরম পবিত্র মিলন তিথি এবং সহস্র পদ্ম নিবেদনের পূজা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Muhurta (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি)"}
    },
    ("Kartika", "Shukla", 15): {
        "en": "Sri Kartik Puja / Rash Yatra / Dev Deepawali / Kartik Purnima",
        "hi": "कार्तिक पूजा / देव दीपावली / रास पूर्णिमा / त्रिपुरारी पूर्णिमा",
        "bn": "শ্রী শ্রী কার্তিক পূজা / শ্রী শ্রী রাসযাত্রা / রাসপূর্ণিমা / দেব দীপাবলি",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Lord Kartikeya, Radha Krishna & Shiva", "hi": "कार्तिकेय, राधा-कृष्ण व शिव जी", "bn": "দেব সেনাপতি কার্তিক, রাধাকৃষ্ণ ও শিব"},
        "description": {
            "en": "Vrindavan Maha Raas, Lord Shiva slaying Tripurasura (Dev Deepawali in Varanasi), and Kartik Puja.",
            "hi": "काशी में देवताओं की देव दीपावली, श्रीराधा-कृष्ण की महारास पूर्णिमा एवं कार्तिकेय पूजन।",
            "bn": "বৃন্দাবনে শ্রীশ্রী রাধাকৃষ্ণের রাসযাত্রা মহোৎসব, কাশীতে দেব দীপাবলি এবং শ্রী কার্তিক পূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal & Full Moon Night", "hi": "प्रदोष काल व दीपदान मुहूर्त", "bn": "প্রদোষ কাল ও দেব দীপাবলি লগ্ন"}
    },

    # --------------------------------------------------------------------------
    # মার্গশীর্ষ মাস (Margashirsha)
    # --------------------------------------------------------------------------
    ("Margashirsha", "Shukla", 5): {
        "en": "Vivah Panchami (Sri Rama-Sita Vivah Mahotsav)",
        "hi": "विवाह पंचमी (श्रीराम-जानकी विवाह महोत्सव)",
        "bn": "বিবাহ পঞ্চমী (শ্রীশ্রী সীতারাম শুভ বিবাহ মহোৎসব)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🏹", "deity": {"en": "Lord Sri Rama & Maa Sita", "hi": "भगवान श्रीराम व माँ सीता", "bn": "ভগবান শ্রীরামচন্দ্র ও মা জানকী"},
        "description": {
            "en": "Celebration of the celestial wedding anniversary of Lord Sri Rama and Maa Sita in Janakpur.",
            "hi": "जनकपुर में मर्यादा पुरुषोत्तम भगवान श्रीराम एवं जगज्जननी जानकी जी के पावन विवाह का उत्सव।",
            "bn": "জনকপুরধামে ভগবান শ্রীরামচন্দ্র ও মা জানকীর পবিত্র স্বর্গীয় শুভ বিবাহ বার্ষিকী মহোৎসব।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Abhijit & Godhuli Muhurta", "hi": "अभिजित व गोधूलि मुहूर्त", "bn": "অভিজিৎ ও গোধূলি শুভ লগ্ন"}
    },
    ("Margashirsha", "Shukla", 6): {
        "en": "Champa Sasthi / Skanda Sasthi",
        "hi": "चंपा षष्ठी / स्कंद षष्ठी",
        "bn": "চম্পা ষষ্ঠী / স্কন্দ ষষ্ঠী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🦚", "deity": {"en": "Lord Kartikeya (Khandoba)", "hi": "भगवान कार्तिकेय (खंडोबा)", "bn": "ভগবান কার্তিকেয়"},
        "description": {
            "en": "Veneration of Lord Kartikeya (Khandoba) offering Champa flowers, brinjal, and millet bread.",
            "hi": "भगवान कार्तिकेय (मल्हारी मार्तंड) को चंपा पुष्प व बाजरा-बैंगन भोग समर्पण कर व्रत।",
            "bn": "দেব সেনাপতি কার্তিকেয়কে চাঁপা ফুল নিবেদন এবং শারীরিক সুস্থতার কামনায় বিশেষ ষষ্ঠী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Morning)", "hi": "पूर्वाह्न काल", "bn": "পূর্বাহ্ন কাল (সকাল)"}
    },
    ("Margashirsha", "Shukla", 11): {
        "en": "Mokshada Ekadashi / Srimad Bhagavad Gita Jayanti",
        "hi": "गीता जयंती / मोक्षदा एकादशी",
        "bn": "শ্রীমদ্ভগবদ্গীতা জয়ন্তী / মোক্ষদা একাদশী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "📜", "deity": {"en": "Bhagwan Sri Krishna & Srimad Bhagavad Gita", "hi": "भगवान श्रीकृष्ण व श्रीमद्भगवद्गीता", "bn": "ভগবান শ্রীকৃষ্ণ ও শ্রীমদ্ভগবদ্গীতা"},
        "description": {
            "en": "The day Lord Krishna delivered the immortal song of Gita to Arjuna on the battlefield of Kurukshetra.",
            "hi": "कुरुक्षेत्र की रणभूमि में भगवान श्रीकृष्ण द्वारा अर्जुन को दिए गए अमर गीता उपदेश का पावन दिवस।",
            "bn": "কুরুক্ষেত্রের পুণ্য রণাঙ্গনে অর্জুনের মোহ দূর করতে ভগবান শ্রীকৃষ্ণ কর্তৃক উচ্চারিত গীতার জন্মতিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal (Gita Path)", "hi": "पूर्वाह्न काल (गीता पाठ)", "bn": "পূর্বাহ্ন কাল (গীতা পাঠ ও পূজা)"}
    },
    ("Margashirsha", "Shukla", 15): {
        "en": "Dattatreya Jayanti / Annapurna Jayanti / Margashirsha Purnima",
        "hi": "दत्तात्रेय जयंती / अन्नपूर्णा जयंती / मार्गशीर्ष पूर्णिमा",
        "bn": "শ্রী দত্তাত্রেয় জয়ন্তী / মা অন্নপূর্ণা আবির্ভাব / মার্গশীর্ষ পূর্ণিমা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Lord Dattatreya & Maa Annapurna", "hi": "भगवान दत्तात्रेय व माँ अन्नपूर्णा", "bn": "ভগবান দত্তাত্রেয় ও মা অন্নপূর্ণা"},
        "description": {
            "en": "Appearance of Lord Dattatreya (the composite trimurti of Brahma, Vishnu, Shiva) and Maa Annapurna.",
            "hi": "ब्रह्मा, विष्णु, महेश के संयुक्त त्रिदेव रूप भगवान दत्तात्रेय एवं माँ अन्नपूर्णा का प्राकट्योत्सव।",
            "bn": "ব্রহ্মা, বিষ্ণু ও শিবের সমন্বিত রূপ ভগবান দত্তাত্রেয় এবং মা অন্নপূর্ণার শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल (संध्याकाल)", "bn": "প্রদোষ কাল (সন্ধ্যাবেলা)"}
    },

    # --------------------------------------------------------------------------
    # পৌষ মাস (Pausha)
    # --------------------------------------------------------------------------
    ("Pausha", "Shukla", 15): {
        "en": "Pausha Purnima / Shakambhari Jayanti",
        "hi": "पौष पूर्णिमा / शाकंभरी जयंती (शाकंभरी नवरात्रि समापन)",
        "bn": "পৌষ পূর্ণিমা / মা শাকম্ভরী দেবী জয়ন্তী (শাকম্ভরী নবরাত্রি সমাপন)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Shakambhari Durga", "hi": "माँ शाकंभरी देवी", "bn": "মা শাকম্ভরী দুর্গা"},
        "description": {
            "en": "Worship of Maa Shakambhari, who alleviated famine and drought with green vegetables and water.",
            "hi": "अकाल व सूखे से पृथ्वी की रक्षा हेतु वनस्पतियों व जल को प्रकट करने वाली देवी शाकंभरी की पूजा।",
            "bn": "অনাবৃষ্টি ও দুর্ভিক্ষ দূর করে সবুজ শস্য-শাকসবজি দানকারিণী মা শাকম্ভরীর বিশেষ আবির্ভাব পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna & Pradosh Kaal", "hi": "पूर्वाह्न व प्रदोष काल", "bn": "পূর্বাহ্ন ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # মাঘ মাস (Magha)
    # --------------------------------------------------------------------------
    ("Magha", "Shukla", 1): {
        "en": "Magha Gupt Navratri Begins",
        "hi": "माघ गुप्त नवरात्रि प्रारंभ / घटस्थापना",
        "bn": "মাঘ গুপ্ত নবরাত্রি আরম্ভ / ঘটস্থাপন ও দশমহাবিদ্যা সাধনা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "সাধনা পর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Das Mahavidya & Maa Durga", "hi": "दस महाविद्या व माँ दुर्गा", "bn": "দশমহাবিদ্যা ও মা দুর্গা"},
        "description": {
            "en": "Auspicious commencement of winter Gupt Navratri for spiritual austerities and Tantric sadhana.",
            "hi": "शिशिर ऋतु में आत्मिक शक्ति व महाविद्याओं की कृपा प्राप्ति हेतु गुप्त नवरात्रि घटस्थापना।",
            "bn": "শীতকালীন গুপ্ত নবরাত্রিতে ঘটস্থাপন ও আত্মশুদ্ধি এবং দশমহাবিদ্যার নিগূঢ় সাধনার শুভ সূচনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Abhijit Muhurta", "hi": "घटस्थापना व अभिजित मुहूर्त", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত"}
    },
    ("Magha", "Shukla", 4): {
        "en": "Ganesha Jayanti / Varad Vinayaka Chaturthi / Til Kund Chaturthi",
        "hi": "गणेश जयंती / वरद चतुर्थी / तिल कुंद चतुर्थी",
        "bn": "শ্রী গণেশ জন্মজয়ন্তী / বরদ বিনায়ক চতুর্থী (তিল চতুর্থী)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha", "hi": "भगवान श्री गणेश", "bn": "ভগবান শ্রী গণেশ"},
        "description": {
            "en": "Traditional appearance day of Lord Ganesha in Magha, offering sesame (til) laddus.",
            "hi": "माघ मास में भगवान श्री गणेश का पावन जन्मोत्सव, तिल-गुड़ के लड्डुओं से विशेष पूजा।",
            "bn": "মাঘ মাসের শুক্ল চতুর্থীতে সিদ্ধিদাতা শ্রী গণেশের জন্মজয়ন্তী এবং তিলের লাড্ডু নিবেদন পূজা।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত"}
    },
    ("Magha", "Shukla", 5): {
        "en": "Sri Saraswati Puja / Vasant Panchami / Sri Panchami",
        "hi": "सरस्वती पूजा / बसंत पंचमी / श्री पंचमी / वाग्देवी आराधना",
        "bn": "শ্রী শ্রী সরস্বতী পূজা / বসন্ত পঞ্চমী / শ্রীপঞ্চমী (বাগদেবী আরাধনা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪕", "deity": {"en": "Maa Saraswati (Vagdevi)", "hi": "वाग्देवी माँ सरस्वती", "bn": "বাগদেবী মা সরস্বতী"},
        "description": {
            "en": "Worship of the Goddess of knowledge, music, and arts, marking the arrival of spring.",
            "hi": "विद्या, बुद्धि, ज्ञान व संगीत की अधिष्ठात्री देवी माँ सरस्वती की आराधना व वसंत ऋतु आगमन।",
            "bn": "বিদ্যা, বুদ্ধি ও জ্ঞানের বরদাত্রী মা সরস্বতীর শ্রীচরণে অঞ্জলি প্রদান ও বসন্তের শুভ আবাহন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Kaal Muhurta", "hi": "पूर्वाह्न काल मुहूर्त", "bn": "পূর্বাহ্ন কাল মুহূর্ত (সরস্বতী পূজা)"}
    },
    ("Magha", "Shukla", 7): {
        "en": "Ratha Saptami / Surya Jayanti / Arogya Saptami",
        "hi": "रथ सप्तमी / सूर्य जयंती / आरोग्य सप्तमी / अचला सप्तमी",
        "bn": "রথ সপ্তমী / সূর্য জয়ন্তী / আরোগ্য সপ্তমী মহোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☀️", "deity": {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"},
        "description": {
            "en": "The day Lord Surya mounted His golden chariot driven by Aruna with seven green horses.",
            "hi": "भगवान सूर्य देव द्वारा अपने सात घोड़ों वाले दिव्य रथ पर आरूढ़ होकर ज्ञान प्रकाश फैलाने का दिन।",
            "bn": "সপ্তরথী ঘোটকবাহী রথে ভগবান সূর্যদেবের আরোহণ ও আরোগ্যলাভের পুণ্য সূর্য জয়ন্তী স্নান।"
        },
        "muhurta_type": "sunrise_snan",
        "muhurta_label": {"en": "Sunrise & Arunodaya Snan Muhurta", "hi": "सूर्योदय व अरुणोदय स्नान मुहूर्त", "bn": "সূর্যোদয় ও অরুণোদয় স্নান মুহূর্ত"}
    },
    ("Magha", "Shukla", 8): {
        "en": "Bhishma Ashtami Vrat & Tarpan",
        "hi": "भीष्म अष्टमी व्रत व तर्पण",
        "bn": "ভীষ্ম অষ্টমী ব্রত ও পিতামহ ভীষ্ম তর্পণ",
        "category": "hindu", "type": {"en": "Vrata", "hi": "তর্পণ পর্ব", "bn": "উপবাস ব্রত"},
        "icon": "🏹", "deity": {"en": "Bhishma Pitamah", "hi": "पितामह भीष्म", "bn": "পিতামহ ভীষ্ম"},
        "description": {
            "en": "Commemorating the departure of Grandsire Bhishma on Uttarayana and offering him water tarpan.",
            "hi": "सूर्य के उत्तरायण होने पर इच्छामृत्यु प्राप्त पितामह भीष्म के मोक्ष गमन पर श्राद्ध व तर्पण।",
            "bn": "সূর্যের উত্তরায়ণে পিতামহ ভীষ্মের মোক্ষলাভ স্মরণে সর্ববর্ণের ভক্তগণের তৃপ্তিদায়ক ভীষ্ম তর্পণ।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Tarpan Kaal", "hi": "मध्याह्न तर्पण काल", "bn": "মধ্যাহ্ন তর্পণ সময়"}
    },
    ("Magha", "Shukla", 15): {
        "en": "Magha Purnima / Maha Maghi Snan / Lalita Jayanti",
        "hi": "माघ पूर्णिमा / महा माघी स्नान / ललिता जयंती",
        "bn": "মাঘী পূর্ণিমা / মহামাঘী স্নান / মা ললিতা জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌊", "deity": {"en": "Lord Vishnu, Ganga & Tripura Sundari", "hi": "विष्णु जी, गंगा व माँ ललिता", "bn": "শ্রীহরি বিষ্ণু, গঙ্গা ও মা ললিতা ত্রিপুরাসুন্দরী"},
        "description": {
            "en": "Confluence of deities in sacred rivers, highly praised for Prayag Triveni Sangam snan.",
            "hi": "प्रयागराज त्रिवेणी संगम में समस्त तीर्थों के वास पर पवित्र स्नान एवं माँ ललिता जयंती।",
            "bn": "প্রয়াগরাজ ও সর্বতীর্থে পুণ্যস্নান, দান এবং দেবী ললিতা ত্রিপুরাসুন্দরীর শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Sunrise Snan", "hi": "ब्रह्म मुहूर्त व सूर्योदय स्नान", "bn": "ব্রাহ্ম মুহূর্ত ও সূর্যোদয় মহাতীর্থ স্নান"}
    },
    ("Magha", "Krishna", 14): {
        "en": "Sri Maha Shivratri Vrat & Mahapuja",
        "hi": "श्री महाशिवरात्रि व्रत व महापूजा / शिव-पार्वती विवाह",
        "bn": "শ্রী শ্রী মহা শিবরাত্রি ব্রত ও চার প্রহর শিবপূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Lord Shiva & Maa Parvati", "hi": "देवाधिदेव महादेव व माँ पार्वती", "bn": "দেবাদিদেব মহাদেব ও মা পার্বতী"},
        "description": {
            "en": "Great night of Shiva observing day-long fast and four-prahar lingam abhishek.",
            "hi": "भगवान शिव-पार्वती के पावन विवाह एवं लिंगोद्भव की महानिशा, चार प्रहर जलाभिषेक व व्रत।",
            "bn": "শিব-পার্বতীর বিবাহ ও জ্যোতির্লিঙ্গ প্রকাশের মহাপর্ব; দিবারাত্র উপবাস ও চার প্রহর রুদ্রাভিষেক।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Muhurta (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ কাল মুহূর্ত (চার প্রহর শিবপূজা)"}
    },
    ("Magha", "Krishna", 15): {
        "en": "Mauni Amavasya / Magha Amavasya Mahasnan",
        "hi": "मौनी अमावस्या / माघ अमावस्या महास्नान",
        "bn": "মৌনী অমাবস্যা / মাঘী অমাবস্যা মহাতীর্থ স্নান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Lord Vishnu & Shiva", "hi": "भगवान विष्णु व शिव जी", "bn": "ভগবান বিষ্ণু ও শিব"},
        "description": {
            "en": "Observing silence (Mauna Vrata) and sacred holy dipping in the Ganges for inner peace.",
            "hi": "मन के संयम हेतु मौन व्रत धारण एवं त्रिवेणी संगम में अमृत स्नान का सर्वोत्कृष्ट दिन।",
            "bn": "মনঃসংযমের জন্য মৌনব্রত পালন এবং পবিত্র গঙ্গাবারি ও ত্রিবেণী সঙ্গমে মহাস্নান।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Dawn Snan", "hi": "ब्रह्म मुहूर्त व प्रातःकाल", "bn": "ব্রাহ্ম মুহূর্ত ও ভোরবেলা"}
    },

    # --------------------------------------------------------------------------
    # ফাল্গুন মাস (Phalguna)
    # --------------------------------------------------------------------------
    ("Phalguna", "Krishna", 14): {
        "en": "Maha Shivratri (Purnimanta tradition) / Masik Shivratri",
        "hi": "महाशिवरात्रि / मासिक शिवरात्रि व्रत",
        "bn": "মহা শিবরাত্রি ব্রত / মাসিক শিবরাত্রি",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান শিব"},
        "description": {
            "en": "Monthly Shivratri worship of the Shiva Linga at midnight for liberation from sins.",
            "hi": "मनोकामना पूर्ति एवं कष्टों के निवारण हेतु मध्यरात्रि में भगवान शिव का जलाभिषेक।",
            "bn": "মনোবাঞ্ছা পূরণ ও সর্বক্লেশ মুক্তির উদ্দেশ্যে নিশীথ কালে শিবলিঙ্গে জলাভিষেক ও উপবাস।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি)"}
    },
    ("Phalguna", "Shukla", 14): {
        "en": "Holika Dahan / Chhanchar Utsav",
        "hi": "होलिका दहन / कामदहन",
        "bn": "হোলিকা দহন / চাঁচর উৎসব (অগ্নি উৎসব)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔥", "deity": {"en": "Bhakt Prahlada & Lord Narasimha", "hi": "भक्त प्रह्लाद व भगवान नृसिंह", "bn": "ভক্ত প্রহ্লাদ ও ভগবান শ্রীনৃসিংহ"},
        "description": {
            "en": "Burning of Holika symbolizing the triumph of devotion (Prahlada) over evil arrogance.",
            "hi": "अहंकार रूपी होलिका का भस्म होना एवं भक्त प्रह्लाद की रक्षा की स्मृति में पावन अग्नि पूजन।",
            "bn": "অহংকারের প্রতীক অসুরিকা হোলিকার দহন এবং অটল হরিভক্তির জয় উদযাপনে চাঁচর বহ্ন্যুৎসব।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Bhadra Free Evening)", "hi": "प्रदोष काल (भद्रा रहित संध्याकाल)", "bn": "প্রদোষ কাল (ভদ্রামুক্ত সন্ধ্যাবেলা)"}
    },
    ("Phalguna", "Shukla", 15): {
        "en": "Dol Jatra / Holi / Sri Gaura Purnima / Lakshmi Jayanti",
        "hi": "होली / डोल पूर्णिमा / गौर पूर्णिमा / लक्ष्मी जयंती",
        "bn": "শ্রী শ্রী দোলযাত্রা / বসন্তোৎসব / শ্রীমন্মহাপ্রভুর শুভ আবির্ভাব / হোলি",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🎨", "deity": {"en": "Radha Krishna, Sri Chaitanya & Lakshmi", "hi": "राधा-कृष्ण, श्री चैतन्य व लक्ष्मी जी", "bn": "রাধাকৃষ্ণ, শ্রীচৈতন্য মহাপ্রভু ও মা লক্ষ্মী"},
        "description": {
            "en": "Festival of colors, Dolotsav of Radha-Krishna, and divine advent of Sri Chaitanya Mahaprabhu.",
            "hi": "रंगोत्सव होली, श्रीराधा-कृष्ण का डोल उत्सव एवं श्री चैतन्य महाप्रभु का पावन प्राकट्योत्सव।",
            "bn": "রাধাকৃষ্ণের প্রেমময় দোল মহোৎসব, রঙের বসন্তোৎসব এবং শ্রী শ্রী গৌরাঙ্গ মহাপ্রভুর শুভ আবির্ভাব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Dolotsav & Pradosh Gaura Arati", "hi": "पूर्वाह्न डोल उत्सव व संध्याकाल", "bn": "পূর্বাহ্ন দোলোৎসব ও সায়ংকালীন আবির্ভাব আরতি"}
    }
}

# ==============================================================================
# ২. ভারতীয় জাতীয় ছুটির দিন ও স্মরণীয় দিবস
# ==============================================================================
INDIAN_NATIONAL_HOLIDAYS = {
    (1, 12): {
        "en": "National Youth Day (Swami Vivekananda Jayanti)", "hi": "राष्ट्रीय युवा दिवस (स्वामी विवेकानंद जयंती)", "bn": "জাতীয় যুব দিবস (স্বামী বিবেকানন্দ জয়ন্তী)",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Swami Vivekananda", "hi": "स्वामी विवेकानंद", "bn": "স্বামী বিবেকানন্দ"},
        "description": {"en": "Birth anniversary of Swami Vivekananda, inspiring youth with wisdom and character.", "hi": "युवाओं को ज्ञान, कर्म व राष्ट्रभक्ति का संदेश देने वाले स्वामी विवेकानंद की जयंती।", "bn": "চরিত্র গঠন ও দেশপ্রেমের প্রেরণাদাতা যুগনায়ক স্বামী বিবেকানন্দের জন্মজয়ন্তী।"},
        "muhurta": {"en": "Morning Commemoration (08:00 - 11:00 AM)", "hi": "प्रातः वंदन सभा (०८:०० - ११:००)", "bn": "প্রাতঃকালীন স্মরণ সভা (সকাল ০৮:০০ - ১১:০০)"}
    },
    (1, 23): {
        "en": "Parakram Diwas (Netaji Subhas Chandra Bose Jayanti)", "hi": "पराक्रम दिवस (नेताजी सुभाष चंद्र बोस जयंती)", "bn": "পরাক্রম দিবস (নেতাজি সুভাষচন্দ্র বসুর জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Observance", "hi": "राष्ट्रीय पर्व", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Netaji Subhas Chandra Bose", "hi": "नेताजी सुभाष चंद्र बोस", "bn": "নেতাজি সুভাষচন্দ্র বসু"},
        "description": {"en": "Birth anniversary of the supreme commander of the Azad Hind Fauj, Netaji Subhas Chandra Bose.", "hi": "आजाद हिंद फौज के सर्वोच्च सेनापति एवं स्वाधीनता संग्राम के महानायक नेताजी का पावन जन्मोत्सव।", "bn": "আজাদ হিন্দ ফৌজের সর্বাধিনায়ক ও ভারতের স্বাধীনতার মহানায়ক দেশনায়ক নেতাজির শুভ জন্মজয়ন্তী।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (1, 26): {
        "en": "Republic Day of India", "hi": "गणतंत्र दिवस", "bn": "ভারতের প্রজাতন্ত্র দিবস",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Holiday", "hi": "राष्ट्रीय पर्व", "bn": "জাতীয় উৎসব"},
        "deity": {"en": "Republic of India & Dr. B.R. Ambedkar", "hi": "भारत गणराज्य व डॉ. आंबेडकर", "bn": "ভারত প্রজাতন্ত্র ও ডঃ বি. আর. আম্বেদকর"},
        "description": {"en": "Commemorating the enactment of the Constitution of India in 1950.", "hi": "१९५० में भारत के संप्रभु लोकतांत्रिक संविधान के लागू होने का राष्ट्रीय गौरव दिवस।", "bn": "১৯৫০ সালের ২৬শে জানুয়ারি ভারতীয় সংবিধান আনুষ্ঠানিকভাবে কার্যকর হওয়ার ঐতিহাসিক জাতীয় দিবস।"},
        "muhurta": {"en": "Morning Flag Hoisting (08:00 - 10:30 AM)", "hi": "प्रातः ध्वजारोहण (०८:०० - १०:३०)", "bn": "সকালবেলা জাতীয় পতাকা উত্তোলন (০৮:০০ - ১০:৩০)"}
    },
    (1, 30): {
        "en": "Martyrs' Day (Shaheed Diwas / Mahatma Gandhi Punyatithi)", "hi": "शहीद दिवस (महात्मा गांधी पुण्यतिथि)", "bn": "শহীদ দিবস (মহাত্মা গান্ধীর প্রয়াণ দিবস)",
        "category": "national", "icon": "🕯️", "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "জাতীয় শোক ও শ্রদ্ধা দিবস"},
        "deity": {"en": "Mahatma Gandhi & Freedom Martyrs", "hi": "महात्मा गांधी व समस्त अमर शहीद", "bn": "মহাত্মা গান্ধী ও অমর শহীদগণ"},
        "description": {"en": "Nationwide 2-minute silence observing the supreme sacrifices of all freedom fighters.", "hi": "राष्ट्रपिता महात्मा गांधी की पुण्यतिथि पर देश के समस्त अमर शहीदों की पावन स्मृति में मौन व श्रद्धांजलि।", "bn": "মহাত্মা গান্ধীর প্রয়াণ দিবসে দেশের সমস্ত বীর শহীদ ও বিপ্লবীদের প্রতি ২ মিনিটের নীরব শ্রদ্ধাঞ্জলি।"},
        "muhurta": {"en": "11:00 AM (2-Minute National Silence)", "hi": "पूर्वाह्न ११:०० (२ मिनट मौन श्रद्धांजलि)", "bn": "সকাল ১১:০০ (২ মিনিট জাতীয় নীরবতা পালন)"}
    },
    (4, 14): {
        "en": "Dr. B.R. Ambedkar Jayanti (Equality Day)", "hi": "डॉ. बी.आर. आंबेडकर जयंती (समानता दिवस)", "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী (সাম্য দিবস)",
        "category": "national", "icon": "📜", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Babasaheb Dr. B.R. Ambedkar", "hi": "बाबासाहेब डॉ. भीमराव आंबेडकर", "bn": "বাবাসাহেব ডঃ বি. আর. আম্বেদকর"},
        "description": {"en": "Birth anniversary of the chief architect of the Indian Constitution and crusader of social equality.", "hi": "संविधान निर्माता एवं वंचितों के उत्थान के मसीहा भारत रत्न बाबासाहेब आंबेडकर की जयंती।", "bn": "ভারতীয় সংবিধানের প্রধান স্থপতি ও সমাজ সংস্কারক ভারতরত্ন বাবাসাহেব আম্বেদকরের জন্মজয়ন্তী।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (8, 15): {
        "en": "Independence Day of India", "hi": "स्वतंत्रता दिवस", "bn": "ভারতের স্বাধীনতা দিবস",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Holiday", "hi": "राष्ट्रीय महापर्व", "bn": "জাতীয় মহোৎসব"},
        "deity": {"en": "Bharat Mata & All Freedom Fighters", "hi": "भारत माता व समस्त अमर बलिदानी", "bn": "ভারত মাতা ও সমস্ত স্বাধীনতা সংগ্রামী"},
        "description": {"en": "Celebration of India achieving freedom from British colonial rule on August 15, 1947.", "hi": "१५ अगस्त १९४७ को प्राप्त भारत की स्वाधीनता का पावन राष्ट्रीय स्वतंत्रता उत्सव।", "bn": "১৯৪৭ সালের ১৫ই আগস্ট পরাধীনতার শৃঙ্খল ভেঙে স্বাধীনতা অর্জনের মহান ও গৌরবময় দিন।"},
        "muhurta": {"en": "Morning Flag Hoisting (07:30 - 10:00 AM)", "hi": "प्रातः ध्वजारोहण (०७:३० - १०:००)", "bn": "প্রাতঃকালে জাতীয় পতাকা উত্তোলন (সকাল ০৭:৩০ - ১০:০০)"}
    },
    (10, 2): {
        "en": "Mahatma Gandhi Jayanti & Lal Bahadur Shastri Jayanti", "hi": "गांधी जयंती व लाल बहादुर शास्त्री जयंती", "bn": "গান্ধী জয়ন্তী ও লাল বাহাদুর শাস্ত্রী জন্মজয়ন্তী",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Holiday", "hi": "राष्ट्रीय महापर्व", "bn": "জাতীয় মহোৎসব"},
        "deity": {"en": "Mahatma Gandhi & Lal Bahadur Shastri", "hi": "महात्मा गांधी व लाल बहादुर शास्त्री", "bn": "মহাত্মা গান্ধী ও লাল বাহাদুর শাস্ত্রী"},
        "description": {"en": "Birth anniversaries of Father of the Nation Mahatma Gandhi and Prime Minister Shastri.", "hi": "सत्य-अहिंसा के प्रणेता महात्मा गांधी एवं 'जय जवान जय किसान' के उद्घोषक शास्त्री जी की पावन जयंती।", "bn": "অহিংসার দূত মহাত্মা গান্ধী এবং 'জয় জওয়ান জয় কিষাণ' স্লোগানের রূপকার লাল বাহাদুর শাস্ত্রীর জন্মতিথি।"},
        "muhurta": {"en": "Morning Prayer Assembly (08:00 - 10:30 AM)", "hi": "प्रातः सर्वधर्म प्रार्थना (०८:०० - १०:३०)", "bn": "প্রাতঃকালীন সর্বধর্ম প্রার্থনা সভা (সকাল ০৮:০০ - ১০:৩০)"}
    },
    (10, 31): {
        "en": "National Unity Day (Rashtriya Ekta Diwas / Sardar Patel Jayanti)", "hi": "राष्ट्रीय एकता दिवस (सरदार वल्लभभाई पटेल जयंती)", "bn": "জাতীয় একতা দিবস (সর্দার বল্লভভাই প্যাটেল জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Sardar Vallabhbhai Patel (Iron Man of India)", "hi": "लौह पुरुष सरदार वल्लभभाई पटेल", "bn": "লৌহমানব সর্দার বল্লভভাই প্যাটেল"},
        "description": {"en": "Honouring the Iron Man of India for integrating over 560 princely states into one united republic.", "hi": "५६० से अधिक रियासतों का विलय कर अखंड भारत का निर्माण करने वाले लौह पुरुष का पावन जन्मोत्सव।", "bn": "৫৬০-র বেশি দেশীয় রাজ্যকে এক করে অখণ্ড ভারত গড়ার রূপকার লৌহমানব সর্দার প্যাটেলের জন্মতিথি।"},
        "muhurta": {"en": "Morning Unity Run (06:30 - 09:00 AM)", "hi": "प्रातः एकता दौड़ (०६:३० - ०९:००)", "bn": "প্রাতঃকালীন একতা পদযাত্রা (সকাল ০৬:৩০ - ০৯:০০)"}
    },
    (11, 14): {
        "en": "Children's Day (Jawaharlal Nehru Jayanti)", "hi": "बाल दिवस (जवाहरलाल नेहरू जयंती)", "bn": "শিশু দিবস (পণ্ডিত জওহরলাল নেহেরু জন্মজয়ন্তী)",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Pt. Jawaharlal Nehru (Chacha Nehru)", "hi": "पं. जवाहरलाल नेहरू (चाचा नेहरू)", "bn": "পণ্ডিত জওহরলাল নেহরু (চাচা নেহরু)"},
        "description": {"en": "Birth anniversary of India's first Prime Minister, dedicated to child welfare and development.", "hi": "बच्चों के प्यारे 'चाचा नेहरू' के जन्मोत्सव पर बाल कल्याण ও शिक्षा संवर्धन दिवस।", "bn": "স্বাধীন ভারতের প্রথম প্রধানমন্ত্রী পণ্ডিত নেহরুর শিশুদের প্রতি স্নেহের স্মরণে শিশু কল্যাণ দিবস।"},
        "muhurta": {"en": "All Day School Celebrations", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন বিদ্যালয়ভিত্তিক উৎসব"}
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
        "description": {"en": "Festival marking the end of the sacred month of Ramadan fasting.", "hi": "रमजान के पवित्र माह के उपवासों (रोज़े) की पूर्णता पर खुशी व भाईचारे का महापर्व।", "bn": "পবিত্র মাহে রমজানের মাসব্যাপী সিয়াম সাধনার শেষে আনন্দ ও ভাতৃত্বের মহাপর্ব।"},
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
        "category": "hindu", "icon": "🐍", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "deity": {"en": "Maa Manasa", "hi": "माँ मनसा देवी", "bn": "মা মনসা দেবী"},
        "description": {"en": "Grand annual worship of Goddess Manasa across Bengal and Assam on Singha Sankranti.", "hi": "सिंह संक्रांति पर बंगाल व असम में विष निवारक माँ मनसा की प्रधान वार्षिक महापूजा।", "bn": "সিংহ সংক্রান্তির পুণ্যলগ্নে সর্পভয়নাশিনী মা মনসার বার্ষিক মহোৎসব ও পূজা সমাপন।"},
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
        "category": "hindu", "icon": "🦚", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "deity": {"en": "Lord Kartikeya", "hi": "भगवान कार्तिकेय", "bn": "দেব সেনাপতি কার্তিক"},
        "description": {"en": "Worship of commander-in-chief Lord Kartikeya on Kartik Sankranti for beauty, courage, and offspring.", "hi": "कार्तिक संक्रांति पर सुयोग्य संतान व साहस प्राप्ति हेतु देवसेनापति कार्तिकेय का पूजन।", "bn": "কার্তিক সংক্রান্তির রাতে রূপবান সন্তান ও বীর্যবত্তার কামনায় দেব সেনাপতি কার্তিকের আরাধনা।"},
        "muhurta": {"en": "Pradosh Kaal (Evening 05:15 - 08:30 PM)", "hi": "प्रदोष काल (संध्या ०५:१५ - ०८:३०)", "bn": "প্রদোষ কাল (সন্ধ্যা ০৫:১৫ - ০৮:৩০)"}
    }
}

def get_language_key(lang: str = "en") -> str:
    value = str(lang or "en").lower().strip()
    if value.startswith("bn") or "বাংলা" in value: return "bn"
    if value.startswith("hi") or "हि" in value: return "hi"
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

    # ১. তিথিভিত্তিক সনাতন উৎসব (HINDU_FESTIVAL_DATABASE)
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
                "muhurta_type": item.get("muhurta_type", "pradosh"),
                "muhurta_label": resolve_field(item.get("muhurta_label"), l_key),
                "muhurta": ""  # panchang.py রিয়েল-টাইমে সুইস এফিমেরিস থেকে হিসাব করে বসাবে
            }
        )

    # ২. সর্বভারতীয় একাদশী ব্রত (Ekadashi Vrata)
    if tithi_num == 11:
        ekadashi_name = {"en": "Ekadashi Vrata / Fast", "hi": "एकादशी व्रत", "bn": "একাদশী ব্রত ও উপবাস"}
        ekadashi_deity = {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"}
        ekadashi_desc = {
            "en": "Sacred fasting day dedicated to Lord Vishnu to cleanse sins and attain spiritual devotion.",
            "hi": "समस्त पापों के नाश एवं भगवान विष्णु की कृपा प्राप्ति हेतु पावन निर्जला/फलाहार व्रत।",
            "bn": "ভগবান শ্রীহরি বিষ্ণুর প্রীত্যর্থে পাপক্ষয় ও আধ্যাত্মিক কল্যাণ কামনায় পরম পবিত্র উপবাস ব্রত।"
        }
        append_festival_once(
            festivals,
            {
                "name": ekadashi_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🕉️",
                "deity": ekadashi_deity[l_key],
                "description": ekadashi_desc[l_key],
                "muhurta_type": "brahma",
                "muhurta_label": {"en": "Brahma Muhurta (Fast Sankalp)", "hi": "ब्रह्म मुहूर्त (व्रत संकल्प)", "bn": "ব্রাহ্ম মুহূর্ত (ব্রত সঙ্কল্প)"}[l_key],
                "muhurta": ""
            }
        )

    # ৩. প্রদোষ ব্রত (Pradosh Vrata)
    elif tithi_num == 13:
        pradosh_name = {"en": "Pradosh Vrata", "hi": "प्रदोष व्रत", "bn": "প্রদোষ ব্রত"}
        pradosh_deity = {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "ভগবান দেবাদিদেব মহাদেব"}
        pradosh_desc = {
            "en": "Twilight worship of Lord Shiva to attain peace, health, and freedom from distress.",
            "hi": "संध्याकाल (प्रदोष काल) में भगवान शिव की आराधना से सुख, आरोग्य एवं संकट मुक्ति।",
            "bn": "সন্ধ্যাবেলায় দেবাদিদেব মহাদেবের আরাধনা করে সর্বসংকট মুক্তি ও মানসিক শান্তি লাভের ব্রত।"
        }
        append_festival_once(
            festivals,
            {
                "name": pradosh_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🔱",
                "deity": pradosh_deity[l_key],
                "description": pradosh_desc[l_key],
                "muhurta_type": "pradosh",
                "muhurta_label": {"en": "Pradosh Kaal Muhurta", "hi": "प्रदोष काल मुहूर्त", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যাবেলা)"}[l_key],
                "muhurta": ""
            }
        )

    # ৪. সত্যনারায়ণ পূজা (Purnima Vrata)
    elif tithi_num == 15 and paksha == "Shukla":
        purnima_name = {"en": "Purnima Vrata / Sri Satyanarayan Puja", "hi": "पूर्णिमा व्रत / श्री सत्यनारायण पूजा", "bn": "পূর্ণিমা ব্রত / শ্রী সত্যনারায়ণ পূজা"}
        purnima_deity = {"en": "Lord Sri Satyanarayan (Vishnu)", "hi": "भगवान श्री सत्यनारायण", "bn": "শ্রী সত্যনারায়ণ নারায়ণ"}
        purnima_desc = {
            "en": "Offering Panchamrit, Shinni bhog, and Katha to Lord Satyanarayan on full moon.",
            "hi": "श्री सत्यनारायण भगवान का पंचामृत भोग, कथा श्रवण एवं पूर्णिमा चंद्र दर्शन।",
            "bn": "শ্রীশ্রী সত্যনারায়ণ দেবের পঞ্চামৃত সিন্নি ভোগ, মাহাত্ম্য কথা শ্রবণ ও পূর্ণিমা উপবাস।"
        }
        append_festival_once(
            festivals,
            {
                "name": purnima_name[l_key],
                "category": "hindu",
                "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
                "icon": "🌕",
                "deity": purnima_deity[l_key],
                "description": purnima_desc[l_key],
                "muhurta_type": "pradosh",
                "muhurta_label": {"en": "Pradosh Kaal (Katha & Puja)", "hi": "प्रदोष काल (कथा व पूजन)", "bn": "প্রদোষ কাল (সন্ধ্যায় সিন্নি ভোগ ও কথা)"}[l_key],
                "muhurta": ""
            }
        )

    # ৫. সৌর সংক্রান্তি ও নির্দিষ্ট পূজা (Solar Festivals)
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
        append_festival_once(festivals, {
            "name": nil_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "🔱", "deity": nil_deity[l_key], "description": nil_desc[l_key],
            "muhurta_type": "pradosh", "muhurta_label": {"en": "Pradosh Kaal", "hi": "प्रदोष काल", "bn": "প্রদোষ কাল"}[l_key], "muhurta": ""
        })

    elif m_d == (4, 15) or ("mesha" in s_name or "aries" in s_name):
        mesha_names = {"en": "Mesha Sankranti / Poila Boishakh", "hi": "मेष संक्रांति / पोइला बैशाख", "bn": "পয়লা বৈশাখ / মেষ সংক্রান্তি (শুভ নববর্ষ)"}
        mesha_deity = {"en": "Surya Deva & Ganesha", "hi": "सूर्य देव व गणेश जी", "bn": "ভগবান সূর্য দেব ও শ্রী গণেশ"}
        mesha_desc = {
            "en": "Solar New Year marking Sun's entry into Aries, opening new business ledgers (Hal Khata).",
            "hi": "सूर्य का मेष राशि में प्रवेश, सौर नववर्षारंभ एवं नए व्यापारिक बहीखातों का पूजन।",
            "bn": "মেষ রাশিতে সূর্যের শুভ প্রবেশ, বাংলা সৌর নববর্ষ উদযাপন ও ব্যবসায়িক শুভ হালখাতা পূজা।"
        }
        append_festival_once(festivals, {
            "name": mesha_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "🌾", "deity": mesha_deity[l_key], "description": mesha_desc[l_key],
            "muhurta_type": "purvahna", "muhurta_label": {"en": "Purvahna Kaal (Morning Puja)", "hi": "पूर्वाह्न काल (प्रातः पूजा)", "bn": "পূর্বাহ্ন কাল (সকালবেলা পূজা)"}[l_key], "muhurta": ""
        })

    elif m_d == (1, 14) or ("makar" in s_name or "capricorn" in s_name):
        makar_names = {"en": "Makar Sankranti / Pongal / Poush Parbon", "hi": "मकर संक्रांति / पोंगल", "bn": "মকর সংক্রান্তি / পৌষ সংক্রান্তি / পৌষ পার্বণ ও গঙ্গাসাগর স্নান"}
        makar_deity = {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"}
        makar_desc = {
            "en": "Sun transits into Capricorn (Makara) marking the auspicious Uttarayana, observed with Gangasagar snan and sesame charity.",
            "hi": "सूर्य का मकर राशि में प्रवेश, उत्तरायण आरंभ एवं गंगासागर महास्नान व तिल-गुड़ दान का महापर्व।",
            "bn": "সূর্যের মকর রাশিতে উত্তরায়ণ গমন, গঙ্গাসাগর তীর্থে পুণ্যস্নান ও নতুন শস্যের পিঠেপুলির পৌষ পার্বণ।"
        }
        append_festival_once(festivals, {
            "name": makar_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": makar_deity[l_key], "description": makar_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Makara Sankranti Punya Kaal", "hi": "मकर संक्रांति पुण्य काल", "bn": "মকর সংক্রান্তি পুণ্যকাল স্নান ও দান"}[l_key], "muhurta": ""
        })

    elif m_d == (9, 17) or ("kanya" in s_name or "virgo" in s_name):
        kanya_names = {"en": "Kanya Sankranti / Vishwakarma Puja", "hi": "कन्या संक्रांति / विश्वकर्मा पूजा", "bn": "কন্যা সংক্রান্তি / শ্রী শ্রী বিশ্বকর্মা পূজা"}
        kanya_deity = {"en": "Lord Vishwakarma", "hi": "भगवान विश्वकर्मा", "bn": "দেবশিল্পী শ্রী শ্রী বিশ্বকর্মা"}
        kanya_desc = {
            "en": "Worship of the divine celestial architect and craftsman, Lord Vishwakarma, in factories and workshops.",
            "hi": "दिव्य वास्तुकार भगवान विश्वकर्मा का यंत्रों, कारखानों व शिल्प संस्थानों में विधिपूर्वक पूजन।",
            "bn": "দেবশিল্পী বিশ্বকর্মার চরণে শিল্প, কলকারখানা ও যন্ত্রপাতির সমৃদ্ধির কামনায় বিশেষ অর্ঘ্য নিবেদন।"
        }
        append_festival_once(festivals, {
            "name": kanya_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "⚙️", "deity": kanya_deity[l_key], "description": kanya_desc[l_key],
            "muhurta_type": "purvahna", "muhurta_label": {"en": "Purvahna & Abhijit Muhurta", "hi": "पूर्वाह्न व अभिजित मुहूर्त", "bn": "পূর্বাহ্ন ও অভিজিৎ মুহূর্ত"}[l_key], "muhurta": ""
        })

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

    # festivals.py ফাইলের একদম শেষে এই ফাংশনটি যুক্ত করুন:

def compute_dynamic_festival_muhurta(festival_name: str, festival_type: str, sunrise_min: int, sunset_min: int, lang: str = "bn") -> dict:
    dina_mana = sunset_min - sunrise_min
    if dina_mana <= 0:
        dina_mana += 1440
    ratri_mana = 1440 - dina_mana

    def min_to_12hr(m: int) -> str:
        m = int(m % 1440)
        hh = m // 60
        mm = m % 60
        period = "AM" if hh < 12 else "PM"
        hh_12 = hh % 12
        if hh_12 == 0:
            hh_12 = 12
        time_str = f"{hh_12:02d}:{mm:02d} {period}"
        if lang == "bn":
            bangla_digits = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
            return time_str.translate(bangla_digits)
        elif lang == "hi":
            hindi_digits = str.maketrans("0123456789", "०१२३४५६७८९")
            return time_str.translate(hindi_digits)
        return time_str

    fn_lower = festival_name.lower()
    
    # বিনায়ক চতুর্থী (দুপুরবেলা / মধ্যাহ্ন কাল)
    if "vinayaka" in fn_lower or "ganesh" in fn_lower or "চতুর্থী" in fn_lower or "चतुर्थी" in fn_lower:
        start_min = sunrise_min + (dina_mana * 2 / 5.0)
        end_min = sunrise_min + (dina_mana * 3 / 5.0)
        type_labels = {
            "bn": "মধ্যাহ্ন গণেশ পূজা মুহূর্ত (দুপুরবেলা)",
            "hi": "मध्याह्न गणेश पूजा मुहूर्त (दोपहर)",
            "en": "Madhyahna Ganesha Puja Muhurta (Afternoon)"
        }
        label_text = {"bn": "শুভ মুহূর্ত:", "hi": "शुभ मुहूर्त:", "en": "Auspicious Timing:"}
        return {
            "label": label_text.get(lang, "Auspicious Timing:"),
            "muhurta_type": type_labels.get(lang, type_labels["en"]),
            "start_time": min_to_12hr(start_min),
            "end_time": min_to_12hr(end_min),
            "formatted_display": f"{type_labels.get(lang, type_labels['en'])} ({min_to_12hr(start_min)} - {min_to_12hr(end_min)})"
        }

    # শিবরাত্রি / মাসিক শিবরাত্রি (নিশীথ কাল / মধ্যরাত্রি)
    elif "shivratri" in fn_lower or "শিবরাত্রি" in fn_lower or "शिवरात्रि" in fn_lower:
        solar_midnight = sunset_min + (ratri_mana / 2.0)
        start_min = solar_midnight - 24
        end_min = solar_midnight + 24
        type_labels = {
            "bn": "নিশীথ কাল পূজা মুহূর্ত (রাত্রিবেলা)",
            "hi": "निशीथ काल पूजा मुहूर्त (रात्रि)",
            "en": "Nishita Kala Shiva Puja Muhurta (Night)"
        }
        label_text = {"bn": "পূজার শুভ মুহূর্ত:", "hi": "पूजा का शुभ मुहूर्त:", "en": "Puja Muhurta:"}
        return {
            "label": label_text.get(lang, "Puja Muhurta:"),
            "muhurta_type": type_labels.get(lang, type_labels["en"]),
            "start_time": min_to_12hr(start_min),
            "end_time": min_to_12hr(end_min),
            "formatted_display": f"{type_labels.get(lang, type_labels['en'])} ({min_to_12hr(start_min)} - {min_to_12hr(end_min)})"
        }

    # প্রদোষ ব্রত / সত্যনারায়ণ পূজা / সন্ধ্যা পূজা
    elif "pradosh" in fn_lower or "প্রদোষ" in fn_lower or "satyanarayan" in fn_lower or "সত্যনারায়ণ" in fn_lower:
        start_min = sunset_min
        end_min = sunset_min + 144
        type_labels = {
            "bn": "প্রদোষ কাল (সন্ধ্যাবেলা)",
            "hi": "प्रदोष काल (संध्या)",
            "en": "Pradosh Kala Muhurta (Evening)"
        }
        label_text = {"bn": "পূজার শুভ মুহূর্ত:", "hi": "पूजा का शुभ मुहूर्त:", "en": "Puja Muhurta:"}
        return {
            "label": label_text.get(lang, "Puja Muhurta:"),
            "muhurta_type": type_labels.get(lang, type_labels["en"]),
            "start_time": min_to_12hr(start_min),
            "end_time": min_to_12hr(end_min),
            "formatted_display": f"{type_labels.get(lang, type_labels['en'])} ({min_to_12hr(start_min)} - {min_to_12hr(end_min)})"
        }

    # সাধারণ শুভ মুহূর্ত (অভিজিৎ / দিবস মুহূর্ত)
    else:
        one_muhurta = dina_mana / 15.0
        start_min = sunrise_min + (7 * one_muhurta)
        end_min = sunrise_min + (8 * one_muhurta)
        type_labels = {
            "bn": "অভিজিৎ শুভ মুহূর্ত (দুপুরবেলা)",
            "hi": "अभिजित शुभ मुहूर्त (दोपहर)",
            "en": "Abhijit Auspicious Muhurta"
        }
        label_text = {"bn": "শুভ মুহূর্ত:", "hi": "शुभ मुहूर्त:", "en": "Auspicious Timing:"}
        return {
            "label": label_text.get(lang, "Auspicious Timing:"),
            "muhurta_type": type_labels.get(lang, type_labels["en"]),
            "start_time": min_to_12hr(start_min),
            "end_time": min_to_12hr(end_min),
            "formatted_display": f"{type_labels.get(lang, type_labels['en'])} ({min_to_12hr(start_min)} - {min_to_12hr(end_min)})"
        }

