def double_integers(input_str):
    return [int(x) * 2 for x in input_str.split(',')]

# Example
print(double_integers("123, 456, 222, 145"))  
print(double_integers("-1, 0, -2, 2, 0, 1")) 