from load_csv import load

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    print(load("../csv_files/life_expectancy_years.csv"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

try:
    print(load(123))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b - Invalid path parameter: empty string
print("Test 2b - Invalid path parameter: empty string")

try:
    print(load(""))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3 - Invalid path parameter: invalid CSV format
print("Test 3 - Invalid path parameter: invalid CSV format")

try:
    print(load("invalid.txt"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4 - Invalid path parameter: file not found
print("Test 4 - Invalid path parameter: file not found")

try:
    print(load("nonexistent.csv"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5 - Invalid path parameter: file is not a file
print("Test 5 - Invalid path parameter: file is not a file")

try:
    print(load("../csv_files/"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6 - Invalid path parameter: file is empty
print("Test 6 - Invalid path parameter: file is empty")

try:
    print(load("../csv_files/empty.csv"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7 - Invalid path parameter: ParserError
print("Test 7 - Invalid path parameter: ParserError")

try:
    print(load("../csv_files/parser_error.csv"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8 - Invalid path parameter: PermissionError
print("Test 8 - Invalid path parameter: PermissionError")

try:
    print(load("../csv_files/permission_error.csv"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
