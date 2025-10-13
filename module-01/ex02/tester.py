from load_image import ft_load

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input")

try:
    print(ft_load("../images/landscape.jpg"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

try:
    print(ft_load(123))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b - Invalid path parameter: empty string
print("Test 2b - Invalid path parameter: empty string")

try:
    print(ft_load(""))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3 - Invalid path parameter: invalid image format
print("Test 3 - Invalid path parameter: invalid image format")

try:
    print(ft_load("invalid.png"))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4 - Invalid path parameter: file not found
print("Test 4 - Invalid path parameter: file not found")

try:
    print(ft_load("nonexistent.jpg"))

except Exception as e:
    print(f"Error: {e}")
