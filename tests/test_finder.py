import pytest
from core.finder import VerseFinder

FAKE_VERSES = [
    {
        "book": "Genesis",
        "chapter": 1,
        "verse": 1,
        "text": "בְּרֵאשִׁית בָּרָא"
    },
    {
        "book": "Genesis",
        "chapter": 1,
        "verse": 2,
        "text": "אֵלֶּה תּוֹלְדוֹת"
    },
    {
        "book": "Exodus",
        "chapter": 3,
        "verse": 5,
        "text": "שְׁלַח נַעֲלֶיךָ"
    },
    {
        "book": "Psalms",
        "chapter": 23,
        "verse": 1,
        "text": "מִזְמוֹר לְדָוִד"
    },
    {
        "book": "Psalms",
        "chapter": 37,
        "verse": 25,
        "text": "נַ֤עַר הָיִ֗יתִי גַּם זָ֫קַ֥נְתִּי וְֽלֹא רָ֭אִיתִי צַדִּ֣יק נֶעֱזָ֑ב וְ֝זַרְע֗וֹ מְבַקֶּשׁ לָֽחֶם"
    },
]


def test_find_name():
    finder = VerseFinder(FAKE_VERSES)
    results = finder.find("נועם")  # ת…ת
    assert len(results) >= 1


def test_index_created():
    finder = VerseFinder(FAKE_VERSES)
    assert len(finder.index) > 0


def test_find_by_name():
    finder = VerseFinder(FAKE_VERSES)

    results = finder.find("ברא")  # ב…א
    assert len(results) == 1
    assert results[0]["book"] == "Genesis"


def test_find_with_book_filter():
    finder = VerseFinder(FAKE_VERSES)

    results = finder.find("ברא", book_name="Genesis")
    assert len(results) == 1

    results = finder.find("ברא", book_name="Exodus")
    assert results == []


def test_find_limit():
    finder = VerseFinder(FAKE_VERSES)

    results = finder.find("ברא", limit=1)
    assert len(results) == 1
