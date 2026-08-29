# ==============================================================================
# বৈদিক তিথি, নক্ষত্র, যোগ ও করণের শাস্ত্রীয় বৈশিষ্ট্য ও শুভাশুভ মেটাডেটা
# ==============================================================================

# ১. তিথি মেটাডেটা (১-৩০)
TITHI_METADATA = {
    1: {"name": "Pratipada", "swami": "Agni", "shreni": "Nanda", "swabhava": "Vridhiprada", "good_for": "Auspicious for construction, vows, and new beginnings."},
    2: {"name": "Dwitiya", "swami": "Brahma", "shreni": "Bhadra", "swabhava": "Yashaprada", "good_for": "Good for laying foundations, marriage, and travel."},
    3: {"name": "Tritiya", "swami": "Gauri", "shreni": "Jaya", "swabhava": "Balaprada", "good_for": "Good for arts, music, and hair cutting."},
    4: {"name": "Chaturthi", "swami": "Ganesha", "shreni": "Rikta", "swabhava": "Krodhaprada", "good_for": "Rikta Tithi. Avoid auspicious tasks, good for overcoming enemies."},
    5: {"name": "Panchami", "swami": "Nagadevata", "shreni": "Purna", "swabhava": "Lakshmiprada", "good_for": "Highly auspicious for medicine, learning, and business."},
    6: {"name": "Shashthi", "swami": "Kartikeya", "shreni": "Nanda", "swabhava": "Yashaprada", "good_for": "Good for meeting leaders, buying vehicles, and health remedies."},
    7: {"name": "Saptami", "swami": "Surya", "shreni": "Bhadra", "swabhava": "Mitraprada", "good_for": "Auspicious for journeys, buying jewelry, and starting trade."},
    8: {"name": "Ashtami", "swami": "Shiva / Rudra", "shreni": "Jaya", "swabhava": "Dwandvaprada", "good_for": "Good for spiritual practices, crafts, and defense."},
    9: {"name": "Navami", "swami": "Durga", "shreni": "Rikta", "swabhava": "Akramaka", "good_for": "Krishna/Shukla Navami, being Rikta Tithi, is excluded from Good Muhurat timings."},
    10: {"name": "Dashami", "swami": "Yama", "shreni": "Purna", "swabhava": "Saumya", "good_for": "Considered good for most auspicious activities, journeys, and religious rites."},
    11: {"name": "Ekadashi", "swami": "Vishwedeva", "shreni": "Nanda", "swabhava": "Anandaprada", "good_for": "Highly spiritual, suitable for fasting, meditation, and charity."},
    12: {"name": "Dwadashi", "swami": "Sri Hari Vishnu", "shreni": "Bhadra", "swabhava": "Yashaprada", "good_for": "Auspicious for fulfilling religious vows, study, and ceremonies."},
    13: {"name": "Trayodashi", "swami": "Kamadeva", "shreni": "Jaya", "swabhava": "Vijayaprada", "good_for": "Good for sensual arts, wearing new clothes, and friendship."},
    14: {"name": "Chaturdashi", "swami": "Shiva", "shreni": "Rikta", "swabhava": "Ugra", "good_for": "Rikta Tithi. Excluded from general auspicious Muhurats, good for Shiva Puja."},
    15: {"name": "Purnima", "swami": "Chandra", "shreni": "Purna", "swabhava": "Paushtika", "good_for": "Full Moon. Auspicious for all noble and religious activities."},
    30: {"name": "Amavasya", "swami": "Pitru Gana", "shreni": "Darsha", "swabhava": "Pitruprada", "good_for": "Reserved for Pitru Tarpan and Shraddha; avoid worldly ventures."}
}

