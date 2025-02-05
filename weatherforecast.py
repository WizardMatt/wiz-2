import requests  # Import requests module to make API calls

# OpenWeatherMap API Key (Replace with your actual API key)
API_KEY = "ab101772809b76c6860c243ce2f78de8"  # Get a free API key from https://openweathermap.org/api
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Base URL for the weather API

# Ask the user for a city name
city = input("Enter city name: ")

# Make an API request to get weather data for the entered city
response = requests.get(f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")

# Check if the API request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Convert the response to JSON format
    
    # Extract and display weather details
    weather_description = data['weather'][0]['description']  # Get weather condition (e.g., Clear, Rain)
    temperature = data['main']['temp']  # Get temperature in Celsius

    print(f"🌤 Weather in {city}: {weather_description.capitalize()}")
    print(f"🌡 Temperature: {temperature}°C")

else:
    # Handle cases where the city is not found or there's an API error
    print("❌ City not found or API error! Please check the city name.")
