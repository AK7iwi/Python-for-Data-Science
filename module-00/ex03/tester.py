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
