from load_image import ft_load

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input")

print(ft_load("../images/valid_images/landscape.jpg"))

print("\n--------------------------------\n")

# Test 1b - Valid input: other image format
print("Test 1b - Valid input: other image format")

print(ft_load("../images/valid_images/animal.png"))

print("\n--------------------------------\n")

# Test 2a - Invalid path parameter: non-string type
print("Test 2a - Invalid path parameter: non-string type")

print(ft_load(123))

print("\n--------------------------------\n")

# Test 2b - Invalid path parameter: non-string type
print("Test 2b - Invalid path parameter: non-string type")

print(ft_load(["../images/valid_images/landscape.jpg"]))

print("\n--------------------------------\n")

# Test 3 - Invalid path parameter: empty string
print("Test 3 - Invalid path parameter: empty string")

print(ft_load(""))

print("\n--------------------------------\n")

# Test 4 - Invalid path parameter: invalid image format
print("Test 4 - Invalid path parameter: invalid image format")

print(ft_load("../images/invalid_images/subject.pdf"))

print("\n--------------------------------\n")

# Test 5 - Invalid path parameter: is a directory
print("Test 5 - Invalid path parameter: is a directory")

print(ft_load("../images/"))

print("\n--------------------------------\n")

# Test 6 - Invalid path parameter: file not found
print("Test 6 - Invalid path parameter: file not found")

print(ft_load("../images/invalid_images/nonexistent.jpg"))

print("\n--------------------------------\n")

# Test 7 - Invalid image: no permission
print("Test 7 - Invalid image: no permission")

print(ft_load("../images/invalid_images/no_permission.jpg"))

print("\n--------------------------------\n")

# Test 8 - Invalid image: unidentified image
print("Test 8 - Invalid image: unidentified image")

print(ft_load("../images/invalid_images/unidentified.jpg"))

print("\n--------------------------------\n")
