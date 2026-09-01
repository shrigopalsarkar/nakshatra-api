from datetime import date
from typing import List, Dict, Any, Optional

# ==============================================================================
# ১. সনাতন/হিন্দু তিথিভিত্তিক সমস্ত পূজা, ব্রত, তাৎপর্য ও শাস্ত্রীয় পূজার মুহূর্ত
# ==============================================================================
HINDU_FESTIVAL_DATABASE = {
    # --------------------------------------------------------------------------
    # চৈত্র মাস (Chaitra)
    # --------------------------------------------------------------------------
    ("Chaitra", "Krishna", 2): {
        "en": "Bhai Dooj / Bhratri Dwitiya (Holi Bhai Dooj)",
        "hi": "भाई दूज / भ्रातृ द्वितीया (होली भाई दूज)",
        "bn": "ভ্রাতৃদ্বিতীয়া / ভাইদুজ (হোলি ভাইফোঁটা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Yamuna & Yamaraja", "hi": "यमुना जी व यमराज", "bn": "যমুনা দেবী ও যমরাজ"},
        "description": {
            "en": "Post-Holi celebration of brother-sister bond with tilak and prayers for brother's longevity.",
            "hi": "होली के उपरांत भाई-बहन के अटूट स्नेह का प्रतीक भ्रातृ द्वितीया (भाई दूज) तिलक पर्व।",
            "bn": "হোলি উৎসব পরবর্তী ভাই-বোনের পবিত্র স্নেহবন্ধন ও ভাইয়ের দীর্ঘায়ু কামনায় ভ্রাতৃদ্বিতীয়া তিলক উৎসব।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tilak Muhurta", "hi": "अपराह्न तिलक मुहूर्त", "bn": "অপরাহ্ন ভাইফোঁটা লগ্ন"}
    },
    ("Chaitra", "Krishna", 4): {
        "en": "Bhalachandra Sankashti Chaturthi",
        "hi": "भालचंद्र संकष्टी चतुर्थी",
        "bn": "শ্রী ভালচন্দ্র সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Bhalachandra Ganesha & Chandra", "hi": "भगवान भालचंद्र गणेश व चन्द्र देव", "bn": "ভগবান ভালচন্দ্র শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Fasting dedicated to Lord Bhalachandra Ganesha to dispel obstacles, broken after moonrise sighting.",
            "hi": "समस्त संकटों के निवारण हेतु भगवान भालचंद्र गणेश का पावन व्रत एवं चंद्रोदय अर्घ्य।",
            "bn": "সর্ববিঘ্ন ও সঙ্কট দূরীকরণে শ্রী ভালচন্দ্র গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Bhalachandra Puja", "hi": "चन्द्रोदय व पूजन मुहूर्त", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}
    },
    ("Chaitra", "Krishna", 5): {
        "en": "Ranga Panchami",
        "hi": "रंग पंचमी",
        "bn": "শ্রী শ্রী রঙ্গ পঞ্চমী মহোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🎨", "deity": {"en": "Sri Radha Krishna & Devas", "hi": "श्रीराधा-कृष्ण व देवगण", "bn": "শ্রীশ্রী রাধাকৃষ্ণ ও দেবগণ"},
        "description": {
            "en": "Joyous celebration of colors dedicated to invocation of positive celestial energies with Gulal.",
            "hi": "देवताओं के स्वागत एवं सकारात्मक ऊर्जा के संचरण हेतु गुलाल-अबीर का पावन रंग पंचमी उत्सव।",
            "bn": "দেবতাদের সন্তুষ্টি ও সমাজে পবিত্র আনন্দ ছড়িয়ে দিতে আবির ও গুলালের ঐশ্বরিক রঙ্গ পঞ্চমী মহোৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Rangaotsav", "hi": "पूर्वाह्न रंगोत्सव", "bn": "পূর্বাহ্ন আবির খেলা ও দেব পূজা"}
    },
    ("Chaitra", "Krishna", 8): {
        "en": "Sheetala Ashtami / Basoda",
        "hi": "शीतला अष्टमी / बसोड़ा",
        "bn": "শ্রী শ্রী শীতলা অষ্টমী ব্রত (বাসোড়া)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Maa Sheetala", "hi": "माँ शीतला", "bn": "মা শীতলা দেবী"},
        "description": {
            "en": "Worship of Maa Sheetala offering stale food (Basoda) to seek protection from ailments.",
            "hi": "आरोग्यता एवं चेचक आदि रोगों से रक्षा हेतु बासी भोजन के भोग सहित माँ शीतला का पूजन।",
            "bn": "নীরোগ স্বাস্থ্য ও মহামারী থেকে সুরক্ষার কামনায় শীতল অন্ন নিবেদনে মা শীতলার বিশেষ ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Sheetala Puja", "hi": "पूर्वाह्न शीतला पूजा", "bn": "পূর্বাহ্ন শীতলা পূজা লগ্ন"}
    },
    ("Chaitra", "Krishna", 11): {
        "en": "Papmochani Ekadashi",
        "hi": "पापमोचिनी एकादशी",
        "bn": "পাপমোচিনী একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Fasting on Papmochani Ekadashi cleanses past misdeeds and grants spiritual purity.",
            "hi": "समस्त पापों के प्रायश्चित एवं आत्मशुद्धि हेतु पावन एकादशी व्रत।",
            "bn": "সর্বপাপ দূরীকরণ ও চিত্তশুদ্ধির কামনায় পরম পবিত্র পাপমোচিনী একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Parana & Vrata", "hi": "प्रातः पारण व पूजा", "bn": "প্রাতঃকালীন পারণ ও ব্রত"}
    },
    ("Chaitra", "Shukla", 1): {
        "en": "Chaitra Navratri Begins / Gudi Padwa / Basanti Durga Puja Bodhan / Ishti",
        "hi": "चैत्र नवरात्रि प्रारंभ / गुड़ी पड़वा / वासंतिक दुर्गा पूजा बोधन / इष्टि",
        "bn": "চৈত্র নবরাত্রি আরম্ভ / বাসন্তী দুর্গাপূজা বোধন / গুড়ি পাড়ওয়া / ইষ্টি",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Maa Shailaputri", "hi": "माँ दुर्गा व माँ शैलपुत्री", "bn": "মা দুর্গা ও দেবী শৈলপুত্রী"},
        "description": {
            "en": "Sacred beginning of Chaitra Vasantik Navratri with Ghatasthapana, Gudi Padwa and Vedic Ishti.",
            "hi": "घटस्थापना, गुड़ी पड़वा व माँ शैलपुत्री आराधना के साथ चैत्र वासंतिक नवरात्रि का शुभारंभ।",
            "bn": "ঘটস্থাপন, গুড়ি পাড়ওয়া ও বোধন পূজার মাধ্যমে চৈত্র বাসন্তী নবরাত্রির শুভ সূচনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Morning Muhurta", "hi": "घटस्थापना व प्रातः मुहूर्त", "bn": "ঘটস্থাপন ও প্রাতঃকাল মুহূর্ত"}
    },
    ("Chaitra", "Shukla", 2): {
        "en": "Sindhara Dooj / Brahmacharini Puja / Chandra Darshana",
        "hi": "सिंधारा दूज / माँ ब्रह्मचारिणी पूजा / चन्द्र दर्शन",
        "bn": "সিন্ধারা দুজ / দেবী ব্রহ্মচারিণী পূজা / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Brahmacharini & Chandra Deva", "hi": "माँ ब्रह्मचारिणी व चन्द्र देव", "bn": "দেবী ব্রহ্মচারিণী ও চন্দ্র দেব"},
        "description": {
            "en": "Worship of Maa Brahmacharini on 2nd day of Navratri and evening crescent moon sighting.",
            "hi": "तप व संयम की वृद्धि हेतु माँ ब्रह्मचारिणी का पूजन एवं सायंकाल नवचंद्र दर्शन।",
            "bn": "তপস্যা ও সংযম বৃদ্ধির উদ্দেশ্যে দেবী ব্রহ্মচারিণীর পূজা এবং সায়ংকালে নবচন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },
    ("Chaitra", "Shukla", 3): {
        "en": "Gangaur / Matsya Jayanti / Chandraghanta Puja",
        "hi": "गणगौर पूजा / मत्स्य जयंती / माँ चंद्रघंटा पूजा",
        "bn": "গণগৌর পূজা / ভগবান মৎস্য জয়ন্তী / দেবী চন্দ্রঘণ্টা পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🐟", "deity": {"en": "Lord Matsya & Maa Gauri", "hi": "भगवान मत्स्य व माँ गौरी", "bn": "ভগবান মৎস্য ও দেবী গৌরী"},
        "description": {
            "en": "Celebration of marital harmony via Gangaur Gauri worship and Lord Vishnu's fish incarnation.",
            "hi": "अखंड सौभाग्य प्राप्ति हेतु गणगौर गौरी पूजन एवं भगवान विष्णु के प्रथम मत्स्य अवतार का जन्मोत्सव।",
            "bn": "অখণ্ড দাম্পত্য সৌভাগ্যে দেবী গৌরী পূজা এবং শ্রীহরি বিষ্ণুর প্রথম মৎস্য অবতারের আবির্ভাব।"
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
            "en": "Sacred fasting and offerings dedicated to Goddess Lakshmi to attract prosperity and wealth.",
            "hi": "धन-धान्य, ऐश्वर्य एवं सौभाग्य की प्राप्ति हेतु चैत्र शुक्ल पंचमी पर माँ लक्ष्मी की आराधना।",
            "bn": "ধনধান্য ও সৌভাগ্য বৃদ্ধির কামনায় চৈত্র শুক্ল পঞ্চমীতে দেবী লক্ষ্মীর চরণে বিশেষ পূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल (संध्याकाल)", "bn": "প্রদোষ কাল মুহূর্ত (সন্ধ্যাবেলা)"}
    },
    ("Chaitra", "Shukla", 6): {
        "en": "Yamuna Chhath / Yamuna Jayanti",
        "hi": "यमुना छठ / यमुना जयंती",
        "bn": "শ্রী শ্রী যমুনা ষষ্ঠী (যমুনা দেবীর শুভ আবির্ভাব)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌊", "deity": {"en": "Goddess Yamuna", "hi": "माँ यमुना देवी", "bn": "মা যমুনা দেবী"},
        "description": {
            "en": "Appearance day of sacred River Yamuna on Chaitra Shukla Shashthi, celebrated with holy dip and deepam.",
            "hi": "चैत्र शुक्ल षष्ठी पर माँ यमुना का अवतरण दिवस, यमुना स्नान एवं दीपदान का पावन पर्व।",
            "bn": "চৈত্র শুক্ল ষষ্ঠীতে পতিতপাবনী যমুনা দেবীর মর্ত্যে শুভ আবির্ভাব ও তীর্থস্নান মহোৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Yamuna Puja", "hi": "पूर्वाह्न यमुना पूजन", "bn": "পূর্বাহ্ন যমুনা পূজা ও আরতি"}
    },
    ("Chaitra", "Shukla", 8): {
        "en": "Basanti Maha Ashtami / Annapurna Puja / Mahagauri Puja",
        "hi": "माँ अन्नपूर्णा पूजा / बासंती महाष्टमी / महागौरी पूजा",
        "bn": "শ্রী শ্রী অন্নপূর্ণা পূজা / বাসন্তী মহাষ্টমী ও কুমারী পূজা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महाপर्व", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Annapurna & Mahagauri", "hi": "माँ अन्नपूर्णा व महागौरी", "bn": "মা অন্নপূর্ণা ও দেবী মহাগৌরী"},
        "description": {
            "en": "Worship of Maa Annapurna for abundance, alongside Basanti Maha Ashtami Kumari Puja.",
            "hi": "धन-धान्य अधिष्ठात्री माँ अन्नपूर्णा एवं बासंती महाष्टमी पर कन्या (कुमारी) पूजन।",
            "bn": "অন্নদাত্রী মা অন্নপূর্ণার বিশেষ আরাধনা এবং বাসন্তী মহাষ্টমীতে পবিত্র কুমারী পূজা।"
        },
        "muhurta_type": "sandhi",
        "muhurta_label": {"en": "Sandhi Puja Muhurta (48 mins)", "hi": "संधि पूजा मुहूर्त (४८ मिनट)", "bn": "সন্ধিপূজা মুহূর্ত (৪৮ মিনিট)"}
    },
    ("Chaitra", "Shukla", 9): {
        "en": "Sri Rama Navami / Swaminarayan Jayanti / Basanti Navami",
        "hi": "श्री राम नवमी / स्वामीनारायण जयंती / बासंती महानवमी",
        "bn": "শ্রী শ্রী রাম নবমী / ভগবান স্বামীনারায়ণ জয়ন্তী / বাসন্তী নবমী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🏹", "deity": {"en": "Lord Sri Rama & Bhagwan Swaminarayan", "hi": "भगवान श्रीराम व स्वामीनारायण", "bn": "ভগবান শ্রীরামচন্দ্র ও স্বামীনারায়ণ"},
        "description": {
            "en": "Divine appearance day of Maryada Purushottam Lord Sri Rama and Bhagwan Swaminarayan at noon.",
            "hi": "दोपहर में मर्यादा पुरुषोत्तम श्रीराम एवं भगवान स्वामीनारायण का पावन जन्मोत्सव।",
            "bn": "শুভ দ্বিপ্রহরে পরম পুরুষোত্তম ভগবান শ্রীরামচন্দ্র ও ভগবান স্বামীনারায়ণের শুভ আবির্ভাব মহোৎসব।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত (আবির্ভাব লগ্ন)"}
    },
    ("Chaitra", "Shukla", 11): {
        "en": "Kamada Ekadashi",
        "hi": "कामदा एकादशी",
        "bn": "কামদা একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Kamada Ekadashi fulfills all righteous desires and eliminates negative karmas.",
            "hi": "मनोकामना पूर्ति एवं पापमुक्ति हेतु चैत्र शुक्ल कामदा एकादशी व्रत।",
            "bn": "মনোবাঞ্ছা পূরণ ও পাপক্ষয়ের জন্য চৈত্র শুক্ল কামদা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Worship", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Chaitra", "Shukla", 13): {
        "en": "Mahavir Jayanti",
        "hi": "महावीर जयंती",
        "bn": "শ্রী মহাবীর জয়ন্তী (২৪তম তীর্থঙ্কর)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🙏", "deity": {"en": "Bhagwan Mahavira", "hi": "भगवान महावीर", "bn": "ভগবান মহাবীর"},
        "description": {
            "en": "Birth anniversary of the 24th Jain Tirthankara, propagating truth, non-violence, and self-restraint.",
            "hi": "सत्य, अहिंसा एवं अपरिग्रह के संदेशवाहक २४वें तीर्थंकर भगवान महावीर का पावन जन्मोत्सव।",
            "bn": "সত্য, অহিংসা ও করুণার বাণী প্রচারক চতুর্বিংশতি তীর্থঙ্কর ভগবান মহাবীরের আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Abhisheka & Rally", "hi": "प्रातः महामस्तकाभिषेक", "bn": "প্রাতঃকালীন মহাজলাভিষেক ও প্রার্থনা"}
    },
    ("Chaitra", "Shukla", 15): {
        "en": "Hanuman Jayanti / Chaitra Purnima (Satyanarayan Puja) / Anvadhan",
        "hi": "हनुमान जयंती / चैत्र पूर्णिमा (सत्यनारायण व्रत) / अन्वाधान",
        "bn": "শ্রী শ্রী হনুমান জয়ন্তী / চৈত্র পূর্ণিমা (শ্রী সত্যনারায়ণ পূজা) / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🚩", "deity": {"en": "Lord Hanuman & Sri Satyanarayan", "hi": "श्री हनुमान जी व श्री सत्यनारायण", "bn": "শ্রী হনুমানজী ও শ্রী সত্যনারায়ণ"},
        "description": {
            "en": "Birth celebration of Lord Hanuman along with Chaitra Satyanarayan Puja and Anvadhan.",
            "hi": "पवनपुत्र श्री हनुमान जी का जन्मोत्सव एवं पूर्णिमा सत्यनारायण पूजन व अन्वाधान।",
            "bn": "ভক্ত ও শক্তির প্রতীক শ্রী হনুমানজীর জন্মজয়ন্তী এবং চৈত্র পূর্ণিমার সত্যনারায়ণ পূজা ও অন্বাধান।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Morning Worship", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃকাল"}
    },

    # --------------------------------------------------------------------------
    # বৈশাখ মাস (Vaisakha)
    # --------------------------------------------------------------------------
    ("Vaishakha", "Krishna", 1): {
        "en": "Vaishakha Krishna Pratipada / Ishti Havan",
        "hi": "वैशाख कृष्ण प्रतिपदा / इष्टि",
        "bn": "বৈশাখ কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Inception of Vaishakha Krishna Paksha with holy Vedic fire oblation.",
            "hi": "वैशाख कृष्ण पक्ष का प्रारंभ एवं सुख-समृद्धि हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "বৈশাখ কৃষ্ণপক্ষের শুভ সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Vaishakha", "Krishna", 4): {
        "en": "Vikata Sankashti Chaturthi",
        "hi": "विकट संकष्टी चतुर्थी",
        "bn": "বিকট সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha (Vikata) & Chandra", "hi": "भगवान विकट गणेश व चन्द्र देव", "bn": "ভগবান বিকট শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Fasting dedicated to Lord Vikata Ganesha to eliminate severe adversities, broken at moonrise.",
            "hi": "कठिन संकटों के निवारण हेतु विकट गणेश का पावन व्रत एवं चंद्रोदय अर्घ्य।",
            "bn": "কঠিন সংকট দূরীকরণে শ্রী বিকট গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Muhurta", "hi": "चन्द्रोदय व पूजन मुहूर्त", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}
    },
    ("Vaishakha", "Krishna", 11): {
        "en": "Varuthini Ekadashi / Vallabhacharya Jayanti",
        "hi": "वरूथिनी एकादशी / वल्लभाचार्य जयंती",
        "bn": "বরূথিনী একাদশী ব্রত / বল্লভাচার্য জয়ন্তী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Vamana & Sri Vallabhacharya", "hi": "भगवान वामन व वल्लभाचार्य", "bn": "ভগবান বামন ও শ্রী বল্লভাচার্য"},
        "description": {
            "en": "Fasting on Varuthini Ekadashi protects against adversities and grants fortune.",
            "hi": "अखंड सौभाग्य व मोक्ष प्रदाता वरूथिनी एकादशी एवं महाप्रभु वल्लभाचार्य जयंती।",
            "bn": "অখণ্ড সৌভাগ্যদায়ী বরূথিনী একাদশী ও মহাপ্রভু বল্লভাচার্যের আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Vaishakha", "Shukla", 1): {
        "en": "Vaishakha Shukla Pratipada / Ishti / Chandra Darshana",
        "hi": "वैशाख शुक्ल प्रतिपदा / इष्टि / चन्द्र दर्शन",
        "bn": "বৈশাখ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🌙", "deity": {"en": "Agni Deva & Chandra Deva", "hi": "अग्नि देव व चन्द्र देव", "bn": "অগ্নি দেব ও চন্দ্র দেব"},
        "description": {
            "en": "Commencement of Vaishakha Shukla Paksha observing Ishti and auspicious crescent moon sighting.",
            "hi": "वैशाख शुक्ल पक्ष का प्रारंभ, वैदिक इष्टि एवं सायंकाल नवचंद्र दर्शन।",
            "bn": "বৈশাখ শুক্লপক্ষের সূচনা, বৈদিক ইষ্টি যজ্ঞ এবং সায়ংকালে নবচন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },
    ("Vaishakha", "Shukla", 3): {
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
    ("Vaishakha", "Shukla", 5): {
        "en": "Adi Shankaracharya Jayanti / Surdas Jayanti",
        "hi": "आदि शंकराचार्य जयंती / सूरदास जयंती",
        "bn": "আদি শঙ্করাচার্য জয়ন্তী / ভক্ত সুরদাস জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "जयंती पर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Jagadguru Adi Shankaracharya", "hi": "जगद्गुरु आदि शंकराचार्य", "bn": "জগদ্গুরু আদি শঙ্করাচার্য"},
        "description": {
            "en": "Advent of Jagadguru Adi Shankaracharya, who revived Sanatana Dharma and Advaita philosophy.",
            "hi": "अद्वैत वेदांत के प्रणेता एवं सनातन धर्म के पुनरुद्धारक जगद्गुरु आदि शंकराचार्य का प्राकट्य दिवस।",
            "bn": "অদ্বৈত বেদান্তের প্রবক্তা ও সনাতন ধর্মের রক্ষাকর্তা জগদ্গুরু আদি শঙ্করাচার্যের আবির্ভাব তিথি।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত"}
    },
    ("Vaishakha", "Shukla", 7): {
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
    ("Vaishakha", "Shukla", 8): {
        "en": "Maa Bagalamukhi Jayanti (Pitambara Jayanti)",
        "hi": "माँ बगलामुखी जयंती (पीताम्बरा जयंती)",
        "bn": "মা বগলামুখী জয়ন্তী (পীতাম্বরা আবির্ভাব)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महाविद्या जयंती", "bn": "মহাবিদ্যা মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Bagalamukhi", "hi": "माँ बगलामुखी (पीताम्बरा)", "bn": "মা বগলামুখী দেবী"},
        "description": {
            "en": "Appearance of the 8th Mahavidya Bagalamukhi, conquering adversaries and speech obstacles.",
            "hi": "शत्रुनाशिनी एवं वाक् सिद्धि प्रदाता आठवीं महाविद्या माँ बगलामुखी का प्राकट्योत्सव।",
            "bn": "শত্রুনাশিনী ও বাক্যস্তম্ভনকারিণী অষ্টম মহাবিদ্যা মা বগলামুখীর শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita & Sandhya Puja", "hi": "निशीथ व संध्या पूजा", "bn": "নিশীথ ও সায়ংকালীন সাধনা লগ্ন"}
    },
    ("Vaishakha", "Shukla", 9): {
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
    ("Vaishakha", "Shukla", 11): {
        "en": "Mohini Ekadashi",
        "hi": "मोहिनी एकादशी",
        "bn": "মোহিনী একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Mohini (Vishnu)", "hi": "भगवान मोहिनी स्वरूप", "bn": "ভগবান মোহিনী অবতার"},
        "description": {
            "en": "Appearance of Lord Vishnu's divine Mohini incarnation during Samudra Manthan.",
            "hi": "अमृत वितरण हेतु भगवान विष्णु के मोहिनी अवतार का प्राकट्य एवं मोहनाशक व्रत।",
            "bn": "সমুদ্র মন্থনে অমৃত বিতরণে শ্রীহরির মোহিনী রূপ ধারণের পুণ্য মোহিনী একাদশী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Vaishakha", "Shukla", 14): {
        "en": "Sri Narasimha Jayanti / Narasimha Chaturdashi",
        "hi": "श्री नृसिंह जयंती / नृसिंह चतुर्दशी व्रत",
        "bn": "শ্রী শ্রীনৃসিংহ চতুর্দশী / নৃসিংহ জয়ন্তী ব্রত",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🦁", "deity": {"en": "Lord Narasimha", "hi": "भगवान नृसिंह देव", "bn": "ভগবান শ্রীনৃসিংহ দেব"},
        "description": {
            "en": "Lord Vishnu assumed the half-lion incarnation at dusk to protect Bhakta Prahlada.",
            "hi": "भक्त प्रह्लाद की रक्षा एवं हिरण्यकशिपु के संहार हेतु गोधूलि वेला में भगवान नृसिंह का प्राकट्य।",
            "bn": "ভক্ত প্রহ্লাদকে রক্ষা ও হিরণ্যকশিপু নিধনে গোধূলি লগ্নে স্তম্ভ বিদীর্ণ করে শ্রীনৃসিংহদেবের প্রকাশ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal / Sandhya Muhurta (Sunset)", "hi": "सायंकाल / संध्या मुहूर्त (सूर्यास्त)", "bn": "সায়ংকাল / সন্ধ্যা মুহূর্ত (সূর্যাস্ত)"}
    },
    ("Vaishakha", "Shukla", 15): {
        "en": "Buddha Purnima / Kurma Jayanti / Vaishakhi Purnima / Anvadhan",
        "hi": "बुद्ध पूर्णिमा / कूर्म जयंती / वैशाखी पूर्णिमा / अन्वाधान",
        "bn": "বুদ্ধ পূর্ণিমা / বৈশাখী পূর্ণিমা / ভগবান কূর্ম জয়ন্তী / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☸️", "deity": {"en": "Gautama Buddha & Lord Kurma", "hi": "गौतम बुद्ध व भगवान कूर्म", "bn": "গৌতম বুদ্ধ ও ভগবান কূর্ম"},
        "description": {
            "en": "Triple celebration of Buddha's life, Kurma Avatar advent, and Vaishakhi full moon.",
            "hi": "भगवान बुद्ध का त्रिविध पावन स्मृति दिवस, कूर्म अवतार प्राकट्य एवं पूर्णिमा स्नान।",
            "bn": "ভগবান বুদ্ধের শুভ আবির্ভাব, সমুদ্র মন্থনের কূর্ম অবতার এবং বৈশাখী পূর্ণিমার পুণ্যস্নান ও অন্বাধান।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Pradosh Kaal", "hi": "ब्रह्म मुहूर्त व प्रदोष काल", "bn": "ব্রাহ্ম মুহূর্ত ও প্রদোষ কাল"}
    },

    # --------------------------------------------------------------------------
    # জ্যৈষ্ঠ মাস (Jyeshtha)
    # --------------------------------------------------------------------------
    ("Jyeshtha", "Krishna", 1): {
        "en": "Narada Jayanti / Ishti Havan",
        "hi": "नारद जयंती / इष्टि",
        "bn": "দেবর্ষি নারদ জয়ন্তী / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापর্ব", "bn": "মহাপর্ব"},
        "icon": "🪕", "deity": {"en": "Devrishi Narada", "hi": "देवर्षि नारद", "bn": "দেবর্ষি নারদ মুনি"},
        "description": {
            "en": "Appearance day of celestial messenger Devrishi Narada and sacred Ishti.",
            "hi": "सृष्टि के प्रथम पत्रकार एवं भगवान नारायण के अनन्य भक्त देवर्षि नारद का जन्मोत्सव।",
            "bn": "ভগবান শ্রীহরির পরম ভক্ত ও স্বর্গীয় বার্তা-বাহক দেবর্ষি নারদের পবিত্র আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Narada Puja", "hi": "पूर्वाह्न नारद पूजन", "bn": "পূর্বাহ্ন নারদ পূজা লগ্ন"}
    },
    ("Jyeshtha", "Krishna", 4): {
        "en": "Ekadanta Sankashti Chaturthi",
        "hi": "एकदंत संकष्टी चतुर्थी",
        "bn": "একদন্ত সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Ekadanta Ganesha & Chandra", "hi": "भगवान एकदंत गणेश व चन्द्र देव", "bn": "ভগবান একদন্ত শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Fasting dedicated to Lord Ekadanta Ganesha to eliminate miseries, concluded at moonrise.",
            "hi": "विघ्नों के निवारण हेतु एकदंत गणेश की उपासना एवं चंद्र दर्शन पश्चात पारण।",
            "bn": "সর্ববিঘ্ন বিনাশে শ্রী একদন্ত গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Muhurta", "hi": "चन्द्रोदय व पूजन मुहूर्त", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}
    },
    ("Jyeshtha", "Krishna", 11): {
        "en": "Apara Ekadashi / Bhadrakali Jayanti",
        "hi": "अपरा एकादशी / भद्रकाली जयंती",
        "bn": "অপরা একাদশী ব্রত / মা ভদ্রকালী জয়ন্তী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Lord Vishnu & Maa Bhadrakali", "hi": "भगवान विष्णु व माँ भद्रकाली", "bn": "ভগবান বিষ্ণু ও মা ভদ্রকালী"},
        "description": {
            "en": "Apara Ekadashi grants limitless fame and merit, observed alongside Bhadrakali Jayanti.",
            "hi": "अपार धन-कीर्ति प्रदाता अपरा एकादशी एवं देवी भद्रकाली का पावन प्राकट्य दिवस।",
            "bn": "অসীম পুণ্য ও যশদাত্রী অপরা একাদশী এবং দেবী ভদ্রকালীর আবির্ভাব জয়ন্তী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Jyeshtha", "Krishna", 15): {
        "en": "Vat Savitri Vrat / Shani Jayanti / Phalaharini Kali Puja / Anvadhan",
        "hi": "वट सावित्री व्रत / शनि जयंती / फलहारिणी काली पूजा / अन्वाधान",
        "bn": "বট সাবিত্রী ব্রত / শ্রী শনি জয়ন্তী / ফলহারিণী কালীপূজা / অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌳", "deity": {"en": "Shani Deva, Savitri & Maa Kali", "hi": "शनि देव, माता सावित्री व माँ काली", "bn": "শ্রী শনি দেব, সতী সাবিত্রী ও মা কালী"},
        "description": {
            "en": "Fast for marital longevity, Shani Deva's birth observance, and midnight Phalaharini Kali Puja.",
            "hi": "अखंड सौभाग्य हेतु वट वृक्ष पूजन, शनि देव जयंती व मध्यरात्रि फलहारिणी काली पूजा।",
            "bn": "অখণ্ড সৌভাগ্যের জন্য বটবৃক্ষ পূজা, শনিদেবের আবির্ভাব তিথি ও ফলহারিণী কালীপূজা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal (Kali Puja) & Purvahna (Vat)", "hi": "निशीथ काल (काली पूजा) व पूर्वाह्न (वट)", "bn": "নিশীথ কাল (কালীপূজা) ও পূর্বাহ্ন (বট পূজা)"}
    },
    ("Jyeshtha", "Shukla", 1): {
        "en": "Jyeshtha Shukla Pratipada / Ishti / Chandra Darshana",
        "hi": "ज्येष्ठ शुक्ल प्रतिपदा / इष्टि / चन्द्र दर्शन",
        "bn": "জ্যৈষ্ঠ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🌙", "deity": {"en": "Agni Deva & Chandra Deva", "hi": "अग्नि देव व चन्द्र देव", "bn": "অগ্নি দেব ও চন্দ্র দেব"},
        "description": {
            "en": "Inception of Jyeshtha Shukla Paksha with Ishti fire oblation and crescent moon sighting.",
            "hi": "ज्येष्ठ शुक्ल पक्ष का प्रारंभ, वैदिक इष्टि एवं सायंकाल नवचंद्र दर्शन।",
            "bn": "জ্যৈষ্ঠ শুক্লপক্ষের সূচনা, বৈদিক ইষ্টি হোম এবং সায়ংকালে নবচন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },
    ("Jyeshtha", "Shukla", 3): {
        "en": "Maharana Pratap Jayanti (Tithi-based)",
        "hi": "महाराणा प्रताप जयंती (तिथि अनुसार)",
        "bn": "বীর শিরোমণি মহারাণা প্রতাপ জয়ন্তী",
        "category": "hindu", "type": {"en": "Jayanti", "hi": "गौरव दिवस", "bn": "বীর স্মরণোৎসব"},
        "icon": "⚔️", "deity": {"en": "Maharana Pratap", "hi": "महाराणा प्रताप", "bn": "বীর মহারাণা প্রতাপ"},
        "description": {
            "en": "Birth anniversary of the legendary Rajput warrior-king Maharana Pratap of Mewar.",
            "hi": "अदम्य साहस एवं स्वाभिमान के प्रतीक मेवाड़ मुकुट महाराणा प्रताप का पावन जन्मोत्सव।",
            "bn": "মাতৃভূমির স্বাধীনতার প্রতীক অসীম সাহসী রাজপুত বীর মহারাণা প্রতাপের পুণ্য জন্মতিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Smaran", "hi": "प्रातः वंदन", "bn": "প্রাতঃকালীন স্মরণ ও শ্রদ্ধাঞ্জলি"}
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
    ("Jyeshtha", "Shukla", 9): {
        "en": "Maa Dhumavati Jayanti (7th Mahavidya)",
        "hi": "माँ धूमावती जयंती",
        "bn": "মা ধূমাবতী জয়ন্তী (৭ম মহাবিদ্যা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महाविद्या जयंती", "bn": "মহাবিদ্যা মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Dhumavati", "hi": "माँ धूमावती", "bn": "মা ধূমাবতী দেবী"},
        "description": {
            "en": "Advent of 7th Mahavidya Dhumavati, dispelling poverty, despair, and deep afflictions.",
            "hi": "दारिद्र्य व समस्त संकटों का नाश करने वाली सातवीं महाविद्या माँ धूमावती का प्राकट्य।",
            "bn": "দারিদ্র্য ও সর্বসংকট বিনাশিনী সপ্তম মহাবিদ্যা মা ধূমাবতীর পবিত্র আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন সাধনা লগ্ন"}
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
        "en": "Nirjala Ekadashi / Bhim Ekadashi / Gayatri Jayanti",
        "hi": "निर्जला एकादशी (भीमसेन एकादशी) / गायत्री जयंती",
        "bn": "নির্জলা একাদশী ব্রত (ভীম একাদশী) / মা গায়ত্রী জয়ন্তী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "महाव्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu & Vedmata Gayatri", "hi": "भगवान श्री हरि विष्णु व माँ गायत्री", "bn": "ভগবান শ্রীহরি বিষ্ণু ও বেদমাতা গায়ত্রী"},
        "description": {
            "en": "The most rigorous Ekadashi fast observed without water alongside Gayatri Jayanti.",
            "hi": "जल की एक बूँद भी ग्रहण किए बिना समस्त २४ एकादशियों का पुण्य फल देने वाला महाव्रत।",
            "bn": "জলস্পর্শ না করে ২৪টি একাদশীর সমতুল্য পুণ্যফলদায়ী নির্জলা ব্রত ও বেদমাতা গায়ত্রীর আবির্ভাব।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Morning Fast", "hi": "ब्रह्म मुहूर्त व प्रातः पूजा", "bn": "ব্রাহ্ম মুহূর্ত ও প্রাতঃ পূজা"}
    },
    ("Jyeshtha", "Shukla", 15): {
        "en": "Snan Yatra (Lord Jagannath) / Vat Purnima Vrat / Kabir Jayanti / Anvadhan",
        "hi": "देवस्नान पूर्णिमा / वट पूर्णिमा / संत कबीर जयंती / अन्वाधान",
        "bn": "শ্রী জগন্নাথদেবের স্নানযাত্রা / বট পূর্ণিমা ব্রত / সন্ত কবির জন্মজয়ন্তী / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Lord Jagannath & Sant Kabir", "hi": "भगवान श्री जगन्नाथ व संत कबीर", "bn": "ভগবান শ্রী জগন্নাথদেব ও সন্ত কবির"},
        "description": {
            "en": "Auspicious bathing ceremony of Lord Jagannath with 108 herbal pots, Vat Purnima and Kabir Jayanti.",
            "hi": "भगवान जगन्नाथ का १०८ कलशों से दिव्य स्नान, वट पूर्णिमा व्रत एवं संत कबीर प्राकट्य उत्सव।",
            "bn": "১০৮ তীর্থকলশে জগন্নাথদেবের মহাজলাভিষেক, বট পূর্ণিমা ব্রত এবং সন্ত কবিরের আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Jyeshtha Purnima Snan Muhurta", "hi": "पूर्णिमा महास्नान मुहूर्त", "bn": "পূর্ণিমা দেবস্নান মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # আষাঢ় মাস (Ashadha)
    # --------------------------------------------------------------------------
    ("Ashadha", "Krishna", 1): {
        "en": "Ashadha Krishna Pratipada / Ishti Havan",
        "hi": "आषाढ़ कृष्ण प्रतिपदा / इष्टि",
        "bn": "আষাঢ় কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Commencement of Ashadha Krishna Paksha observing sacred Ishti fire rituals.",
            "hi": "आषाढ़ कृष्ण पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "আষাঢ় কৃষ্ণপক্ষের সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Ashadha", "Krishna", 4): {
        "en": "Krishnapingala Sankashti Chaturthi",
        "hi": "कृष्णपिङ्गल संकष्टी चतुर्थी",
        "bn": "শ্রী কৃষ্ণপিঙ্গল সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Krishnapingala Ganesha & Chandra", "hi": "भगवान कृष्णपिङ्गल गणेश व चन्द्र देव", "bn": "ভগবান কৃষ্ণপিঙ্গল শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Fasting dedicated to Lord Krishnapingala Ganesha, concluded with moonrise offerings.",
            "hi": "संकटनाशक कृष्णपिङ्गल गणेश का पावन व्रत एवं रात्रि में चंद्र दर्शन अर्घ्य।",
            "bn": "বিঘ্নবিনাশে শ্রী কৃষ্ণপিঙ্গল গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Muhurta", "hi": "चन्द्रोदय व पूजन मुहूर्त", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}
    },
    ("Ashadha", "Krishna", 11): {
        "en": "Yogini Ekadashi",
        "hi": "योगिनी एकादशी",
        "bn": "যোগিনী একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Fasting on Yogini Ekadashi relieves bodily ailments and cleanses previous karmas.",
            "hi": "समस्त रोगों व शापों से मुक्ति दिलाकर पुण्य प्रदान करने वाला पावन योगिनी एकादशी व्रत।",
            "bn": "সর্বপ্রকার রোগব্যাধি ও পাপ থেকে মুক্তিদায়ী পরম পবিত্র যোগিনী একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Ashadha", "Shukla", 1): {
        "en": "Ashadha Gupt Navratri Begins / Varahi Puja / Ishti",
        "hi": "आषाढ़ गुप्त नवरात्रि प्रारंभ / वाराही देवी पूजा / इष्टि",
        "bn": "আষাঢ় গুপ্ত নবরাত্রি আরম্ভ / দেবী বারাহী পূজা / ইষ্টি",
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
        "en": "Jagannath Ratha Yatra Mahotsav / Chandra Darshana",
        "hi": "श्री जगन्नाथ रथ यात्रा महोत्सव / चन्द्र दर्शन",
        "bn": "শ্রী শ্রী জগন্নাথদেবের রথযাত্রা মহোৎসব / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🚩", "deity": {"en": "Lord Jagannath, Balabhadra & Subhadra", "hi": "भगवान जगन्नाथ, बलभद्र व सुभद्रा", "bn": "ভগবান জগন্নাথ, বলভদ্র ও দেবী সুভদ্রা"},
        "description": {
            "en": "Grand chariot procession of Lord Jagannath, Balabhadra, and Subhadra to Gundicha Temple.",
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
    ("Ashadha", "Shukla", 13): {
        "en": "Jayaparvati Vrat Begins",
        "hi": "जयापार्वती व्रत प्रारंभ",
        "bn": "শ্রী শ্রী জয়াপার্বতী ব্রতারম্ভ",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌺", "deity": {"en": "Lord Shiva & Maa Parvati", "hi": "शिव-पार्वती", "bn": "দেবাদিদেব শিব ও মা পার্বতী"},
        "description": {
            "en": "Inception of the 5-day Jayaparvati fast observed by maidens and women for marital bliss.",
            "hi": "सुहाग एवं सुयोग्य जीवनसाथी की प्राप्ति हेतु कन्याओं व महिलाओं का ५ दिवसीय जयापार्वती व्रत।",
            "bn": "মনোমত পতি ও দাম্পত্য সুখের কামনায় ৫ দিনব্যাপী পবিত্র জয়াপার্বতী ব্রতের সূচনা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal Puja", "hi": "प्रदोष काल", "bn": "প্রদোষ কাল পূজা লগ্ন"}
    },
    ("Ashadha", "Shukla", 15): {
        "en": "Guru Purnima / Maharshi Vyasa Puja / Kokila Vrat / Anvadhan",
        "hi": "गुरु पूर्णिमा / वेदव्यास पूजा / कोकिला व्रत / अन्वाधान",
        "bn": "গুরু পূর্ণিমা / মহর্ষি বেদব্যাস পূজা / কোকিলা ব্রত / অন্বাধান",
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
    ("Shravana", "Krishna", 1): {
        "en": "Shravana Krishna Pratipada / Ishti Havan",
        "hi": "श्रावण कृष्ण प्रतिपदा / इष्टि",
        "bn": "শ্রাবণ কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Commencement of holy Shravana month Krishna Paksha with Vedic Ishti fire oblations.",
            "hi": "पवित्र श्रावण मास के कृष्ण पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "পবিত্র শ্রাবণ কৃষ্ণপক্ষের শুভ সূচনা এবং পরম কল্যাণ কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Shravana", "Krishna", 3): {
        "en": "Jayaparvati Vrat Ends / Mangala Gauri Vrat",
        "hi": "जयापार्वती व्रत जागरण समापन / मंगला गौरी व्रत",
        "bn": "জয়াপার্বতী ব্রত সমাপন (জাগরণ ও পারণ) / মঙ্গলা গৌরী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌸", "deity": {"en": "Maa Gauri & Shiva", "hi": "माँ गौरी व शिव", "bn": "দেবী গৌরী ও মহাদেব"},
        "description": {
            "en": "Conclusion of Jayaparvati fast through all-night vigil (Jagran) and morning parana.",
            "hi": "रात्रि जागरण के पश्चात प्रातःकाल पारण के साथ जयापार्वती व्रत की पूर्णता।",
            "bn": "সারারাত ভক্তিগীতি সহযোগে জাগরণ শেষে সকালে পারণের মাধ্যমে জয়াপার্বতী ব্রতের পূর্ণতা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Parana Muhurta", "hi": "प्रातः पारण मुहूर्त", "bn": "প্রাতঃকালীন পারণ লগ্ন"}
    },
    ("Shravana", "Krishna", 4): {
        "en": "Gajanana Sankashti Chaturthi",
        "hi": "गजानन संकष्टी चतुर्थी",
        "bn": "শ্রী গজানন সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Gajanana (Ganesha)", "hi": "भगवान गजानन", "bn": "ভগবান শ্রী গজানন গণেশ"},
        "description": {
            "en": "Shravana Krishna Chaturthi fast dedicated to Lord Gajanana, concluded with moonrise arghya.",
            "hi": "समस्त विघ्न बाधाओं के निवारण हेतु श्रावण मास की गजानन संकष्टी चतुर्थी का पावन व्रत।",
            "bn": "সর্ববিঘ্ন বিনাশ ও শান্তির কামনায় শ্রাবণ কৃষ্ণ চতুর্থীতে শ্রী গজানন গণেশের উপবাস ও চন্দ্রোদয়ে পূজা।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },
    ("Shravana", "Krishna", 11): {
        "en": "Kamika Ekadashi / Vaishnava Kamika Ekadashi",
        "hi": "कामिका एकादशी / वैष्णव कामिका एकादशी",
        "bn": "কামিকা একাদশী ব্রত / বৈষ্ণব কামিকা একাদশী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Worshipping Lord Vishnu with Tulsi leaves on Kamika Ekadashi cleanses sins.",
            "hi": "तुलसी दल से भगवान विष्णु के पूजन द्वारा समस्त मनोकामना पूर्ति हेतु कामिका एकादशी।",
            "bn": "তুলসীপত্র দিয়ে শ্রীহরির পূজায় সর্বপাপ মুক্তিদায়ী শ্রাবণ মাসের কামিকা একাদশী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Shravana", "Krishna", 15): {
        "en": "Hariyali Amavasya / Shravana Amavasya / Darsha Amavasya / Anvadhan",
        "hi": "हरियाली अमावस्या / श्रावणी अमावस्या / दर्श अमावस्या / अन्वाधान",
        "bn": "হরিয়ালী অমাবস্যা / শ্রাবণী অমাবস্যা / দর্শ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "उपवास व तर्पण", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "Lord Shiva & Pitrus", "hi": "भगवान शिव व पितृ गण", "bn": "দেবাদিদেব মহাদেব ও পিতৃপুরুষ"},
        "description": {
            "en": "Planting sacred trees, worshipping Shiva, and offering oblation to ancestors on Hariyali Amavasya.",
            "hi": "पर्यावरण शुद्धि हेतु वृक्षारोपण, शिव आराधना एवं पितृ तर्पण का पावन हरियाली अमावस्या दिवस।",
            "bn": "বৃক্ষরোপণ, মহাদেবের অর্চনা এবং পিতৃপুরুষের তৃপ্তির উদ্দেশ্যে পবিত্র হরিয়ালী অমাবস্যা।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan & Shiva Puja", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ ও শিবপূজা লগ্ন"}
    },
    ("Shravana", "Shukla", 1): {
        "en": "Shravana Shukla Pratipada / Ishti / Chandra Darshana",
        "hi": "श्रावण शुक्ल प्रतिपदा / इष्टि / चन्द्र दर्शन",
        "bn": "শ্রাবণ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🌙", "deity": {"en": "Agni Deva & Chandra Deva", "hi": "अग्नि देव व चन्द्र देव", "bn": "অগ্নি দেব ও চন্দ্র দেব"},
        "description": {
            "en": "Inception of Shravana Shukla Paksha observing Ishti and auspicious crescent moon sighting.",
            "hi": "श्रावण शुक्ल पक्ष का प्रारंभ, वैदिक इष्टि एवं सायंकाल नवचंद्र दर्शन।",
            "bn": "শ্রাবণ শুক্লপক্ষের সূচনা, বৈদিক ইষ্টি যজ্ঞ এবং সায়ংকালে নবচন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },
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
        "category": "hindu", "type": {"en": "Major Festival", "hi": "जयंती পর্ব", "bn": "মহাপর্ব"},
        "icon": "⚔️", "deity": {"en": "Lord Kalki", "hi": "भगवान कल्कि देव", "bn": "ভগবান কল্কি দেব"},
        "description": {
            "en": "Prophesied future advent of Lord Vishnu's tenth incarnation to establish Satya Yuga.",
            "hi": "कलयुग के अंत में अधर्म का विनाश कर पुनः सत्ययुग स्थापित करने वाले भगवान कल्कि का प्राकट्य पर्व।",
            "bn": "কলিযুগের শেষে পাপক্ষয় করে সত্যযুগ পুনঃপ্রতিষ্ঠার উদ্দেশ্যে দশম কল্কি অবতারের আগমন স্মরণ।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal / Pradosh Kaal", "hi": "सायंकाल / प्रदोष काल", "bn": "সায়ংকাল / প্রদোষ কাল"}
    },
    ("Shravana", "Shukla", 7): {
        "en": "Bhanu Saptami / Tulsidas Jayanti",
        "hi": "भानु सप्तमी / तुलसीदास जयंती",
        "bn": "ভানু সপ্তমী ব্রত / গোস্বামী তুলসীদাস জন্মজয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "☀️", "deity": {"en": "Surya Deva & Sant Tulsidas", "hi": "सूर्य देव व संत तुलसीदास", "bn": "ভগবান সূর্য দেব ও ভক্ত তুলসীদাস"},
        "description": {
            "en": "Sunday alignment with Saptami (Bhanu Saptami) and birth celebration of Ramcharitmanas author Sant Tulsidas.",
            "hi": "सूर्य उपासना का महापर्व भानु सप्तमी एवं रामचरितमानस के रचयिता गोस्वामी तुलसीदास जयंती।",
            "bn": "রোগব্যাধি নাশে সূর্যদেবের ভানু সপ্তমী স্নান এবং রামচরিতমানসের রচয়িতা গোস্বামী তুলসীদাসের জন্মতিথি।"
        },
        "muhurta_type": "sunrise_snan",
        "muhurta_label": {"en": "Sunrise Arghya & Purvahna Puja", "hi": "सूर्योदय अर्घ्य व प्रातः पूजा", "bn": "সূর্যোদয় অর্ঘ্য ও প্রাতঃপূজা লগ্ন"}
    },
    ("Shravana", "Shukla", 8): {
        "en": "Maa Chinnamasta Jayanti (5th Mahavidya)",
        "hi": "माँ छिन्नमस्ता जयंती",
        "bn": "মা ছিন্নমস্তা জয়ন্তী (৫ম মহাবিদ্যা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महाविद्या जयंती", "bn": "মহাবিদ্যা মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Chinnamasta", "hi": "माँ छिन्नमस्ता", "bn": "মা ছিন্নমস্তা দেবী"},
        "description": {
            "en": "Appearance of the 5th Mahavidya Chinnamasta, granting courage and sensory victory.",
            "hi": "इंद्रिय संयम व आत्मबल की अधिष्ठात्री पांचवीं महाविद्या माँ छिन्नमस्ता का पावन प्राकट्य।",
            "bn": "আত্মসংযম ও কুণ্ডলিনী শক্তির বরদাত্রী পঞ্চম মহাবিদ্যা মা ছিন্নমস্তার আবির্ভাব তিথি।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Midnight Puja", "hi": "निशीथ काल पूजा", "bn": "নিশীথ কাল সাধনা মুহূর্ত"}
    },
    ("Shravana", "Shukla", 11): {
        "en": "Shravana Putrada Ekadashi / Pavitropana / Jhulan Yatra Begins",
        "hi": "श्रावण पुत्रदा एकादशी / पवित्रा एकादशी / झूलन यात्रा प्रारंभ",
        "bn": "শ্রাবণ পুত্রদা একাদশী (পবিত্রারোপণ ব্রত) / শ্রী শ্রী ঝুলনযাত্রা আরম্ভ",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu & Radha Krishna", "hi": "भगवान श्री हरि विष्णु व राधा-कृष्ण", "bn": "ভগবান শ্রীহরি বিষ্ণু ও শ্রীশ্রী রাধাকৃষ্ণ"},
        "description": {
            "en": "Fasting for progeny welfare and inception of the 5-day divine swing festival (Jhulanotsav).",
            "hi": "संतान प्राप्ति हेतु पुत्रदा एकादशी एवं वृंदावन में श्रीराधा-कृष्ण झूलनोत्सव का शुभारंभ।",
            "bn": "সুসন্তান লাভ কামনায় পুত্রদা একাদশী এবং বৃন্দাবনে শ্রীশ্রী রাধাকৃষ্ণের ঝুলন মহোৎসবের সূচনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja & Sayankal Jhulan", "hi": "प्रातः पूजा व सायं झूलन", "bn": "প্রাতঃকালীন পূজা ও সায়ং ঝুলন আরতি"}
    },
    ("Shravana", "Shukla", 12): {
        "en": "Varalakshmi Vrat / Damodara Dwadashi / Vaishnava Putrada Ekadashi",
        "hi": "वरलक्ष्मी व्रत / दामोदर द्वादशी / वैष्णव पुत्रदा एकादशी",
        "bn": "শ্রী শ্রী বরলক্ষ্মী ব্রত / দামোদর দ্বাদশী / বৈষ্ণব পুত্রদা একাদশী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Varalakshmi & Lord Damodara", "hi": "माँ वरलक्ष्मी व भगवान दामोदर", "bn": "মা বরলক্ষ্মী ও শ্রী দামোদর"},
        "description": {
            "en": "Grand worship of Goddess Varalakshmi for prosperity and offering sacred silk thread to Lord Damodara.",
            "hi": "अखंड सौभाग्य व ऐश्वर्य हेतु माँ वरलक्ष्मी का महापूजन एवं दामोदर द्वादशी अनुष्ठान।",
            "bn": "অখণ্ড সৌভাগ্য ও সমৃদ্ধির কামনায় মা বরলক্ষ্মীর বিশেষ ব্রত এবং শ্রীদামোদর পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Varalakshmi Puja", "hi": "पूर्वाह्न वरलक्ष्मी पूजन", "bn": "পূর্বাহ্ন বরলক্ষ্মী পূজা লগ্ন"}
    },
    # --------------------------------------------------------------------------
    # শ্রাবণ শুক্ল ১৫ (পূর্ণিমা) - ৬টি সম্পূর্ণ পৃথক শাস্ত্রীয় উৎসব ও ব্রত
    # --------------------------------------------------------------------------
    ("Shravana", "Shukla", 15):
        # ১. রাখীবন্ধন উৎসব
        {
            "en": "Raksha Bandhan (Rakhi)",
            "hi": "रक्षाबंधन (राखी पर्व)",
            "bn": "পবিত্র রাখীবন্ধন উৎসব",
            "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
            "icon": "🧵", "deity": {"en": "Lord Krishna & Draupadi", "hi": "भगवान श्रीकृष्ण व द्रौपदी", "bn": "শ্রীকৃষ্ণ ও দ্রৌপদী"},
            "description": {
                "en": "Sacred festival celebrating the eternal protective bond of love and trust between brothers and sisters.",
                "hi": "भाई-बहन के अटूट स्नेह, विश्वास एवं रक्षा संकल्प का परम पावन पर्व।",
                "bn": "ভাই ও বোনের মধ্যকার অকৃত্রিম স্নেহ, সুরক্ষা ও সৌভ্রাতৃত্বের পবিত্র মিলনোৎসব।"
            },
            "muhurta_type": "aparahna",
            "muhurta_label": {"en": "Aparahna Rakhi Muhurta (Bhadra Free)", "hi": "अपराह्न राखी मुहूर्त (भद्रा रहित)", "bn": "অপরাহ্ন রাখীবন্ধন লগ্ন (ভদ্রামুক্ত)"}
        },

        # ২. শ্রী শ্রী বলরাম পূর্ণিমা (বলরাম জয়ন্তী)
        ("Shravana", "Shukla", 15): {
            "en": "Sri Balarama Purnima (Balarama Jayanti)",
            "hi": "श्री बलराम पूर्णिमा (बलराम जयंती)",
            "bn": "শ্রী শ্রী বলরাম পূর্ণিমা (বলরাম জয়ন্তী)",
            "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
            "icon": "🌾", "deity": {"en": "Lord Balarama (Sheshanaga)", "hi": "भगवान बलराम", "bn": "ভগবান বলরাম দেব ও শেষনাগ"},
            "description": {
                "en": "Divine appearance day of Lord Balarama, the elder brother of Lord Krishna and incarnation of Sheshanaga.",
                "hi": "भगवान श्रीकृष्ण के अग्रज एवं शेषनाग अवतारी भगवान बलराम जी का पावन प्राकट्योत्सव।",
                "bn": "ভগবান শ্রীকৃষ্ণের জ্যেষ্ঠ ভ্রাতা এবং শেষাবতার শ্রী বলরামদেবের পরম শুভ আবির্ভাব মহোৎসব।"
            },
            "muhurta_type": "madhyahna",
            "muhurta_label": {"en": "Madhyahna Abhisheka Muhurta", "hi": "मध्याह्न महाभिषेक मुहूर्त", "bn": "মধ্যাহ্ন মহাজলাভিষেক লগ্ন"}
        },

        # ৩. ভগবান হয়গ্রীব জয়ন্তী
        ("Shravana", "Shukla", 15): {
            "en": "Lord Hayagriva Jayanti",
            "hi": "भगवान हयग्रीव जयंती",
            "bn": "ভগবান হয়গ্রীব জয়ন্তী",
            "category": "hindu", "type": {"en": "Jayanti", "hi": "जयंती पर्व", "bn": "জয়ন্তী উৎসব"},
            "icon": "🐴", "deity": {"en": "Lord Hayagriva (Vishnu)", "hi": "भगवान हयग्रीव", "bn": "ভগবান হয়গ্রীব (শ্রীহরি বিষ্ণু)"},
            "description": {
                "en": "Advent of Lord Vishnu's horse-headed incarnation to restore the sacred Vedas from demons.",
                "hi": "असुरों से वेदों का उद्धार करने हेतु भगवान विष्णु के हयग्रीव स्वरूप का पावन प्राकट्य।",
                "bn": "অসুরদের থেকে বেদ উদ্ধার করে জ্ঞান পুনঃপ্রতিষ্ঠার উদ্দেশ্যে শ্রীহরির অশ্বমুখী হয়গ্রীব অবতারের আবির্ভাব।"
            },
            "muhurta_type": "purvahna",
            "muhurta_label": {"en": "Purvahna Veda Puja", "hi": "पूर्वाह्न वेद पूजन", "bn": "পূর্বাহ্ন বেদ পূজা ও সাধনা"}
        },

        # ৪. বেদমাতা গায়ত্রী জয়ন্তী
        ("Shravana", "Shukla", 15): {
            "en": "Vedmata Gayatri Jayanti",
            "hi": "वेदमंत्र अधिष्ठात्री माँ गायत्री जयंती",
            "bn": "বেদমাতা গায়ত্রী জন্মজয়ন্তী",
            "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
            "icon": "🪷", "deity": {"en": "Vedmata Gayatri", "hi": "माँ गायत्री", "bn": "বেদমাতা দেবী গায়ত্রী"},
            "description": {
                "en": "Appearance day of Goddess Gayatri, the mother of all Vedas and supreme knowledge.",
                "hi": "समस्त वेदों की जननी एवं ज्ञान प्रदाता माँ गायत्री का पावन प्राकट्योत्सव।",
                "bn": "সর্ববেদের জননী এবং দিব্য প্রজ্ঞার দেবী শ্রী গায়ত্রী মাতার শুভ আবির্ভাব তিথি।"
            },
            "muhurta_type": "sunrise_snan",
            "muhurta_label": {"en": "Sunrise Gayatri Japa Muhurta", "hi": "सूर्योदय गायत्री जप मुहूर्त", "bn": "সূর্যোদয় গায়ত্রী জপ মুহূর্ত"}
        },

        # ৫. শ্রী শ্রী ঝুলনযাত্রা সমাপন
        ("Shravana", "Shukla", 15): {
            "en": "Jhulan Yatra Samapti (Culmination)",
            "hi": "झूलन यात्रा समापन",
            "bn": "শ্রী শ্রী ঝুলনযাত্রা সমাপন",
            "category": "hindu", "type": {"en": "Major Festival", "hi": "उत्सव समापन", "bn": "মহোৎসব সমাপন"},
            "icon": "🌸", "deity": {"en": "Sri Radha Krishna", "hi": "श्रीराधा-कृष्ण", "bn": "শ্রীশ্রী রাধাকৃষ্ণ"},
            "description": {
                "en": "Grand culmination of the 5-day divine monsoon swing festival of Sri Radha-Krishna in Braj.",
                "hi": "ब्रज एवं वृंदावन में श्रीराधा-कृष्ण के ५ दिवसीय पावन झूलनोत्सव की पूर्णता।",
                "bn": "ব্রজমণ্ডলে শ্রীশ্রী রাধাকৃষ্ণের ৫ দিনব্যাপী প্রেমময় ঝুলন মহোৎসবের ভক্তিপূর্ণ সমাপন।"
            },
            "muhurta_type": "sayankal",
            "muhurta_label": {"en": "Sayankal Maha Arati", "hi": "सायंकाल महाआरती", "bn": "সায়ংকালীন মহাঝুলন আরতি"}
        },

        # ৬. শ্রাবণী পূর্ণিমা সত্যনারায়ণ পূজা
        ("Shravana", "Shukla", 15): {
            "en": "Shravana Purnima (Sri Satyanarayan Puja)",
            "hi": "श्रावण पूर्णिमा (सत्यनारायण व्रत)",
            "bn": "শ্রাবণী পূর্ণিমা (শ্রী সত্যনারায়ণ পূজা)",
            "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
            "icon": "🌕", "deity": {"en": "Lord Sri Satyanarayan", "hi": "भगवान सत्यनारायण", "bn": "শ্রী সত্যনারায়ণ নারায়ণ"},
            "description": {
                "en": "Offering holy shinni and listening to the sacred Katha of Lord Satyanarayan on Shravana Purnima.",
                "hi": "श्रावण पूर्णिमा पर सत्यनारायण भगवान का पूजन, पंचामृत भोग एवं पावन कथा श्रवण।",
                "bn": "শ্রাবণ পূর্ণিমায় শ্রী সত্যনারায়ণ দেবের সিন্নি ভোগ নিবেদন ও মাহাত্ম্য কথা শ্রবণ।"
            },
            "muhurta_type": "pradosh",
            "muhurta_label": {"en": "Pradosh Satyanarayan Puja", "hi": "प्रदोष सत्यनारायण कथा", "bn": "প্রদোষ সত্যনারায়ণ পূজা লগ্ন"}
        },
    ("Shravana", "Shukla", 15): {
        "en": "Anvadhan (Vedic Ritual)",
        "hi": "अन्वाधान (वैदिक अनुष्ठान)",
        "bn": "বৈদিক অন্বাধান সংস্কার",
        "category": "hindu",
        "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥",
        "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Sacred Vedic rite of adding fuel to sacrificial fires and observing austerity prior to Ishti.",
            "hi": "इष्टि अनुष्ठान से पूर्व पवित्र यज्ञाग्नि में समिधा स्थापन व संयम का पावन वैदिक संस्कार।",
            "bn": "ইষ্টি যজ্ঞের পূর্বে যজ্ঞের পবিত্র অগ্নি প্রজ্বলন, রক্ষা ও সংযম পালনের বৈদিক অন্বাধান সংস্কার।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Havan Muhurta", "hi": "पूर्वाह्न हवन मुहूर्त", "bn": "পূর্বাহ্ন সংস্কার লগ্ন"}
    },

    # --------------------------------------------------------------------------
    # ভাদ্রপদ মাস (Bhadrapada)
    # --------------------------------------------------------------------------
    ("Bhadrapada", "Krishna", 1): {
        "en": "Bhadrapada Krishna Pratipada / Ishti Havan",
        "hi": "भाद्रपद कृष्ण प्रतिपदा / इष्टि",
        "bn": "ভাদ্রপদ কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Pitru Devas", "hi": "अग्नि देव व पितृ गण", "bn": "অগ্নি দেব ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Beginning of Bhadrapada Krishna Paksha observing traditional Ishti fire oblations.",
            "hi": "भाद्रपद कृष्ण पक्ष का प्रारंभ एवं पितृ-देव तृप्ति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "ভাদ্রপদ কৃষ্ণপক্ষের শুভ সূচনা এবং শান্তি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ লগ্ন"}
    },
    ("Bhadrapada", "Krishna", 3): {
        "en": "Kajari Teej / Badi Teej / Heramba Sankashti Chaturthi",
        "hi": "कजरी तीज / कजली तीज / हेरम्ब संकष्टी चतुर्थी",
        "bn": "কাজরী তীজ ব্রত / হেরম্ব সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌺", "deity": {"en": "Lord Shiva, Parvati & Heramba Ganesha", "hi": "शिव-पार्वती व हेरम्ब गणेश", "bn": "শিব-পার্বতী ও হেরম্ব গণেশ"},
        "description": {
            "en": "Fasting dedicated to Goddess Parvati, Lord Shiva and five-headed Heramba Ganesha.",
            "hi": "सुहाग की रक्षा हेतु कजरी तीज का कठोर उपवास एवं पंचमुखी हेरम्ब गणेश पूजन।",
            "bn": "দাম্পত্য সুখ কামনায় কাজরী তীজ এবং পঞ্চমুখী হেরম্ব গণেশের উপবাস ব্রত।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Pradosh Kaal", "hi": "चन्द्रोदय व प्रदोष काल", "bn": "চন্দ্রোদয় ও প্রদোষ ব্রত লগ্ন"}
    },
    ("Bhadrapada", "Krishna", 4): {
        "en": "Bahula Chaturthi / Bol Choth",
        "hi": "बहुला चतुर्थी (बोल चौथ) / गो-पूजा",
        "bn": "বহুলা চতুর্থী (গোরু ও বাছুর পূজা)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐄", "deity": {"en": "Gau Mata & Lord Krishna", "hi": "बहुला गाय व श्रीकृष्ण", "bn": "বহুলা গাভী ও শ্রীকৃষ্ণ"},
        "description": {
            "en": "Veneration of Mother Cow and her calf with fast observed until moonrise.",
            "hi": "संतान रक्षा हेतु बहुला गाय व बछड़े का सत्कार एवं चंद्रोदय तक व्रत।",
            "bn": "সন্তানের মঙ্গল কামনায় বহুলা গাভী পূজা ও চন্দ্রোদয় পর্যন্ত উপবাস ব্রত।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Gau Puja", "hi": "चन्द्रोदय व गो-पूजा", "bn": "চন্দ্রোদয় ও গো-পূজা কাল"}
    },
    # --------------------------------------------------------------------------
    # ভাদ্রপদ কৃষ্ণ ৫ (পঞ্চমী তিথি) - পৃথক পৃথক উৎসব ও ব্রত
    # --------------------------------------------------------------------------
        # ১. ভগবান শ্রী বলরাম জন্মজয়ন্তী
        ("Bhadrapada", "Krishna", 5): {
            "en": "Sri Balarama Jayanti",
            "hi": "श्री बलराम जयंती",
            "bn": "শ্রী শ্রী বলরাম জন্মজয়ন্তী",
            "category": "hindu",
            "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
            "icon": "🌾",
            "deity": {
                "en": "Lord Balarama (Sheshanaga)",
                "hi": "भगवान बलराम (शेषनाग अवतार)",
                "bn": "ভগবান বলরাম দেব ও শেষনাগ"
            },
            "description": {
                "en": "Divine appearance day of Lord Balarama, the elder brother of Lord Krishna bearing the sacred golden plough.",
                "hi": "भगवान श्रीकृष्ण के बड़े भाई एवं शेषनाग अवतारी भगवान बलराम जी का पावन प्राकट्योत्सव।",
                "bn": "ভগবান শ্রীকৃষ্ণের জ্যেষ্ঠ ভ্রাতা ও দিব্য হলধারী শেষাবতার শ্রী বলরামদেবের পরম আবির্ভাব তিথি।"
            },
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Abhisheka & Puja Muhurta",
                "hi": "पूर्वाह्न अभिषेक व पूजन मुहूर्त",
                "bn": "পূর্বাহ্ন অভিষেক ও পূজা লগ্ন"}
        },

        # ২. হল ষষ্ঠী ব্রত (হরছট)
        ("Bhadrapada", "Krishna", 5): {
            "en": "Hal Sasthi Vrat (Har Chhath)",
            "hi": "हलषष्ठी व्रत (हरछठ)",
            "bn": "শ্রী শ্রী হল ষষ্ঠী ব্রত (হরছট)",
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
            "icon": "🌾",
            "deity": {
                "en": "Haladhara Balarama & Lord Shiva",
                "hi": "हलधर बलराम व भगवान शिव",
                "bn": "হলধর বলরাম ও দেবাদিদেব শিব"
            },
            "description": {
                "en": "Fasting observed by mothers for their children's long life, consuming only unplowed produce (Pasin rice) and buffalo milk.",
                "hi": "संतान की दीर्घायु हेतु माताओं द्वारा आचरित हलषष्ठी व्रत, जिसमें बिना जुते हुए अन्न व भैंस के दूध का प्रयोग होता है।",
                "bn": "সন্তানের নীরোগ দীর্ঘায়ুর কামনায় মায়েদের হল ষষ্ঠী ব্রত; বিনা চাষের উৎপন্ন শস্য ও মহিষের দুগ্ধ গ্রহণ।"
            },
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Hal Sasthi Puja",
                "hi": "पूर्वाह्न हलषष्ठी पूजन",
                "bn": "পূর্বাহ্ন হল ষষ্ঠী পূজা লগ্ন"}          
        },

        # ৩. ললহী ছট ব্রত
        ("Bhadrapada", "Krishna", 5): {
            "en": "Lahaee Chhath Vrat (Lalhi Chhath)",
            "hi": "ललही छठ व्रत (संतान रक्षा पर्व)",
            "bn": "শ্রী শ্রী ললহী ছট ব্রত (সন্তান রক্ষা পর্ব)",
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
            "icon": "🪔",
            "deity": {
                "en": "Maa Sasthi & Lord Balarama",
                "hi": "माँ षष्ठी व बलराम जी",
                "bn": "মা ষষ্ঠী দেবী ও শ্রী বলরাম"
            },
            "description": {
                "en": "Traditional maternal observance invoking blessings of Maa Sasthi and Lord Balarama for progeny protection.",
                "hi": "संतान की सर्वविपत्ति से रक्षा एवं सौभाग्य प्राप्ति हेतु ललही छठ की पावन पूजा।",
                "bn": "সন্তানের সর্বপ্রকার বিপদমুক্তি ও কল্যাণের কামনায় মা ষষ্ঠী ও বলরামদেবের পুণ্য ললহী ছট অর্চনা।"
            },
            "muhurta_type": "sayankal",
            "muhurta_label": {
                "en": "Sayankal Pradosh Vrat Puja",
                "hi": "सायंकाल प्रदोष पूजा",
                "bn": "সায়ংকালীন প্রদোষ পূজা লগ্ন"}
            },
    # --------------------------------------------------------------------------
    # ভাদ্রপদ কৃষ্ণ ৬ (ষষ্ঠী তিথি) - পৃথক পৃথক উৎসব ও ব্রত
    # --------------------------------------------------------------------------
    ("Bhadrapada", "Krishna", 6):
        # ১. হল ষষ্ঠী ব্রত (হরছট / বলরাম পূজা)
        {
            "en": "Hal Sasthi Vrat (Har Chhath)",
            "hi": "हलषष्ठी व्रत (हरछठ)",
            "bn": "শ্রী শ্রী হল ষষ্ঠী ব্রত (হরছট)",
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
            "icon": "🌾",
            "deity": {
                "en": "Haladhara Balarama",
                "hi": "हलधर बलराम जी",
                "bn": "হলধর বলরাম দেব"
            },
            "description": {
                "en": "Strict maternal fasting for children's longevity and health, worshipping the sacred plough and Lord Balarama.",
                "hi": "संतान की दीर्घायु व आरोग्य हेतु माताओं द्वारा निर्जला हलषष्ठी व्रत एवं बलराम जी का पावन पूजन।",
                "bn": "সন্তানের দীর্ঘায়ু ও সুস্বাস্থ্যের কামনায় মায়েদের নির্জলা হল ষষ্ঠী ব্রত এবং লাঙলধারী বলরামদেবের আরাধনা।"
            },
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Hal Sasthi Puja",
                "hi": "पूर्वाह्न हलषष्ठी पूजन",
                "bn": "পূর্বাহ্ন হল ষষ্ঠী পূজা লগ্ন"
            }
        },

        # ২. শ্রী বলরাম আবির্ভাব স্মরণ
        ("Bhadrapada", "Krishna", 6):{
            "en": "Sri Balarama Jayanti (Appearance Day)",
            "hi": "श्री बलराम जयंती (प्राकट्योत्सव)",
            "bn": "শ্রী শ্রী বলরাম জয়ন্তী (আবির্ভাব স্মরণ)",
            "category": "hindu",
            "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
            "icon": "🌾",
            "deity": {
                "en": "Lord Balarama",
                "hi": "भगवान बलराम",
                "bn": "ভগবান বলরাম দেব"
            },
            "description": {
                "en": "Advent of Lord Balarama, the source of spiritual strength and elder brother of Lord Krishna.",
                "hi": "आत्मिक बल प्रदाता एवं भगवान श्रीकृष्ण के बड़े भाई शेषनाग अवतारी बलराम जी का पावन आविर्भाव।",
                "bn": "আধ্যাত্মিক শক্তির আধার এবং ভগবান শ্রীকৃষ্ণের জ্যেষ্ঠ ভ্রাতা শেষাবতার বলরামদেবের পবিত্র আবির্ভাব।"
            },
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Puja Muhurta",
                "hi": "पूर्वाह्न पूजा मुहूर्त",
                "bn": "পূর্বাহ্ন পূজা লগ্ন"
            }
        },

        # ৩. ললহী ছট ব্রত
        ("Bhadrapada", "Krishna", 6):
            "en": "Lahaee Chhath Vrat (Lalhi Chhath)",
            "hi": "ललही छठ व्रत (संतान रक्षा पर्व)",
            "bn": "শ্রী শ্রী ললহী ছট ব্রত (সন্তান রক্ষা পর্ব)",
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
            "icon": "🪔",
            "deity": {
                "en": "Maa Sasthi",
                "hi": "माँ षष्ठी",
                "bn": "মা ষষ্ঠী দেবী"
            },
            "description": {
                "en": "Maternal worship of Maa Sasthi on Shashthi tithi for progeny protection and blessings.",
                "hi": "षष्ठी तिथि पर संतानों के कल्याण एवं रक्षा हेतु माता षष्ठी की पावन आराधना।",
                "bn": "ষষ্ঠী তিথিতে সন্তানের সার্বিক সুরক্ষা ও কল্যাণের জন্য মা ষষ্ঠী দেবীর বিশেষ ব্রত।"
            },
            "muhurta_type": "sayankal",
            "muhurta_label": {
                "en": "Sayankal Pradosh Vrat Puja",
                "hi": "सायंकाल प्रदोष पूजा",
                "bn": "সায়ংকালীন প্রদোষ পূজা লগ্ন"}
            },
    ("Bhadrapada", "Krishna", 8): {
        "en": "Krishna Janmashtami / Gokulashtami",
        "hi": "श्रीकृष्ण जन्माष्टमी / गोकुलाष्टमी",
        "bn": "শ্রী শ্রী কৃষ্ণ জন্মাষ্টমী মহাপর্ব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
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
        "en": "Dahi Handi / Sri Nandotsava",
        "hi": "दही हांडी महोत्सव / श्री नंदोत्सव",
        "bn": "দহি হাণ্ডি মহোৎসব / শ্রী শ্রী নন্দোৎসব",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🍯", "deity": {"en": "Balakrishna & Govinda", "hi": "बालकृष्ण गोविंदा", "bn": "বালগোপাল ও গোবিন্দ"},
        "description": {
            "en": "Commemorating Balakrishna's childhood pastime of stealing butter through human pyramids.",
            "hi": "गोकुल में माखन चोरी की लीला को साकार करते हुए गोविंदा टोलियों द्वारा दही हांडी फोड़ने का उत्सव।",
            "bn": "বালগোপালের মাখনচুরির মধুর লীলা স্মরণে আনন্দোল্লাসে দহি হাণ্ডি ভাঙার সর্বজনীন উৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Utsav Muhurta", "hi": "पूर्वाह्न उत्सव काल", "bn": "পূর্বাহ্ন মহোৎসব লগ্ন"}
    },
    ("Bhadrapada", "Krishna", 11): {
        "en": "Aja Ekadashi",
        "hi": "अजा एकादशी",
        "bn": "অজা একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Aja Ekadashi dispels all past grief, observed by King Harishchandra.",
            "hi": "राजा हरिश्चंद्र द्वारा समस्त कष्टों से मुक्ति हेतु आचरित परम फलदायी अजा एकादशी व्रत।",
            "bn": "রাজা হরিশচন্দ্র কর্তৃক সর্বকষ্ট মুক্তির উদ্দেশ্যে পালিত পবিত্র অজা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Bhadrapada", "Krishna", 14): {
        "en": "Aghora Chaturdashi / Masik Shivratri",
        "hi": "अघोर चतुर्दशी / मासिक शिवरात्रि",
        "bn": "অঘোর চতুর্দশী / মাসিক শিবরাত্রি ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Lord Shiva (Aghora)", "hi": "भगवान शिव (अघोर रूप)", "bn": "ভগবান শিব (অঘোরেশ্বর)"},
        "description": {
            "en": "Worshipping Lord Shiva's peaceful Aghora form at midnight to eliminate dread.",
            "hi": "भय व नकारात्मकता के नाश हेतु अघोरेश्वर शिव का मध्यरात्रि रुद्राभिषेक।",
            "bn": "সর্বভয় নাশ ও আধ্যাত্মিক শান্তির জন্য ভগবান শিবের অঘোর রূপের পূজা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Midnight Muhurta", "hi": "निशीथ काल", "bn": "নিশীথ কাল পূজা"}
    },
    ("Bhadrapada", "Krishna", 15): {
        "en": "Pithori Amavasya / Pola / Bhadrapada Amavasya / Anvadhan",
        "hi": "पिठोरी अमावस्या (पोला) / भाद्रपद अमावस्या / अन्वाधान",
        "bn": "পিথোরী অমাবস্যা (মায়েদের পুণ্য ব্রত) / ভাদ্রপদ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "উপবাস ও তর্পণ", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "64 Yoginis, Maa Durga & Pitrus", "hi": "६४ योगिनी, माँ दुर्गा व पितृ गण", "bn": "চৌষট্টি যোগিনী, মা দুর্গা ও পিতৃপুরুষ"},
        "description": {
            "en": "Mothers worship 64 Yoginis using flour figurines (Pith) for progeny longevity and health.",
            "hi": "संतान की दीर्घायु व समृद्धि हेतु आटे की पिंडी बनाकर ६४ योगिनियों का विशेष पिठोरी व्रत।",
            "bn": "সন্তানের নীরোগ দীর্ঘায়ু কামনায় পিঠালির প্রতিমা গড়ে ৬৪ যোগিনী ও মা দুর্গার বিশেষ ব্রত।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan & Sayankal Vrat", "hi": "अपराह्न तर्पण व सायं व्रत", "bn": "অপরাহ্ন তর্পণ ও সায়ংকালীন ব্রত"}
    },
    ("Bhadrapada", "Shukla", 1): {
        "en": "Bhadrapada Shukla Pratipada / Ishti Havan",
        "hi": "भाद्रपद शुक्ल प्रतिपदा / इष्टि",
        "bn": "ভাদ্রপদ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Inception of Bhadrapada Shukla Paksha with sacred fire offerings.",
            "hi": "भाद्रपद शुक्ल पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "ভাদ্রপদ শুক্লপক্ষের শুভ সূচনা এবং শান্তি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Bhadrapada", "Shukla", 2): {
        "en": "Chandra Darshana (Bhadrapada Shukla)",
        "hi": "भाद्रपद चन्द्र दर्शन",
        "bn": "ভাদ্রপদ শুক্ল দ্বিতীয়া চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Observance", "hi": "धार्मिक दर्शन", "bn": "চন্দ্র দর্শন"},
        "icon": "🌙", "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"},
        "description": {
            "en": "Auspicious sighting of the crescent moon after sunset for peace and prosperity.",
            "hi": "मानसिक शांति व सौभाग्य वृद्धि हेतु सायंकाल नवचंद्र দর্শন ও अर्घ्य।",
            "bn": "মানসিক শান্তি ও সৌভাগ্য বৃদ্ধির কামনায় সায়ংকালে অমাবস্যা-পরবর্তী দ্বিতীয়ার শুভ চন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
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
        "en": "Ganesh Chaturthi / Vinayaka Chavithi / Rishi Panchami",
        "hi": "श्री गणेश चतुर्थी / विनायक पूजा / ऋषि पंचमी",
        "bn": "শ্রী শ্রী গণেশ চতুর্থী / বিনায়ক পূজা (গণেশোৎসব আরম্ভ) / ঋষি পঞ্চমী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha & Sapta Rishis", "hi": "भगवान श्री गणेश व सप्तर्षि", "bn": "ভগবান শ্রী গণেশ ও সপ্তর্ষি"},
        "description": {
            "en": "Festive commencement of Ganeshotsav welcoming Lord Ganesha alongside Rishi Panchami rituals.",
            "hi": "विघ्नहर्ता भगवान श्री गणेश के पावन प्राकट्य पर गणेशोत्सव का शुभारंभ एवं सप्तर्षि पूजन।",
            "bn": "বিঘ্নবিনাশক শ্রী গণেশের শুভ আরাধনা, গণেশোৎসব আরম্ভ এবং পবিত্র সপ্তর্ষি ব্রত।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Kaal Muhurta", "hi": "मध्याह्न काल मुहूर्त", "bn": "মধ্যাহ্ন কাল মুহূর্ত (গণেশ পূজা)"}
    },
    ("Bhadrapada", "Shukla", 5): {
        "en": "Rishi Panchami Vrat (Dedicated)",
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
    ("Bhadrapada", "Shukla", 7): {
        "en": "Lalita Saptami / Mahalakshmi Vrat Begins / Durva Ashtami",
        "hi": "ललिता सप्तमी / महालक्ष्मी व्रत प्रारंभ / दूर्वा अष्टमी",
        "bn": "শ্রী শ্রী ললিতা সপ্তমী / মহালক্ষ্মী ব্রতারম্ভ / দূর্বা অষ্টমী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Lalita Sakhi, Maa Mahalakshmi & Ganesha", "hi": "ललिता सखी, माँ महालक्ष्मी व गणेश जी", "bn": "ললিতা সখী, মা মহালক্ষ্মী ও শ্রী গণেশ"},
        "description": {
            "en": "Appearance of Srimati Radharani's foremost companion Lalita Sakhi and inception of 16-day Mahalakshmi fast.",
            "hi": "श्रीमती राधारानी की प्रधान सखी ललिता जी का प्राकट्य एवं १६ दिवसीय महालक्ष्मी व्रत का शुभारंभ।",
            "bn": "শ্রীমতী রাধারাণীর প্রধানা সখী ললিতা দেবীর আবির্ভাব এবং ১৬ দিনব্যাপী মহালক্ষ্মী ব্রতের শুভ সূচনা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Lalita & Lakshmi Puja", "hi": "पूर्वाह्न महालक्ष्मी पूजा", "bn": "পূর্বাহ্ন ললিতা ও মহালক্ষ্মী পূজা লগ্ন"}
    },
    ("Bhadrapada", "Shukla", 8): {
        "en": "Radhashtami / Mahalakshmi Vrat",
        "hi": "श्री राधाष्टमी / महालक्ष्मी व्रत",
        "bn": "শ্রী শ্রী রাধাষ্টমী মহাপর্ব / মহালক্ষ্মী ব্রত",
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
        "en": "Parsva Ekadashi (Parivartini)",
        "hi": "परिवर्तिनी एकादशी (पार्श्व एकादशी)",
        "bn": "পার্শ্ব একাদশী (পরিবর্তিনী একাদশী ব্রত)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Lord Vishnu shifts side in cosmic slumber, granting enormous merits to fasting devotees.",
            "hi": "शयन करते हुए भगवान विष्णु करवट बदलते हैं, समस्त पापों का नाश करने वाली एकादशी।",
            "bn": "যোগনিদ্রায় শ্রীহরির পার্শ্ব পরিবর্তন এবং সর্বপাপমুক্তির কামনায় পরম পবিত্র একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Bhadrapada", "Shukla", 12): {
        "en": "Vamana Jayanti",
        "hi": "वामन जयंती",
        "bn": "ভগবান বামন অবতার জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Lord Vamana", "hi": "भगवान वामन देव", "bn": "ভগবান বামন দেব"},
        "description": {
            "en": "Appearance of Vamana Deva to restore cosmic balance and redeem King Bali.",
            "hi": "राजा बलि का उद्धार करने एवं धर्म रक्षा हेतु भगवान वामन का पावन प्राकट्योत्सव।",
            "bn": "দানবীর বলিকে উদ্ধার ও ধর্ম রক্ষার কামনায় ভগবান বামনের পরম শুভ আবির্ভাব তিথি।"
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
        "en": "Bhadrapada Purnima / Purnima Shraddha / Pitru Paksha Begins / Anvadhan",
        "hi": "भाद्रपद पूर्णिमा / पूर्णिमा श्राद्ध / महालय पक्ष प्रारंभ / अन्वाधान",
        "bn": "ভাদ্রপদ পূর্ণিমা / পূর্ণিমা শ্রাদ্ধ / ১৬ দিনের পিতৃপক্ষ আরম্ভ / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🙏", "deity": {"en": "Pitru Devas & Sri Satyanarayan", "hi": "पितृ गण व श्री सत्यनारायण", "bn": "পিতৃপুরুষগণ ও শ্রী সত্যনারায়ণ"},
        "description": {
            "en": "Commencement of the 16-day sacred Mahalaya Pitru Paksha with Purnima Shraddha and Vedic Anvadhan.",
            "hi": "पूर्वजों की तृप्ति हेतु १६ दिवसीय महालय श्राद्ध पक्ष का पावन प्रारंभ एवं पूर्णिमा श्राद्ध।",
            "bn": "পরলোকগত পিতৃপুরুষের আত্মার সদগতির জন্য ১৬ দিনের পিতৃপক্ষ আরম্ভ ও পূর্ণিমা শ্রাদ্ধ নিবেদন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Kutapa & Aparahna (Tarpan)", "hi": "कुतप व अपराह्न (तर्पण काल)", "bn": "কুতপ ও অপরাহ্ন কাল (তর্পণ লগ্ন)"}
    },

    # --------------------------------------------------------------------------
    # আশ্বিন মাস (Ashvina)
    # --------------------------------------------------------------------------
    ("Ashvina", "Krishna", 4): {
        "en": "Vighnaraja Sankashti Chaturthi",
        "hi": "विघ्नराज संकष्टी चतुर्थी",
        "bn": "শ্রী বিঘ্নরাজ সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Vighnaraja Ganesha", "hi": "भगवान विघ्नराज गणेश", "bn": "ভগবান বিঘ্নরাজ শ্রী গণেশ"},
        "description": {
            "en": "Ashwina Krishna Chaturthi fast invoking Lord Vighnaraja for eliminating life's adversities.",
            "hi": "जीवन के समस्त संकटों व विघ्नों के समूल नाश हेतु विघ्नराज गणेश की चंद्रोदय पूजा।",
            "bn": "জীবনের সর্বসংকট ও বাধা দূরীকরণে আশ্বিন কৃষ্ণ চতুর্থীতে বিঘ্নরাজ গণেশের নিষ্ঠাপূর্ণ ব্রতপালন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },
    ("Ashvina", "Krishna", 8): {
        "en": "Jitiya Vrat (Jivitputrika Vrat)",
        "hi": "जितिया व्रत (जीवित्पुत्रिका व्रत)",
        "bn": "শ্রী শ্রী জীতুয়া / জীবিতপুত্রিকা ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🪔", "deity": {"en": "Jimutavahana & Lord Surya", "hi": "जीमूतवाहन व सूर्य देव", "bn": "জীমূতবাহন ও ভগবান সূর্য"},
        "description": {
            "en": "Mothers observe severe 24-hour nirjala fast invoking Jimutavahana for children's longevity.",
            "hi": "संतानों की दीर्घायु, स्वास्थ्य व रक्षा हेतु माताओं द्वारा २४ घंटे का निर्जला जीवित्पुत्रिका व्रत।",
            "bn": "সন্তানের নীরোগ দীর্ঘায়ু কামনায় মায়েদের পরম নিষ্ঠাপূর্ণ ২৪ ঘণ্টার নির্জলা জীবিতপুত্রিকা ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Puja & Paran", "hi": "पूर्वाह्न पूजन व पारण", "bn": "পূর্বাহ্ন বিহিত পূজা ও পারণ"}
    },
    ("Ashvina", "Krishna", 11): {
        "en": "Indira Ekadashi (Pitru Paksha Ekadashi)",
        "hi": "इन्दिरा एकादशी (पितृपक्ष एकादशी)",
        "bn": "ইন্দিরা একাদশী ব্রত (পিতৃপক্ষীয় একাদশী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Fasting on Indira Ekadashi delivers departed ancestors from lower realms to Vaikuntha.",
            "hi": "पितरों को मोक्ष प्रदान करने एवं यमलोक के कष्टों से मुक्ति हेतु पावन इन्दिरा एकादशी व्रत।",
            "bn": "পরলোকগত পিতৃপুরুষের নরকক্লেশ মুক্তি ও বৈকুণ্ঠ ধাম প্রাপ্তির কামনায় ইন্দিরা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
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
        "en": "Sharad Navratri Begins / Ghatasthapana / Maharaja Agrasen Jayanti / Ishti",
        "hi": "शारदीय नवरात्रि प्रारंभ / घटस्थापना / महाराजा अग्रसेन जयंती / इष्टि",
        "bn": "শারদীয়া নবরাত্রি আরম্ভ / ঘটস্থাপন / মহারাজা অগ্রসেন জয়ন্তী / ইষ্টি",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Maharaja Agrasen", "hi": "माँ दुर्गा व महाराजा अग्रसेन", "bn": "মা দুর্গা ও মহারাজা অগ্রসেন"},
        "description": {
            "en": "Inception of Sharad Navratri, birth celebration of Maharaja Agrasen, and sacred Vedic Ishti havan.",
            "hi": "शारदीय घटस्थापना, समाज सुधारक महाराजा अग्रसेन की पावन जयंती एवं वैदिक इष्टि अनुष्ठान।",
            "bn": "শারদীয়া নবরাত্রির শুভ ঘটস্থাপন, দানশীল মহারাজা অগ্রসেনের জন্মজয়ন্তী এবং বৈদিক ইষ্টি যজ্ঞ।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Abhijit Muhurta", "hi": "घटस्थापना व अभिजित", "bn": "ঘটস্থাপন ও অভিজিৎ মুহূর্ত"}
    },
    ("Ashvina", "Shukla", 2): {
        "en": "Navratri Day 2: Brahmacharini Puja / Chandra Darshana",
        "hi": "नवरात्रि दिवस २: माँ ब्रह्मचारिणी पूजा / चन्द्र दर्शन",
        "bn": "শারদ নবরাত্রি ২য় দিন: দেবী ব্রহ্মচারিণী পূজা / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Brahmacharini", "hi": "माँ ब्रह्मचारिणी", "bn": "দেবী ব্রহ্মচারিণী"},
        "description": {
            "en": "Second day of Navratri dedicated to the goddess of austerity and divine asceticism.",
            "hi": "तपस्या व ज्ञान की प्रदाता देवी ब्रह्मचारिणी का नवरात्रि के द्वितीय दिवस पर पावन पूजन।",
            "bn": "তপোনিষ্ঠা ও দিব্য প্রজ্ঞার দেবী ব্রহ্মচারিণীর চরণে নবরাত্রির দ্বিতীয় দিনে ভক্তিপূর্ণ নিবেদন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
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
        "en": "Durga Puja: Maha Saptami / Saraswati Avahan (Mula Nakshatra)",
        "hi": "दुर्गा सप्तमी (नवपत्रिका प्रवेश) / सरस्वती आवाहन",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাসপ্তমী (নবপত্রিকা প্রবেশ ও মহাস্নান) / সরস্বতী আবাহন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga & Saraswati", "hi": "माँ दुर्गा व माँ सरस्वती", "bn": "মা দুর্গা ও মা সরস্বতী"},
        "description": {
            "en": "Bathing and entry of Navapatrika and invoking Goddess Saraswati under Mula Nakshatra.",
            "hi": "प्रकृति स्वरूपा नवपत्रिका प्रवेश एवं मूल नक्षत्र में देवी सरस्वती का पावन आवाहन।",
            "bn": "প্রকৃতির ৯টি ঔষধি রূপ নবপত্রিকা স্নান-প্রবেশ এবং মূল নক্ষত্রে দেবী সরস্বতীর আবাহন।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal Navapatrika Entry & Snan", "hi": "प्रातःकाल नवपत्रिका प्रवेश व स्नान", "bn": "প্রাতঃকালে নবপত্রিকা প্রবেশ ও মহাস্নান"}
    },
    ("Ashvina", "Shukla", 8): {
        "en": "Durga Puja: Maha Ashtami / Sandhi Puja / Kumari Puja / Saraswati Visarjan",
        "hi": "दुर्गा महाष्टमी / संधि पूजा / कुमारी पूजा / सरस्वती विसर्जन",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহাঅষ্টমী, সন্ধিপূজা ও কুমারী পূজা / সরস্বতী বিসর্জন",
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
        "en": "Durga Puja: Maha Navami / Navami Homa / Ayudha Puja",
        "hi": "दुर्गा महानवमी पूजा / नवमी हवन / आयुध पूजा",
        "bn": "শ্রী শ্রী দুর্গাপূজা: মহানবমী পূজা ও মহাহোম / আয়ুধ পূজা",
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
    ("Ashvina", "Shukla", 11): {
        "en": "Papankusha Ekadashi",
        "hi": "पापांकुशा एकादशी",
        "bn": "পাপাঙ্কুশা একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Padmanabha (Vishnu)", "hi": "भगवान पद्मनाभ विष्णु", "bn": "ভগবান পদ্মনাভ বিষ্ণু"},
        "description": {
            "en": "Papankusha Ekadashi subdues past demerits like an elephant goad.",
            "hi": "समस्त पाप रूपी गज को वश में करने वाली कल्याणकारी पापांकुशा एकादशी।",
            "bn": "পাপরূপ বন্য হস্তীকে দমনকারী পরম কল্যাণপ্রদ পাপাঙ্কুশা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Ashvina", "Shukla", 14): {
        "en": "Kojagari Lakshmi Puja (Purvaviddha) / Anvadhan",
        "hi": "कोजागरी लक्ष्मी पूजा (पूर्वाविद्धा) / अन्वाधान",
        "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা (পূর্বাবিদ্ধা) / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Lakshmi & Sri Hari", "hi": "माँ महालक्ष्मी व श्रीहरि", "bn": "মা লক্ষ্মী ও শ্রীহরি নারায়ণ"},
        "description": {
            "en": "Midnight vigil (Kojagara) invoking Goddess Lakshmi on Sharad Purnima eve with Vedic Anvadhan.",
            "hi": "शरद पूर्णिमा की पूर्व संध्या पर रात्रि जागरण कोजागरी लक्ष्मी पूजन एवं वैदिक अन्वाधान अनुष्ठान।",
            "bn": "শারদ পূর্ণিমার নিশীথ রাতে ধন-সমৃদ্ধির কামনায় কোজাগরী জাগরণ লক্ষ্মীপূজা ও বৈদিক অন্বাধান।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh & Nishita Kaal", "hi": "प्रदोष व निशीथ काल", "bn": "প্রদোষ ও নিশীথ কাল লগ্ন"}
    },
    ("Ashvina", "Shukla", 15): {
        "en": "Kojagari Lakshmi Puja / Sharad Purnima / Valmiki Jayanti",
        "hi": "कोजागरी लक्ष्मी पूजा / शरद पूर्णिमा / वाल्मीकि जयंती",
        "bn": "শ্রী শ্রী কোজাগরী লক্ষ্মীপূজা / শারদ পূর্ণিমা / মহর্ষি বাল্মীকি জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪷", "deity": {"en": "Maa Lakshmi & Maharshi Valmiki", "hi": "माँ महालक्ष्मी व महर्षि वाल्मीकि", "bn": "মা লক্ষ্মী ও মহর্ষি বাল্মীকি"},
        "description": {
            "en": "Worship of Maa Lakshmi on full moon night and celebrating the birth of Adi Kavi Valmiki.",
            "hi": "शरद पूर्णिमा की धवल रात्रि में माँ लक्ष्मी की पूजा एवं आदि कवि महर्षि वाल्मीकि जयंती।",
            "bn": "শারদ পূর্ণিমার রাতে ধনদাত্রী মা লক্ষ্মীর আরাধনা এবং রামায়ণ রচয়িতা মহর্ষি বাল্মীকির জন্মতিথি।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh & Nishita Kaal", "hi": "प्रदोष व निशीथ काल", "bn": "প্রদোষ ও নিশীথ কাল মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # কার্তিক মাস (Kartika) - সম্পূর্ণ ও নিখুঁত তিথি ম্যাপিং
    # --------------------------------------------------------------------------
    ("Kartika", "Krishna", 4): {
        "en": "Karwa Chauth / Vakratunda Sankashti Chaturthi",
        "hi": "करवा चौथ / वक्रतुण्ड संकष्टी चतुर्थी",
        "bn": "করবা চৌথ ব্রত / বক্রতুণ্ড সংকষ্টী চতুর্থী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌙", "deity": {"en": "Lord Ganesha & Chandra Deva", "hi": "श्री गणेश व चन्द्र देव", "bn": "শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Nirjala fast for spouse's longevity alongside Vakratunda Sankashti moonrise arghya.",
            "hi": "अखंड सौभाग्य हेतु करवा चौथ निर्जला व्रत एवं विघ्नहर्ता वक्रतुण्ड गणेश चंद्रोदय पूजन।",
            "bn": "স্বামীর দীর্ঘায়ু কামনায় নির্জলা ব্রত এবং বিঘ্নহারী বক্রতুণ্ড গণেশের উদ্দেশ্যে চন্দ্রোদয়ে অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Pradosh Kaal", "hi": "चन्द्रोदय व प्रदोष काल", "bn": "চন্দ্রোদয় ও প্রদোষ লগ্ন"}
    },
    ("Kartika", "Krishna", 7): {
        "en": "Bhanu Saptami (Surya Saptami / Vrata)",
        "hi": "भानु सप्तमी (सूर्य सप्तमी)",
        "bn": "ভানু সপ্তমী ব্রত (পবিত্র রবি সপ্তমী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "☀️", "deity": {"en": "Lord Surya Narayana", "hi": "भगवान सूर्यनारायण", "bn": "ভগবান সূর্য নারায়ণ"},
        "description": {
            "en": "Auspicious alignment of Saptami Tithi with Sunday, granting radiant health and prosperity.",
            "hi": "रविवार युक्त सप्तमी पर भगवान सूर्य को तांबे के लोटे से अर्घ्य समर्पण एवं रोगमुक्ति व्रत।",
            "bn": "রবিবার যুক্ত সপ্তমীতে রোগব্যাধি মুক্তি ও তেজস্বী আয়ু কামনায় ভগবান সূর্যদেবের মহাতর্পণ।"
        },
        "muhurta_type": "sunrise_snan",
        "muhurta_label": {"en": "Sunrise Arghya Muhurta", "hi": "सूर्योदय अर्घ्य मुहूर्त", "bn": "সূর্যোদয় অর্ঘ্যদান মুহূর্ত"}
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
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
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
        "en": "Kali Chaudas / Bhoot Chaturdashi / Naraka Chaturdashi / 14 Pradeep Dan",
        "hi": "काली चौदस / नरक चतुर्दशी / छोटी दिवाली",
        "bn": "কালী চৌদাস / ভূত চতুর্দশী / নরক চতুর্দশী (১৪ প্রদীপ দান)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Yamaraja & Maa Kali", "hi": "यमराज व महाकाली", "bn": "যমরাজ ও মা কালী"},
        "description": {
            "en": "Lighting 14 lamps and invoking Mahakali/Yamaraja to dispel dark and negative energies.",
            "hi": "चौदह यमदीप प्रज्वलित कर नकारात्मकता दूर करना एवं अभ्यंग स्नान।",
            "bn": "চোদ্দ প্রদীপ প্রজ্বলন ও চোদ্দ পুরুষের স্মরণে ভূত চতুর্দশী ও নরক চতুর্দশী ব্রত।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal 14 Deepam & Abhyanga Snan", "hi": "सायंकाल यम दीपदान व अभ्यंग स्नान", "bn": "সায়ংকালে ১৪ প্রদীপ দান ও তৈলাভ্যঙ্গ স্নান"}
    },
    ("Kartika", "Krishna", 15): {
        "en": "Diwali / Lakshmi Puja / Shyama Puja / Darsha Amavasya",
        "hi": "दीपावली / महालक्ष्मी पूजा / श्यामप पूजा / दर्श अमावस्या",
        "bn": "শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / দীপাবলি ও দর্শ অমাবস্যা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Maa Kali & Maa Mahalakshmi", "hi": "माँ काली व माँ महालक्ष्मी", "bn": "মা শ্যামা কালী ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Victory of light over darkness with earthen lamps, midnight worship of Maa Kali, and Darsha Amavasya.",
            "hi": "अंधकार पर प्रकाश की विजय का दीपोत्सव, मध्यरात्रि माँ काली पूजा व दर्श अमावस्या।",
            "bn": "অন্ধকার দূর করে আলোর দীপাবলি, অমাবস্যার নিশীথ রাতে মা শ্যামা কালীর আরাধনা ও দর্শ অমাবস্যা।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal (Kali Puja) & Pradosh", "hi": "निशीथ काल (काली पूजा) व प्रदोष", "bn": "নিশীথ কাল (কালীপূজা) ও প্রদোষ লগ্ন"}
    },
    ("Kartika", "Shukla", 1): {
        "en": "Govardhan Puja / Annakut / Dyuta Krida / Ishti / Gujarati New Year",
        "hi": "गोवर्धन पूजा / अन्नकूट / द्यूत क्रीड़ा / इष्टि / गुजराती नववर्ष",
        "bn": "শ্রী শ্রী গোবর্ধন পূজা / অন্নকূট মহোৎসব / দ্যূত ক্রীড়া / ইষ্টি / গুজরাটি নববর্ষ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "⛰️", "deity": {"en": "Lord Giriraj Krishna & Shiva", "hi": "गिरिराज भगवान श्रीकृष्ण व शिव", "bn": "গিরিরাজ শ্রীকৃষ্ণ ও শিব-পার্বতী"},
        "description": {
            "en": "Worship of Govardhan Hill with 56 delicacies, traditional Dyuta Krida, and Gujarati New Year.",
            "hi": "५६ भोग अन्नकूट समर्पण, सुख-समृद्धि हेतु पारंपरिक द्यूत क्रीड़ा एवं नूतन वर्षारंभ।",
            "bn": "ছাপ্পান্ন ভোগসহ গোবর্ধন পর্বত পূজা, শিব-পার্বতের পাশাখেলা স্মরণে দ্যূত ক্রীড়া ও গুজরাটি নববর্ষ।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah & Sayankal Annakut", "hi": "प्रातः व सायंकाल पूजा", "bn": "প্রাতঃ ও সায়ংকালীন অন্নকূট লগ্ন"}
    },
    ("Kartika", "Shukla", 2): {
        "en": "Bhaiya Dooj / Bhai Phonta / Yama Dwitiya / Chandra Darshana",
        "hi": "भाई दूज / यम द्वितीया / भ्रातृ द्वितीया / चन्द्र दर्शन",
        "bn": "পবিত্র ভাইফোঁটা (যমদ্বিতীয়া / ভ্রাতৃদ্বিতীয়া) / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Yamuna, Yamaraja & Chandra", "hi": "यमुना, यमराज व चन्द्र देव", "bn": "যমুনা দেবী, যমরাজ ও চন্দ্র দেব"},
        "description": {
            "en": "Sisters pray for their brothers' long life and evening sighting of the crescent moon.",
            "hi": "भाई की दीर्घायु हेतु तिलक संस्कार एवं सायंकाल नवचंद्र (द्वितीया चंद्र) दर्शन।",
            "bn": "ভ্রাতার দীর্ঘায়ু ও সর্ববিপদমুক্তির পবিত্র আশীর্বাদ লগ্ন এবং সায়ংকালে শুক্ল দ্বিতীয়া চন্দ্র দর্শন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna & Chandra Darshan", "hi": "अपराह्न व चंद्र दर्शन", "bn": "অপরাহ্ন ও চন্দ্র দর্শন লগ্ন"}
    },
    ("Kartika", "Shukla", 5): {
        "en": "Labh Pancham (Saubhagya Panchami)",
        "hi": "लाभ पंचम (सौभाग्य पंचमी)",
        "bn": "লাভ পঞ্চম (সৌভাগ্য পঞ্চমী)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "व्यापारिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🪙", "deity": {"en": "Lord Ganesha & Maa Lakshmi", "hi": "भगवान गणेश व माँ लक्ष्मी", "bn": "শ্রী গণেশ ও মা লক্ষ্মী"},
        "description": {
            "en": "Auspicious day for opening new business ventures and ledgers after Diwali.",
            "hi": "दीपावली के बाद नए व्यापार, दुकान व प्रतिष्ठानों को पुनः खोलने का परम शुभ दिन।",
            "bn": "দীপাবলির পর নতুন ব্যবসা ও দোকান খোলার পরম সৌভাগ্যদায়ী লাভ পঞ্চম তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Labh Muhurta (Morning)", "hi": "लाभ काल मुहूर्त", "bn": "লাভ কাল প্রাতঃ মুহূর্ত"}
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
    ("Kartika", "Shukla", 12): {
        "en": "Gauna Devutthana Ekadashi / Vaishnava Ekadashi / Tulsi Vivah",
        "hi": "गौण देवउठनी एकादशी / वैष्णव एकादशी / तुलसी विवाह",
        "bn": "গৌণ দেবউত্থান একাদশী / বৈষ্ণব একাদশী / তুলসী বিবাহ",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌿", "deity": {"en": "Lord Shaligram & Tulsi Maharani", "hi": "भगवान शालिग्राम व तुलसी", "bn": "ভগবান শালগ্রাম ও তুলসী মহারাণী"},
        "description": {
            "en": "Special Vaishnava observance of Devutthana Ekadashi and ceremonial wedding of Shaligram and Tulsi.",
            "hi": "वैष्णव संप्रदाय का देवउठनी एकादशी व्रत एवं शालिग्राम-तुलसी विवाह का पावन अनुष्ठान।",
            "bn": "বৈষ্ণব পরম্পরার দেবউত্থান একাদশী ব্রত এবং ভগবান শালগ্রাম ও তুলসী মহারাণীর বিবাহোৎসব।"
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
    # ==============================================================================
# কার্তিক মাস (Kartika) - বিশুদ্ধ শাস্ত্রীয় চান্দ্রতিথি ভিত্তিক ডাটাবেস
# (সম্পূর্ণরূপে সূর্য-চন্দ্রের অবস্থান ও তিথির ওপর নির্ভরশীল, কোনো ফিক্সড তারিখ নেই)
# ==============================================================================
    # --- কার্তিক কৃষ্ণ পক্ষ ---
    ("Kartika", "Krishna", 7): {
        "en": "Surya Saptami Vrata",
        "hi": "सूर्य सप्तमी व्रत",
        "bn": "সূর্য সপ্তমী ব্রত (ভানু সপ্তমী স্নান ও অর্ঘ্যদান)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "☀️", "deity": {"en": "Lord Surya Narayana", "hi": "भगवान सूर्य नारायण", "bn": "ভগবান সূর্য নারায়ণ"},
        "description": {
            "en": "Auspicious solar day dedicated to Sun God for health, vitality, and freedom from afflictions.",
            "hi": "आरोग्य व तेज की प्राप्ति हेतु भगवान सूर्यनारायण को तांबे के पात्र से अर्घ्य समर्पण।",
            "bn": "আরোগ্য ও তেজ বৃদ্ধির কামনায় ভগবান সূর্যদেবের উদ্দেশ্যে পবিত্র স্নান ও রক্তচন্দন সহযোগে তর্পণ।"
        },
        "muhurta_type": "sunrise_snan",
        "muhurta_label": {"en": "Sunrise Arghya Muhurta", "hi": "सूर्योदय अर्घ्य मुहूर्त", "bn": "সূর্যোদয় অর্ঘ্যদান মুহূর্ত"}
    },

    ("Kartika", "Krishna", 8): {
        "en": "Ahoi Ashtami Vrat / Radha Kunda Snan",
        "hi": "अहोई अष्टमी व्रत / राधा कुंड स्नान",
        "bn": "শ্রী শ্রী অহোই অষ্টমী ব্রত / শ্রী রাধাকুণ্ডে মধ্যরাত্রি মহাস্নান",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪔", "deity": {"en": "Maa Ahoi & Srimati Radharani", "hi": "माँ अहोई व श्रीमती राधारानी", "bn": "মা অহোই ও শ্রীমতী রাধারাণী"},
        "description": {
            "en": "Mothers observe nirjala fast for child longevity until evening star sighting, alongside sacred Radha Kunda snan.",
            "hi": "संतान की दीर्घायु हेतु माताओं द्वारा निर्जला अहोई व्रत, संध्या तारा दर्शन एवं राधाकुंड मध्यरात्रि स्नान।",
            "bn": "সন্তানের দীর্ঘায়ু কামনায় সায়াহ্নে নক্ষত্র দর্শন পর্যন্ত অহোই ব্রত এবং ব্রজমণ্ডলে পবিত্র রাধাকুণ্ডে নিশীথ স্নান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Star Gazing & Puja", "hi": "सायंकाल तारा दर्शन व पूजा", "bn": "সায়ংকালে তারা দর্শন ও পূজা লগ্ন"}
    },

    ("Kartika", "Krishna", 11): {
        "en": "Rama Ekadashi Vrata",
        "hi": "रमा एकादशी व्रत",
        "bn": "শ্রী শ্রী রমা একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪷", "deity": {"en": "Lord Sri Hari Vishnu & Maa Rama (Lakshmi)", "hi": "भगवान विष्णु व माता रमा (लक्ष्मी)", "bn": "শ্রীহরি বিষ্ণু ও দেবী রমা (লক্ষ্মী)"},
        "description": {
            "en": "Auspicious fast prior to Diwali to invoke the divine grace of Lord Vishnu and Goddess Lakshmi.",
            "hi": "दीपावली से पूर्व अखंड सौभाग्य एवं लक्ष्मी-नारायण की कृपा प्राप्ति हेतु रमा एकादशी महाव्रत।",
            "bn": "দীপাবলির প্রাক্কালে শ্রীশ্রী লক্ষ্মী-নারায়ণের চিরকৃপা ও সর্বপাপ মুক্তির উদ্দেশ্যে পরম পবিত্র ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा व व्रत", "bn": "প্রাতঃকালীন পূজা ও উপবাস সংকল্প"}
    },

    ("Kartika", "Krishna", 12): {
        "en": "Govatsa Dwadashi (Bachh Baras / Gau Puja)",
        "hi": "गोवत्स द्वादशी (बछ बारस / गौ माता पूजा)",
        "bn": "শ্রী শ্রী গোবৎসা দ্বাদশী (কামধেনু রূপিণী গাভী ও বাছুর পূজা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "पारंपरिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🐄", "deity": {"en": "Kamadhenu Gau Mata & Sri Krishna", "hi": "कामधेनु गौ माता व श्रीकृष्ण", "bn": "কামধেনু গো-মাতা ও শ্রীকৃষ্ণ"},
        "description": {
            "en": "Veneration of sacred Mother Cow and her calf with traditional offerings, expressing gratitude to Kamadhenu.",
            "hi": "संतान रक्षा ও सुख-समृद्धि हेतु कामधेनु स्वरूपा गौ माता एवं बछड़े का कृतज्ञतापूर्वक पूजन।",
            "bn": "সন্তানের মঙ্গল ও পারিবারিক সমৃদ্ধির কামনায় গো-মাতা ও বাছুরের সস্নেহ আরাধনা ও খাদ্য নিবেদন।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal Gau Puja", "hi": "प्रदोष काल गो-पूजा", "bn": "প্রদোষ কাল গো-পূজা মুহূর্ত"}
    },

    ("Kartika", "Krishna", 13): {
        "en": "Dhanteras / Dhanvantari Jayanti / Kuber Puja / Yama Deepam",
        "hi": "धनतेरस / धन्वंतरि जयंती / कुबेर पूजा / यम दीपदान",
        "bn": "শ্রী শ্রী ধনতেরাস / ধন্বন্তরি জয়ন্তী / কুবের পূজা / যম প্রদীপ দান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪙", "deity": {"en": "Lord Dhanvantari, Kuber & Yamaraja", "hi": "भगवान धन्वंतरि, कुबेर व यमराज", "bn": "ভগবান ধন্বন্তরি, কুবের দেব ও যমরাজ"},
        "description": {
            "en": "Appearance of Lord Dhanvantari with the pot of Amrita, worshipping Lord Kuber, and evening Yama Deepam.",
            "hi": "समुद्र मंथन से अमृत कलश युक्त भगवान धन्वंतरि का प्राकट्य, कुबेर पूजन एवं अकाल मृत्यु निवारण दीपदान।",
            "bn": "সমুদ্র মন্থনে অমৃত কলশসহ ধন্বন্তরীর আবির্ভাব, কুবের দেবের অর্চনা এবং অকালমৃত্যু নিবারণে যম প্রদীপ দান।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal & Vrishabha Lagna", "hi": "प्रदोष काल व स्थिर वृषभ लग्न", "bn": "প্রদোষ কাল ও স্থির বৃষ লগ্ন"}
    },

    ("Kartika", "Krishna", 14): {
        "en": "Kali Chaudas / Naraka Chaturdashi / Bhoot Chaturdashi / 14 Deepam",
        "hi": "काली चौदस / नरक चतुर्दशी / रूप चौदस / यम दीपदान",
        "bn": "শ্রী শ্রী কালী চৌদস / নরক চতুর্দশী / ভূত চতুর্দশী (১৪ প্রদীপ ও ১৪ শাক গ্রহণ)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Mahakali, Yamaraja & Sri Krishna", "hi": "माँ महाकाली, यमराज व श्रीकृष्ण", "bn": "মা মহাকালী, যমরাজ ও শ্রীকৃষ্ণ"},
        "description": {
            "en": "Midnight worship of Mahakali, Abhyanga Snan, and lighting 14 lamps to dispel dark energies and honour ancestors.",
            "hi": "नकारात्मक शक्तियों के नाश हेतु मध्यरात्रि महाकाली पूजा, अभ्यंग स्नान एवं चौदह यमदीप प्रज्वलन।",
            "bn": "নিশীথ রাতে মা মহাকালীর আরাধনা, চতুর্দশ প্রদীপ দান ও চোদ্দ শাক গ্রহণ করে অশুভ শক্তি দূরীকরণ।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Mahakali Puja", "hi": "निशीथ काल महाकाली पूजा", "bn": "নিশীথ কাল মহাকালী পূজা লগ্ন"}
    },

    ("Kartika", "Krishna", 15): {
        "en": "Diwali (Lakshmi Puja) / Shyama Kali Puja / Kartika Amavasya",
        "hi": "दीपावली (महालक्ष्मी पूजा) / श्यामा काली पूजा / कार्तिक अमावस्या",
        "bn": "শ্রী শ্রী দীপাবলি মহোৎসব (মহালক্ষ্মী পূজা) / শ্রী শ্রী শ্যামাপূজা (কালীপূজা) / অমাবস্যা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Maa Mahalakshmi, Ganesha & Maa Shyama Kali", "hi": "माँ महालक्ष्मी, गणेश जी व माँ श्यामा काली", "bn": "মা মহালক্ষ্মী, শ্রী গণেশ ও মা শ্যামা কালী"},
        "description": {
            "en": "Grand celebration of light over darkness, worshipping Goddess Lakshmi in Pradosha and Mother Kali at midnight.",
            "hi": "अंधकार पर प्रकाश की विजय का दीपोत्सव, प्रदोष काल में महालक्ष्मी पूजन एवं मध्यरात्रि में तांत्रिक काली पूजा।",
            "bn": "অজ্ঞানতার অন্ধকার বিনাশে আলোর দীপাবলি, প্রদোষে মা লক্ষ্মী পূজা এবং অমাবস্যার নিশীথে শ্যামাপূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh & Nishita Kaal Puja", "hi": "प्रदोष व निशीथ काल", "bn": "প্রদোষ ও নিশীথ কাল মহালগ্ন"}
    },

    # --- কার্তিক শুক্ল পক্ষ ---
    ("Kartika", "Shukla", 1): {
        "en": "Govardhan Puja / Annakut Mahotsav / Dyuta Krida / Ishti Havan",
        "hi": "गोवर्धन पूजा / अन्नकूट महोत्सव / द्यूत क्रीड़ा / वैदिक इष्टि",
        "bn": "শ্রী শ্রী গোবর্ধন পূজা / অন্নকূট মহোৎসব / দ্যূত ক্রীড়া / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "⛰️", "deity": {"en": "Lord Giriraj Krishna & Shiva-Parvati", "hi": "गिरिराज भगवान श्रीकृष्ण व शिव-पार्वती", "bn": "গিরিরাজ ভগবান শ্রীকৃষ্ণ ও শিব-পার্বতী"},
        "description": {
            "en": "Offering 56 delicacies (Chhappan Bhog) to Govardhan Hill, traditional Dyuta Krida, and Vedic Ishti rituals.",
            "hi": "भगवान श्रीकृष्ण द्वारा गोवर्धन पर्वत धारण, ५६ भोग अन्नकूट समर्पण, पावन द्यूत क्रीड़ा एवं इष्टि दिवस।",
            "bn": "ছাপ্পান্ন ভোগসহ শ্রীগোবর্ধন পূজা, অন্নকূট মহোৎসব, পাশাখেলা স্মরণে দ্যূত ক্রীড়া ও বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah & Sayankal Annakut", "hi": "प्रातः व सायंकाल अन्नकूट", "bn": "প্রাতঃ ও সায়ংকালীন অন্নকূট লগ্ন"}
    },

    ("Kartika", "Shukla", 2): {
        "en": "Bhai Phonta / Bhaiya Dooj / Yama Dwitiya / Chandra Darshana",
        "hi": "भाई दूज / यम द्वितीया / भ्रातृ द्वितीया / चन्द्र दर्शन",
        "bn": "পবিত্র ভাইফোঁটা (ভ্রাতৃদ্বিতীয়া / যমদ্বিতীয়া) / শুক্ল দ্বিতীয়া চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Yamuna, Yamaraja & Chandra Deva", "hi": "यमुना जी, यमराज व चन्द्र देव", "bn": "যমুনা দেবী, যমরাজ ও চন্দ্র দেব"},
        "description": {
            "en": "Sisters apply protective tilak for brothers' longevity on Yama Dwitiya, followed by evening crescent moon sighting.",
            "hi": "भाई की दीर्घायु व सर्वविपत्ति नाश हेतु तिलक संस्कार एवं सायंकाल नवचंद्र (द्वितीया चंद्र) दर्शन।",
            "bn": "যমের দুয়ারে কাঁটা দিয়ে ভাইয়ের দীর্ঘায়ু কামনায় পবিত্র ভাইফোঁটা প্রদান এবং সায়াহ্নে শুক্ল দ্বিতীয়া চন্দ্র দর্শন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tilak & Chandra Darshan", "hi": "अपराह्न तिलक व चंद्र दर्शन", "bn": "অপরাহ্ন ভাইফোঁটা ও চন্দ্র দর্শন লগ্ন"}
    },

    ("Kartika", "Shukla", 5): {
        "en": "Labh Panchami (Saubhagya Panchami / Chopda Pujan)",
        "hi": "लाभ पंचम (सौभाग्य पंचमी / चोपड़ा पूजन)",
        "bn": "শ্রী শ্রী লাভ পঞ্চম (সৌভাগ্য পঞ্চমী / ব্যবসায়িক শুভ খাতা পূজা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "व्यापारिक पर्व", "bn": "মহাপর্ব"},
        "icon": "🪙", "deity": {"en": "Lord Ganesha & Maa Mahalakshmi", "hi": "भगवान श्री गणेश व माँ महालक्ष्मी", "bn": "শ্রী গণেশ ও মা মহালক্ষ্মী"},
        "description": {
            "en": "Auspicious day for opening new ledgers, shops, and business enterprises following Diwali.",
            "hi": "दीपावली के बाद नए व्यापार, दुकान व प्रतिष्ठानों के शुभ उद्घाटन हेतु लाभ पंचम।",
            "bn": "দীপাবলি পরবর্তী নতুন ব্যবসা, দোকান ও হিসাবের খাতা খোলার পরম সৌভাগ্যদায়ী লাভ পঞ্চম তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Labh Muhurta (Morning)", "hi": "लाभ काल मुहूर्त", "bn": "লাভ কাল প্রাতঃ মুহূর্ত"}
    },

    ("Kartika", "Shukla", 6): {
        "en": "Chhath Puja (Sandhya Arghya / Surya Sashthi)",
        "hi": "छठ पूजा (संध्या अर्घ्य / सूर्य षष्ठी महाव्रत)",
        "bn": "ছট পূজা (সন্ধ্যার অর্ঘ্যদান ও সূর্য ষষ্ঠী মহাব্রত)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "☀️", "deity": {"en": "Surya Deva & Chhathi Maiya", "hi": "भगवान सूर्य व छठी मइया", "bn": "ভগবান সূর্য দেব ও ছটি মাইয়া"},
        "description": {
            "en": "Offering sacred evening oblation (Sanjhiya Arghya) in water bodies to the setting Sun God.",
            "hi": "पवित्र जलाशयों में खड़े होकर अस्ताचलगामी भगवान सूर्य एवं छठी मइया को प्रथम संध्या अर्घ्य अर्पण।",
            "bn": "জলে দাঁড়িয়ে অস্তগামী ভগবান সূর্য দেব ও পরমাপ্রকৃতি ছটি মাইয়ার উদ্দেশ্যে পবিত্র সায়ং অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sunset / Sandhya Arghya Muhurta", "hi": "सूर्यास्त संध्या अर्घ्य मुहूर्त", "bn": "সূর্যাস্ত সায়ং অর্ঘ্যদান মুহূর্ত"}
    },

    # --------------------------------------------------------------------------
    # মার্গশীর্ষ মাস (Margashirsha)
    # --------------------------------------------------------------------------
    ("Margashirsha", "Krishna", 4): {
        "en": "Ganadhipa Sankashti Chaturthi",
        "hi": "गणाधिप संकष्टी चतुर्थी",
        "bn": "গণাধিপ সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha (Ganadhipa)", "hi": "भगवान गणाधिप गणेश", "bn": "ভগবান গণাধিপ শ্রী গণেশ"},
        "description": {
            "en": "Margashirsha Krishna Chaturthi fast invoking Ganadhipa Ganesha for eliminating hindrances.",
            "hi": "मार्गशीर्ष कृष्ण चतुर्थी पर समस्त विघ्नों के शमन हेतु गणाधिप गणेश का चंद्रोदय व्रत।",
            "bn": "মার্গশীর্ষ কৃষ্ণ চতুর্থীতে বিঘ্নবিনাশক শ্রী গণাধিপ গণেশের ব্রত ও চন্দ্রোদয়ে পূজা সমাপন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Muhurta", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },
    ("Margashirsha", "Krishna", 8): {
        "en": "Kalabhairav Jayanti / Mahakaal Ashtami",
        "hi": "कालभैरव जयंती / महाकाल भैरवाष्टमी",
        "bn": "শ্রী শ্রী কালভৈরব জয়ন্তী / মহাকাল ভৈরবাষ্টমী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Lord Kalabhairava & Shiva", "hi": "भगवान कालभैरव", "bn": "ভগবান কালভৈরব ও শিব"},
        "description": {
            "en": "Divine appearance day of Lord Kalabhairava, the fierce manifestation of Lord Shiva to protect Dharma.",
            "hi": "धर्म रक्षा एवं भक्तों के भय निवारण हेतु भगवान शिव के उग्र रूप कालभैरव का प्राकट्योत्सव।",
            "bn": "ভক্তদের সর্বভয় দূর করতে দেবাদিদেব শিবের রুদ্র রূপ শ্রী কালভৈরবের শুভ আবির্ভাব মহোৎসব।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Puja", "hi": "निशीथ काल पूजा", "bn": "নিশীথ কাল ভৈরব পূজা"}
    },
    ("Margashirsha", "Krishna", 11): {
        "en": "Utpanna Ekadashi",
        "hi": "उत्पन्ना एकादशी",
        "bn": "উৎপন্না একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Ekadashi Devi & Lord Vishnu", "hi": "एकादशी देवी व श्री हरि", "bn": "একাদশী দেবী ও ভগবান বিষ্ণু"},
        "description": {
            "en": "Celebrates the emergence of Ekadashi Devi from Lord Vishnu's body to slay Mura.",
            "hi": "भगवान विष्णु के शरीर से एकादशी देवी के पावन प्राकट्य का मूल एकादशी दिवस।",
            "bn": "মুর অসুর বিনাশে শ্রীহরির অঙ্গ থেকে একাদশী দেবীর শুভ উৎপত্তির মহাপুণ্য তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
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
    ("Margashirsha", "Shukla", 14): {
        "en": "Maa Matangi Jayanti (9th Mahavidya)",
        "hi": "माँ मातंगी जयंती (नवमी महाविद्या)",
        "bn": "মা মাতঙ্গী জয়ন্তী (৯ম মহাবিদ্যা)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महाविद्या जयंती", "bn": "মহাবিদ্যা মহাপর্ব"},
        "icon": "🦜", "deity": {"en": "Maa Matangi (Tantric Saraswati)", "hi": "माँ मातंगी देवी", "bn": "মা মাতঙ্গী দেবী"},
        "description": {
            "en": "Appearance of the 9th Mahavidya Matangi, presiding over arts and divine speech.",
            "hi": "संगीत, कला व तंत्र विद्या की अधिष्ठात्री नौवीं महाविद्या माँ मातंगी का प्राकट्योत्सव।",
            "bn": "শিল্প, সংগীত ও সর্ববিদ্যার অধিষ্ঠাত্রী নবম মহাবিদ্যা মা মাতঙ্গীর শুভ আবির্ভাব।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Midnight Puja", "hi": "निशीथ काल", "bn": "নিশীথ কাল সাধনা মুহূর্ত"}
    },
    ("Margashirsha", "Shukla", 15): {
        "en": "Dattatreya Jayanti / Annapurna Jayanti / Margashirsha Purnima",
        "hi": "दत्तात्रेय जयंती / अन्नपूर्णा जयंती / मार्गशीर्ष पूर्णिमा",
        "bn": "শ্রী দত্তাত্রেয় জয়ন্তী / মা অন্নপূর্ণা আবির্ভাব / মার্গশীর্ষ পূর্ণিমা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Lord Dattatreya & Maa Annapurna", "hi": "भगवान दत्तात्रेय व माँ अन्नपूर्णा", "bn": "ভগবান দত্তাত্রেয় ও মা অন্নপূর্ণা"},
        "description": {
            "en": "Appearance of Lord Dattatreya (composite trimurti) and Maa Annapurna.",
            "hi": "ब्रह्मा, विष्णु, महेश के संयुक्त त्रिदेव रूप भगवान दत्तात्रेय एवं माँ अन्नपूर्णा का प्राकट्योत्सव।",
            "bn": "ব্রহ্মা, বিষ্ণু ও শিবের সমন্বিত রূপ ভগবান দত্তাত্রেয় এবং মা অন্নপূর্ণার শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Evening)", "hi": "प्रदोष काल (संध्याकाल)", "bn": "প্রদোষ কাল (সন্ধ্যাবেলা)"}
    },

    # --------------------------------------------------------------------------
    # পৌষ মাস (Pausha)
    # --------------------------------------------------------------------------
    ("Pausha", "Krishna", 11): {
        "en": "Saphala Ekadashi",
        "hi": "सफला एकादशी",
        "bn": "সফলা একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Narayana", "hi": "भगवान नारायण", "bn": "ভগবান নারায়ণ"},
        "description": {
            "en": "Saphala Ekadashi makes all noble endeavors and efforts entirely fruitful.",
            "hi": "समस्त कार्यों को सफल बनाने एवं सद्गति देने वाला सफला एकादशी व्रत।",
            "bn": "সকল সৎকর্মকে সফল ও সার্থক করে তোলার পরম কল্যাণদায়ী সফলা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Pausha", "Shukla", 1): {
        "en": "Pausha Shukla Pratipada / Ishti Havan",
        "hi": "पौष शुक्ल प्रतिपदा / इष्टि",
        "bn": "পৌষ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Auspicious commencement of Pausha Shukla Paksha observing sacred Vedic Ishti havan.",
            "hi": "पौष शुक्ल पक्ष का पावन प्रारंभ एवं सुख-समृद्धि हेतु वैदिक इष्टि अनुष्ठान।",
            "bn": "পৌষ শুক্লপক্ষের পুণ্য সূচনা এবং পরম কল্যাণ কামনায় বৈদিক ইষ্টি যজ্ঞ অনুষ্ঠান।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Pausha", "Shukla", 2): {
        "en": "Chandra Darshana (Pausha Shukla)",
        "hi": "पौष चन्द्र दर्शन",
        "bn": "পৌষ শুক্ল দ্বিতীয়া চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Observance", "hi": "धार्मिक दर्शन", "bn": "চন্দ্র দর্শন"},
        "icon": "🌙", "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"},
        "description": {
            "en": "Auspicious sighting of the crescent moon after sunset for peace, harmony, and mental clarity.",
            "hi": "मानसिक शांति व सौभाग्य वृद्धि हेतु सायंकाल नवचंद्र (द्वितीया चंद्र) दर्शन व अर्घ्य।",
            "bn": "মানসিক প্রশান্তি ও সৌভাগ্য বৃদ্ধির কামনায় সায়ংকালে অমাবস্যা-পরবর্তী নবচন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },
    ("Pausha", "Shukla", 7): {
        "en": "Guru Gobind Singh Jayanti (Prakash Parv)",
        "hi": "गुरु गोबिंद सिंह जयंती (प्रकाश पर्व)",
        "bn": "দশম গুরু গোবিন্দ সিংহ জয়ন্তী (প্রকাশ পর্ব)",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "प्रकाश पर्व", "bn": "মহাপর্ব"},
        "icon": "⚔️", "deity": {"en": "Guru Gobind Singh Ji", "hi": "गुरु गोबिंद सिंह जी", "bn": "শ্রী গুরু গোবিন্দ সিংহ জী"},
        "description": {
            "en": "Birth anniversary of the tenth Sikh Guru, warrior-poet and founder of the Khalsa Panth.",
            "hi": "खालसा पंथ के संस्थापक एवं दशम सिख गुरु गोबिंद सिंह जी का पावन प्रकाश जन्मोत्सव।",
            "bn": "খালসা পন্থের প্রতিষ্ঠাতা ও দশম শিখ গুরু গোবিন্দ সিংহজীর পরম পবিত্র প্রকাশ পর্ব ও জন্মজয়ন্তী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Kaal Prakash Utsav", "hi": "प्रातः प्रकाश पर्व", "bn": "প্রাতঃকালীন প্রকাশ মহোৎসব"}
    },
    ("Pausha", "Shukla", 11): {
        "en": "Pausha Putrada Ekadashi / Tailang Swami Jayanti",
        "hi": "पौष पुत्रदा एकादशी / तैलंग स्वामी जयंती",
        "bn": "পৌষ পুত্রদা একাদশী ব্রত / ত্রৈলঙ্গ স্বামী জয়ন্তী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Vishnu & Trailanga Swami", "hi": "भगवान विष्णु व तैलंग स्वामी", "bn": "ভগবান শ্রীহরি বিষ্ণু ও ত্রৈলঙ্গ স্বামী"},
        "description": {
            "en": "Fasting for child welfare alongside the birth celebration of the Walking Shiva of Varanasi, Trailanga Swami.",
            "hi": "संतान कल्याणकारी पुत्रदा एकादशी एवं काशी के सचल विश्वनाथ स्वामी तैलंग का पावन जन्मोत्सव।",
            "bn": "সন্তানের কল্যাণদায়ী পুত্রদা একাদশী এবং কাশীর সচল শিব যোগীরাজ ত্রৈলঙ্গ স্বামীর আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
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
    ("Magha", "Krishna", 1): {
        "en": "Magha Krishna Pratipada / Ishti Havan",
        "hi": "माघ कृष्ण प्रतिपदा / इष्टि",
        "bn": "মাঘ কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Pitru Devas", "hi": "अग्नि देव व पितृ गण", "bn": "অগ্নি দেব ও পিতৃপুরুষগণ"},
        "description": {
            "en": "Beginning of Magha Krishna Paksha observing traditional Ishti fire oblations.",
            "hi": "माघ कृष्ण पक्ष का प्रारंभ एवं पितृ-देव तृप्ति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "মাঘ কৃষ্ণপক্ষের শুভ সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ লগ্ন"}
    },
    ("Magha", "Krishna", 4): {
        "en": "Sakat Chauth / Lambodara Sankashti Chaturthi / Tilkuta Chauth",
        "hi": "सकट चौथ / लंबोदर संकष्टी चतुर्थी / तिलकुटा चौथ",
        "bn": "সঙ্কট চৌথ / লম্বোদর সংকষ্টী চতুর্থী (তিলকুটা চতুর্থী ব্রত)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Lambodara (Ganesha) & Chandra", "hi": "भगवान लंबोदर गणेश व चन्द्र देव", "bn": "ভগবান লম্বোদর গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Mothers observe severe fast offering sesame laddus to Lord Lambodara for children's longevity, broken at moonrise.",
            "hi": "संतानों के संकट निवारण व दीर्घायु हेतु माताओं द्वारा तिल-गुड़ भोग युक्त निर्जला सकट चौथ व्रत।",
            "bn": "সন্তানের দীর্ঘায়ু ও সর্বসংকট নাশে মায়েদের পরম নিষ্ঠাপূর্ণ তিলকুটা উপবাস ও চন্দ্রোদয়ে অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },
    ("Magha", "Krishna", 7): {
        "en": "Swami Vivekananda Jayanti (Tithi-based / Samvat)",
        "hi": "स्वामी विवेकानंद जयंती (संवत / तिथि आधारित)",
        "bn": "যুগনায়ক স্বামী বিবেকানন্দ জন্মতিথি (তিথিভিত্তিক / পৌষী কৃষ্ণা সপ্তমী)",
        "category": "hindu", "type": {"en": "Jayanti", "hi": "पावन जयंती", "bn": "আবির্ভাব জয়ন্তী"},
        "icon": "🕉️", "deity": {"en": "Swami Vivekananda & Sri Ramakrishna", "hi": "स्वामी विवेकानंद व रामकृष्ण परमहंस", "bn": "স্বামী বিবেকানন্দ ও শ্রীরামকৃষ্ণ"},
        "description": {
            "en": "Traditional Hindu lunar tithi celebration of the advent of Swami Vivekananda on Magha Krishna Saptami.",
            "hi": "माघ कृष्ण सप्तमी पर सनातन धर्म के पुनर्जागरणकर्ता स्वामी विवेकानंद का पावन जन्मतिथी उत्सव।",
            "bn": "সনাতন ধর্মের বিশ্বদূত যুগনায়ক স্বামী বিবেকানন্দের শাস্ত্রীয় তিথিভিত্তিক জন্মজয়ন্তী মহোৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Pratah Smaran & Puja", "hi": "प्रातः वंदन व पूजा", "bn": "প্রাতঃকালীন স্মরণ ও পূজার্চনা"}
    },
    ("Magha", "Krishna", 11): {
        "en": "Shattila Ekadashi (6 Sesame Rituals)",
        "hi": "षटतिला एकादशी",
        "bn": "ষট্তিলা একাদশী ব্রত (৬ প্রকার তিল দান)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Observing 6 types of sesame charity on Shattila Ekadashi eradicates afflictions.",
            "hi": "तिल के ६ प्रकार के प्रयोग व दान से दरिद्रता का नाश करने वाली षटतिला एकादशी।",
            "bn": "৬ প্রকার তিলের ব্যবহারে পাপ ও দুর্ভাগ্য দূরকারী মহাপুণ্যময়ী ষট্তিলা একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Snan & Til Dan", "hi": "प्रातः स्नान व तिल दान", "bn": "প্রাতঃস্নান ও তিল দান লগ্ন"}
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
        "en": "Mauni Amavasya / Magha Amavasya Mahasnan / Darsha Amavasya",
        "hi": "मौनी अमावस्या / माघ अमावस्या महास्नान / दर्श अमावस्या",
        "bn": "মৌনী অমাবস্যা / মাঘী অমাবস্যা মহাতীর্থ স্নান / দর্শ অমাবস্যা",
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
    ("Magha", "Shukla", 1): {
        "en": "Magha Gupt Navratri Begins / Ishti Havan",
        "hi": "माघ गुप्त नवरात्रि प्रारंभ / घटस्थापना / इष्टि",
        "bn": "মাঘ গুপ্ত নবরাত্রি আরম্ভ / ঘটস্থাপন / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "साधना पर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Das Mahavidya & Maa Durga", "hi": "दस महाविद्या व माँ दुर्गा", "bn": "দশমহাবিদ্যা ও মা দুর্গা"},
        "description": {
            "en": "Auspicious commencement of winter Gupt Navratri with Ghatasthapana and sacred Vedic Ishti oblations.",
            "hi": "शिशिर ऋतु में आत्मिक शक्ति हेतु गुप्त नवरात्रि घटस्थापना एवं वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "শীতকালীন গুপ্ত নবরাত্রির পুণ্য ঘটস্থাপন এবং সর্বকল্যাণ কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Ghatasthapana & Ishti Muhurta", "hi": "घटस्थापना व इष्टि मुहूर्त", "bn": "ঘটস্থাপন ও ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Magha", "Shukla", 2): {
        "en": "Chandra Darshana (Magha Shukla)",
        "hi": "माघ चन्द्र दर्शन",
        "bn": "মাঘ শুক্ল দ্বিতীয়া চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Observance", "hi": "धार्मिक दर्शन", "bn": "চন্দ্র দর্শন"},
        "icon": "🌙", "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"},
        "description": {
            "en": "Sighting of the auspicious new crescent moon after sunset for peace, mental clarity, and fortune.",
            "hi": "मानसिक शांति व सौभाग्य वृद्धि हेतु सायंकाल नवचंद्र (द्वितीया चंद्र) दर्शन व अर्घ्य।",
            "bn": "মানসিক শান্তি ও সৌভাগ্য বৃদ্ধির কামনায় সায়ংকালে অমাবস্যা-পরবর্তী দ্বিতীয়ার শুভ চন্দ্র দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
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
        "category": "hindu", "type": {"en": "Vrata", "hi": "तর্পণ পর্ব", "bn": "উপবাস ব্রত"},
        "icon": "🏹", "deity": {"en": "Bhishma Pitamah", "hi": "पितामह भीष्म", "bn": "পিতামহ ভীষ্ম"},
        "description": {
            "en": "Commemorating the departure of Grandsire Bhishma on Uttarayana and offering him water tarpan.",
            "hi": "सूर्य के उत्तरायण होने पर इच्छामृत्यु प्राप्त पितामह भीष्म के मोक्ष गमन पर श्राद्ध व तर्पण।",
            "bn": "সূর্যের উত্তরায়ণে পিতামহ ভীষ্মের মোক্ষলাভ স্মরণে সর্ববর্ণের ভক্তগণের তৃপ্তিদায়ক ভীষ্ম তর্পণ।"
        },
        "muhurta_type": "madhyahna",
        "muhurta_label": {"en": "Madhyahna Tarpan Kaal", "hi": "मध्याह्न तर्पण काल", "bn": "মধ্যাহ্ন তর্পণ সময়"}
    },
    ("Magha", "Shukla", 11): {
        "en": "Jaya Ekadashi / Bhaimi Ekadashi",
        "hi": "जया एकादशी (भैमी एकादशी)",
        "bn": "জয়া একাদশী ব্রত (ভৈমী একাদশী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Jaya Ekadashi prevents falling into ghostly realms and bestows victory.",
            "hi": "पिशाच योनि से मुक्ति दिलाकर विजय प्रदान करने वाला जया एकादशी महाव्रत।",
            "bn": "প্রেতযোনি থেকে মুক্তি ও সর্বক্ষেত্রে জয়লাভের বরদাত্রী জয়া একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Magha", "Shukla", 15): {
        "en": "Magha Purnima / Guru Ravidas Jayanti / Maha Maghi Snan / Lalita Jayanti / Anvadhan",
        "hi": "माघ पूर्णिमा / संत रविदास जयंती / महा माघी स्नान / ललिता जयंती / अन्वाधान",
        "bn": "মাঘী পূর্ণিমা / সন্ত রবিদাস জয়ন্তী / মহামাঘী স্নান / মা ললিতা জয়ন্তী / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🌊", "deity": {"en": "Lord Vishnu, Ganga & Sant Ravidas", "hi": "विष्णु जी, गंगा व संत रविदास", "bn": "শ্রীহরি বিষ্ণু, গঙ্গা ও সন্ত রবিদাস"},
        "description": {
            "en": "Confluence of deities in sacred rivers, highly praised for Prayag Triveni Sangam snan and Ravidas Jayanti.",
            "hi": "प्रयागराज त्रिवेणी संगम में पावन स्नान, संत रविदास जयंती एवं माँ ललिता प्राकट्योत्सव।",
            "bn": "প্রয়াগরাজ ও সর্বতীর্থে পুণ্যস্নান, দান, সন্ত রবিদাসের আবির্ভাব ও দেবী ললিতা ত্রিপুরাসুন্দরীর শুভ আবির্ভাব।"
        },
        "muhurta_type": "brahma",
        "muhurta_label": {"en": "Brahma Muhurta & Sunrise Snan", "hi": "ब्रह्म मुहूर्त व सूर्योदय स्नान", "bn": "ব্রাহ্ম মুহূর্ত ও সূর্যোদয় মহাতীর্থ স্নান"}
    },

    # --------------------------------------------------------------------------
    # ফাল্গুন মাস (Phalguna)
    # --------------------------------------------------------------------------
    ("Phalguna", "Krishna", 1): {
        "en": "Phalguna Krishna Pratipada / Ishti Havan",
        "hi": "फाल्गुन कृष्ण प्रतिपदा / इष्टि",
        "bn": "ফাল্গুন কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Inception of Phalguna Krishna Paksha observing traditional Ishti fire rituals.",
            "hi": "फाल्गुन कृष्ण पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "ফাল্গুন কৃষ্ণপক্ষের সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Phalguna", "Krishna", 4): {
        "en": "Dwijapriya Sankashti Chaturthi / Bhalachandra Sankashti",
        "hi": "द्विजप्रिय संकष्टी चतुर्थी / भालचंद्र संकष्टी",
        "bn": "দ্বিজপ্রিয় সংকষ্টী চতুর্থী ব্রত / ভালচন্দ্র সংকষ্টী",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Dwijapriya Ganesha & Chandra", "hi": "भगवान द्विजप्रिय गणेश व चन्द्र देव", "bn": "ভগবান দ্বিজপ্রিয় শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Fasting dedicated to Lord Dwijapriya Ganesha to attain wisdom and overcome obstacles.",
            "hi": "बुद्धि व आरोग्यता की प्राप्ति हेतु द्विजप्रिय गणेश का पावन व्रत एवं चंद्र दर्शन।",
            "bn": "জ্ঞান ও সুস্বাস্থ্য কামনায় শ্রী দ্বিজপ্রিয় গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Muhurta", "hi": "चन्द्रोदय व पूजन मुहूर्त", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}
    },
    ("Phalguna", "Krishna", 10): {
        "en": "Maharishi Dayanand Saraswati Jayanti",
        "hi": "महर्षि दयानंद सरस्वती जयंती",
        "bn": "মহর্ষি দয়ানন্দ সরস্বতী জয়ন্তী",
        "category": "hindu", "type": {"en": "Jayanti", "hi": "जयंती पर्व", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Maharishi Dayanand Saraswati", "hi": "महर्षि दयानंद सरस्वती", "bn": "মহর্ষি দয়ানন্দ সরস্বতী"},
        "description": {
            "en": "Birth anniversary of Swami Dayanand Saraswati, the founder of Arya Samaj and Vedic revivalist.",
            "hi": "आर्य समाज के संस्थापक एवं वेदों के प्रचारक महर्षि दयानंद सरस्वती का पावन जन्मोत्सव।",
            "bn": "আর্য সমাজের প্রতিষ্ঠাতা ও বৈদিক দর্শনের পুনরুজ্জীবক মহর্ষি দয়ানন্দ সরস্বতীর শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Prayer & Havan", "hi": "प्रातः वंदन व हवन", "bn": "প্রাতঃকালীন স্মরণ ও বৈদিক যজ্ঞ"}
    },
    ("Phalguna", "Krishna", 11): {
        "en": "Vijaya Ekadashi",
        "hi": "विजया एकादशी",
        "bn": "বিজয়া একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🏹", "deity": {"en": "Lord Sri Rama & Vishnu", "hi": "भगवान श्रीराम व विष्णु", "bn": "ভগবান শ্রীরামচন্দ্র ও বিষ্ণু"},
        "description": {
            "en": "Lord Rama observed Vijaya Ekadashi prior to Lanka crossing, granting victory in struggles.",
            "hi": "लंका विजय हेतु भगवान श्रीराम द्वारा आचरित सर्वविजय प्रदाता एकादशी व्रत।",
            "bn": "লঙ্কা বিজয়ের উদ্দেশ্যে শ্রীরামচন্দ্র কর্তৃক পালিত সর্বসংকটে বিজয়দাত্রী একাদশী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
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
        "muhurta_label": {"en": "Nishita Kaal (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ काल मुहूर्त (মধ্যরাত্রি)"}
    },
    ("Phalguna", "Krishna", 15): {
        "en": "Phalguna Amavasya / Darsha Amavasya / Anvadhan",
        "hi": "फाल्गुन अमावस्या / दर्श अमावस्या / अन्वाधान",
        "bn": "ফাল্গুনী অমাবস্যা / দর্শ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "উপবাস ও তর্পণ", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "Pitru Devas & Lord Shiva", "hi": "पितृ देव व भगवान शिव", "bn": "পিতৃপুরুষ ও মহাদেব"},
        "description": {
            "en": "Auspicious new moon day of Phalguna for sacred holy dip, ancestor charity, and Vedic Anvadhan rituals.",
            "hi": "पितरों की शांति, पवित्र तीर्थ स्नान एवं इष्टि पूर्व अन्वाधान अनुष्ठान का पावन दिन।",
            "bn": "পিতৃপুরুষের আত্মার তৃপ্তির জন্য পবিত্র স্নান, তর্পণ, দান এবং বৈদিক অন্বাধান সংস্কার পালন।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan & Snan", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ ও স্নান লগ্ন"}
    },
    ("Phalguna", "Shukla", 1): {
        "en": "Phalguna Shukla Pratipada / Ishti Havan",
        "hi": "फाल्गुन शुक्ल प्रतिपदा / इष्टि",
        "bn": "ফাল্গুন শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Lord Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Commencement of Phalguna Shukla Paksha observing sacred Vedic Ishti fire rituals for auspiciousness.",
            "hi": "फाल्गुन शुक्ल पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "ফাল্গুন শুক্লপক্ষের শুভ সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Phalguna", "Shukla", 2): {
        "en": "Phulera Dooj / Ramakrishna Paramahamsa Jayanti / Chandra Darshana",
        "hi": "फुलेरा दूज / रामकृष्ण परमहंस जयंती / चन्द्र दर्शन",
        "bn": "শ্রী শ্রী ফুলেরা দুজ / যুগাবতার শ্রীরামকৃষ্ণ জন্মজয়ন্তী / চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌸", "deity": {"en": "Sri Radha Krishna & Sri Ramakrishna", "hi": "श्रीराधा-कृष्ण व रामकृष्ण परमहंस", "bn": "শ্রীশ্রী রাধাকৃষ্ণ ও যুগাবতার শ্রীরামকৃষ্ণ"},
        "description": {
            "en": "Joyous flower festival (Phulera Dooj) of Radha-Krishna in Braj and the divine advent of Sri Ramakrishna Paramahamsa.",
            "hi": "ब्रज में फूलों की होली (फुलेरा दूज) एवं युगपुरुष श्री रामकृष्ण परमहंस का पावन प्राकट्य दिवस।",
            "bn": "ব্রজমণ্ডলে ফুল দিয়ে হোলি খেলার পুণ্য ফুলেরা দুজ এবং যুগাবতার ভগবান শ্রী শ্রী রামকৃষ্ণ পরমহংসদেবের শুভ আবির্ভাব তিথি।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan & Puja", "hi": "सायंकाल चंद्र दर्शन व पूजा", "bn": "সায়ংকালীন চন্দ্র দর্শন ও আরতি লগ্ন"}
    },
    ("Phalguna", "Shukla", 11): {
        "en": "Amalaki Ekadashi / Rangbhari Ekadashi",
        "hi": "आमलकी एकादशी (रंगभरी एकादशी)",
        "bn": "আমলকী একাদশী ব্রত (রংভরী একাদশী / কাশী উৎসব)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌿", "deity": {"en": "Lord Shiva, Parvati & Sri Hari", "hi": "काशी विश्वनाथ व श्रीहरि", "bn": "কাশী বিশ্বনাথ, পার্বতী ও শ্রীহরি"},
        "description": {
            "en": "Worshipping Amla tree alongside Shiva-Parvati's joyous arrival in Kashi.",
            "hi": "आँवला वृक्ष पूजन एवं काशी में माँ गौरा का प्रथम आगमन रंगोत्सव।",
            "bn": "আমলকী বৃক্ষ পূজা এবং কাশীতে মহাদেব ও মা পার্বতীর প্রথম গুলাল খেলার আনন্দোৎসব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Amla Puja", "hi": "पूर्वाह्न आमलकी पूजा", "bn": "পূর্বাহ্ন আমলকী পূজা লগ্ন"}
    },
    ("Phalguna", "Shukla", 12): {
        "en": "Vaishnava Amalaki Ekadashi",
        "hi": "वैष्णव आमलकी एकादशी",
        "bn": "শ্রী শ্রী বৈষ্ণব আমলকী একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🌿", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Vaishnava observance of Amalaki Ekadashi worshipping the sacred Amla tree and Lord Vishnu.",
            "hi": "वैष्णव संप्रदाय द्वारा आमलकी एकादशी व्रत एवं आँवला वृक्ष सहित श्रीहरि का पावन पूजन।",
            "bn": "বৈষ্ণব পরম্পরায় আমলকী বৃক্ষ পূজা এবং শ্রীহরি নারায়ণের প্রীত্যর্থে পরম পবিত্র একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Amla Puja", "hi": "पूर्वाह्न आमलकी पूजा", "bn": "পূর্বাহ্ন আমলকী পূজা লগ্ন"}
    },
    ("Phalguna", "Shukla", 14): {
        "en": "Holika Dahan / Chhanchar Utsav / Chhoti Holi",
        "hi": "होलिका दहन / कामदहन / छोटी होली",
        "bn": "হোলিকা দহন / চাঁচর উৎসব (অগ্নি উৎসব) / ছোট হোলি",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔥", "deity": {"en": "Bhakt Prahlada & Lord Narasimha", "hi": "भक्त प्रह्लाद व भगवान नृसिंह", "bn": "ভক্ত প্রহ্লাদ ও ভগবান শ্রীনৃসিংহ"},
        "description": {
            "en": "Burning of Holika symbolizing the triumph of devotion (Prahlada) over evil arrogance.",
            "hi": "अहंकार रूपी होलिका का भस्म होना एवं भक्त प्रह्लाद की रक्षा की स्मृति में पावन अग्नि पूजन।",
            "bn": "অহংকারের প্রতীক অসুরিকা হোলিকার দহন এবং অটল হরিভক্তির জয় উদযাপনে চাঁচর বহ্ন্যুৎসব।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Bhadra Free Evening)", "hi": "प्रदोष काल (भद्रा रहित संध्याकाल)", "bn": "প্রদোষ काल (ভদ্রামুক্ত সন্ধ্যাবেলা)"}
    },
    ("Phalguna", "Shukla", 15): {
        "en": "Dol Jatra / Holi / Sri Gaura Purnima / Vasanta Purnima / Anvadhan",
        "hi": "होली / डोल पूर्णिमा / गौर पूर्णिमा / वसंत पूर्णिमा / अन्वाधान",
        "bn": "শ্রী শ্রী দোলযাত্রা / বসন্তোৎসব / শ্রীমন্মহাপ্রভুর শুভ আবির্ভাব / হোলি / অন্বাধান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🎨", "deity": {"en": "Radha Krishna & Sri Chaitanya Mahaprabhu", "hi": "राधा-कृष्ण व श्री चैतन्य महाप्रभु", "bn": "শ্রীশ্রী রাধাকৃষ্ণ ও শ্রীমন্মহাপ্রভু"},
        "description": {
            "en": "Festival of colors, Dolotsav of Radha-Krishna, and divine advent of Sri Chaitanya Mahaprabhu.",
            "hi": "रंगोत्सव होली, श्रीराधा-कृष्ण का डोल उत्सव एवं श्री चैतन्य महाप्रभु का पावन प्राकट्योत्सव।",
            "bn": "রাধাকৃষ্ণের প্রেমময় দোল মহোৎসব, রঙের বসন্তোৎসব এবং শ্রী শ্রী গৌরাঙ্গ মহাপ্রভুর শুভ আবির্ভাব।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Dolotsav & Pradosh Gaura Arati", "hi": "पूर्वाह्न डोल उत्सव व संध्याकाल", "bn": "পূর্বাহ্ন দোলোৎসব ও সায়ংকালীন আবির্ভাব আরতি"}
    },
    # ==========================================================================
    # PDF 2026 ক্যালেন্ডার থেকে চিহ্নিত মিসিং সনাতন উৎসব ও ব্রতসমূহ
    # ==========================================================================

    # --- চৈত্র মাস (Chaitra) ---
    ("Chaitra", "Krishna", 7): {
        "en": "Sheetala Saptami",
        "hi": "शीतला सप्तमी",
        "bn": "শ্রী শ্রী শীতলা সপ্তমী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🌸", "deity": {"en": "Maa Sheetala", "hi": "माँ शीतला", "bn": "মা শীতলা দেবী"},
        "description": {
            "en": "Worship of Maa Sheetala one day prior to Basoda to seek protection from epidemics and heat-borne diseases.",
            "hi": "शीतला अष्टमी से पूर्व आरोग्य ও शीतलता की प्राप्ति हेतु माँ शीतला का पावन पूजन।",
            "bn": "বসন্ত ও সংক্রামক রোগব্যাধি থেকে সুরক্ষার কামনায় মা শীতলা দেবীর বিশেষ সপ্তমী পূজা।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Purvahna Sheetala Puja", "hi": "पूर्वाह्न शीतला पूजा", "bn": "পূর্বাহ্ন শীতলা পূজা লগ্ন"}
    },

    # --- বৈশাখ মাস (Vaishakha) ---
    ("Vaishakha", "Krishna", 15): {
        "en": "Vaishakha Amavasya / Darsha Amavasya / Anvadhan",
        "hi": "वैशाख अमावस्या / दर्श अमावस्या / अन्वाधान",
        "bn": "বৈশাখী অমাবস্যা / দর্শ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "उपवास व तर्पण", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "Pitru Devas & Lord Shiva", "hi": "पितृ देव व भगवान शिव", "bn": "পিতৃপুরুষ ও মহাদেব"},
        "description": {
            "en": "Auspicious Vaishakha new moon for holy river bath, pitru tarpan, and charity.",
            "hi": "पितरों की शांति, पवित्र नदियों में स्नान एवं दान-पुण्य का पावन वैशाख अमावस्या पर्व।",
            "bn": "পিতৃপুরুষের আত্মার তৃপ্তির জন্য গঙ্গা ও পবিত্র তীর্থে মহাস্নান, তর্পণ ও অন্নদান।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan & Snan", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ ও স্নান লগ্ন"}
    },

    # --- আষাঢ় মাস (Ashadha) ---
    ("Ashadha", "Krishna", 12): {
        "en": "Gauna Yogini Ekadashi / Vaishnava Yogini Ekadashi",
        "hi": "गौण योगिनी एकादशी / वैष्णव योगिनी एकादशी",
        "bn": "গৌণ যোগিনী একাদশী / বৈষ্ণব যোগিনী একাদশী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Sri Hari Vishnu", "hi": "भगवान श्री हरि विष्णु", "bn": "ভগবান শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Special Vaishnava community observance of Yogini Ekadashi to eliminate bodily ailments.",
            "hi": "वैष्णव संप्रदाय द्वारा आचरित रोगनाशक एवं पापमुक्ति प्रदाता योगिनी एकादशी व्रत।",
            "bn": "বৈষ্ণব পরম্পরায় সর্বপ্রকার রোগব্যাধি ও পাপ মুক্তির কামনায় যোগিনী একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Ashadha", "Krishna", 15): {
        "en": "Ashadha Amavasya / Darsha Amavasya / Anvadhan",
        "hi": "आषाढ़ अमावस्या / दर्श अमावस्या / अन्वाधान",
        "bn": "আষাঢ়ী অমাবস্যা / দর্শ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "उपवास व तर्पण", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "Pitru Devas & Lord Shiva", "hi": "पितृ देव व भगवान शिव", "bn": "পিতৃপুরুষ ও মহাদেব"},
        "description": {
            "en": "New moon of Ashadha dedicated to ancestor oblations and sacred charity before Chaturmasya.",
            "hi": "चातुर्मास से पूर्व पितरों के निमित्त तर्पण, पिंडदान एवं दीपदान का पावन दिवस।",
            "bn": "চাতুর্মাস্য শুরুর প্রাক্কালে পিতৃপুরুষের তৃপ্তির জন্য পবিত্র তর্পণ ও জলদান।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan Kaal", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ লগ্ন"}
    },

    # --- আশ্বিন মাস (Ashvina) ---
    ("Ashvina", "Krishna", 1): {
        "en": "Pitru Paksha Begins / Mahalaya Paksha Ishti",
        "hi": "पितृपक्ष प्रारंभ / महालय पक्ष इष्टि",
        "bn": "১৬ দিনের মহালয়া পিতৃপক্ষ আরম্ভ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "तर्पण पर्व", "bn": "তর্পণ ও পিতৃশ্রাদ্ধ"},
        "icon": "🙏", "deity": {"en": "Pitru Devas & Lord Yama", "hi": "पितृ गण व यमराज", "bn": "পিতৃপুরুষগণ ও যমরাজ"},
        "description": {
            "en": "Sacred beginning of the 16-day fortnight for ancestor shraddha, tarpan, and remembrance.",
            "hi": "पूर्वजों के प्रति कृतज्ञता समर्पण एवं १६ दिवसीय महालय श्राद्ध पक्ष का पावन शुभारंभ।",
            "bn": "পরলোকগত পিতৃপুরুষের উদ্দেশ্যে জলদান, তর্পণ ও পার্বণ শ্রাদ্ধের ১৬ দিনব্যাপী পুণ্য পক্ষ আরম্ভ।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Kutapa & Aparahna Tarpan", "hi": "कुतप व अपराह्न तर्पण", "bn": "কুতপ ও অপরাহ্ন তর্পণ সময়"}
    },
    ("Ashvina", "Shukla", 10): {
        "en": "Vijaya Dashami / Dussehra / Madhvacharya Jayanti",
        "hi": "विजयादशमी / दशहरा / मध्वाचार्य जयंती",
        "bn": "শ্রী শ্রী বিজয়া দশমী / দশহরা / শ্রী মধ্বাচার্য জয়ন্তী",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🔱", "deity": {"en": "Maa Durga, Lord Rama & Sri Madhvacharya", "hi": "माँ दुर्गा, श्रीराम व मध्वाचार्य", "bn": "মা দুর্গা, শ্রীরাম ও শ্রী মধ্বাচার্য"},
        "description": {
            "en": "Triumph of good over evil, Durga Visarjan, and appearance day of Dvaita philosopher Sri Madhvacharya.",
            "hi": "बुराई पर अच्छाई की विजय, रावण दहन एवं द्वैत वेदांत के प्रवर्तक मध्वाचार्य का पावन जन्मोत्सव।",
            "bn": "অসুরের বিনাশে শুভর জয়, অপরাজিতা পূজা এবং দ্বৈত বেদান্তের প্রবক্তা শ্রীমধ্বাচার্যের আবির্ভাব তিথি।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparajita & Vijaya Muhurta", "hi": "अपराजिता व विजय मुहूर्त", "bn": "অপরাজিতা পূজা ও বিজয় মুহূর্ত"}
    },

    # --- কার্তিক মাস (Kartika) ---
    ("Kartika", "Shukla", 11): {
        "en": "Devutthana Ekadashi / Tulsi Vivah / Kansa Vadh / Bhishma Panchak Begins",
        "hi": "देवउठनी एकादशी / तुलसी विवाह / कंस वध / भीष्म पंचक प्रारंभ",
        "bn": "দেবউত্থান একাদশী / তুলসী বিবাহ / কংস বধ মহোৎসব / ভীষ্ম পঞ্চক ব্রতারম্ভ",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "icon": "🌿", "deity": {"en": "Lord Shaligram, Tulsi & Sri Krishna", "hi": "भगवान शालिग्राम, तुलसी व श्रीकृष्ण", "bn": "ভগবান শালগ্রাম, তুলসী ও শ্রীকৃষ্ণ"},
        "description": {
            "en": "Lord Vishnu awakens from cosmic slumber, inception of 5-day Bhishma Panchak and celebrating Kansa Vadh in Mathura.",
            "hi": "चातुर्मास समाप्ति, भीष्म पंचक महाव्रत प्रारंभ, शालिग्राम-तुलसी विवाह एवं मथुरा में कंस वध लीला।",
            "bn": "শ্রীহরির যোগনিদ্রা ভঙ্গ, ভীষ্ম পঞ্চক ব্রতারম্ভ এবং মথুরায় শ্রীকৃষ্ণ কর্তৃক কংস বধ মহোৎসব।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal (Tulsi Vivah)", "hi": "प्रदोष काल (तुलसी विवाह)", "bn": "প্রদোষ কাল (তুলসী বিবাহ সময়)"}
    },
    ("Kartika", "Shukla", 13): {
        "en": "Vishweshwara Vrat / Vaikuntha Trayodashi / Pradosh Vrat",
        "hi": "विश्वेश्वर व्रत / वैकुंठ त्रयोदशी / प्रदोष व्रत",
        "bn": "শ্রী শ্রী বিশ্বেশ্বর ব্রত / বৈকুণ্ঠ ত্রয়োদশী / প্রদোষ ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "উপবাস ব্রত", "bn": "উপবাস ব্রত"},
        "icon": "🔱", "deity": {"en": "Lord Vishweshwara (Shiva) & Vishnu", "hi": "काशी विश्वनाथ व भगवान विष्णु", "bn": "কাশী বিশ্বনাথ ও ভগবান শ্রীহরি"},
        "description": {
            "en": "Sacred fasting in Varanasi dedicated to Kashi Vishwanath and Lord Vishnu before Dev Deepawali.",
            "hi": "काशी में देव दीपावली से पूर्व भगवान विश्वेश्वर एवं श्रीहरि के मिलन का पावन व्रत।",
            "bn": "কাশী বিশ্বনাথ ও শ্রীহরির প্রীত্যর্থে পরম পবিত্র বিশ্বেশ্বর ব্রত ও প্রদোষ শিবপূজা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Kaal Puja", "hi": "प्रदोष काल", "bn": "প্রদোষ কাল পূজা লগ্ন"}
    },
    ("Kartika", "Shukla", 14): {
        "en": "Vaikuntha Chaturdashi / Manikarnika Snan",
        "hi": "वैकुंठ चतुर्दशी / मणिकर्णिका महास्नान",
        "bn": "শ্রী বৈকুণ্ঠ চতুর্দশী / কাশীতে মণিকর্ণিকা ঘাট মহাস্নান",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🕉️", "deity": {"en": "Lord Shiva & Lord Vishnu", "hi": "भगवान शिव व भगवान विष्णु", "bn": "দেবাদিদেব শিব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Hari-Hara union and taking sacred bath in Manikarnika Kund in Varanasi at midnight.",
            "hi": "भगवान शिव व विष्णु का पावन मिलन एवं काशी मणिकर्णिका तीर्थ में मध्यरात्रि मुक्ति स्नान।",
            "bn": "ভগবান শিব ও শ্রীহরির মিলন তিথি এবং কাশীর পবিত্র মণিকর্ণিকা তীর্থে নিশীথ কাল মহাস্নান।"
        },
        "muhurta_type": "nishita",
        "muhurta_label": {"en": "Nishita Kaal Muhurta (Midnight)", "hi": "निशीथ काल मुहूर्त (मध्यरात्रि)", "bn": "নিশীথ কাল মুহূর্ত (মধ্যরাত্রি)"}
    },
    ("Kartika", "Shukla", 15): {
        "en": "Dev Diwali / Guru Nanak Jayanti (Prakash Utsav) / Kartika Purnima / Rash Yatra",
        "hi": "देव दीपावली / गुरु नानक जयंती (प्रकाश पर्व) / कार्तिक पूर्णिमा / रास पूर्णिमा",
        "bn": "দেব দীপাবলি / শ্রী গুরু নানক জন্মজয়ন্তী (প্রকাশ পর্ব) / কার্তিক পূর্ণিমা / শ্রী শ্রী রাসযাত্রা",
        "category": "hindu", "type": {"en": "Major Festival", "hi": "মহাপর্ব", "bn": "মহাপর্ব"},
        "icon": "🪔", "deity": {"en": "Lord Shiva, Guru Nanak Dev Ji & Radha Krishna", "hi": "भगवान शिव, गुरु नानक देव जी व राधा-कृष्ण", "bn": "দেবাদিদেব শিব, শ্রী গুরু নানক দেব ও রাধাকৃষ্ণ"},
        "description": {
            "en": "Varanasi Dev Deepawali with millions of earthen lamps, Guru Nanak Dev Ji's birth anniversary, and Vrindavan Raas Purnima.",
            "hi": "काशी में दीपदान का महापर्व देव दीपावली, सिख धर्म के संस्थापक गुरु नानक देव जी का प्रकाश पर्व एवं महारास।",
            "bn": "কাশীতে লক্ষ প্রদীপ প্রজ্বলনে দেব দীপাবলি, শিখ গুরু নানক দেবজীর শুভ জন্মজয়ন্তী ও রাসপূর্ণিমা।"
        },
        "muhurta_type": "pradosh",
        "muhurta_label": {"en": "Pradosh Deepdan & Full Moon Night", "hi": "प्रदोष काल दीपदान", "bn": "প্রদোষ কাল ও দেব দীপাবলি লগ্ন"}
    },

    # --- মার্গশীর্ষ মাস (Margashirsha) ---
    ("Margashirsha", "Krishna", 1): {
        "en": "Margashirsha Krishna Pratipada / Ishti Havan",
        "hi": "मार्गशीर्ष कृष्ण प्रतिपदा / इष्टि",
        "bn": "মার্গশীর্ষ কৃষ্ণ প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Inception of Margashirsha Krishna Paksha observing sacred Ishti fire rituals.",
            "hi": "मार्गशीर्ष कृष्ण पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "অগ্রহায়ণ কৃষ্ণপক্ষের শুভ সূচনা এবং শান্তি ও সমৃদ্ধি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Margashirsha", "Krishna", 15): {
        "en": "Margashirsha Amavasya / Darsha Amavasya / Anvadhan",
        "hi": "मार्गशीर्ष अमावस्या / दर्श अमावस्या / अन्वाधान",
        "bn": "মার্গশীর্ষ অমাবস্যা / দর্শ অমাবস্যা ও অন্বাধান",
        "category": "hindu", "type": {"en": "Vrata & Tarpan", "hi": "उपवास व तर्पण", "bn": "উপবাস ও তর্পণ"},
        "icon": "🌑", "deity": {"en": "Pitru Devas & Lord Shiva", "hi": "पितृ देव व भगवान शिव", "bn": "পিতৃপুরুষ ও মহাদেব"},
        "description": {
            "en": "Sacred new moon of Margashirsha for ancestral peace, holy snan, and charity.",
            "hi": "पितरों की तृप्ति, पवित्र तीर्थ स्नान एवं पुण्य फल हेतु मार्गशीर्ष अमावस्या व्रत।",
            "bn": "পিতৃপুরুষের আত্মার তৃপ্তির জন্য পবিত্র স্নান, তর্পণ ও দানকার্যের অগ্রহায়ণ অমাবস্যা।"
        },
        "muhurta_type": "aparahna",
        "muhurta_label": {"en": "Aparahna Tarpan Kaal", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ লগ্ন"}
    },
    ("Margashirsha", "Shukla", 1): {
        "en": "Margashirsha Shukla Pratipada / Ishti Havan",
        "hi": "मार्गशीर्ष शुक्ल प्रतिपदा / इष्टि",
        "bn": "মার্গশীর্ষ শুক্ল প্রতিপদ / বৈদিক ইষ্টি যজ্ঞ",
        "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"},
        "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"},
        "description": {
            "en": "Commencement of Margashirsha Shukla Paksha observing auspicious Ishti.",
            "hi": "मार्गशीर्ष शुक्ल पक्ष का प्रारंभ एवं सुख-शांति हेतु वैदिक इष्टि यज्ञानुष्ठान।",
            "bn": "অগ্রহায়ণ শুক্লপক্ষের শুভ সূচনা এবং শান্তি কামনায় বৈদিক ইষ্টি হোম।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Ishti Havan", "hi": "प्रातः इष्टि मुहूर्त", "bn": "প্রাতঃকালীন ইষ্টি যজ্ঞ মুহূর্ত"}
    },
    ("Margashirsha", "Shukla", 2): {
        "en": "Chandra Darshana (Margashirsha Shukla)",
        "hi": "मार्गशीर्ष चन्द्र दर्शन",
        "bn": "মার্গশীর্ষ শুক্ল দ্বিতীয়া চন্দ্র দর্শন",
        "category": "hindu", "type": {"en": "Observance", "hi": "धार्मिक दर्शन", "bn": "চন্দ্র দর্শন"},
        "icon": "🌙", "deity": {"en": "Chandra Deva", "hi": "चन्द्र देव", "bn": "চন্দ্র দেব"},
        "description": {
            "en": "Auspicious sighting of the crescent moon after sunset for peace and mental clarity.",
            "hi": "मानसिक शांति व सौभाग्य वृद्धि हेतु सायंकाल नवचंद्र दर्शन व अर्घ्य।",
            "bn": "মানসিক শান্তি ও সৌভাগ্য বৃদ্ধির কামনায় সায়ংকালে নবচন্দ্রের শুভ দর্শন।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Sayankal Chandra Darshan", "hi": "सायंकाल चंद्र दर्शन", "bn": "সায়ংকালীন চন্দ্র দর্শন লগ্ন"}
    },

    # --- পৌষ মাস (Pausha) ---
    ("Pausha", "Krishna", 4): {
        "en": "Akhuratha Sankashti Chaturthi",
        "hi": "अखुरथ संकष्टी चतुर्थी",
        "bn": "শ্রী আখুরথ সংকষ্টী চতুর্থী ব্রত",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Akhuratha Ganesha & Chandra", "hi": "भगवान अखुरथ गणेश व चन्द्र देव", "bn": "ভগবান আখুরথ শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Pausha Krishna Chaturthi fast dedicated to Lord Akhuratha Ganesha, concluded with moonrise arghya.",
            "hi": "समस्त विघ्नों व संकटों के निवारण हेतु पौष मास की अखुरथ संकष्टी चतुर्थी का पावन व्रत।",
            "bn": "সর্বসঙ্কট দূরীকরণে পৌষ কৃষ্ণ চতুর্থীতে শ্রী আখুরথ গণেশের উপবাস ব্রত এবং চন্দ্রোদয়ে ভক্তিপূর্ণ অর্ঘ্যদান।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },

    # --- অতিরিক্ত মাস / অধিক মাস (Adhika Masa Festivals 2026) ---
    ("Adhika_Jyeshtha", "Shukla", 11): {
        "en": "Padmini Ekadashi (Kamala Ekadashi)",
        "hi": "पद्मिनी एकादशी (कमला एकादशी / अधिक मास एकादशी)",
        "bn": "পদ্মিনী একাদশী ব্রত (কমলা একাদশী / অধিক মাস)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "महाव्रत", "bn": "উপবাস ব্রত"},
        "icon": "🪷", "deity": {"en": "Lord Purushottama (Vishnu)", "hi": "भगवान पुरुषोत्तम विष्णु", "bn": "ভগবান পুরুষোত্তম শ্রীহরি"},
        "description": {
            "en": "Rare Ekadashi falling in Adhika Masa (Purushottam Masa), granting Vaikuntha attainment and boundless merits.",
            "hi": "अधिक मास (मलमास) के शुक्ल पक्ष की परम दुर्लभ पद्मिनी एकादशी, जो समस्त तीर्थों का पुण्य प्रदान करती है।",
            "bn": "পুরুষোত্তম অধিক মাসের শুক্লপক্ষের পরম পুণ্যময়ী পদ্মিনী একাদশী ব্রত।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
    },
    ("Adhika_Jyeshtha", "Krishna", 4): {
        "en": "Vibhuvana Sankashti Chaturthi (Adhika Masa)",
        "hi": "विभुवन संकष्टी चतुर्थी (अधिक मास)",
        "bn": "শ্রী বিভুবন সংকষ্টী চতুর্থী ব্রত (অধিক মাস)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"},
        "icon": "🐘", "deity": {"en": "Lord Ganesha & Chandra", "hi": "भगवान गणेश व चन्द्र देव", "bn": "ভগবান শ্রী গণেশ ও চন্দ্র দেব"},
        "description": {
            "en": "Rare Sankashti Chaturthi observed during Adhika Masa for removal of deep-rooted sorrows.",
            "hi": "अधिक मास में समस्त मनोकामनाओं की पूर्ति हेतु विभुवन संकष्टी चतुर्थी का पावन व्रत।",
            "bn": "অধিক মাসে সর্বকষ্ট ও বাধা নাশে বিভুবন সংকষ্টী চতুর্থীর বিশেষ উপবাস ও চন্দ্রোদয়ে পূজা।"
        },
        "muhurta_type": "sayankal",
        "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व पूजन", "bn": "চন্দ্রোদয় ও পূজা লগ্ন"}
    },
    ("Adhika_Jyeshtha", "Krishna", 11): {
        "en": "Parama Ekadashi (Adhika Krishna Ekadashi)",
        "hi": "परमा एकादशी (अधिक मास कृष्ण एकादशी)",
        "bn": "পরমা একাদশী ব্রত (অধিক মাস কৃষ্ণ একাদশী)",
        "category": "hindu", "type": {"en": "Vrata", "hi": "महाव्रत", "bn": "উপবাস ব্রত"},
        "icon": "🕉️", "deity": {"en": "Lord Purushottama (Vishnu)", "hi": "भगवान पुरुषोत्तम विष्णु", "bn": "ভগবান পুরুষোত্তম শ্রীহরি"},
        "description": {
            "en": "Observed in the dark fortnight of Adhika Masa to eradicate poverty and grant immense spiritual merit.",
            "hi": "दरिद्रता का समूल नाश करने एवं अक्षय पुण्य प्रदान करने वाली अधिक मास की परमा एकादशी।",
            "bn": "দারিদ্র্য দূরীকরণ ও মোক্ষলাভের কামনায় অধিক মাসের কৃষ্ণপক্ষের পরম পবিত্র পরমা একাদশী।"
        },
        "muhurta_type": "purvahna",
        "muhurta_label": {"en": "Morning Fast & Puja", "hi": "प्रातः पूजा", "bn": "প্রাতঃকালীন পূজা"}
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
    (3, 23): {
        "en": "Shaheed Diwas (Bhagat Singh, Sukhdev & Rajguru Martyrdom Day)",
        "hi": "शहीद दिवस (भगत सिंह, सुखदेव व राजगुरु बलिदान दिवस)",
        "bn": "শহীদ দিবস (বীর ভগৎ সিং, সুখদেব ও রাজগুরুর আত্মোৎসর্গ দিবস)",
        "category": "national", "icon": "🇮🇳", "type": {"en": "Martyrdom Day", "hi": "बलिदान दिवस", "bn": "জাতীয় শ্রদ্ধা দিবস"},
        "deity": {"en": "Bhagat Singh, Sukhdev & Rajguru", "hi": "अमर शहीद भगत सिंह, सुखदेव व राजगुरु", "bn": "অমর বিপ্লবী ভগৎ সিং, সুখদেব ও রাজগুরু"},
        "description": {
            "en": "Tribute to the supreme sacrifice of Shaheed Bhagat Singh, Sukhdev, and Rajguru for Indian Independence.",
            "hi": "भारत माता की स्वाधीनता हेतु हँसते-हँसते फाँसी के फंदे चूमने वाले अमर क्रांतिकारियों को नमन।",
            "bn": "ভারতের স্বাধীনতা সংগ্রামে আত্মাহুতি দানকারী অমর বিপ্লবী ভগৎ সিং, সুখদেব ও রাজগুরুর অমর স্মৃতির প্রতি শ্রদ্ধাঞ্জলি।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (4, 14): {
        "en": "Dr. B.R. Ambedkar Jayanti (Equality Day)", "hi": "डॉ. बी.आर. आंबेडकर जयंती (समानता दिवस)", "bn": "ডঃ বি. আর. আম্বেদকর জয়ন্তী (সাম্য দিবস)",
        "category": "national", "icon": "📜", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Babasaheb Dr. B.R. Ambedkar", "hi": "बाबासाहेब डॉ. भीमराव आंबेडकर", "bn": "বাবাসাহেব ডঃ বি. আর. আম্বেদকর"},
        "description": {"en": "Birth anniversary of the chief architect of the Indian Constitution and crusader of social equality.", "hi": "संविधान निर्माता एवं वंचितों के उत्थान के मसीहा भारत रत्न बाबासाहेब आंबेडकर की जयंती।", "bn": "ভারতীয় সংবিধানের প্রধান স্থপতি ও সমাজ সংস্কারক ভারতরত্ন বাবাসাহেব আম্বেদকরের জন্মজয়ন্তী।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (5, 7): {
        "en": "Rabindra Jayanti (Pachishe Boishakh)",
        "hi": "रवीन्द्रनाथ टैगोर जयंती",
        "bn": "রবীন্দ্র জয়ন্তী (পঁচিশে বৈশাখ)",
        "category": "national", "icon": "📜", "type": {"en": "Observance", "hi": "सांस्कृतिक पर्व", "bn": "সাংস্কৃতিক উৎসব"},
        "deity": {"en": "Kabiguru Rabindranath Tagore", "hi": "कविगुरु रवीन्द्रनाथ ठाकुर", "bn": "বিশ্বকবি রবীন্দ্রনাথ ঠাকুর"},
        "description": {
            "en": "Birth anniversary of Asia's first Nobel laureate, polymath, and poet Rabindranath Tagore.",
            "hi": "नोबेल पुरस्कार विजेता, राष्ट्रगान के रचयिता विश्वकवि रवीन्द्रनाथ टैगोर का पावन जन्मोत्सव।",
            "bn": "এশিয়া মহাদেশের প্রথম নোবেলজয়ী বিশ্বকবি রবীন্দ্রনাথ ঠাকুরের শুভ জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (8, 15): {
        "en": "Independence Day of India", "hi": "स्वतंत्रता दिवस", "bn": "ভারতের স্বাধীনতা দিবস",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Holiday", "hi": "राष्ट्रीय महापर्व", "bn": "জাতীয় মহোৎসব"},
        "deity": {"en": "Bharat Mata & All Freedom Fighters", "hi": "भारत माता व समस्त अमर बलिदानी", "bn": "ভারত মাতা ও সমস্ত স্বাধীনতা সংগ্রামী"},
        "description": {"en": "Celebration of India achieving freedom from British colonial rule on August 15, 1947.", "hi": "१५ अगस्त १९४७ को प्राप्त भारत की स्वाधीनता का पावन राष्ट्रीय स्वतंत्रता उत्सव।", "bn": "১৯৪৭ সালের ১৫ই আগস্ট পরাধীনতার শৃঙ্খল ভেঙে স্বাধীনতা অর্জনের মহান ও গৌরবময় দিন।"},
        "muhurta": {"en": "Morning Flag Hoisting (07:30 - 10:00 AM)", "hi": "प्रातः ध्वजारोहण (०७:३० - १०:००)", "bn": "প্রাতঃকালে জাতীয় পতাকা উত্তোলন (সকাল ০৭:৩০ - ১০:০০)"}
    },
    (9, 5): {
        "en": "Teachers' Day (Dr. Radhakrishnan Jayanti)",
        "hi": "शिक्षक दिवस (डॉ. सर्वपल्ली राधाकृष्णन जयंती)",
        "bn": "জাতীয় শিক্ষক দিবস (ডঃ সর্বপল্লী রাধাকৃষ্ণণ জন্মজয়ন্তী)",
        "category": "national", "icon": "📚", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Dr. Sarvepalli Radhakrishnan", "hi": "डॉ. सर्वपल्ली राधाकृष्णन", "bn": "ডঃ সর্বপল্লী রাধাকৃষ্ণণ"},
        "description": {
            "en": "Honouring teachers and celebrating the birth of philosopher-statesman Dr. S. Radhakrishnan.",
            "hi": "शिक्षकों के प्रति कृतज्ञता समर्पण एवं पूर्व राष्ट्रपति डॉ. राधाकृष्णन की पावन जयंती।",
            "bn": "মানুষ গড়ার কারিগর শিক্ষক মহাশয়দের প্রতি শ্রদ্ধা নিবেদন ও প্রাক্তন রাষ্ট্রপতির জন্মতিথি।"
        },
        "muhurta": {"en": "All Day School Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন শিক্ষাপ্রতিষ্ঠানভিত্তিক উদযাপন"}
    },
    (9, 14): {
        "en": "Hindi Diwas (National Hindi Day)",
        "hi": "हिन्दी दिवस",
        "bn": "জাতীয় হিন্দি দিবস",
        "category": "national", "icon": "🇮🇳", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Official Language of India", "hi": "राजभाषा हिन्दी", "bn": "ভারত সরকারি ভাষা"},
        "description": {
            "en": "Commemorating the adoption of Hindi as the official language of the Republic of India in 1949.",
            "hi": "१४ सितंबर १९४९ को हिन्दी को भारत की राजभाषा का दर्जा मिलने पर गौरवशाली हिन्दी दिवस।",
            "bn": "১৯৪৯ সালের ১৪ই সেপ্টেম্বর ভারতীয় গণপরিষদ কর্তৃক হিন্দিকে সরকারি ভাষার স্বীকৃতিদানের স্মারক দিবস।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    # ১৫ সেপ্টেম্বর: ইঞ্জিনিয়ার্স ডে / ডঃ বিশ্বেশ্বরায়া জয়ন্তী (PDF September 15)
    (9, 15): {
        "en": "Engineer's Day (Sir M. Visvesvaraya Jayanti)",
        "hi": "अभियंता दिवस (इंजीनियर्स डे / डॉ. मोक्षगुंडम विश्वेश्वरैया जयंती)",
        "bn": "জাতীয় প্রকৌশলী দিবস (ইঞ্জিনিয়ার্স ডে / স্যার এম. বিশ্বেশ্বরায়া জন্মজয়ন্তী)",
        "category": "national", "icon": "⚙️", "type": {"en": "National Observance", "hi": "राष्ट्रीय दिवस", "bn": "জাতীয় দিবস"},
        "deity": {"en": "Sir M. Visvesvaraya", "hi": "सर मोक्षगुंडम विश्वेश्वरैया", "bn": "ভারতরত্ন স্যার এম. বিশ্বেশ্বরায়া"},
        "description": {
            "en": "Birth anniversary of Bharat Ratna Sir M. Visvesvaraya, honouring the engineering innovations of India.",
            "hi": "महान भारत रत्न अभियंता सर एम. विश्वेश्वरैया के योगदान के सम्मान में राष्ट्रीय इंजीनियर्स डे।",
            "bn": "ভারতের আধুনিক প্রযুক্তির রূপকার ভারতরত্ন স্যার মোক্ষগুন্ডম বিশ্বেশ্বরায়ার শুভ জন্মজয়ন্তী।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
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
        "description": {"en": "Birth anniversary of India's first Prime Minister, dedicated to child welfare and development.", "hi": "बच्चों के प्यारे 'चाचा नेहरू' के जन्मोत्सव पर बाल कल्याण व शिक्षा संवर्धन दिवस।", "bn": "স্বাধীন ভারতের প্রথম প্রধানমন্ত্রী পণ্ডিত নেহরুর শিশুদের প্রতি স্নেহের স্মরণে শিশু কল্যাণ দিবস।"},
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
    (1, 13): {
        "en": "Lohri Festival",
        "hi": "लोहड़ी पर्व",
        "bn": "লোহড়ী মহোৎসব (বহ্নি উৎসব)",
        "category": "hindu", "icon": "🔥", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"},
        "deity": {"en": "Agni Deva & Surya Deva", "hi": "अग्नि देव व सूर्य देव", "bn": "অগ্নি দেব ও সূর্য দেব"},
        "description": {
            "en": "Harvest bonfire festival marking the culmination of winter and welcoming longer days.",
            "hi": "अग्नि पूजन, तिल-गुड़ भोग एवं रबी फसल के आगमन का उल्लासमय पर्व।",
            "bn": "নতুন ফসল আহরণ ও শীতের অবসানে পবিত্র অগ্নি প্রজ্বলন ও তিল-গুড় নিবেদনের উৎসব।"
        },
        "muhurta": {"en": "Evening Bonfire (06:00 - 08:30 PM)", "hi": "सायंकाल अग्नि पूजन (०६:०० - ०८:३०)", "bn": "সায়ংকালে বহ্নি প্রজ্বলন (সন্ধ্যা ০৬:০০ - ০৮:৩০)"}
    },
    (2, 4): {
        "en": "World Cancer Day",
        "hi": "विश्व कैंसर दिवस",
        "bn": "বিশ্ব ক্যান্সার দিবস",
        "category": "world", "icon": "🎗️", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {
            "en": "Global awareness initiative encouraging cancer prevention, early detection, and treatment.",
            "hi": "कैंसर के प्रति वैश्विक जागरूकता, रोकथाम एवं उपचार को बढ़ावा देने का दिवस।",
            "bn": "ক্যান্সার প্রতিরোধ, সচেতনতা বৃদ্ধি এবং রোগীদের প্রতি সংহতি প্রকাশের আন্তর্জাতিক দিবস।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (2, 14): {
        "en": "Valentine's Day",
        "hi": "वैलेंटाइन डे (प्रेम दिवस)",
        "bn": "ভ্যালেন্টাইনস ডে (বিশ্ব ভালোবাসা দিবস)",
        "category": "world", "icon": "💖", "type": {"en": "Global Celebration", "hi": "अंतर्राष्ट्रीय पर्व", "bn": "আন্তর্জাতিক উৎসব"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {
            "en": "Celebration of affection, love, and goodwill among partners and companions worldwide.",
            "hi": "स्नेह, प्रेम व आत्मीयता की अभिव्यक्ति का वैश्विक उत्सव दिवस।",
            "bn": "ভালোবাসা, সম্প্রীতি ও পারস্পরিক শ্রদ্ধাবোধ প্রকাশের সার্বজনীন উৎসব।"
        },
        "muhurta": {"en": "All Day Celebration", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (3, 8): {
        "en": "International Women's Day", "hi": "अंतर्राष्ट्रीय महिला दिवस", "bn": "আন্তর্জাতিক নারী দিবস",
        "category": "world", "icon": "🌍", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {"en": "Honouring women's social, economic, cultural, and political achievements worldwide.", "hi": "नारी शक्ति के अधिकारों, समानता व उपलब्धियों के सम्मान का पावन दिवस।", "bn": "নারীর অধিকার, মর্যাদা ও সমাজে তাদের গৌরবময় অবদানের স্বীকৃতি উদযাপনের দিন।"},
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },
    (3, 21): {
        "en": "Vernal Equinox (Spring Equinox)",
        "hi": "वसंत विषुव (दिन-रात बराबर)",
        "bn": "মহাবিষুব (বসন্ত বিষুব / দিন ও রাত্রি সমান)",
        "category": "world", "icon": "☀️", "type": {"en": "Astronomical Event", "hi": "खगोलीय घटना", "bn": "জ্যোতির্বৈজ্ঞানিক ঘটনা"},
        "deity": {"en": "Surya Deva & Mother Nature", "hi": "भगवान सूर्य व प्रकृति", "bn": "ভগবান সূর্য দেব ও প্রকৃতি"},
        "description": {
            "en": "Astronomical day where the plane of Earth's equator passes through the geometric center of the Sun's disk.",
            "hi": "खगोलीय दिवस जब सूर्य विषुवत रेखा पर सीधा चमकता है और दिन-रात की अवधि पूर्णतः बराबर होती है।",
            "bn": "যে জ্যোতির্বৈজ্ঞানিক দিনে সূর্য বিষুবরেখায় অবস্থান করে এবং পৃথিবীর সর্বত্র দিন ও রাত্রির দৈর্ঘ্য সমান হয়।"
        },
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
    (5, 31): {
        "en": "World No Tobacco Day",
        "hi": "विश्व तंबाकू निषेध दिवस",
        "bn": "বিশ্ব তামাকমুক্ত দিবস",
        "category": "world", "icon": "🚭", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "World Health Organization", "hi": "विश्व स्वास्थ्य संगठन", "bn": "বিশ্ব স্বাস্থ্য সংস্থা"},
        "description": {
            "en": "Global awareness campaign highlighting health risks associated with tobacco consumption.",
            "hi": "तंबाकू व धूम्रपान के दुष्प्रभावों के प्रति जन-जागरूकता एवं स्वास्थ्य रक्षा का वैश्विक दिवस।",
            "bn": "তামাক সেবনের মারাত্মক স্বাস্থ্যঝুঁকি সম্পর্কে জনসচেতনতা সৃষ্টির লক্ষ্যে আন্তর্জাতিক দিবস।"
        },
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
        "en": "International Yoga Day / Longest Day of Year", "hi": "अंतर्राष्ट्रीय योग दिवस", "bn": "আন্তর্জাতিক যোগ দিবস / দীর্ঘতম দিন",
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
    (12, 1): {
        "en": "World AIDS Day",
        "hi": "विश्व एड्स दिवस",
        "bn": "বিশ্ব এইডস দিবস",
        "category": "world", "icon": "🎗️", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"},
        "deity": {"en": "Universal", "hi": "सर्वव्यापी", "bn": "সার্বজনীন"},
        "description": {
            "en": "Global health awareness campaign showing solidarity with people affected by HIV.",
            "hi": "एचआईवी संक्रमण के प्रति वैश्विक जागरूकता एवं स्वास्थ्य सुरक्षा का अंतर्राष्ट्रीय दिवस।",
            "bn": "এইচআইভি সংক্রমণ রোধে সচেতনতা বৃদ্ধি ও আক্রান্তদের প্রতি সংহতি প্রকাশের আন্তর্জাতিক দিবস।"
        },
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
    },
    # ২৩ সেপ্টেম্বর: শারদ বিষুব (Autumnal Equinox - PDF September 23)
    (9, 23): {
        "en": "Autumnal Equinox (Autumn Equinox)",
        "hi": "शरद विषुव (दिन-रात बराबर)",
        "bn": "শারদ বিষুব (জলবিষুব / দিন ও রাত্রি সমান)",
        "category": "world", "icon": "☀️", "type": {"en": "Astronomical Event", "hi": "खगोलीय घटना", "bn": "জ্যোতির্বৈজ্ঞানিক ঘটনা"},
        "deity": {"en": "Surya Deva & Mother Nature", "hi": "भगवान सूर्य व प्रकृति", "bn": "ভগবান সূর্য দেব ও প্রকৃতি মাতা"},
        "description": {
            "en": "Astronomical day where the Sun crosses the celestial equator going southward, making day and night equal.",
            "hi": "खगोलीय दिवस जब सूर्य विषुवत रेखा पर सीधा चमकता है और दिन-रात की अवधि बराबर होती है।",
            "bn": "যে জ্যোতির্বৈজ্ঞানিক দিনে সূর্য বিষুবরেখায় অবস্থান করায় দিন ও রাত্রির দৈর্ঘ্য সমান হয়।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    },

    # ২২ ডিসেম্বর: বছরের ক্ষুদ্রতম দিন / উত্তরায়ণ প্রাক্কাল (Winter Solstice - PDF December 22)
    (12, 22): {
        "en": "Shortest Day of Year (Winter Solstice)",
        "hi": "वर्ष का सबसे छोटा दिन (शीतकालीन अयनांत)",
        "bn": "বছরের ক্ষুদ্রতম দিন (শীতকালীন অয়নান্ত / দীর্ঘতম রাত)",
        "category": "world", "icon": "❄️", "type": {"en": "Astronomical Event", "hi": "खगोलीय घटना", "bn": "জ্যোতির্বৈজ্ঞানিক ঘটনা"},
        "deity": {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"},
        "description": {
            "en": "Winter Solstice in Northern Hemisphere marking the shortest daylight period of the year.",
            "hi": "उत्तरी गोलार्ध में वर्ष का सबसे छोटा दिन एवं सबसे लंबी रात्रि का खगोलीय दिवस।",
            "bn": "উত্তর গোলার্ধে বছরের সবচেয়ে ছোট দিন এবং সবচেয়ে দীর্ঘতম রাতের জ্যোতির্বৈজ্ঞানিক দিন।"
        },
        "muhurta": {"en": "All Day Observance", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}
    }
}

# ==============================================================================
# ৪. পরিবর্তনশীল মুসলিম, খ্রিস্টান ও বিশেষ আঞ্চলিক পূজা
# ==============================================================================
VARIABLE_RELIGIOUS_DAYS = {
    # --- 2026 ---
    (2026, 8, 27): {
        "en": "Thiruvonam / Onam Festival (Kerala)", "hi": "ओणम / थिरुवोणम (महाबली आगमन)", "bn": "ওনাম উৎসব / তিরুভোনাম (মহারাজ বলি আগমন)",
        "category": "hindu", "icon": "🌸", "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"},
        "deity": {"en": "Lord Vamana & King Mahabali", "hi": "भगवान वामन व राजा बलि", "bn": "ভগবান বামন ও রাজা বলি"},
        "description": {"en": "Grand harvest festival of Kerala welcoming the annual return of King Mahabali.", "hi": "केरल का पावन फसल उत्सव एवं दानवीर राजा बलि के स्वागत का महापर्व।", "bn": "কেরালার ঐতিহ্যবাহী ফসল কাটার মহোৎসব ও প্রজাবৎসল রাজা বলির ধরাধামে আগমন।"},
        "muhurta": {"en": "Purvahna Thiruvonam Puja", "hi": "पूर्वाह्न ओणम पूजा", "bn": "পূর্বাহ্ন ওনাম পূজা ও পুকলম লগ্ন"}
    },
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
    if value.startswith("bn") or "bengali" in value or "bangla" in value:
        return "bn"
    elif value.startswith("hi") or "hindi" in value:
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
    m_d = (current_date.month, current_date.day)
    s_name = normalize_sankranti_name(sankranti_name)

    try:
        tithi_num = int(tithi_num)
    except (TypeError, ValueError):
        tithi_num = 0

    # ১. তিথিভিত্তিক সনাতন উৎসব
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
                "muhurta": ""
            }
        )

    # ২. সর্বভারতীয় একাদশী ব্রত
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

    # ৩. মাসিক সংকষ্টী চতুর্থী
    if tithi_num == 4 and paksha == "Krishna":
        sankashti_name = {"en": "Sankashti Chaturthi Vrat", "hi": "संकष्टी चतुर्थी व्रत", "bn": "সংকষ্টী চতুর্থী ব্রত (চন্দ্রোদয় পূজা)"}
        append_festival_once(festivals, {
            "name": sankashti_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🐘", "deity": {"en": "Lord Ganesha & Chandra Deva", "hi": "भगवान श्री गणेश व चन्द्र देव", "bn": "শ্রী গণেশ ও চন্দ্র দেব"}[l_key],
            "description": {
                "en": "Fasting dedicated to Lord Ganesha to remove obstacles, broken after moonrise sighting.",
                "hi": "विघ्नहर्ता भगवान गणेश का व्रत, जो रात्रि में चंद्र दर्शन व अर्घ्य के बाद खोला जाता है।",
                "bn": "বিঘ্নবিনাশক শ্রী গণেশের উদ্দেশ্যে উপবাস এবং রাতে চন্দ্র দর্শন ও অর্ঘ্যদানের মাধ্যমে পারণ।"
            }[l_key],
            "muhurta_type": "sayankal", "muhurta_label": {"en": "Moonrise & Puja Time", "hi": "चन्द्रोदय व गणेश पूजन", "bn": "চন্দ্রোদয় ও গণেশ পূজা লগ্ন"}[l_key], "muhurta": ""
        })

    # ৪. মাসিক বিনায়ক চতুর্থী
    elif tithi_num == 4 and paksha == "Shukla":
        vinayaka_name = {"en": "Vinayaka Chaturthi Vrat", "hi": "विनायक चतुर्थी व्रत", "bn": "বিনায়ক চতুর্থী ব্রত (মধ্যাহ্ন পূজা)"}
        append_festival_once(festivals, {
            "name": vinayaka_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🐘", "deity": {"en": "Lord Ganesha (Vinayaka)", "hi": "भगवान श्री गणेश", "bn": "ভগবান শ্রী গণেশ"}[l_key],
            "description": {
                "en": "Monthly Shukla Chaturthi fast observing Madhyahna Ganesha Puja for wisdom and success.",
                "hi": "बुद्धि व सिद्धि की प्राप्ति हेतु शुक्ल पक्ष की चतुर्थी पर मध्याह्न गणेश पूजन।",
                "bn": "জ্ঞান, বুদ্ধি ও সর্বসিদ্ধির কামনায় শুক্লপক্ষের চতুর্থীতে মধ্যাহ্নকালে শ্রী গণেশ পূজা।"
            }[l_key],
            "muhurta_type": "madhyahna", "muhurta_label": {"en": "Madhyahna Puja Muhurta", "hi": "मध्याह्न गणेश पूजा", "bn": "মধ্যাহ্ন গণেশ পূজা মুহূর্ত"}[l_key], "muhurta": ""
        })

    # ৫. মাসিক কালাষ্টমী / ভৈরব অষ্টমী
    elif tithi_num == 8 and paksha == "Krishna":
        kalashtami_name = {"en": "Kalashtami / Bhairava Ashtami Vrat", "hi": "कालाष्टमी / भैरव अष्टमी व्रत", "bn": "কালাষ্টমী ব্রত (কালভৈরব পূজা)"}
        append_festival_once(festivals, {
            "name": kalashtami_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🔱", "deity": {"en": "Lord Kalabhairava & Shiva", "hi": "भगवान कालभैरव", "bn": "ভগবান কালভৈরব ও শিব"}[l_key],
            "description": {
                "en": "Monthly fasting dedicated to Lord Bhairava to eliminate fears, afflictions, and negativities.",
                "hi": "समस्त भय, बाधा व संकटों के निवारण हेतु भगवान कालभैरव की विशेष रात्रि पूजा।",
                "bn": "সর্বপ্রকার ভয় ও বিঘ্ন বিনাশের জন্য ভগবান কালভৈরবের বিশেষ পূজা ও উপবাস।"
            }[l_key],
            "muhurta_type": "nishita", "muhurta_label": {"en": "Nishita Kaal Puja", "hi": "निशीथ काल पूजा", "bn": "নিশীথ কাল ভৈরব পূজা"}[l_key], "muhurta": ""
        })

    # ৬. মাসিক দুর্গাশ্টমী
    elif tithi_num == 8 and paksha == "Shukla":
        durga_ashtami_name = {"en": "Masik Durgashtami Vrat", "hi": "मासिक दुर्गाष्टमी व्रत", "bn": "মাসিক দুর্গাশ্টমী ব্রত (দেবী দুর্গা পূজা)"}
        append_festival_once(festivals, {
            "name": durga_ashtami_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🔱", "deity": {"en": "Maa Durga", "hi": "माँ दुर्गा", "bn": "মা দুর্গা দেবী"}[l_key],
            "description": {
                "en": "Monthly fasting dedicated to Goddess Durga invoking strength, prosperity, and protection.",
                "hi": "शक्ति, सामर्थ्य एवं परिवार की रक्षा हेतु शुक्ल पक्ष की अष्टमी पर माँ दुर्गा की विशेष पूजा।",
                "bn": "পারিবারিক সমৃদ্ধি ও সুরক্ষার কামনায় প্রতি মাসের শুক্ল অষ্টমী তিথিতে মা দুর্গার বিশেষ পূজা।"
            }[l_key],
            "muhurta_type": "sandhi", "muhurta_label": {"en": "Sandhya / Pradosh Puja", "hi": "संध्या व प्रदोष काल", "bn": "সন্ধ্যা ও প্রদোষ লগ্ন"}[l_key], "muhurta": ""
        })

    # ৭. মাসিক স্কন্দ ষষ্ঠী ব্রত
    elif tithi_num == 6 and paksha == "Shukla":
        skanda_name = {"en": "Masik Skanda Sasthi Vrat", "hi": "मासिक स्कंद षष्ठी व्रत", "bn": "মাসিক স্কন্দ ষষ্ঠী ব্রত (কার্তিক পূজা)"}
        append_festival_once(festivals, {
            "name": skanda_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🦚", "deity": {"en": "Lord Kartikeya (Murugan)", "hi": "भगवान कार्तिकेय (मुरुगन)", "bn": "ভগবান কার্তিকেয় (মুরুগান)"}[l_key],
            "description": {
                "en": "Fast observed for health, courage, and offspring dedicated to Lord Skanda.",
                "hi": "संतान सुख व आरोग्यता की प्राप्ति हेतु भगवान कार्तिकेय (स्कंद) का पावन षष्ठी व्रत।",
                "bn": "সুস্বাস্থ্য, সাহস ও সন্তান কামনায় দেব সেনাপতি ভগবান কার্তিকেয়ের ষষ্ঠী ব্রত।"
            }[l_key],
            "muhurta_type": "purvahna", "muhurta_label": {"en": "Purvahna Puja", "hi": "पूर्वाह्न काल", "bn": "পূর্বাহ্ন কাল পূজা"}[l_key], "muhurta": ""
        })

    # ৮. মাসিক শিবরাত্রি
    elif tithi_num == 14 and paksha == "Krishna":
        shivratri_name = {"en": "Masik Shivratri Vrat", "hi": "मासिक शिवरात्रि व्रत", "bn": "মাসিক শিবরাত্রি ব্রত (নিশীথ পূজা)"}
        append_festival_once(festivals, {
            "name": shivratri_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🔱", "deity": {"en": "Lord Shiva", "hi": "भगवान शिव", "bn": "দেবাদিদেব মহাদেব"}[l_key],
            "description": {
                "en": "Monthly Shivratri fasting observed with midnight Shiva Lingam worship for liberation.",
                "hi": "मनोकामना पूर्ति एवं कष्ट निवारण हेतु मध्यरात्रि में भगवान शिव का जलाभिषेक व व्रत।",
                "bn": "মনোবাঞ্ছা পূরণ ও সর্বক্লেশ মুক্তির উদ্দেশ্যে নিশীথ কালে শিবলিঙ্গে জলাভিষেক ও উপবাস।"
            }[l_key],
            "muhurta_type": "nishita", "muhurta_label": {"en": "Nishita Midnight Puja", "hi": "निशीथ काल मुहूर्त", "bn": "নিশীথ काल পূজা মুহূর্ত"}[l_key], "muhurta": ""
        })

    # ৯. দর্শ অমাবস্যা ও পিতৃ তর্পণ
    elif (tithi_num == 15 and paksha == "Krishna") or tithi_num == 30:
        amavasya_name = {"en": "Darsha Amavasya / Pitru Tarpan", "hi": "दर्श अमावस्या / पितृ तर्पण", "bn": "দর্শ অমাবস্যা / পিতৃপুরুষের তর্পণ ও দান"}
        append_festival_once(festivals, {
            "name": amavasya_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ও তর্পণ"}[l_key],
            "icon": "🌑", "deity": {"en": "Pitru Devas & Lord Shiva", "hi": "पितृ देव व भगवान शिव", "bn": "পিতৃপুরুষ ও মহাদেব"}[l_key],
            "description": {
                "en": "Monthly Amavasya day for offering sacred water oblation (tarpan) and charity for ancestors' peace.",
                "hi": "पूर्वजों की शांति व तृप्ति हेतु पवित्र जल तर्पण, अन्नदान एवं पुण्य स्नान का दिन।",
                "bn": "পিতৃপুরুষের আত্মার তৃপ্তির উদ্দেশ্যে পবিত্র তর্পণ, দান ও মহাদেবের অর্চনা।"
            }[l_key],
            "muhurta_type": "aparahna", "muhurta_label": {"en": "Aparahna (Tarpan)", "hi": "अपराह्न तर्पण काल", "bn": "অপরাহ্ন তর্পণ লগ্ন"}[l_key], "muhurta": ""
        })

    # ১০. প্রদোষ ব্রত
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

    # ১১. সত্যনারায়ণ পূজা
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

    # ১২. সৌর সংক্রান্তি
    if m_d == (1, 14) or ("makar" in s_name or "capricorn" in s_name):
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

    elif m_d == (2, 13) or ("kumbha" in s_name or "aquarius" in s_name):
        kumbha_names = {"en": "Kumbha Sankranti / Phalguna Sankranti", "hi": "कुम्भ संक्रांति", "bn": "কুম্ভ সংক্রান্তি / ফাল্গুন সংক্রান্তি মহাতীর্থ স্নান"}
        kumbha_deity = {"en": "Surya Deva & Lord Shiva", "hi": "भगवान सूर्य व शिव जी", "bn": "ভগবান সূর্য দেব ও মহাদেব"}
        kumbha_desc = {
            "en": "Sun enters Aquarius (Kumbha Rashi), highly auspicious for sacred snan and charity.",
            "hi": "सूर्य का कुम्भ राशि में प्रवेश, पवित्र तीर्थ स्नान एवं अन्न-वस्त्र दान का पावन दिन।",
            "bn": "সূর্যের কুম্ভ রাশিতে শুভ প্রবেশ, গঙ্গা ও পুণ্যতীর্থ স্নান এবং দানকার্যের শ্রেষ্ঠ লগ্ন।"
        }
        append_festival_once(festivals, {
            "name": kumbha_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": kumbha_deity[l_key], "description": kumbha_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Kumbha Sankranti Punya Kaal", "hi": "कुम्भ संक्रांति पुण्य काल", "bn": "কুম্ভ সংক্রান্তি পুণ্যকাল স্নান ও দান"}[l_key], "muhurta": ""
        })

    elif m_d == (3, 15) or ("meena" in s_name or "pisces" in s_name):
        meena_names = {"en": "Meena Sankranti", "hi": "मीन संक्रांति", "bn": "মীন সংক্রান্তি পুণ্যস্নান ও দান"}
        meena_deity = {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"}
        meena_desc = {
            "en": "Sun transits into Pisces (Meena Rashi), highly auspicious for holy dip and charity.",
            "hi": "सूर्य का मीन राशि में प्रवेश, पवित्र नदियों में स्नान एवं पुण्य दान का विशेष दिन।",
            "bn": "সূর্যের মীন রাশিতে শুভ সংক্রমণ, পবিত্র গঙ্গাস্নান ও পুণ্য অর্জনের লগ্ন।"
        }
        append_festival_once(festivals, {
            "name": meena_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": meena_deity[l_key], "description": meena_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Meena Sankranti Punya Kaal", "hi": "मीन संक्रांति पुण्य काल", "bn": "মীন সংক্রান্তি পুণ্যকাল স্নান ও দান"}[l_key], "muhurta": ""
        })

    elif m_d == (4, 14):
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

    elif m_d == (5, 15) or ("vrishabha" in s_name or "taurus" in s_name):
        vrish_names = {"en": "Vrishabha Sankranti", "hi": "वृषभ संक्रांति", "bn": "বৃষ সংক্রান্তি মহাতীর্থ স্নান ও দান"}
        vrish_deity = {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"}
        vrish_desc = {
            "en": "Sun transits into Taurus (Vrishabha Rashi), highly sacred for holy water oblations.",
            "hi": "सूर्य का वृषभ राशि में प्रवेश, पवित्र तीर्थ स्नान एवं गौ-दान का विशेष पावन दिन।",
            "bn": "সূর্যের বৃষ রাশিতে শুভ সংক্রমণ, পুণ্যতীর্থ স্নান ও গো-দানের শ্রেষ্ঠ দিন।"
        }
        append_festival_once(festivals, {
            "name": vrish_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": vrish_deity[l_key], "description": vrish_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Vrishabha Sankranti Punya Kaal", "hi": "वृषभ संक्रांति पुण्य काल", "bn": "বৃষ সংক্রান্তি পুণ্যকাল স্নান"}[l_key], "muhurta": ""
        })

    elif m_d == (6, 15) or ("mithuna" in s_name or "gemini" in s_name):
        mithuna_names = {"en": "Mithuna Sankranti / Raja Parba", "hi": "मिथुन संक्रांति / राजा पर्ब", "bn": "মিথুন সংক্রান্তি / রাজা পর্ব (ভূদেবী পূজা)"}
        mithuna_deity = {"en": "Surya Deva & Mother Earth", "hi": "भगवान सूर्य व भूदेवी", "bn": "ভগবান সূর্য দেব ও ধরিত্রী মাতা"}
        mithuna_desc = {
            "en": "Sun enters Gemini (Mithuna Rashi), celebrated as agricultural festivity honoring Mother Earth.",
            "hi": "सूर्य का मिथुन राशि में प्रवेश, धरती माता के सत्कार एवं नवीन कृषि उत्सव (राजा पर्ब) का पावन दिन।",
            "bn": "সূর্যের মিথুন রাশিতে শুভ সংক্রমণ এবং ধরিত্রী মাতার উর্বরতা কামনায় ঐতিহ্যবাহী ভূদেবী পূজা।"
        }
        append_festival_once(festivals, {
            "name": mithuna_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": mithuna_deity[l_key], "description": mithuna_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Mithuna Sankranti Punya Kaal", "hi": "मिथुन संक्रांति पुण्य काल", "bn": "মিথুন সংক্রান্তি পুণ্যকাল স্নান ও দান"}[l_key], "muhurta": ""
        })

    elif m_d == (7, 16) or m_d == (7, 17) or ("karka" in s_name or "cancer" in s_name):
        karka_names = {"en": "Karka Sankranti / Dakshinayana Begins", "hi": "कर्क संक्रांति / दक्षिणायन प्रारंभ", "bn": "কর্কট সংক্রান্তি (সূর্যের দক্ষিণায়ন গমন)"}
        karka_deity = {"en": "Surya Deva & Lord Vishnu", "hi": "भगवान सूर्य व श्री हरि", "bn": "ভগবান সূর্য দেব ও শ্রীহরি নারায়ণ"}
        karka_desc = {
            "en": "Sun transits into Cancer (Karka Rashi) marking the start of Dakshinayana, dedicated to Pitru tarpan.",
            "hi": "सूर्य का कर्क राशि में प्रवेश, देवताओं की रात्रि (दक्षिणायन) का आरंभ एवं पवित्र स्नान-दान दिवस।",
            "bn": "সূর্যের কর্কট রাশিতে প্রবেশ ও ৬ মাসব্যাপী দক্ষিণায়নের সূচনা; পিতৃপুরুষের তর্পণে পুণ্যফলদায়ী লগ্ন।"
        }
        append_festival_once(festivals, {
            "name": karka_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": karka_deity[l_key], "description": karka_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Karka Sankranti Punya Kaal", "hi": "कर्क संक्रांति पुण्य काल", "bn": "কর্কট সংক্রান্তি পুণ্যকাল স্নান ও দান"}[l_key], "muhurta": ""
        })

    elif m_d == (8, 17) or ("simha" in s_name or "leo" in s_name):
        simha_names = {"en": "Simha Sankranti / Main Manasa Puja", "hi": "सिंह संक्रांति / मुख्य मनसा पूजा", "bn": "সিংহ সংক্রান্তি / প্রধান শ্রী শ্রী মনসা পূজা"}
        simha_deity = {"en": "Surya Deva & Maa Manasa", "hi": "भगवान सूर्य व माँ मनसा", "bn": "ভগবান সূর্য দেব ও মা মনসা দেবী"}
        simha_desc = {
            "en": "Sun transits into Leo (Simha Rashi) and annual worship of Goddess Manasa in Bengal and Assam.",
            "hi": "सूर्य का सिंह राशि में प्रवेश एवं बंगाल व असम में माँ मनसा की प्रधान वार्षिक महापूजा।",
            "bn": "সূর্যের সিংহ রাশিতে সংক্রমণ এবং সর্পভয়নাশিনী মা মনসার বার্ষিক মহোৎসব ও পূজা সমাপন।"
        }
        append_festival_once(festivals, {
            "name": simha_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "🐍", "deity": simha_deity[l_key], "description": simha_desc[l_key],
            "muhurta_type": "purvahna", "muhurta_label": {"en": "Simha Sankranti Punya Kaal", "hi": "सिंह संक्रांति पुण्य काल", "bn": "সিংহ সংক্রান্তি পুণ্যকাল"}[l_key], "muhurta": ""
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

    elif m_d == (10, 17) or ("tula" in s_name or "libra" in s_name):
        tula_names = {"en": "Tula Sankranti / Garbhana Sankranti", "hi": "तुला संक्रांति / गर्भाना संक्रांति", "bn": "তুলা সংক্রান্তি / গর্ভণা সংক্রান্তি ও ডাক সংক্রান্তি"}
        tula_deity = {"en": "Surya Deva & Maa Lakshmi", "hi": "भगवान सूर्य व माँ लक्ष्मी", "bn": "ভগবান সূর্য দেব ও মা লক্ষ্মী"}
        tula_desc = {
            "en": "Sun transits into Libra (Tula Rashi), celebrated with holy river baths and harvest prayers.",
            "hi": "सूर्य का तुला राशि में संक्रमण, कावेरी तीर्थ स्नान एवं नवीन धान्य समृद्धि का पावन दिन।",
            "bn": "সূর্যের তুলা রাশিতে শুভ সংক্রমণ, তীর্থস্নান এবং ধানের শীষে সমৃদ্ধি কামনায় বিশেষ অর্চনা।"
        }
        append_festival_once(festivals, {
            "name": tula_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": tula_deity[l_key], "description": tula_desc[l_key],
            "muhurta_type": "purvahna", "muhurta_label": {"en": "Tula Sankranti Punya Kaal", "hi": "तुला संक्रांति पुण्य काल", "bn": "তুলা সংক্রান্তি পুণ্যকাল"}[l_key], "muhurta": ""
        })

    # ১৩. ডায়নামিক আন্তর্জাতিক রবিবার ভিত্তিক দিবস
    if current_date.weekday() == 6:
        if current_date.month == 5 and 8 <= current_date.day <= 14:
            append_festival_once(festivals, {
                "name": {"en": "Mother's Day", "hi": "मातृ दिवस (मदर्स डे)", "bn": "বিশ্ব মা দিবস (মাদার্স ডে)"}[l_key],
                "category": "world", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"}[l_key],
                "icon": "👩‍👧‍👦", "deity": {"en": "Motherhood", "hi": "मातृ शक्ति", "bn": "মাতৃশক্তি"}[l_key],
                "description": {"en": "Honouring motherhood and maternal bonds.", "hi": "मातृ प्रेम व समर्पण के सम्मान का दिन।", "bn": "মায়েদের নিঃস্বার্থ স্নেহ, মমতা ও ভালোবাসার প্রতি শ্রদ্ধার্ঘ্য।"}[l_key],
                "muhurta": {"en": "All Day Celebration", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}[l_key]
            })
        elif current_date.month == 6 and 15 <= current_date.day <= 21:
            append_festival_once(festivals, {
                "name": {"en": "Father's Day", "hi": "पितृ दिवस (फादर्स डे)", "bn": "বিশ্ব বাবা দিবস (ফাদার্স ডে)"}[l_key],
                "category": "world", "type": {"en": "Observance", "hi": "अंतर्राष्ट्रीय दिवस", "bn": "আন্তর্জাতিক দিবস"}[l_key],
                "icon": "👨‍👧‍👦", "deity": {"en": "Fatherhood", "hi": "पितृ शक्ति", "bn": "পিতৃশক্তি"}[l_key],
                "description": {"en": "Honouring fatherhood and paternal contributions.", "hi": "पिता के त्याग व मार्गदर्शन के प्रति सम्मान का दिन।", "bn": "বাবার ত্যাগ, নিষ্ঠা ও ভালোবাসার প্রতি গভীর শ্রদ্ধা নিবেদনের দিন।"}[l_key],
                "muhurta": {"en": "All Day Celebration", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}[l_key]
            })
        elif current_date.month == 8 and current_date.day <= 7:
            append_festival_once(festivals, {
                "name": {"en": "International Friendship Day", "hi": "अंतर्राष्ट्रीय मित्रता दिवस (फ्रेंडशिप डे)", "bn": "আন্তর্জাতিক বন্ধু দিবস (ফ্রেন্ডশিপ ডে)"}[l_key],
                "category": "world", "type": {"en": "Global Celebration", "hi": "अंतर्राष्ट्रीय पर्व", "bn": "আন্তর্জাতিক উৎসব"}[l_key],
                "icon": "🤝", "deity": {"en": "Companionship", "hi": "मित्रता", "bn": "বন্ধুত্ব"}[l_key],
                "description": {"en": "Celebrating the enduring spirit of friendship and mutual support.", "hi": "सच्ची मित्रता एवं सद्भाव को समर्पित पावन दिवस।", "bn": "সত্যিকারের বন্ধুত্ব ও ভ্রাতৃত্বের মেলবন্ধন উদযাপনের বিশেষ দিন।"}[l_key],
                "muhurta": {"en": "All Day Celebration", "hi": "सम्पूर्ण दिवस", "bn": "সারাদিন উদযাপিত"}[l_key]
            })

    # ১৪. ভারতীয় জাতীয় দিবস
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

    # ১৫. আন্তর্জাতিক দিবস
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

    # ১৬. পরিবর্তনশীল দিবস
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

    # ভানু সপ্তমী (যেকোনো সপ্তমী তিথি যদি রবিবারে পড়ে)
    if tithi_num == 7 and current_date.weekday() == 6:
        bhanu_name = {"en": "Bhanu Saptami (Surya Saptami)", "hi": "भानु सप्तमी (सूर्य सप्तमी)", "bn": "পবিত্র ভানু সপ্তমী মহাতর্পণ"}
        append_festival_once(festivals, {
            "name": bhanu_name[l_key], "category": "hindu", "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "☀️", "deity": {"en": "Lord Surya Narayana", "hi": "भगवान सूर्य नारायण", "bn": "ভগবান সূর্য নারায়ণ"}[l_key],
            "description": {
                "en": "Sunday alignment with Saptami Tithi dedicated to Sun God.",
                "hi": "रविवार युक्त सप्तमी पर भगवान सूर्य को अर्घ्य समर्पण।",
                "bn": "রবিবার যুক্ত সপ্তমীতে সূর্যদেবের বিশেষ তর্পণ ও পূজা।"
            }[l_key],
            "muhurta_type": "sunrise_snan",
            "muhurta_label": {"en": "Sunrise Arghya Muhurta", "hi": "सूर्योदय अर्घ्य मुहूर्त", "bn": "সূর্যোদয় অর্ঘ্যদান মুহূর্ত"}[l_key],
            "muhurta": ""
        })

    # অন্বাধান (অমাবস্যা বা চতুর্দশী সংযোগে বৈদিক যজ্ঞ তিথি)
    if (tithi_num == 15 and paksha == "Krishna") or (tithi_num == 14 and paksha == "Krishna"):
        anvadhan_name = {"en": "Anvadhan (Vedic Ritual)", "hi": "अन्वाधान (वैदिक अनुष्ठान)", "bn": "বৈদিক অন্বাধান সংস্কার"}
        append_festival_once(festivals, {
            "name": anvadhan_name[l_key], "category": "hindu", "type": {"en": "Vedic Ritual", "hi": "वैदिक अनुष्ठान", "bn": "বৈদিক সংস্কার"}[l_key],
            "icon": "🔥", "deity": {"en": "Agni Deva & Sri Vishnu", "hi": "अग्नि देव व श्री विष्णु", "bn": "অগ্নি দেব ও শ্রীহরি বিষ্ণু"}[l_key],
            "description": {
                "en": "Vedic rite performed prior to Ishti.",
                "hi": "इष्टि अनुष्ठान से पूर्व अग्नि प्रज्वलन का पावन वैदिक संस्कार।",
                "bn": "ইষ্টি যজ্ঞের পূর্বে যজ্ঞাগ্নি রক্ষা ও সংযমের বৈদিক অন্বাধান সংস্কার।"
            }[l_key],
            "muhurta_type": "purvahna",
            "muhurta_label": {"en": "Purvahna Havan", "hi": "पूर्वाह्न हवन", "bn": "পূর্বাহ্ন সংস্কার লগ্ন"}[l_key],
            "muhurta": ""
        })

    elif m_d == (11, 16) or ("vrishchika" in s_name or "scorpio" in s_name):
        vrishchika_names = {"en": "Vrishchika Sankranti", "hi": "वृश्चिक संक्रांति", "bn": "বৃশ্চিক সংক্রান্তি মহাতীর্থ স্নান ও দান"}
        vrishchika_deity = {"en": "Surya Deva", "hi": "भगवान सूर्य देव", "bn": "ভগবান সূর্য দেব"}
        vrishchika_desc = {
            "en": "Sun transits into Scorpio (Vrishchika Rashi), highly auspicious for holy dip and charity.",
            "hi": "सूर्य का वृश्चिक राशि में प्रवेश, पवित्र तीर्थ स्नान एवं पुण्य दान का विशेष दिन।",
            "bn": "সূর্যের বৃশ্চিক রাশিতে শুভ সংক্রমণ, তীর্থস্নান ও অন্নদানের পবিত্র লগ্ন।"
        }
        append_festival_once(festivals, {
            "name": vrishchika_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": vrishchika_deity[l_key], "description": vrishchika_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Vrishchika Sankranti Punya Kaal", "hi": "वृश्चिक संक्रांति पुण्य काल", "bn": "বৃশ্চিক সংক্রান্তি পুণ্যকাল"}[l_key], "muhurta": ""
        })

    elif m_d == (12, 16) or ("dhanu" in s_name or "sagittarius" in s_name):
        dhanu_names = {"en": "Dhanu Sankranti / Dhanurmas Begins", "hi": "धनु संक्रांति / धनुर्मास प्रारंभ", "bn": "ধনু সংক্রান্তি / ধনুর্মাস আরম্ভ"}
        dhanu_deity = {"en": "Surya Deva & Lord Vishnu", "hi": "भगवान सूर्य व श्रीहरि", "bn": "ভগবান সূর্য দেব ও শ্রীহরি নারায়ণ"}
        dhanu_desc = {
            "en": "Sun enters Sagittarius (Dhanu Rashi), commencing the sacred month of Dhanurmas.",
            "hi": "सूर्य का धनु राशि में संक्रमण एवं भगवान विष्णु की विशेष आराधना के धनुर्मास का शुभारंभ।",
            "bn": "সূর্যের ধনু রাশিতে প্রবেশ ও শ্রীহরির বিশেষ আরাধনাময় ধনুর্মাসের শুভ সূচনা।"
        }
        append_festival_once(festivals, {
            "name": dhanu_names[l_key], "category": "hindu", "type": {"en": "Solar Festival", "hi": "सौर पर्व", "bn": "সৌর মহাপর্ব"}[l_key],
            "icon": "☀️", "deity": dhanu_deity[l_key], "description": dhanu_desc[l_key],
            "muhurta_type": "sunrise_snan", "muhurta_label": {"en": "Dhanu Sankranti Punya Kaal", "hi": "धनु संक्रांति पुण्य काल", "bn": "ধনু সংক্রান্তি পুণ্যকাল"}[l_key], "muhurta": ""
        })


    # --------------------------------------------------------------------------
    # ভাদ্রপদ কৃষ্ণ পঞ্চমী ও ষষ্ঠী (Bhadrapada Krishna 5 & 6) - পৃথক পৃথক উৎসব
    # --------------------------------------------------------------------------
    if lunar_month == "Bhadrapada" and paksha == "Krishna" and tithi_num in [5, 6]:
        
        # ১. ভগবান শ্রী বলরাম জন্মজয়ন্তী
        append_festival_once(festivals, {
            "name": {
                "en": "Sri Balarama Jayanti",
                "hi": "श्री बलराम जयंती",
                "bn": "শ্রী শ্রী বলরাম জন্মজয়ন্তী"
            }[l_key],
            "category": "hindu",
            "type": {"en": "Major Festival", "hi": "महापर्व", "bn": "মহাপর্ব"}[l_key],
            "icon": "🌾",
            "deity": {
                "en": "Lord Balarama (Sheshanaga)",
                "hi": "भगवान बलराम (शेषनाग अवतार)",
                "bn": "ভগবান বলরাম দেব ও শেষনাগ"
            }[l_key],
            "description": {
                "en": "Divine appearance day of Lord Balarama, the elder brother of Sri Krishna bearing the golden plough.",
                "hi": "भगवान श्रीकृष्ण के बड़े भाई एवं शेषनाग अवतारी भगवान बलराम जी का पावन प्राकट्योत्सव।",
                "bn": "ভগবান শ্রীকৃষ্ণের জ্যেষ্ঠ ভ্রাতা ও দিব্য হলধারী শেষাবতার শ্রী বলরামদেবের পরম আবির্ভাব তিথি।"
            }[l_key],
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Abhisheka Muhurta",
                "hi": "पूर्वाह्न अभिषेक मुहूर्त",
                "bn": "পূর্বাহ্ন অভিষেক ও পূজা লগ্ন"
            }[l_key],
            "muhurta": ""
        })

        # ২. হল ষষ্ঠী ব্রত (হরছট)
        append_festival_once(festivals, {
            "name": {
                "en": "Hal Sasthi Vrat (Har Chhath)",
                "hi": "हलषष्ठी व्रत (हरछठ)",
                "bn": "শ্রী শ্রী হল ষষ্ঠী ব্রত (হরছট)"
            }[l_key],
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🌾",
            "deity": {
                "en": "Haladhara & Lord Shiva",
                "hi": "हलधर बलराम व भगवान शिव",
                "bn": "হলধর বলরাম ও দেবাদিদেব শিব"
            }[l_key],
            "description": {
                "en": "Fasting observed by mothers for their children's long life, consuming only unplowed produce (Pasin rice) and buffalo milk.",
                "hi": "संतान की दीर्घायु हेतु माताओं द्वारा आचरित हलषष्ठी व्रत, जिसमें बिना जुते हुए अन्न व भैंस के दूध का प्रयोग होता है।",
                "bn": "সন্তানের নীরোগ দীর্ঘায়ুর কামনায় মায়েদের হল ষষ্ঠী ব্রত; বিনা চাষের উৎপন্ন শস্য ও মহিষের দুগ্ধ গ্রহণ।"
            }[l_key],
            "muhurta_type": "purvahna",
            "muhurta_label": {
                "en": "Purvahna Hal Sasthi Puja",
                "hi": "पूर्वाह्न हलषष्ठी पूजन",
                "bn": "পূর্বাহ্ন হল ষষ্ঠী পূজা লগ্ন"
            }[l_key],
            "muhurta": ""
        })

        # ৩. ললহী ছট ব্রত
        append_festival_once(festivals, {
            "name": {
                "en": "Lahaee Chhath Vrat (Lalhi Chhath)",
                "hi": "ललही छठ व्रत (संतान रक्षा पर्व)",
                "bn": "শ্রী শ্রী ললহী ছট ব্রত (সন্তান রক্ষা পর্ব)"
            }[l_key],
            "category": "hindu",
            "type": {"en": "Vrata", "hi": "उपवास व्रत", "bn": "উপবাস ব্রত"}[l_key],
            "icon": "🪔",
            "deity": {
                "en": "Maa Sasthi & Lord Balarama",
                "hi": "माँ षष्ठी व बलराम जी",
                "bn": "মা ষষ্ঠী দেবী ও শ্রী বলরাম"
            }[l_key],
            "description": {
                "en": "Traditional maternal observance invoking blessings of Maa Sasthi and Lord Balarama for progeny protection.",
                "hi": "संतान की सर्वविपत्ति से रक्षा एवं सौभाग्य प्राप्ति हेतु ललही छठ की पावन पूजा।",
                "bn": "সন্তানের সর্বপ্রকার বিপদমুক্তি ও কল্যাণের কামনায় মা ষষ্ঠী ও বলরামদেবের পুণ্য ললহী ছট অর্চনা।"
            }[l_key],
            "muhurta_type": "sayankal",
            "muhurta_label": {
                "en": "Sayankal Pradosh Vrat Puja",
                "hi": "सायंकाल प्रदोष पूजा",
                "bn": "সায়ংকালীন প্রদোষ পূজা লগ্ন"
            }[l_key],
            "muhurta": ""
        })

    return festivals

# ==============================================================================
# ডায়নামিক মুহূর্ত গণক
# ==============================================================================
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
        
    # লোহড়ী বহ্নিপূজা ও প্রদোষ মুহূর্ত
    elif "lohri" in fn_lower or "লোহড়ী" in fn_lower or "लोहड़ी" in fn_lower:
        start_min = sunset_min
        end_min = sunset_min + 144
        type_labels = {
            "bn": "লোহড়ী বহ্নি প্রজ্বলন ও প্রদোষ লগ্ন",
            "hi": "लोहड़ी अग्नि पूजन व प्रदोष काल",
            "en": "Lohri Bonfire & Pradosha Muhurta"
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

    # সাধারণ শুভ মুহূর্ত
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
