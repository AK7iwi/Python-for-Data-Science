from give_bmi import give_bmi, apply_limit

# Test give_bmi
print("--------------------------------")
print("Test give_bmi")
print("--------------------------------")

# Test 1a: Basic valid input
print("Test 1a: Basic valid input")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1b: Valid input (containing both integer and float values)
print("Test 1b: Valid input (containing both integer and float values)")

height = [2, 1, 1.81]
weight = [165.3, 38, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a: Invalid height parameter (non-list type)
print("Test 2a: Invalid height parameter (non-list type)")

height = "invalid"
weight = [165.3, 38.4]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b: Invalid weight parameter (non-list type)
print("Test 2b: Invalid weight parameter (non-list type)")

height = [2.71, 1.15]
weight = (165.3, 38.4)
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid height parameter (empty list)
print("Test 3: Invalid height parameter (empty list)")

height = []
weight = [165.3, 38.4]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4a: Invalid height parameter (containing non-numeric values)
print("Test 4a: Invalid height parameter (containing non-numeric values)")

height = [2.71, 1.15, "invalid"]
weight = [165.3, 38.4, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4b: Invalid weight parameter (containing non-numeric values)
print("Test 4b: Invalid weight parameter (containing non-numeric values)")

height = [2.71, 1.15, 1.81]
weight = [165.3, [35, 89], "invalid"]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5a: Invalid height parameter (containing infinite values)
print("Test 5a: Invalid height parameter (containing infinite values)")

height = [2.71, float('inf'), 1.81]
weight = [165.3, 38.4, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5b: Invalid weight parameter (containing NaN values)
print("Test 5b: Invalid weight parameter (containing NaN values)")

height = [2.71, 1.15, 1.81]
weight = [165.3, 38.4, float('nan')]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6a: Invalid weight parameter (containing negative values)
print("Test 6a: Invalid weight parameter (containing negative values)")

height = [2.71, 1.15, 1.81]
weight = [-5, 38.4, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6b: Invalid height parameter (containing zero values)
print("Test 6b: Invalid height parameter (containing zero values)")

height = [0, 1.15, 1.81]
weight = [165.3, 38.4, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7: Invalid height and weight parameters (different length)
print("Test 7: Invalid height and weight parameters (different length)")

height = [2.71, 1.15, 1.81]
weight = [165.3, 38.4]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test apply_limit
print("--------------------------------")
print("Test apply_limit")
print("--------------------------------")

# Test 1a: Basic valid input
print("Test 1a: Basic valid input")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 1b: Valid input with different limit value
print("Test 1b: Valid input with different limit value")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 15

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2a: Invalid limit parameter (non-integer value)
print("Test 2a: Invalid limit parameter (non-integer value)")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26.5

try:
    bmi = give_bmi(height, weight)

    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b: Invalid limit parameter (non-integer value)
print("Test 2b: Invalid limit parameter (non-integer value)")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = ["invalid", "list"]

try:
    bmi = give_bmi(height, weight)

    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid limit parameter (negative value)
print("Test 3: Invalid limit parameter (negative value)")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = -1

try:
    bmi = give_bmi(height, weight)

    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4: Invalid BMI parameter (non-list type)
print("Test 4: Invalid BMI parameter (non-list type)")

bmi = {22.507863455018317, 29.0359168241966}
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5: Invalid BMI parameter (empty list)
print("Test 5: Invalid BMI parameter (empty list)")

bmi = []
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6: Invalid BMI parameter (containing non-numeric values)
print("Test 6: Invalid BMI parameter (containing non-numeric values)")

bmi = ["invalid", 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7: Invalid BMI parameter (containing infinite values)
print("Test 7: Invalid BMI parameter (containing infinite values)")

bmi = [float('inf'), 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8a: Invalid BMI parameter (containing negative values)
print("Test 8a: Invalid BMI parameter (containing negative values)")

bmi = [22.507863455018317, -1]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8b: Invalid BMI parameter (containing zero values)
print("Test 8b: Invalid BMI parameter (containing zero values)")

bmi = [0, 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
