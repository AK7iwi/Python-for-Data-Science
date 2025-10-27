from array2D import slice_me

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print("\n--------------------------------\n")

# Test 1b - Valid input: 2D array containing non-numeric values
print("Test 1b - Valid input: 2D array containing non-numeric values")

family = [[1.80, 78.4, "2"],
          [2.15, "valid", 5],
          [2.10, 98, 31],
          [1.88, 75.2, 22]]

print(slice_me(family, -4, -1))

print("\n--------------------------------\n")

# Test 1c - Valid input: start and end indices being the same
print("Test 1c - Valid input: start and end indices being the same")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 2, 2))

print("\n--------------------------------\n")

# Test 1d - Valid input: start index being the last index
print("Test 1d - Valid input: start index being the last index")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 3, 4))

print("\n--------------------------------\n")

# Test 1e - Valid input: end index being the first index
print("Test 1e - Valid input: end index being the first index")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, -4, 0))

print("\n--------------------------------\n")

# Test 2a - Invalid 2D array parameter: non-list type
print("Test 2a - Invalid 2D array parameter: non-list type")

family = {1.80: 78.4,
          2.15: 102.7,
          2.10: 98.5,
          1.88: 75.2}

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 2b - Invalid 2D array parameter: non-list type
print("Test 2b - Invalid 2D array parameter: non-list type")

family = ([1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2])

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 3 - Invalid 2D array parameter: empty list
print("Test 3 - Invalid 2D array parameter: empty list")

family = []

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 4a - Invalid 2D array parameter: contains non-list elements
print("Test 4a - Invalid 2D array parameter: contains non-list elements")

family = [[1.80, 78.4],
          "invalid",
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 4b - Invalid 2D array parameter: contains non-list elements
print("Test 4b - Invalid 2D array parameter: contains non-list elements")

family = [[1.80, 78.4],
          [2.15, 102.7],
          {2.10: 98.5},
          [1.88, 75.2]]

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 5 - Invalid 2D array parameter: contains empty rows
print("Test 5 - Invalid 2D array parameter: contains empty rows")

family = [[], [], []]

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 6 - Invalid 2D array parameter: contains different size rows
print("Test 6 - Invalid 2D array parameter: contains different size rows")

family = [[1.80],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))

print("\n--------------------------------\n")

# Test 7a - Invalid start parameter: non-integer value
print("Test 7a - Invalid start parameter: non-integer value")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, "start", 2))

print("\n--------------------------------\n")

# Test 7b - Invalid end parameter: non-integer value
print("Test 7b - Invalid end parameter: non-integer value")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, [0, 2]))

print("\n--------------------------------\n")

# Test 8a - Invalid start parameter: out of bounds
print("Test 8a - Invalid start parameter: out of bounds")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, -5, 2))

print("\n--------------------------------\n")

# Test 8b - Invalid end parameter: out of bounds
print("Test 8b - Invalid end parameter: out of bounds")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 1, 5))

print("\n--------------------------------\n")

# Test 9 - Invalid end parameter: end index smaller than start index
print("Test 9 - Invalid end parameter: end index smaller than start index")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 2, -4))

print("\n--------------------------------\n")
