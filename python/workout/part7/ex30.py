def flatten(list_to_flatten):
    return None


def test_flatten():
    list_to_flatten = [[1,2], [3,4]]
    result = flatten(list_to_flatten)
    assert result == [1, 2, 3, 4]
