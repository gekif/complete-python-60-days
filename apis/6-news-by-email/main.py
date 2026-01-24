import requests
from config import API_KEY

url = "https://newsapi.org/v2/everything?q=tesla" \
      "&sortBy=publishedAt" \
      f"&apiKey={API_KEY}"

# Make request
request = requests.get(url)

# Set a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])