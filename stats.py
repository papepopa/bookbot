def get_num_words(path):
    with open(path) as f:
        string = f.read()

    words_list = string.lower().split()
    return words_list