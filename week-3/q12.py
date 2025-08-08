def first_non_repeating_char(s):
    from collections import Counter
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

# Example
print(first_non_repeating_char("swiss")) 