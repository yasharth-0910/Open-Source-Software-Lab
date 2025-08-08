from collections import Counter

def most_repetitive_word(file_path):
    with open(file_path, 'r') as f:
        words = f.read().split()
    return Counter(words).most_common(1)[0]


print(most_repetitive_word("file1.txt"))