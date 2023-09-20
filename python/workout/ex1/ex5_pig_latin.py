def to_pig_latin(word):
    vowels = ['a', 'i', 'e', 'o', 'u']
    if word[0] in vowels:
        word += 'way'
    else:
        word = word[1:] + word[0] + 'ay'
    return word