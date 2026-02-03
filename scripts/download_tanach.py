import requests
import json
import time
from pathlib import Path
import re

HTML_TAG_RE = re.compile(r"<[^>]+>")
BASE_URL = "https://www.sefaria.org/api/texts"

BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth",
    "I Samuel", "II Samuel",
    "I Kings", "II Kings",
    "Isaiah", "Jeremiah", "Ezekiel",
    "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
    "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi",
    "Psalms", "Proverbs", "Job",
    "Song of Songs", "Lamentations", "Ecclesiastes", "Esther",
    "Daniel", "Ezra", "Nehemiah",
    "I Chronicles", "II Chronicles"
]

# יעד שמירה
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT_FILE = DATA_DIR / "tanach.json"

DATA_DIR.mkdir(exist_ok=True)

all_verses = []

for book in BOOKS:
    print(f"📘 {book}")
    chapter = 1

    while True:
        ref = f"{book}.{chapter}"
        url = f"{BASE_URL}/{ref}"

        r = requests.get(url, params={"lang": "he"}, timeout=20)
        if r.status_code != 200:
            break

        data = r.json()
        verses = data.get("he")

        if not verses:
            break

        for i, verse in enumerate(verses, start=1):
            verse = HTML_TAG_RE.sub("", verse).strip()
            if verse:
                all_verses.append({
                    "book": book,
                    "chapter": chapter,
                    "verse": i,
                    "text": verse
                })

        chapter += 1
        time.sleep(0.1)  # להיות מנומס ל־API

print(f"\n✅ סה״כ פסוקים: {len(all_verses)}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_verses, f, ensure_ascii=False, indent=2)

print(f"📦 הקובץ נשמר ב־{OUTPUT_FILE}")
