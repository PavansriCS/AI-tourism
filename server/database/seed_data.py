DEFAULT_IMAGE = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80"

OFFICIAL_TOURISM_URLS = {
    "Taj Mahal": "https://www.tajmahal.gov.in/",
    "Jaipur": "https://www.tourism.rajasthan.gov.in/jaipur.html",
    "Udaipur": "https://www.tourism.rajasthan.gov.in/udaipur.html",
    "Ooty": "https://www.tamilnadutourism.tn.gov.in/destinations/ooty",
    "Kodaikanal": "https://www.tamilnadutourism.tn.gov.in/destinations/kodaikanal",
    "Yercaud": "https://www.tamilnadutourism.tn.gov.in/destinations/yercaud",
    "Madurai": "https://www.tamilnadutourism.tn.gov.in/destinations/madurai",
    "Meenakshi Amman Temple": "https://maduraimeenakshi.hrce.tn.gov.in/",
    "Rameswaram": "https://www.tamilnadutourism.tn.gov.in/destinations/rameswaram",
    "Kanyakumari": "https://www.tamilnadutourism.tn.gov.in/destinations/kanniyakumari",
    "Goa": "https://goa-tourism.com/",
    "Mumbai": "https://www.maharashtratourism.gov.in/-/mumbai-city",
    "Gateway of India": "https://www.maharashtratourism.gov.in/-/gateway-of-india",
    "Munnar": "https://www.keralatourism.org/destination/munnar/202",
    "Kochi": "https://www.keralatourism.org/destination/kochi-ernakulam/179",
    "Mysuru": "https://www.karnatakatourism.org/tour-item/mysuru/",
    "Hampi": "https://www.karnatakatourism.org/tour-item/hampi/",
    "Coorg": "https://www.karnatakatourism.org/tour-item/coorg/",
    "Statue of Unity": "https://www.soutickets.in/",
    "Andaman Islands": "https://www.andamantourism.gov.in/",
    "Cellular Jail": "https://www.andamantourism.gov.in/"
}

