from ex7_ubbi_dubbi import ubbi_dubbi_word, ubbi_dubbi_sentence


def test_milk():
    result = ubbi_dubbi_word("milk")
    assert result == "mubilk"


def test_pig():
    assert ubbi_dubbi_word("pig") == "pubig"


def test_tree():
    assert ubbi_dubbi_word("tree") == "trubeube"


def test_umbrella():
    assert ubbi_dubbi_word("umbrella") == "ubumbrubelluba"


def test_python():
    assert ubbi_dubbi_word("python") == "pythubon"


def test_computer():
    assert ubbi_dubbi_word("computer") == "cubompubutuber"


def test_sentence_ex1():
    assert ubbi_dubbi_sentence("octopus sits in a tree") == "uboctubopubus subits ubin uba trubeube"
