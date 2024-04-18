def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
        print("The total number of words in the file is:", num_words)