from NULL_not_found import NULL_not_found

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

print("\n--------------------------------\n")

# Test 2 - Invalid input: Type not found
print("Test 2 - Invalid input: Type not found\n")

NULL_not_found([31, 10, 2007])
NULL_not_found(10.5)
NULL_not_found(float("-inf"))
NULL_not_found(2)
NULL_not_found("Hello")
NULL_not_found(True)

print("\n--------------------------------\n")
