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

# Test 2a: Invalid input with non-list values
print("Test 2a: Invalid input with non-list values")

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

# Test 2b: Invalid input with non-list values
print("Test 2b: Invalid input with non-list values")

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

# Test 3: Invalid input with empty list
print("Test 3: Invalid input with empty list")

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

# Test 4a: Invalid input with non-numeric values
print("Test 4a: Invalid input with non-numeric values")

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

# Test 4b: Invalid input with non-numeric values
print("Test 4b: Invalid input with non-numeric values")

height = [2.71, 1.15, 1.81]
weight = [165.3, [35, 89], 57]
limit = 26

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5a: Invalid input with infinite values
print("Test 5a: Invalid input with infinite values")

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

# Test 5b: Invalid input with NaN values
print("Test 5b: Invalid input with NaN values")

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

# Test 6a: Invalid input with negative values
print("Test 6a: Invalid input with negative values")

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

# Test 6b: Invalid input with zero values
print("Test 6b: Invalid input with zero values")

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

# Test 7: Invalid input with different length
print("Test 7: Invalid input with different length")

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

# Test 2a: Invalid limit with non-integer values
print("Test 2a: Invalid limit with non-integer values")

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

# Test 2b: Invalid limit with non-integer values
print("Test 2b: Invalid limit with non-integer values")

height = [2.71, 1.15]
weight = [165.3, 38.4]
limit = ["invalid", "list"]

try:
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3: Invalid limit with negative values
print("Test 3: Invalid limit with negative values")

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

# Test 4: Invalid BMI with non-list values
print("Test 4: Invalid BMI with non-list values")

bmi = {22.507863455018317, 29.0359168241966}
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 5: Invalid BMI with empty list
print("Test 5: Invalid BMI with empty list")

bmi = []
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 6: Invalid BMI with non-numeric values
print("Test 6: Invalid BMI with non-numeric values")

bmi = ["invalid", 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 7: Invalid BMI with infinite values
print("Test 7: Invalid BMI with infinite values")

bmi = [float('inf'), 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8a: Invalid BMI with negative values
print("Test 8a: Invalid BMI with negative values")

bmi = [22.507863455018317, -1]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 8b: Invalid BMI with zero values
print("Test 8b: Invalid BMI with zero values")

bmi = [0, 29.0359168241966]
limit = 26

try:
    print(apply_limit(bmi, limit))

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