VERIFIED_LISTINGS = {
    "Taj Mahal": {
        "hotel_budget": ("Taj Hotel & Convention Centre, Agra", "https://www.tajhotels.com/en-in/hotels/taj-hotel-convention-centre-agra"),
        "hotel_premium": ("The Oberoi Amarvilas, Agra", "https://www.oberoihotels.com/hotels-in-agra-amarvilas-resort/"),
        "resort": ("ITC Mughal, Agra", "https://www.itchotels.com/in/en/itcmughal-agra"),
        "restaurant": ("Esphahan, The Oberoi Amarvilas", "https://www.oberoihotels.com/hotels-in-agra-amarvilas-resort/restaurants/esphahan/")
    },
    "Jaipur": {
        "hotel_budget": ("Jai Mahal Palace, Jaipur", "https://www.tajhotels.com/en-in/hotels/jai-mahal-palace-jaipur"),
        "hotel_premium": ("Rambagh Palace, Jaipur", "https://www.tajhotels.com/en-in/hotels/rambagh-palace-jaipur"),
        "resort": ("The Oberoi Rajvilas, Jaipur", "https://www.oberoihotels.com/hotels-in-jaipur-rajvilas-resort/"),
        "restaurant": ("Suvarna Mahal, Rambagh Palace", "https://www.tajhotels.com/en-in/hotels/rambagh-palace-jaipur/restaurants/suvarna-mahal")
    },
    "Udaipur": {
        "hotel_budget": ("Fateh Prakash Palace, Udaipur", "https://www.hrhhotels.com/fateh-prakash-palace-udaipur/"),
        "hotel_premium": ("Taj Lake Palace, Udaipur", "https://www.tajhotels.com/en-in/hotels/taj-lake-palace-udaipur"),
        "resort": ("The Oberoi Udaivilas, Udaipur", "https://www.oberoihotels.com/hotels-in-udaipur-udaivilas-resort/"),
        "restaurant": ("Sheesh Mahal, The Leela Palace Udaipur", "https://www.theleela.com/the-leela-palace-udaipur/restaurants/sheesh-mahal")
    },
    "Ooty": {
        "hotel_budget": ("Savoy, Ooty - IHCL SeleQtions", "https://www.seleqtionshotels.com/en-in/hotels/savoy-ooty"),
        "hotel_premium": ("Gem Park Ooty", "https://www.gempakooty.com/"),
        "resort": ("Sterling Ooty Elk Hill", "https://www.sterlingholidays.com/resorts-hotels/ooty-elk-hill"),
        "restaurant": ("Earl's Secret, Ooty", "https://www.kingscliff.in/earls-secret-restaurant-ooty/")
    },
    "Kodaikanal": {
        "hotel_budget": ("The Carlton, Kodaikanal", "https://www.carlton-kodaikanal.com/"),
        "hotel_premium": ("Great Trails Kodaikanal by GRT Hotels", "https://www.grthotels.com/great-trails-kodaikanal"),
        "resort": ("Sterling Kodai Lake", "https://www.sterlingholidays.com/resorts-hotels/kodai-lake"),
        "restaurant": ("Kodaikanal Official Dining Information", "https://www.tamilnadutourism.tn.gov.in/destinations/kodaikanal")
    },
    "Goa": {
        "hotel_budget": ("Cidade de Goa - IHCL SeleQtions", "https://www.seleqtionshotels.com/en-in/hotels/cidade-de-goa"),
        "hotel_premium": ("Taj Fort Aguada Resort & Spa, Goa", "https://www.tajhotels.com/en-in/hotels/taj-fort-aguada-goa"),
        "resort": ("The St. Regis Goa Resort", "https://www.marriott.com/en-us/hotels/goixr-the-st-regis-goa-resort/overview/"),
        "restaurant": ("Thalassa Goa", "https://thalassagoa.com/")
    },
    "Mumbai": {
        "hotel_budget": ("President, Mumbai - IHCL SeleQtions", "https://www.seleqtionshotels.com/en-in/hotels/president-mumbai"),
        "hotel_premium": ("The Taj Mahal Palace, Mumbai", "https://www.tajhotels.com/en-in/hotels/taj-mahal-palace-mumbai"),
        "resort": ("The Resort Mumbai", "https://www.theresortmumbai.com/"),
        "restaurant": ("Wasabi by Morimoto, Mumbai", "https://www.tajhotels.com/en-in/hotels/taj-mahal-palace-mumbai/restaurants/wasabi-by-morimoto")
    },
    "Munnar": {
        "hotel_budget": ("Fragrant Nature Munnar", "https://www.fragrantnature.com/fragrant-nature-munnar/"),
        "hotel_premium": ("The Tall Trees Munnar", "https://www.thetalltreesmunnar.com/"),
        "resort": ("Windermere Estate, Munnar", "https://www.windermereresorts.com/munnar/"),
        "restaurant": ("Munnar Official Dining Information", "https://www.keralatourism.org/destination/munnar/202")
    }
}

