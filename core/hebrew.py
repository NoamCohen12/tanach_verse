import unicodedata

FINAL_TO_REGULAR = {
    "ך": "כ",
    "ם": "מ",
    "ן": "נ",
    "ף": "פ",
    "ץ": "צ",
}


def normalize_letter(letter: str) -> str:
    return FINAL_TO_REGULAR.get(letter, letter)


def normalize_text_edges(first: str, last: str) -> tuple[str, str]:
    return normalize_letter(first), normalize_letter(last)


def strip_niqqud(text: str) -> str:
    return "".join(
        c for c in text
        if unicodedata.category(c) != "Mn"
    )


def first_last_letters(word: str) -> tuple:
    """Return the first and last letters of a Hebrew word."""
    clean_word = strip_niqqud(word)
    clean_word = clean_word.replace(" ", "")

    if not clean_word:
        raise ValueError("empty name")

    return clean_word[0], clean_word[-1]
