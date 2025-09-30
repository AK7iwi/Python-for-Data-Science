from array2D import slice_me

# Test 1a: Basic valid input
print("Test 1a: Basic valid input")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1b: Valid input (containing non-numeric values)
print("Test 1b: Valid input (containing non-numeric values)")

family = [[1.80, 78.4],
          [2.15, "valid"],
          [2.10, 98],
          [1.88, 75.2]]

try:
    print(slice_me(family, 1, -1))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1c: Valid input (with start and end indices being the same)
print("Test 1c: Valid input with start and end indices being the same")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 2, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1d: Valid input (with start index being the last index)
print("Test 1d: Valid input (with start index being the last index)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 3, 4))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1e: Valid input (with end index being the first index)
print("Test 1e: Valid input with end index being the first index")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, -4, 0))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a: Invalid family parameter (non-list type)
print("Test 2a: Invalid family parameter (non-list type)")

family = {1.80: 78.4,
          2.15: 102.7,
          2.10: 98.5,
          1.88: 75.2}

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b: Invalid family parameter (non-list type)
print("Test 2b: Invalid family parameter (non-list type)")

family = ([1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2])

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid family parameter (empty list)
print("Test 3: Invalid family parameter (empty list)")

family = []

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4a: Invalid family parameter (containing non-list elements)
print("Test 4a: Invalid family parameter (containing non-list elements)")

family = [[1.80, 78.4],
          "invalid",
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4b: Invalid family parameter (containing non-list elements)
print("Test 4b: Invalid family parameter (containing non-list elements)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          {2.10: 98.5},
          [1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5: Invalid family parameter (containing empty rows)
print("Test 5: Invalid family parameter (containing empty rows)")

family = [[], [], []]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6: Invalid family parameter (containing different size rows)
print("Test 6: Invalid family parameter (containing different size rows)")

family = [[1.80],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7a: Invalid start parameter (non-integer value)
print("Test 7a: Invalid start parameter (non-integer value)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, "start", 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7b: Invalid end parameter (non-integer value)
print("Test 7b: Invalid end parameter (non-integer value)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 0, [0, 2]))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8a: Invalid start parameter (out of bounds)
print("Test 8a: Invalid start parameter (out of bounds)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, -5, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8b: Invalid end parameter (out of bounds)
print("Test 8b: Invalid end parameter (out of bounds)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 1, 4))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 9: Invalid end parameter (end index smaller than start index)
print("Test 9: Invalid end parameter (end index smaller than start index)")

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

try:
    print(slice_me(family, 2, -4))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
