from pathlib import Path


def word_count(file_name):

    return {
        "characters": 0,
        "words": 0,
        "lines": 0,
        "unique_words": 0
    }

def test_word_count():
    file_name = Path(__file__).parent / "ex20.txt"

    result = word_count(file_name)

    assert result["characters"] == 253
    assert result["words"] == 40
    assert result["lines"] == 7
    assert result["unique_words"] == 33
