import requests
from config import API_KEY
from send_email import send_email
from helper import today

topic = "Tesla"
language = "en"

url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={API_KEY}&" \
      f"language={language}"


# Make request
request = requests.get(url)


# Set a dictionary with data
content = request.json()


# ===== SUBJECT (HANYA SEKALI) =====
subject = f"Subject: Today's News on {topic} - {today()}"

# ===== BODY =====
body = ""


for article in content["articles"][:20]:
    if article["title"]:
        body += (
            f"Title: {article['title']}\n"
            f"{article['description']}\n"
            f"Link: {article['url']}\n\n"
        )

# RFC 5322 → header + blank line + body
email_message = f"{subject}\n\n{body}".encode("utf-8")


try:
    send_email(subject=subject, body=body)
    print("Email sent successfully.")
except Exception as e:
    print("Failed to send email:", e)