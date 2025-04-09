from collections import Counter


def most_repeating_letter_count(word: str) -> int:
    pass


def most_repeating_word(words):
    pass


def test_one_word():
    result = most_repeating_word(["hello", "world"])
    assert result == ["hello"]


def test_word_banana():
    result = most_repeating_word(["hellow", "banana"])
    assert result == ["banana"]


def test_words():
    result = most_repeating_word(["hello", "world", "python", "programming"])
    assert result == ["hello", "programming"]
