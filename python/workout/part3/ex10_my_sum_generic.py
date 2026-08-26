def my_sum_generic(*args):
    return () if len(args) == 0 else "".join(args) if all(type(arg) == str for arg in args) else sum(args) if all(type(arg) == int for arg in args) else None


def test_my_sum_int():
    assert my_sum_generic(1, 2, 3, 4) == 10


def test_my_sum_string():
    assert my_sum_generic("a", "b", "c") == "abc"


def test_my_sum_no_arguments():
    assert my_sum_generic() == ()

