def remove_parenthesis_area(data):
    return [s.split('(')[0].strip() for s in data]

# Example
data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
print(remove_parenthesis_area(data))  