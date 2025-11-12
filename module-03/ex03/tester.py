from ft_calculator import calculator

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5

print("\n--------------------------------\n")

# Test 2 - Invalid input: Division by zero
print("Test 2 - Invalid input: Division by zero\n")

v4 = calculator([10.0, 15.0, 20.0])
v4 / 0

print("\n--------------------------------\n")
