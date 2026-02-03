import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "tanach.json"
OUTPUT_FILE = BASE_DIR / "data" / "tanach_clean.json"


HTML_TAG_RE = re.compile(r"<[^>]+>")
NBSP_RE = re.compile(r"&nbsp;")
PARASHA_RE = re.compile(r"\{[פס]\}")

def clean_text(text: str) -> str:
    text = HTML_TAG_RE.sub("", text)
    text = NBSP_RE.sub(" ", text)
    text = PARASHA_RE.sub("", text)
    return text.strip()

def main():
    with INPUT_FILE.open(encoding="utf-8") as f:
        verses = json.load(f)

    cleaned = []
    removed_tags = 0

    for v in verses:
        original = v["text"]
        cleaned_text = clean_text(v["text"])

        if original != cleaned_text:
            removed_tags += 1

        cleaned.append({
            "book": v["book"],
            "chapter": v["chapter"],
            "verse": v["verse"],
            "text": cleaned_text
        })

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print(f"✅ סיום")
    print(f"📦 פסוקים: {len(cleaned)}")
    print(f"🧹 פסוקים שנוקו מ־HTML: {removed_tags}")
    print(f"💾 נשמר ב־{OUTPUT_FILE}")

if __name__ == "__main__":
    main()