DESTINATION_NAMES = [
    ("Taj Mahal", "Uttar Pradesh", "Heritage", "Mid-range"),
    ("Jaipur", "Rajasthan", "Heritage City", "Mid-range"),
    ("Udaipur", "Rajasthan", "Lake City", "Mid-range"),
    ("Jodhpur", "Rajasthan", "Heritage City", "Budget"),
    ("Jaisalmer", "Rajasthan", "Desert", "Mid-range"),
    ("Varanasi", "Uttar Pradesh", "Spiritual", "Budget"),
    ("Golden Temple", "Punjab", "Spiritual", "Budget"),
    ("Amritsar", "Punjab", "Heritage City", "Budget"),
    ("Leh", "Ladakh", "Mountain", "Mid-range"),
    ("Pangong Lake", "Ladakh", "Lake", "Mid-range"),
    ("Nubra Valley", "Ladakh", "Adventure", "Mid-range"),
    ("Manali", "Himachal Pradesh", "Hill Station", "Budget"),
    ("Shimla", "Himachal Pradesh", "Hill Station", "Budget"),
    ("Spiti Valley", "Himachal Pradesh", "Adventure", "Mid-range"),
    ("Srinagar", "Jammu and Kashmir", "Lake City", "Mid-range"),
    ("Gulmarg", "Jammu and Kashmir", "Mountain", "Mid-range"),
    ("Mahabalipuram", "Tamil Nadu", "Heritage Coast", "Budget"),
    ("Kodaikanal", "Tamil Nadu", "Hill Station", "Budget"),
    ("Ooty", "Tamil Nadu", "Hill Station", "Budget"),
    ("Yercaud", "Tamil Nadu", "Hill Station", "Budget"),
    ("Madurai", "Tamil Nadu", "Temple City", "Budget"),
    ("Meenakshi Amman Temple", "Tamil Nadu", "Temple", "Budget"),
    ("Rameswaram", "Tamil Nadu", "Spiritual Coast", "Budget"),
    ("Kanyakumari", "Tamil Nadu", "Coast", "Budget"),
    ("Mysuru", "Karnataka", "Heritage City", "Budget"),
    ("Hampi", "Karnataka", "Heritage", "Budget"),
    ("Coorg", "Karnataka", "Hill Station", "Mid-range"),
    ("Munnar", "Kerala", "Hill Station", "Budget"),
    ("Alleppey", "Kerala", "Backwaters", "Mid-range"),
    ("Wayanad", "Kerala", "Nature", "Budget"),
    ("Kochi", "Kerala", "Port City", "Budget"),
    ("Hyderabad", "Telangana", "Heritage City", "Budget"),
    ("Charminar", "Telangana", "Monument", "Budget"),
    ("Konark Sun Temple", "Odisha", "Temple", "Budget"),
    ("Puri", "Odisha", "Spiritual Coast", "Budget"),
    ("Darjeeling", "West Bengal", "Hill Station", "Budget"),
    ("Kolkata", "West Bengal", "Metro Heritage", "Budget"),
    ("Sundarbans National Park", "West Bengal", "Wildlife", "Mid-range"),
    ("Gangtok", "Sikkim", "Mountain City", "Mid-range"),
    ("Shillong", "Meghalaya", "Hill City", "Budget"),
    ("Cherrapunji", "Meghalaya", "Nature", "Budget"),
    ("Mumbai", "Maharashtra", "Metro Coast", "Mid-range"),
    ("Gateway of India", "Maharashtra", "Monument", "Budget"),
    ("Ajanta Caves", "Maharashtra", "Heritage Caves", "Budget"),
    ("Ellora Caves", "Maharashtra", "Heritage Caves", "Budget"),
    ("Goa", "Goa", "Beach", "Mid-range"),
    ("Panaji", "Goa", "Capital City", "Budget"),
    ("Statue of Unity", "Gujarat", "Monument", "Budget"),
    ("Andaman Islands", "Andaman and Nicobar Islands", "Island", "Mid-range"),
    ("Cellular Jail", "Andaman and Nicobar Islands", "Heritage", "Budget")
]

COORDINATES = {
    "Taj Mahal": (27.1751, 78.0421),
    "Jaipur": (26.9124, 75.7873),
    "Udaipur": (24.5854, 73.7125),
    "Jodhpur": (26.2389, 73.0243),
    "Jaisalmer": (26.9157, 70.9083),
    "Varanasi": (25.3176, 82.9739),
    "Golden Temple": (31.6200, 74.8765),
    "Amritsar": (31.6340, 74.8723),
    "Leh": (34.1526, 77.5771),
    "Pangong Lake": (33.7597, 78.6676),
    "Nubra Valley": (34.6869, 77.5628),
    "Manali": (32.2396, 77.1887),
    "Shimla": (31.1048, 77.1734),
    "Spiti Valley": (32.2461, 78.0172),
    "Srinagar": (34.0837, 74.7973),
    "Gulmarg": (34.0484, 74.3805),
    "Mahabalipuram": (12.6269, 80.1927),
    "Kodaikanal": (10.2381, 77.4892),
    "Ooty": (11.4102, 76.6950),
    "Yercaud": (11.7753, 78.2093),
    "Madurai": (9.9252, 78.1198),
    "Meenakshi Amman Temple": (9.9195, 78.1193),
    "Rameswaram": (9.2876, 79.3129),
    "Kanyakumari": (8.0883, 77.5385),
    "Mysuru": (12.2958, 76.6394),
    "Hampi": (15.3350, 76.4600),
    "Coorg": (12.3375, 75.8069),
    "Munnar": (10.0889, 77.0595),
    "Alleppey": (9.4981, 76.3388),
    "Wayanad": (11.6854, 76.1320),
    "Kochi": (9.9312, 76.2673),
    "Hyderabad": (17.3850, 78.4867),
    "Charminar": (17.3616, 78.4747),
    "Konark Sun Temple": (19.8876, 86.0945),
    "Puri": (19.8135, 85.8312),
    "Darjeeling": (27.0410, 88.2663),
    "Kolkata": (22.5726, 88.3639),
    "Sundarbans National Park": (21.9497, 89.1833),
    "Gangtok": (27.3314, 88.6138),
    "Shillong": (25.5788, 91.8933),
    "Cherrapunji": (25.2702, 91.7323),
    "Mumbai": (19.0760, 72.8777),
    "Gateway of India": (18.9220, 72.8347),
    "Ajanta Caves": (20.5519, 75.7033),
    "Ellora Caves": (20.0268, 75.1793),
    "Goa": (15.2993, 74.1240),
    "Panaji": (15.4909, 73.8278),
    "Statue of Unity": (21.8380, 73.7191),
    "Andaman Islands": (11.7401, 92.6586),
    "Cellular Jail": (11.6756, 92.7470)
}

