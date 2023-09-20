from python.workout.ex1.ex5_pig_latin import to_pig_latin


def test_a():
    assert to_pig_latin("apple") == "appleway"


def test_e():
    assert to_pig_latin("egg") == "eggway"


def test_i():
    assert to_pig_latin("ice") == "iceway"


def test_o():
    assert to_pig_latin("oak") == "oakway"


def test_u():
    assert to_pig_latin("umbrella") == "umbrellaway"


def test_b():
    assert to_pig_latin("banana") == "ananabay"


def test_c():
    assert to_pig_latin("cat") == "atcay"