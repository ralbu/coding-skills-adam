def my_sum_generic(*args):
    if len(args) == 0:
        return ()
    elif all(type(arg) == str for arg in args):
        return "".join(args)
    elif all(type(arg) == int for arg in args):
        return sum(args)


def test_my_sum_int():
    assert my_sum_generic(1, 2, 3, 4) == 10


def test_my_sum_string():
    assert my_sum_generic("a", "b", "c") == "abc"


def test_my_sum_no_arguments():
    assert my_sum_generic() == ()

