from twttr import shorten


def test_default():
    assert shorten() == "wrld"


def test_vogals_only():
    assert shorten("Oia") == ""


def test_normal():
    assert shorten("AbcdeF") == "bcdF"


def test_consonants_only():
    assert shorten("qwrt") == "qwrt"


def test_uppercase():
    assert shorten("ABCDE") == "BCD"


def test_lowercase():
    assert shorten("abcde") == "bcd"


def test_with_numbers_and_ponctuation():
    assert shorten("!Oi1") == "!1"
