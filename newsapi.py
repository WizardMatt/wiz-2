import requests  # Import requests module for API calls

# Replace with your NewsAPI key (Get one from https://newsapi.org/)
API_KEY = "9f87243491554f1cb1b47a13f4cb667d"  
BASE_URL = "https://newsapi.org/v2/top-headlines"  # API endpoint

def fetch_news(country="us", category="general"):
    """
    Fetches top news headlines from NewsAPI.
    
    Parameters:
    - country (str): Country code (default: 'us' for the United States)
    - category (str): News category (default: 'general')

    Returns:
    - List of news articles (headlines + descriptions)
    """
    params = {
        "apiKey": API_KEY,
        "country": country,  # Country code (e.g., 'us', 'in', 'gb', 'ca')
        "category": category,  # News category (e.g., 'business', 'sports', 'technology')
        "pageSize": 5  # Number of articles to fetch
    }

    response = requests.get(BASE_URL, params=params)  # Make API request

    if response.status_code == 200:  # If request is successful
        data = response.json()
        articles = data.get("articles", [])  # Extract articles
        return articles
    else:
        print("❌ Error fetching news! Check your API key and internet connection.")
        return None

# Function to display news
def display_news(articles):
    if not articles:
        print("No news articles available.")
        return

    print("\n📰 Latest News Headlines:\n")
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']}")  # Print headline
        print(f"   {article['description']}\n")  # Print brief description
        print(f"   🔗 Read more: {article['url']}\n")  # Print news link

# Ask user for country and category preference
country_code = input("Enter country code (e.g., us, in, gb, ca): ").strip().lower()
category = input("Enter news category (e.g., business, sports, technology): ").strip().lower()

# Fetch and display news
news_articles = fetch_news(country_code, category)
display_news(news_articles)
