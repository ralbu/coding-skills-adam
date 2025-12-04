from collections import Counter


def most_repeating_letter_count(word: str) -> int:
    c = Counter(word)

    return c.most_common(1)[0][1]


def most_repeating_word_single(words: list[str]) -> list[str]:
    most_letters = max(words, key=most_repeating_letter_count)
    print(most_letters)


def most_repeating_word_adam(words: list[str]) -> list[str]:
    # Store each letter count of each word
    repeating_letters_words = {}

    for word in words:
        repeating_letters = most_repeating_letter_count(word)
        repeating_letters_words[word] = repeating_letters

    # Determine which one is most common
    most_letters = max(repeating_letters_words.values())
    most_repeating_letters_words = []

    for word in repeating_letters_words:
        if repeating_letters_words[word] == most_letters:
            most_repeating_letters_words.append(word)
    return most_repeating_letters_words


def most_repeating_word(words: list[str]):
    max_letters = max([most_repeating_letter_count(word) for word in words])

    # return [word for word in words if most_repeating_letter_count(word) == max_letters]

    return list(
        filter(lambda word: most_repeating_letter_count(word) == max_letters, words)
    )


def test_one_word():
    result = most_repeating_word(["hello", "world"])
    assert result == ["hello"]


def test_word_banana():
    result = most_repeating_word(["hellow", "banana"])
    assert result == ["banana"]


def test_words():
    result = most_repeating_word(["hello", "world", "python", "programming"])
    assert result == ["hello", "programming"]
