import requests  # Import requests module to make API calls

# API Endpoint for ISS location
ISS_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_location():
    """
    Fetches the real-time latitude and longitude of the International Space Station (ISS).
    
    Returns:
    - Dictionary containing latitude, longitude, and Google Maps link.
    """
    response = requests.get(ISS_URL)  # Make API request
    
    if response.status_code == 200:  # If request is successful
        data = response.json()  # Convert response to JSON
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"

        return {"latitude": latitude, "longitude": longitude, "maps_link": google_maps_link}
    else:
        return None

# Fetch and display ISS location
iss_location = get_iss_location()

if iss_location:
    print("\n🛰️ Current Location of the International Space Station:")
    print(f"🌍 Latitude: {iss_location['latitude']}")
    print(f"🌍 Longitude: {iss_location['longitude']}")
    print(f"📍 View on Google Maps: {iss_location['maps_link']}")
else:
    print("❌ Error fetching ISS location. Check your internet connection!")
