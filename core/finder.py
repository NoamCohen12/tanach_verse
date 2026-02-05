import json
import re
from pathlib import Path
from core.hebrew import strip_niqqud, first_last_letters, normalize_text_edges

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tanach_clean.json"
HEBREW_LETTERS = r"\u0590-\u05FF"


class VerseFinder:
    def __init__(self, verses: list | None = None):
        if verses is None:
            with DATA_FILE.open(encoding="utf-8") as f:
                self.verses = json.load(f)
        else:
            self.verses = verses

        self.index = self._build_index()

    def _build_index(self) -> dict:
        index = {}

        for v in self.verses:
            text = strip_niqqud(v["text"]).replace(" ", "")
            if not text:
                continue

            first, last = first_last_letters(text)
            first, last = normalize_text_edges(first, last)
            key = (first, last)
            index.setdefault(key, []).append(v)

        return index

    def find(self, name: str, book_name: str | None = None, limit: int = 100):
        first, last = first_last_letters(name)
        first, last = normalize_text_edges(first, last)

        results = self.index.get((first, last), [])

        if book_name:
            results = [v for v in results if v["book"] == book_name]

        return results[:limit]

    def find_contains(self, name: str, book_name: str | None = None, limit: int = 100):
        name_clean = strip_niqqud(name)

        # regex: מילה שלמה בעברית
        pattern = re.compile(
            rf'(^|[^{HEBREW_LETTERS}]){re.escape(name_clean)}([^{HEBREW_LETTERS}]|$)'
        )

        results = []
        for v in self.verses:
            verse_text = strip_niqqud(v["text"])

            if pattern.search(verse_text):
                results.append(v)

        if book_name:
            results = [v for v in results if v["book"] == book_name]

        return results[:limit]
