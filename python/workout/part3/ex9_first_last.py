# Ex 1

def first_last(sequence):
    return [sequence[0], sequence[-1]] if type(sequence) == list else (sequence[0], sequence[-1]) if type(sequence) == tuple else str(sequence[0]) + str(sequence[-1]) if type(sequence) == str else None
        

def test_first_last_list():
    assert first_last([1, 2, 3, 4, 5]) == [1, 5]

def test_first_last_tuple():
    assert first_last((1, 2, 3, 4, 5)) == (1, 5)


def test_first_last_string():
    assert first_last("abcde") == 'ae'


# Ex 2
def even_odd_sums(sequence):
        return sum([num for num in sequence if num % 2 == 1]), sum([num for num in sequence if num % 2 == 0])


def test_even_odd_sums():
    assert even_odd_sums([1, 2, 3, 4, 5]) == (9, 6)
    assert even_odd_sums((1, 2, 3, 4, 5, 6)) == (9, 12)


# Ex 3
def plus_minus(sequence):
    return sum([num if i % 2 == 1 else -num for i, num in enumerate(sequence)]) + sequence[0] * 2


def test_plus_minus():
    # 10 + 20 - 30 + 40 - 50 + 60
    assert plus_minus([10, 20, 30, 40, 50, 60]) == 50
    assert plus_minus((10, 20, 30, 40, 50, 60)) == 50


# Ex 4
def custom_zip(list1, list2):
    return [(list1[i], list2[i]) for i in range(len(list1))]


def test_custom_zip():
    list1 = [10, 20, 30]
    list2 = "abc"

    result = custom_zip(list1, list2)
    assert result[0] == (10, "a")


# Ex 5
def custom_zip_any_parameters(*args):
    return [tuple(arg[i] for arg in args) for i in range(len(args[[len(i) for i in args].index(min([len(i) for i in args]))]))]


def test_custom_zip_any_parameters():
    p1 = [10, 20, 30, 40]
    p2 = "ab"
    p3 = [1, 2, 3, 4, 5]

    result = custom_zip_any_parameters(p1, p2, p3)
    assert result == [(10, 'a', 1), (20, 'b', 2)]