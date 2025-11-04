from load_csv import load

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

print(load("../csv_files/valid_csv/life_expectancy_years.csv"))

print("\n--------------------------------\n")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

print(load(123))

print("\n--------------------------------\n")

# Test 2b - Invalid path parameter: empty string
print("Test 2b - Invalid path parameter: empty string")

print(load(""))

print("\n--------------------------------\n")

# Test 3a - Invalid path parameter: invalid CSV format
print("Test 3a - Invalid path parameter: invalid CSV format")

print(load("../csv_files/invalid_csv/invalid_format.txt"))

print("\n--------------------------------\n")

# Test 3b - Invalid path parameter: invalid CSV format
print("Test 3b - Invalid path parameter: invalid CSV format")

print(load("../csv_files/invalid_csv/subject.pdf"))

print("\n--------------------------------\n")

# Test 4 - Invalid path parameter: file not found
print("Test 4 - Invalid path parameter: file not found")

print(load("../csv_files/invalid_csv/nonexistent.csv"))

print("\n--------------------------------\n")

# Test 5 - Invalid path parameter: file is a directory
print("Test 5 - Invalid path parameter: file is a directory")

print(load("../csv_files/"))

print("\n--------------------------------\n")

# Test 6 - Invalid path parameter: file is empty
print("Test 6 - Invalid path parameter: file is empty")

print(load("../csv_files/invalid_csv/empty.csv"))

print("\n--------------------------------\n")

# Test 7 - Invalid path parameter: ParserError
print("Test 7 - Invalid path parameter: ParserError")

print(load("../csv_files/invalid_csv/parser_error.csv"))

print("\n--------------------------------\n")

# Test 8 - Invalid path parameter: PermissionError
print("Test 8 - Invalid path parameter: PermissionError")

print(load("../csv_files/invalid_csv/permission_error.csv"))

print("\n--------------------------------\n")
