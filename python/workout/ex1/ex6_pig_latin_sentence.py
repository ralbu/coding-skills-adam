from ex5_pig_latin import to_pig_latin

sentence = input("Enter a sentence to convert to pig latin (only letters): ")
split_sentence = sentence.split()
translated_sentence = []

for word in split_sentence:
    translated_sentence.append(to_pig_latin(word))

translated_sentence = ' '.join(translated_sentence)

print(translated_sentence)