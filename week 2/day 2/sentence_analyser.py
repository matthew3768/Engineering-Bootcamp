sentence  = input('Please enter a sentence: ')

sentence_joined = sentence.strip()
sentence_characters = len(sentence_joined)
print(sentence_characters)

sentence_split = len(sentence.split())
print(sentence_split)


vowels = 0
v = {'a','e','i','o','u'}
for character in sentence:
    if character in v:
        vowels += 1
print(vowels)
