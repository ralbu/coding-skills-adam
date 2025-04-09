import operator

PEOPLE = [
    {"first": "Will", "last": "Feinman"},
    {"first": "Richard", "last": "Feinman"},
    {"first": "Alan", "last": "Turing"},
    {"first": "Ada", "last": "Lovelace"},
    {"first": "Grace", "last": "Hopper"},
    {"first": "Claude", "last": "Shannon"},
    {"first": "Tim", "last": "Berners-Lee"},
]


def alphabetize_names_lambda(dict):
    pass


def alphabetize_names_itemgetter(dict):
    pass


def test_alphabetize_names_lambda():
    result = alphabetize_names_lambda(PEOPLE)
    assert result[0] == {"first": "Tim", "last": "Berners-Lee"}
    assert result[1] == {"first": "Richard", "last": "Feinman"}
    assert result[2] == {"first": "Will", "last": "Feinman"}
    assert result[3] == {"first": "Grace", "last": "Hopper"}
    assert result[4] == {"first": "Ada", "last": "Lovelace"}
    assert result[5] == {"first": "Claude", "last": "Shannon"}
    assert result[6] == {"first": "Alan", "last": "Turing"}


def test_alphabetize_names_itemgetter():
    result = alphabetize_names_lambda(PEOPLE)
    assert result[0] == {"first": "Tim", "last": "Berners-Lee"}
    assert result[1] == {"first": "Richard", "last": "Feinman"}
    assert result[2] == {"first": "Will", "last": "Feinman"}
    assert result[3] == {"first": "Grace", "last": "Hopper"}
    assert result[4] == {"first": "Ada", "last": "Lovelace"}
    assert result[5] == {"first": "Claude", "last": "Shannon"}
    assert result[6] == {"first": "Alan", "last": "Turing"}
