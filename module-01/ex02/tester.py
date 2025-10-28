from load_image import ft_load

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

print(ft_load("../images/landscape.jpg"))

print("\n--------------------------------\n")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

print(ft_load(123))

print("\n--------------------------------\n")

# Test 2b - Invalid path parameter: empty string
print("Test 2b - Invalid path parameter: empty string")

print(ft_load(""))

print("\n--------------------------------\n")

# Test 3 - Invalid path parameter: invalid image format
print("Test 3 - Invalid path parameter: invalid image format")

print(ft_load("invalid.png"))

print("\n--------------------------------\n")

# Test 4 - Invalid path parameter: file not found
print("Test 4 - Invalid path parameter: file not found")

print(ft_load("nonexistent.jpg"))

print("\n--------------------------------\n")
