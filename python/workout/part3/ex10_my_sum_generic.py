def my_sum_generic(*args):
    pass


def test_my_sum_int():
    assert my_sum_generic(1, 2, 3, 4) == 10


def test_my_sum_string():
    assert my_sum_generic("a", "b", "c") == "abc"


def test_my_sum_no_arguments():
    assert my_sum_generic() == ()

