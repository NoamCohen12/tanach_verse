import json
from pathlib import Path

# =========================
# Paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "tanach_clean.json"
OUTPUT_FILE = BASE_DIR / "data" / "tanach_clean.json"


# =========================
# Book names (EN → HE)
# =========================
BOOK_NAME_HE = {
    "Genesis": "בראשית",
    "Exodus": "שמות",
    "Leviticus": "ויקרא",
    "Numbers": "במדבר",
    "Deuteronomy": "דברים",

    "Joshua": "יהושע",
    "Judges": "שופטים",
    "Ruth": "רות",

    "I Samuel": "שמואל א",
    "II Samuel": "שמואל ב",

    "I Kings": "מלכים א",
    "II Kings": "מלכים ב",

    "Isaiah": "ישעיהו",
    "Jeremiah": "ירמיהו",
    "Ezekiel": "יחזקאל",

    "Hosea": "הושע",
    "Joel": "יואל",
    "Amos": "עמוס",
    "Obadiah": "עובדיה",
    "Jonah": "יונה",
    "Micah": "מיכה",
    "Nahum": "נחום",
    "Habakkuk": "חבקוק",
    "Zephaniah": "צפניה",
    "Haggai": "חגי",
    "Zechariah": "זכריה",
    "Malachi": "מלאכי",

    "Psalms": "תהילים",
    "Proverbs": "משלי",
    "Job": "איוב",

    "Song of Songs": "שיר השירים",
    "Lamentations": "איכה",
    "Ecclesiastes": "קהלת",
    "Esther": "אסתר",

    "Daniel": "דניאל",
    "Ezra": "עזרא",
    "Nehemiah": "נחמיה",

    "I Chronicles": "דברי הימים א",
    "II Chronicles": "דברי הימים ב",
}


# =========================
# Hebrew numbers (Gematria)
# =========================
HEBREW_NUMBERS = {
    1: "א", 2: "ב", 3: "ג", 4: "ד", 5: "ה",
    6: "ו", 7: "ז", 8: "ח", 9: "ט",
    10: "י", 20: "כ", 30: "ל", 40: "מ",
    50: "נ", 60: "ס", 70: "ע", 80: "פ",
    90: "צ", 100: "ק", 200: "ר", 300: "ש", 400: "ת",
}


def number_to_hebrew(n: int) -> str:
    if n <= 0:
        raise ValueError("number must be positive")

    result = ""

    # מאות
    for value in (400, 300, 200, 100):
        while n >= value:
            result += HEBREW_NUMBERS[value]
            n -= value

    # חריגים מסורתיים (ט״ו, ט״ז) – על השארית
    if n == 15:
        return result + "טו"
    if n == 16:
        return result + "טז"

    # עשרות
    for value in (90, 80, 70, 60, 50, 40, 30, 20, 10):
        while n >= value:
            result += HEBREW_NUMBERS[value]
            n -= value

    # יחידות
    for value in (9, 8, 7, 6, 5, 4, 3, 2, 1):
        if n == value:
            result += HEBREW_NUMBERS[value]
            break

    return result


# =========================
# Main
# =========================
def main():
    with INPUT_FILE.open(encoding="utf-8") as f:
        verses = json.load(f)

    output = []

    for v in verses:
        book_en = v["book"]
        chapter_num = v["chapter"]
        verse_num = v["verse"]

        book_he = BOOK_NAME_HE.get(book_en, book_en)
        chapter_he = number_to_hebrew(chapter_num)
        verse_he = number_to_hebrew(verse_num)

        output.append({
            "book": book_he,                 # ← שם ספר בעברית
            "chapter": chapter_he,           # ← פרק באותיות
            "verse": verse_he,               # ← פסוק באותיות
            "text": v["text"],               # ← טקסט הפסוק (כבר נקי)
            "ref": f"{book_he} {chapter_he},{verse_he}"
        })

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print("✅ הסתיים בהצלחה")
    print(f"📦 פסוקים: {len(output)}")
    print(f"💾 נשמר ב־{OUTPUT_FILE}")


if __name__ == "__main__":
    main()
