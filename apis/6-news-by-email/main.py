import requests
from config import API_KEY

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}"

request = requests.get(url)
content = request.text
print(content)