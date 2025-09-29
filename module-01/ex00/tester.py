from give_bmi import give_bmi, apply_limit

# Test give_bmi
print("--------------------------------")
print("Test give_bmi")
print("--------------------------------")

# Test 1a: Valid input
print("Test 1a: Valid input")

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

# Test 1b: Valid input
print("Test 1b: Valid input")

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

# Test 2a: Invalid input with non-numeric values
print("Test 2a: Invalid input with non-numeric values")

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

# Test 2b: Invalid input with non-numeric values
print("Test 2b: Invalid input with non-numeric values")

height = [2.71, 1.15, 1.81]
weight = [165.3, "invalid", 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a: Invalid input with different length
print("Test 3a: Invalid input with different length")

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

# Test 3b: Invalid input with different length
print("Test 3b: Invalid input with different length")

height = [2.71, 1.15]
weight = [165.3, 38.4, 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 4a: Invalid input with infinite
print("Test 4a: Invalid input with infinite values")

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

# Test 4b: Invalid input with NaN values
print("Test 4b: Invalid input with NaN values")

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

# Test 5a: Invalid input with negative values
print("Test 5a: Invalid input with negative values")

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

# Test 5b: Invalid input with zero values
print("Test 5b: Invalid input with zero values")

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

# Test apply_limit
print("--------------------------------")
print("Test apply_limit")
print("--------------------------------")

# Test 1a: Valid input
print("Test 1a: Valid input")

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

# Test 1b: Valid input
print("Test 1b: Valid input")

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

# Test 2a: Invalid input with non-integer values
print("Test 2a: Invalid input with non-numeric values")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = 26.5

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2b: Invalid input with non-numeric values
print("Test 2b: Invalid input with non-numeric values")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = "invalid"

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid input with negative values
print("Test 3: Invalid input with negative values")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = -1

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
