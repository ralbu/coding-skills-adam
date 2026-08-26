def dictdiff(first: dict[str, int], second: dict[str, int]) -> dict:
    all_keys = first.keys() | second.keys()

    differences = {}

    for key in all_keys:
        if first.get(key) != second.get(key):
            differences[key] = [first.get(key), second.get(key)]


    return differences

def test_the_same_data():
    d = {'a': 1, 'b': 2, 'c': 3}

    assert dictdiff(d, d) == {}


def test_both_dict_have_same_keys_different_values():
    first = {'a': 1, 'b': 2, 'c': 3}
    second = {'a': 1, 'b': 2, 'c': 4}

    assert dictdiff(first, second) == {'c': [3, 4]}


def test_both_dict_have_different_keys():
    first = {'a': 1, 'b': 2, 'd': 3}
    second = {'a': 1, 'b': 2, 'c': 4}

    assert dictdiff(first, second) == {'c': [None, 4], 'd': [3, None]}