DESTINATION_IMAGES = {
    "Taj Mahal": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
    "Jaipur": "https://images.unsplash.com/photo-1599661046827-dacde6976549?auto=format&fit=crop&w=1200&q=80",
    "Udaipur": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
    "Varanasi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
    "Leh": "https://images.unsplash.com/photo-1581793746486-2c8b4b1cf7f8?auto=format&fit=crop&w=1200&q=80",
    "Manali": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
    "Kodaikanal": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=1200&q=80",
    "Ooty": "https://images.unsplash.com/photo-1622739366076-720ca7115c18?auto=format&fit=crop&w=1200&q=80",
    "Yercaud": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
    "Goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
    "Mumbai": "https://images.unsplash.com/photo-1567157577867-05ccb1388e66?auto=format&fit=crop&w=1200&q=80",
    "Andaman Islands": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80"
}


def slugify(value):
    return value.lower().replace("&", "and").replace(" ", "-").replace("'", "").replace(",", "")


def destination_id(name):
    return f"dest-{slugify(name)}"


def maps_url(name):
    return f"https://www.google.com/maps/search/?api=1&query={name.replace(' ', '+')}"


def tourism_url(name):
    return OFFICIAL_TOURISM_URLS.get(name, "https://www.incredibleindia.gov.in/")


def photo_url(name, listing_type):
    query = f"{name} {listing_type}".replace(" ", ",")
    return f"https://source.unsplash.com/1200x800/?{query}"


def verified_listing(destination_name, listing_key, fallback_name, fallback_url):
    listing = VERIFIED_LISTINGS.get(destination_name, {}).get(listing_key)
    if listing:
        return listing
    return fallback_name, fallback_url


def booking_platform_details(destination_name, listing_name, listing_type, index):
    query = f"{listing_name} {destination_name}".replace(" ", "+")
    city = destination_name.replace(" ", "+")
    platforms = [
        ("Booking.com", f"https://www.booking.com/searchresults.html?ss={query}", "https://www.booking.com/customer-service.html"),
        ("MakeMyTrip", f"https://www.makemytrip.com/hotels/hotel-listing/?searchText={city}", "https://support.makemytrip.com/"),
        ("Agoda", f"https://www.agoda.com/search?city={city}&textToSearch={query}", "https://www.agoda.com/info/contact.html"),
        ("Expedia", f"https://www.expedia.co.in/Hotel-Search?destination={city}", "https://www.expedia.co.in/service/"),
        ("Cleartrip", f"https://www.cleartrip.com/hotels/results?city={city}", "https://www.cleartrip.com/support/"),
        ("Yatra", f"https://www.yatra.com/hotels/hotels-in-{slugify(destination_name)}", "https://www.yatra.com/support"),
        ("EaseMyTrip", f"https://www.easemytrip.com/hotels/hotels-in-{slugify(destination_name)}.html", "https://www.easemytrip.com/contact-us.html")
    ]
    if listing_type == "restaurant":
        platforms = [
            ("EazyDiner", f"https://www.eazydiner.com/search?location={city}&q={query}", "https://www.eazydiner.com/contact-us"),
            ("Dineout", f"https://www.dineout.co.in/{slugify(destination_name)}-restaurants", "https://www.dineout.co.in/contactus"),
            ("Zomato", f"https://www.zomato.com/{slugify(destination_name)}/restaurants", "https://www.zomato.com/contact"),
            ("Swiggy", f"https://www.swiggy.com/search?query={query}", "https://www.swiggy.com/contact-us")
        ]
    if listing_type == "attraction":
        platforms = [
            ("GetYourGuide", f"https://www.getyourguide.com/s/?q={query}", "https://www.getyourguide.com/contact/"),
            ("Viator", f"https://www.viator.com/searchResults/all?text={query}", "https://www.viator.com/help"),
            ("Klook", f"https://www.klook.com/en-IN/search/result/?query={query}", "https://www.klook.com/en-IN/contact-us/"),
            ("MakeMyTrip Activities", f"https://www.makemytrip.com/activities/search?query={query}", "https://support.makemytrip.com/")
        ]
    provider, url, help_url = platforms[index % len(platforms)]
    return {
        "bookingProvider": provider,
        "bookingUrl": url,
        "providerContact": help_url,
        "providerHelpUrl": help_url
    }


