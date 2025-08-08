from itertools import product

def letter_combinations(digits, string_maps):
    return [''.join(p) for p in product(*(string_maps[d] for d in digits))]

# Example
string_maps = {
    "1": "abc", "2": "def", "3": "ghi", "4": "jkl",
    "5": "mno", "6": "pqrs", "7": "tuv", "8": "wxy", "9": "z"
}
print(letter_combinations("12", string_maps)) 