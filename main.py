from stats import get_num_words
dicktschneri = dict()
for word in get_num_words("books/frankenstein.txt"):
    for char in word:
        dicktschneri[char] = dicktschneri.get(char, 0) + 1
print(dicktschneri)