def destination_description(name, state, category):
    return f"{name} in {state} is a {category.lower()} destination curated for smart itineraries, nearby stays, restaurants, attractions, navigation, and official booking access."


DESTINATIONS = []
HOTELS = []
RESORTS = []
RESTAURANTS = []
ATTRACTIONS = []

for index, (name, state, category, budget_category) in enumerate(DESTINATION_NAMES, start=1):
    lat, lng = COORDINATES.get(name, (20.5937, 78.9629))
    dest_id = destination_id(name)
    image = DESTINATION_IMAGES.get(name, DEFAULT_IMAGE)
    official = tourism_url(name)
    DESTINATIONS.append({
        "_id": dest_id,
        "name": name,
        "state": state,
        "category": category,
        "budgetCategory": budget_category,
        "description": destination_description(name, state, category),
        "imageUrl": image,
        "latitude": lat,
        "longitude": lng,
        "officialWebsite": official,
        "googleMapsUrl": maps_url(name),
        "slug": slugify(name),
        "rating": round(4.1 + (index % 8) * 0.1, 1),
        "interests": [category, budget_category, "Culture" if "Heritage" in category or "Temple" in category else "Nature"]
    })

    budget_base = 1800 if budget_category == "Budget" else 3200
    mid_base = budget_base + 1800
    resort_base = budget_base + 3000
    budget_hotel_name, budget_hotel_url = verified_listing(
        name, "hotel_budget", f"Official Hotels in {name}", official
    )
    premium_hotel_name, premium_hotel_url = verified_listing(
        name, "hotel_premium", f"Official Premium Stays in {name}", official
    )
    resort_name, resort_url = verified_listing(
        name, "resort", f"Official Resorts in {name}", official
    )
    restaurant_name, restaurant_url = verified_listing(
        name, "restaurant", f"Official Restaurants in {name}", official
    )
    budget_booking = booking_platform_details(name, budget_hotel_name, "hotel", index)
    standard_booking = booking_platform_details(name, premium_hotel_name, "hotel", index + 1)
    high_class_booking = booking_platform_details(name, resort_name, "hotel", index + 2)
    restaurant_booking = booking_platform_details(name, restaurant_name, "restaurant", index)
    signature_booking = booking_platform_details(name, f"{name} Signature Experience", "attraction", index)
    guided_booking = booking_platform_details(name, f"{name} Guided Local Tour", "attraction", index + 1)
    HOTELS.extend([
        {
            "_id": f"hotel-{slugify(name)}-budget",
            "destinationId": dest_id,
            "name": budget_hotel_name,
            "bookingTier": "Budget",
            "rating": round(4.0 + (index % 6) * 0.1, 1),
            "pricePerNight": budget_base,
            "imageUrl": photo_url(budget_hotel_name, "hotel exterior room"),
            "officialWebsite": budget_hotel_url,
            **budget_booking,
            "address": f"Central {name}, {state}",
            "facilities": ["Budget Friendly", budget_booking["bookingProvider"], "WiFi", "Breakfast"],
            "distanceKm": round(1.2 + (index % 5) * 0.7, 1)
        },
        {
            "_id": f"hotel-{slugify(name)}-premium",
            "destinationId": dest_id,
            "name": premium_hotel_name,
            "bookingTier": "Standard",
            "rating": round(4.3 + (index % 5) * 0.1, 1),
            "pricePerNight": mid_base,
            "imageUrl": photo_url(premium_hotel_name, "hotel exterior lobby"),
            "officialWebsite": premium_hotel_url,
            **standard_booking,
            "address": f"Prime Tourism Zone, {name}, {state}",
            "facilities": ["Standard Option", standard_booking["bookingProvider"], "Restaurant", "Concierge"],
            "distanceKm": round(2.0 + (index % 4) * 0.9, 1)
        }
    ])
    RESORTS.append({
        "_id": f"resort-{slugify(name)}-nature",
        "destinationId": dest_id,
        "name": resort_name,
        "bookingTier": "High-Class",
        "rating": round(4.2 + (index % 6) * 0.1, 1),
        "pricePerNight": resort_base,
        "imageUrl": photo_url(resort_name, "resort exterior pool"),
        "officialWebsite": resort_url,
        **high_class_booking,
        "address": f"Scenic Belt, {name}, {state}",
        "facilities": ["High-Class", high_class_booking["bookingProvider"], "Pool", "Travel Desk"],
        "distanceKm": round(3.0 + (index % 6) * 1.1, 1)
    })
    RESTAURANTS.append({
        "_id": f"restaurant-{slugify(name)}-local",
        "destinationId": dest_id,
        "name": restaurant_name,
        "bookingTier": ["Budget", "Standard", "High-Class"][index % 3],
        "rating": round(4.0 + (index % 7) * 0.1, 1),
        "priceForTwo": 500 + (index % 8) * 250,
        "imageUrl": photo_url(restaurant_name, "restaurant dining food"),
        "officialWebsite": restaurant_url,
        **restaurant_booking,
        "address": f"Market Road, {name}, {state}",
        "facilities": [["Budget Friendly", "Standard Option", "High-Class"][index % 3], restaurant_booking["bookingProvider"], "Local Cuisine", "Family Friendly"],
        "openingHours": "8:00 AM - 10:30 PM",
        "distanceKm": round(0.8 + (index % 5) * 0.6, 1)
    })
    ATTRACTIONS.extend([
        {
            "_id": f"attraction-{slugify(name)}-signature",
            "destinationId": dest_id,
            "name": f"{name} Signature Experience",
            "bookingTier": "Standard",
            "category": category,
            "description": f"A must-visit {category.lower()} experience in {name}, suitable for day-wise AI itinerary planning.",
            "entryFee": 0 if budget_category == "Budget" else 250,
            **signature_booking,
            "officialWebsite": official,
            "imageUrl": image,
            "rating": round(4.2 + (index % 6) * 0.1, 1),
            "distanceKm": round(1.0 + (index % 7) * 0.8, 1)
        },
        {
            "_id": f"attraction-{slugify(name)}-guided",
            "destinationId": dest_id,
            "name": f"{name} Guided Local Tour",
            "bookingTier": "High-Class",
            "category": "Guided Tour",
            "description": f"Local guided route covering culture, food, viewpoints, and practical navigation around {name}.",
            "entryFee": 499 + (index % 6) * 250,
            **guided_booking,
            "officialWebsite": official,
            "imageUrl": photo_url(name, "tourism guided tour"),
            "rating": round(4.0 + (index % 7) * 0.1, 1),
            "distanceKm": round(1.4 + (index % 5) * 0.9, 1)
        }
    ])


