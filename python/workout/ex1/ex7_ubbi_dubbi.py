vowels = ['a', 'e', 'i', 'o', 'u']


def ubbi_dubbi_word(word):
    # ub before vowels
    translated_word = []
    for character in word:
        if character in vowels:
            translated_word.append('ub' + character)
        else:
            translated_word.append(character)

    translated_word = ''.join(translated_word)
    return translated_word


def ubbi_dubbi_sentence(sentence):
    split_sentence = sentence.split()
    translated_sentence = []

    for word in split_sentence:
        translated_sentence.append(ubbi_dubbi_word(word))

    translated_sentence = ' '.join(translated_sentence)

    return translated_sentence
