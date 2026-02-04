import pytest
from core.hebrew import (
    strip_niqqud,
    normalize_letter,
    normalize_text_edges,
    first_last_letters,
)


def test_strip_niqqud_simple():
    assert strip_niqqud("בְּרֵאשִׁית") == "בראשית"


def test_strip_niqqud_sentence():
    assert strip_niqqud("וַיֹּאמֶר אֱלֹהִים") == "ויאמר אלהים"


def test_normalize_letter_regular():
    assert normalize_letter("מ") == "מ"


def test_normalize_letter_final():
    assert normalize_letter("ך") == "כ"
    assert normalize_letter("ץ") == "צ"


def test_first_last_letters_simple():
    assert first_last_letters("נועה") == ("נ", "ה")


def test_first_last_letters_with_niqqud():
    assert first_last_letters("נֹעָה") == ("נ", "ה")


def test_first_last_letters_with_spaces():
    assert first_last_letters(" אֵ לִ י ") == ("א", "י")


def test_first_last_letters_empty():
    with pytest.raises(ValueError):
        first_last_letters("   ")


def test_normalize_text_edges():
    first, last = normalize_text_edges("נ", "ך")
    assert first == "נ"
    assert last == "כ"
