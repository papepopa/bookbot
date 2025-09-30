from stats import get_num_words

dicktschneri = {}

for word in get_num_words("books/frankenstein.txt"):

    for char in word:
        dicktschneri[char] = dicktschneri.get(char, 0) + 1

list_of_dicks = list()

def sorter(item):
    return item["num"]

for dick in dicktschneri:
    if dick.isalpha():
        num = dicktschneri[dick]
        list_of_dicks.append({"char": dick, "num": num})

list_of_dicks.sort(reverse=True, key=sorter)

print(
    "--------- Character Count -------"
)
