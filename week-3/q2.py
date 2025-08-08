def value_sort(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

# Example
d = {'a': 3, 'b': 1, 'c': 2}
print(value_sort(d)) 