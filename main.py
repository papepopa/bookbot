from stats import get_num_words
import sys

def sorter_num(item):
    return item["num"]

def sorter_char(item):
    return item["char"]
try:
    path = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
big_ass_string = get_num_words(path)

num_words = len(big_ass_string)

list_of_dicks = list()

dicktschneri = {}

for word in big_ass_string:
    for char in word:
        if char.isalpha():
            dicktschneri[char] = dicktschneri.get(char, 0) + 1

for dick in dicktschneri:
    num = dicktschneri[dick]
    list_of_dicks.append({"char": dick, "num": num})

list_of_dicks.sort(reverse=True, key=sorter_num)

print(
        "============ BOOKBOT ============"
)
print(
        f"Analyzing book found at {path}..."
)
print(
        "----------- Word Count ----------"
)
print(
        f"Found {num_words} total words"
)

print(
        "--------- Character Count -------"
)

for alpha in list_of_dicks:
    print(f"{sorter_char(alpha)}: {sorter_num(alpha)}")

print(
        "============= END ==============="
)