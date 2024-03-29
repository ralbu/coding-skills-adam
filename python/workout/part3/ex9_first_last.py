# Ex 1
def first_last(sequence):
    pass


def test_first_last_list():
    assert first_last([1, 2, 3, 4, 5]) == [1, 5]


def test_first_last_tuple():
    assert first_last((1, 2, 3, 4, 5)) == (1, 5)


def test_first_last_string():
    assert first_last("abcde") == 'ae'


# Ex 2
def even_odd_sums(sequence):
    pass


def test_even_odd_sums():
    assert even_odd_sums([1, 2, 3, 4, 5]) == (9, 6)
    assert even_odd_sums((1, 2, 3, 4, 5, 6)) == (9, 12)


# Ex 3
def plus_minus(sequence):
    pass


def test_plus_minus():
    # 10 + 20 - 30 + 40 - 50 + 60
    assert plus_minus([10, 20, 30, 40, 50, 60]) == 50
    assert plus_minus((10, 20, 30, 40, 50, 60)) == 50


# Ex 4
def custom_zip(list1, list2):
    pass


def test_custom_zip():
    list1 = [10, 20, 30]
    list2 = "abc"

    result = custom_zip_mine(list1, list2)
    assert result[0] == (10, "a")


# Ex 5
def custom_zip_any_parameters(*args):
    pass


def test_custom_zip_any_parameters():
    p1 = [10, 20, 30, 40]
    p2 = "ab"
    p3 = [1, 2, 3, 4, 5]

    result = custom_zip_any_parameters_ai(p1, p2, p3)
    assert result == [(10, 'a', 1), (20, 'b', 2)]