NOTIFICATIONS = [
    {"id": "notif-1", "userId": "system", "type": "Safety", "title": "Check route and weather", "message": "Confirm weather, road, and local advisories before long transfers or late-evening travel."},
    {"id": "notif-2", "userId": "system", "type": "Booking Reminder", "title": "Book on official provider sites", "message": "All Tourism Assistant redirects bookings to verified provider websites and does not process payments."},
    {"id": "notif-3", "userId": "system", "type": "Recommendation", "title": "Plan popular slots early", "message": "Reserve high-demand attractions, restaurants, and stays ahead of peak travel windows."}
]

SAFETY = {
    "emergency": [
        {"title": "India Emergency Response", "phone": "112"},
        {"title": "Ambulance", "phone": "108"},
        {"title": "Women Helpline", "phone": "1091"}
    ],
    "alerts": [
        {"title": "Weather Advisory", "description": "Check local weather before beaches, islands, mountain roads, forests, and cave routes."},
        {"title": "Official Booking Guidance", "description": "Use provider websites for bookings and avoid sharing payment details inside unofficial chats."}
    ],
    "safeAreas": [
        {"title": "Stay central", "description": "Choose well-reviewed accommodation near central tourism zones or transport corridors."},
        {"title": "Late arrival", "description": "Use official taxis, hotel pickups, and well-lit pickup points when arriving late."}
    ],
    "nearbyHelp": [
        {"name": "Nearby hospitals", "address": "Use the map panel to locate hospitals near your current destination."},
        {"name": "Nearby police stations", "address": "Use Google Maps navigation and call 112 in an emergency."}
    ]
}

COLLECTIONS = {
    "destinations": DESTINATIONS,
    "hotels": HOTELS,
    "resorts": RESORTS,
    "restaurants": RESTAURANTS,
    "attractions": ATTRACTIONS,
    "notifications": NOTIFICATIONS,
    "users": [],
    "trips": [],
    "chatbot_history": []
}
