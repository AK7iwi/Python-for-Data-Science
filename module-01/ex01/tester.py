from array2D import slice_me

# Test 1a: Valid input
print("Test 1a: Valid input")

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

# Test 1b: Valid input
print("Test 1b: Valid input")

family = [[1.80, 78.4],
[2.15, "valid"],
[2.10, 98],
[1.88, 75.2]]

try:
    print(slice_me(family, 1, -1))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a: Invalid input with family not being a list
print("Test 2a: Invalid input with family not being a list")

family = {1.80: 78.4,
2.15: 102.7,
2.10: 98.5,
1.88: 75.2}

try:
    print(slice_me(family, 0, 2)) 

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b: Invalid input with family not being a list
print("Test 2b: Invalid input with family not being a list")

family = ([1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2])

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid input with empty list
print("Test 3: Invalid input with empty list")

family = []

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4a: Invalid input with non-list elements
print("Test 4a: Invalid input with non-list elements")

family = [[1.80, 78.4],
"invalid",
[2.10, 98.5],
[1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4b: Invalid input with non-list elements
print("Test 4b: Invalid input with non-list elements")

family = [[1.80, 78.4],
[2.15, 102.7],
{2.10: 98.5},
[1.88, 75.2]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5: Invalid input with different size rows
print("Test 5: Invalid input with different size rows")

family = [[1.80],
[2.15, 102.7],
[2.10, 98.5]]

try:
    print(slice_me(family, 0, 2))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")