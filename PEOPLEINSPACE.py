import requests  # Import requests module to make API calls

# API Endpoint for people in space
ASTRONAUTS_URL = "http://api.open-notify.org/astros.json"

def get_people_in_space():
    """
    Fetches the number of astronauts currently in space along with their names and spacecraft.
    
    Returns:
    - Dictionary containing count and a list of astronauts.
    """
    response = requests.get(ASTRONAUTS_URL)  # Make API request
    
    if response.status_code == 200:  # If request is successful
        data = response.json()  # Convert response to JSON
        return {"count": data["number"], "astronauts": data["people"]}
    else:
        return None

# Fetch and display astronauts in space
people_in_space = get_people_in_space()

if people_in_space:
    print(f"\n👨‍🚀 Currently, there are {people_in_space['count']} astronauts in space:\n")
    for astronaut in people_in_space['astronauts']:
        print(f"🔹 {astronaut['name']} - 🚀 {astronaut['craft']}")
else:
    print("❌ Error fetching astronaut data. Check your internet connection!")
