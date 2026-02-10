import time
from config import URL, HEADERS, CONNECTION
import requests
import selectorlib
from send_email import Email


HEADERS
CONNECTION


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value

def store(extracted):
   row = extracted.split(",")
   row = [item.strip() for item in row]
   cursor = CONNECTION.cursor()
   cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
   CONNECTION.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = CONNECTION.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    return rows

def init_db():
    cursor = CONNECTION.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            band TEXT,
            city TEXT,
            date TEXT
        )
    """)
    CONNECTION.commit()


if __name__ == "__main__":

    init_db()

    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                email = Email()
                email.send(message="Hey, new event was found")

        time.sleep(2)

