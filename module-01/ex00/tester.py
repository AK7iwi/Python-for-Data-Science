from give_bmi import give_bmi, apply_limit

# Test give_bmi
print("--------------------------------")
print("Test give_bmi")
print("--------------------------------")

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 1b - Valid input: measurement parameter (height and weight)
# containing both integer and float values
print("Test 1b - Valid input: measurement parameter (height and weight) "
      "containing both integer and float values")

height = [2, 1, 1.81]
weight = [165.3, 38, 57]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 2a - Invalid measurement parameter: height is not a list
print("Test 2a - Invalid measurement parameter: height is not a list")

height = "invalid"
weight = [165.3, 38.4]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 2b - Invalid measurement parameter: weight is not a list
print("Test 2b - Invalid measurement parameter: weight is not a list")

height = [2.71, 1.15]
weight = (165.3, 38.4)
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 3 - Invalid measurement parameter: height is an empty list
print("Test 3 - Invalid measurement parameter: height is an empty list")

height = []
weight = [165.3, 38.4]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 4a - Invalid measurement parameter: height contains non-numeric values
print("Test 4a - Invalid measurement parameter: height contains "
      "non-numeric values")

height = [2.71, 1.15, "invalid"]
weight = [165.3, 38.4, 57]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 4b - Invalid measurement parameter: weight contains non-numeric values
print("Test 4b - Invalid measurement parameter: weight contains "
      "non-numeric values")

height = [2.71, 1.15, 1.81]
weight = [165.3, [35, 89], "invalid"]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 5a - Invalid measurement parameter: height contains infinite values
print("Test 5a - Invalid measurement parameter: height contains "
      "infinite values")

height = [2.71, float('inf'), 1.81]
weight = [165.3, 38.4, 57]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 5b - Invalid measurement parameter: weight contains NaN values
print("Test 5b - Invalid measurement parameter: weight contains NaN values")

height = [2.71, 1.15, 1.81]
weight = [165.3, 38.4, float('nan')]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 6a - Invalid measurement parameter: weight contains negative values
print("Test 6a - Invalid measurement parameter: weight contains "
      "negative values")

height = [2.71, 1.15, 1.81]
weight = [-5, 38.4, 57]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 6b - Invalid measurement parameter: height contains zero values
print("Test 6b - Invalid measurement parameter: height contains zero values")

height = [0, 1.15, 1.81]
weight = [165.3, 38.4, 57]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 7 - Invalid measurement parameter: height and weight have
# different lengths
print("Test 7 - Invalid measurement parameter: height and weight have "
      "different lengths")

height = [2.71, 1.15, 1.81]
weight = [165.3, 38.4]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test apply_limit
print("--------------------------------")
print("Test apply_limit")
print("--------------------------------")

# Test 1a - Valid input: Basic input
print("Test 1a - Valid input: Basic input")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 1b - Valid input: different limit value
print("Test 1b - Valid input: different limit value")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 15

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 2a - Invalid limit parameter: non-integer value
print("Test 2a - Invalid limit parameter: non-integer value")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26.5

bmi = give_bmi(height, weight)
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 2b - Invalid limit parameter: non-integer value
print("Test 2b - Invalid limit parameter: non-integer value")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = ["invalid", "list"]

bmi = give_bmi(height, weight)
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 3 - Invalid limit parameter: negative value
print("Test 3 - Invalid limit parameter: negative value")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = -1

bmi = give_bmi(height, weight)
print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 4 - Invalid bmi parameter: non-list type
print("Test 4 - Invalid bmi parameter: non-list type")

bmi = {22.507863455018317, 29.0359168241966}
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 5 - Invalid bmi parameter: empty list
print("Test 5 - Invalid bmi parameter: empty list")

bmi = []
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 6 - Invalid bmi parameter: contains non-numeric values
print("Test 6 - Invalid bmi parameter: contains non-numeric values")

bmi = ["invalid", 29.0359168241966]
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 7 - Invalid bmi parameter: contains infinite values
print("Test 7 - Invalid bmi parameter: contains infinite values")

bmi = [float('inf'), 29.0359168241966]
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 8a - Invalid bmi parameter: contains negative values
print("Test 8a - Invalid bmi parameter: contains negative values")

bmi = [22.507863455018317, -1]
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")

# Test 8b - Invalid bmi parameter: contains zero values
print("Test 8b - Invalid bmi parameter: contains zero values")

bmi = [0, 29.0359168241966]
limit = 26

print(apply_limit(bmi, limit))

print("\n--------------------------------\n")