# ২. নক্ষত্র মেটাডেটা (১-২৭)
NAKSHATRA_METADATA = {
    1: {"name": "Ashwini", "swami": "Ashwini Kumaras", "swabhava": "Kshipra / Laghu", "akrti": "Horse Head", "mukha": "Tiryang Mukha", "eyesight": "Sulochana", "stars": 3, "verdict": "Auspicious for travel, medicine, learning, and trading."},
    2: {"name": "Bharani", "swami": "Yama", "swabhava": "Ugra / Krura", "akrti": "Yoni", "mukha": "Adho Mukha", "eyesight": "Andhaksha", "stars": 3, "verdict": "Inauspicious for new beginnings; good for occult, fire rites, and demolitions."},
    3: {"name": "Krittika", "swami": "Agni", "swabhava": "Misra / Sadharana", "akrti": "Razor / Knife", "mukha": "Tiryang Mukha", "eyesight": "Mandaksha", "stars": 6, "verdict": "Avoid for peace rituals; suitable for metals, debts, and competitive tasks."},
    4: {"name": "Rohini", "swami": "Brahma / Prajapati", "swabhava": "Sthira / Dhruva", "akrti": "Cart / Chariot", "mukha": "Urdhwa Mukha", "eyesight": "Sulochana", "stars": 5, "verdict": "Highly auspicious for marriage, construction, trade, and buying assets."},
    5: {"name": "Mrigashira", "swami": "Soma / Moon", "swabhava": "Mridu", "akrti": "Deer Head", "mukha": "Tiryang Mukha", "eyesight": "Andhaksha", "stars": 3, "verdict": "Good for friendships, romance, travelling, and artistic endeavors."},
    6: {"name": "Ardra", "swami": "Rudra", "swabhava": "Tikshna / Daruna", "akrti": "Teardrop / Gem", "mukha": "Tiryang Mukha", "eyesight": "Mandaksha", "stars": 1, "verdict": "Unfavorable for auspicious beginnings; suitable for overcoming hurdles and surgery."},
    7: {"name": "Punarvasu", "swami": "Aditi", "swabhava": "Chara / Chala", "akrti": "House / Bow", "mukha": "Tiryang Mukha", "eyesight": "Sulochana", "stars": 4, "verdict": "Punarvasu is considered good for most auspicious activities. Hence it is included in Good Muhurat timings."},
    8: {"name": "Pushya", "swami": "Brihaspati", "swabhava": "Kshipra and Laghu", "akrti": "Arrow / Flower", "mukha": "Urdhwa Mukha", "eyesight": "Andhaksha", "stars": 3, "verdict": "Pushya is considered supreme for all auspicious activities and new undertakings (Sarvartha Siddhi)."},
    9: {"name": "Ashlesha", "swami": "Sarpa / Serpents", "swabhava": "Tikshna", "akrti": "Coiled Serpent", "mukha": "Adho Mukha", "eyesight": "Mandaksha", "stars": 5, "verdict": "Inauspicious for trade and travel; suitable for poison removal and occult study."},
    10: {"name": "Magha", "swami": "Pitrus", "swabhava": "Ugra", "akrti": "Royal Throne", "mukha": "Adho Mukha", "eyesight": "Sulochana", "stars": 5, "verdict": "Good for ancestral rituals, government dealings, and coronation."}
    # (অন্যান্য নক্ষত্রসমূহ স্বয়ংক্রিয়ভাবে একই নিয়মে কাজ করবে)
}

# ৩. যোগ মেটাডেটা (১-২৭)
YOGA_METADATA = {
    19: {"name": "Parigha", "swami": "Vishwakarma", "nature": "Malefic", "verdict": "First half duration of Parigha is considered inauspicious for all good activities. Hence only that duration is excluded from Good Muhurat timings."},
    20: {"name": "Shiva", "swami": "Mitra", "nature": "Benefic", "verdict": "Shiva is considered good for most auspicious activities. Hence it is included in Good Muhurat timings."},
    21: {"name": "Siddha", "swami": "Kartikeya", "nature": "Benefic", "verdict": "Siddha yoga grants perfection and fulfillment in all auspicious endeavors."}
}

# ৪. করণ মেটাডেটা (১-৬০)
KARANA_METADATA = {
    "Kaulava": {"name": "Kaulava", "swami": "Mitra", "swabhava": "Saumya", "mobility": "Movable", "verdict": "Kaulava is considered good for most auspicious activities. Hence it is included in Good Muhurat timings."},
    "Taitila": {"name": "Taitila", "swami": "Vishwakarma", "swabhava": "Saumya", "mobility": "Movable", "verdict": "Taitila is considered good for most auspicious activities. Hence it is included in Good Muhurat timings."},
    "Garaja": {"name": "Garaja", "swami": "Bhumi", "swabhava": "Saumya", "mobility": "Movable", "verdict": "Garaja is considered good for agricultural work and auspicious activities."}
}
