def find_n_largest(lst, n):
    return sorted(lst, reverse=True)[:n]

# Example
lst = [4, 1, 7, 3, 8, 5]
print(find_n_largest(lst, 3)) 