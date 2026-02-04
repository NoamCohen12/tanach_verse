from scripts.hebraize_tanach_data import number_to_hebrew


def test_number_to_hebrew_basic():
    assert number_to_hebrew(15) == "טו"
    assert number_to_hebrew(16) == "טז"
    assert number_to_hebrew(25) == "כה"


def test_number_to_hebrew_hundreds():
    assert number_to_hebrew(101) == "קא"
    assert number_to_hebrew(115) == "קטו"
    assert number_to_hebrew(116) == "קטז"