def how_many_different_numbers(numbers: list[int]):
    return len(set(numbers))

def test_how_many_different_numbers():
    numbers = [1, 2, 3, 1, 1, 3, 4, 1, 3, 4]

    assert how_many_different_numbers(numbers) == 4
