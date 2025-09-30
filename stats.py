def get_num_words(path):
    with open(path) as f:
        string = f.read()
    words = string.lower().split()
    num_words = len(words)

    print(f"Found {num_words} total words")
    
    return words