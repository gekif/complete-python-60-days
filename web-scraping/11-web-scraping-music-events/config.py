import os
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
SENDER = "dzulfikar.maulana@gmail.com"
RECEIVER = "dzulfikar.maulana@gmail.com"
PASSWORD = "jyoz gsqo neag saii"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data.db")

CONNECTION = sqlite3.connect(DB_PATH)
