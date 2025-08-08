def extract_characters(file_list):
    result = []
    for file in file_list:
        with open(file, 'r') as f:
            result.extend(list(f.read()))
    return result

print(extract_characters(["file1.txt", "file2.txt"]))