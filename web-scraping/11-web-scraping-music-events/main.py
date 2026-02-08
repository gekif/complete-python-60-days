from config import URL
import requests
import selectorlib

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

if __name__ == "__main__":
    print(scrape(URL))

