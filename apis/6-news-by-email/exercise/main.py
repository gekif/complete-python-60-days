import requests
from config import API_KEY
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      f"{API_KEY}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")

try:
    send_email(message=body)
    print("Email sent successfully.")
except Exception as e:
    print("Failed to send email:", e)