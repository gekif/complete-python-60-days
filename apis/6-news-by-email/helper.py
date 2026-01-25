import base64
import datetime

def encrypt(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decrypt(cipher: str) -> str:
    return base64.b64decode(cipher.encode()).decode()

def today(fmt: str = "%d %B %Y") -> str:
    """Return today's date formatted (default: 'January 25, 2026')."""
    return datetime.date.today().strftime(fmt)