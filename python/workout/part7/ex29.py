def sum_numbers(text):

    return text


def test_sum_numbers():
    to_test = "10 abc 20 de44 30 55fg 40"
    sums = sum_numbers(to_test)
    assert sums == 100
