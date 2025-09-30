def get_num_words(path):
    with open(path) as f:
        string = f.read()
    words_list = string.lower().split()
    num_words = len(words_list)

    print(f"Found {num_words} total words")

    return words_list