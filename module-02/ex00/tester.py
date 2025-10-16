from load_csv import load

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

result = load("../csv_files/life_expectancy_years.csv")
print(result)
if result is not None:
    print("✅ Test 1 passed: Valid CSV loaded successfully")
else:
    print("❌ Test 1 failed: Valid CSV should load successfully")


print("--------------------------------")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

result = load(123)
print(result)
if result is None:
    print("✅ Test 2a passed: Non-string input correctly rejected")
else:
    print("❌ Test 2a failed: Non-string input should be rejected")

print("--------------------------------")

# Test 2b - Invalid path parameter: empty string
print("Test 2b - Invalid path parameter: empty string")

result = load("")
print(result)
if result is None:
    print("✅ Test 2b passed: Empty string correctly rejected")
else:
    print("❌ Test 2b failed: Empty string should be rejected")

print("--------------------------------")

# Test 3 - Invalid path parameter: invalid CSV format
print("Test 3 - Invalid path parameter: invalid CSV format")

result = load("../csv_files/invalid_format.txt")
print(result)
if result is None:
    print("✅ Test 3 passed: Non-CSV file correctly rejected")
else:
    print("❌ Test 3 failed: Non-CSV file should be rejected")

print("--------------------------------")

# Test 4 - Invalid path parameter: file not found
print("Test 4 - Invalid path parameter: file not found")

result = load("nonexistent.csv")
print(result)
if result is None:
    print("✅ Test 4 passed: Non-existent file correctly rejected")
else:
    print("❌ Test 4 failed: Non-existent file should be rejected")

print("--------------------------------")

# Test 5 - Invalid path parameter: file is not a file
print("Test 5 - Invalid path parameter: file is not a file")

result = load("../csv_files/")
print(result)
if result is None:
    print("✅ Test 5 passed: Directory correctly rejected")
else:
    print("❌ Test 5 failed: Directory should be rejected")

print("--------------------------------")

# Test 6 - Invalid path parameter: file is empty
print("Test 6 - Invalid path parameter: file is empty")

result = load("../csv_files/empty.csv")
print(result)
if result is None:
    print("✅ Test 6 passed: Empty file correctly rejected")
else:
    print("❌ Test 6 failed: Empty file should be rejected")

print("--------------------------------")

# Test 7 - Invalid path parameter: ParserError
print("Test 7 - Invalid path parameter: ParserError")

result = load("../csv_files/parser_error.csv")
print(result)
if result is None:
    print("✅ Test 7 passed: Invalid CSV format correctly rejected")
else:
    print("❌ Test 7 failed: Invalid CSV format should be rejected")

print("--------------------------------")

# Test 8 - Invalid path parameter: PermissionError
print("Test 8 - Invalid path parameter: PermissionError")

result = load("../csv_files/permission_error.csv")
print(result)
if result is None:
    print("✅ Test 8 passed: Permission error correctly handled")
else:
    print("❌ Test 8 failed: Permission error should be handled")

print("--------------------------------")
