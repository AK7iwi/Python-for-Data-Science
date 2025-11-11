from S1E9 import Character, Stark


# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

print("\n--------------------------------\n")

# Test 2 - Invalid input: Invalid class
print("Test 2 - Invalid input: Invalid class\n")

try:
    hodor = Character("hodor")
    print(hodor.__dict__)
except TypeError as e:
    print(f"TypeError: {e}")

print("\n--------------------------------\n")

# Test 3 - Invalid input: Invalid first_name type
print("Test 3 - Invalid input: Invalid first_name type\n")

try:
    Kiwi = Stark([5, 6, 7], 7)
    print(Kiwi.__dict__)
    print(Kiwi.is_alive)
    Kiwi.die()
    print(Kiwi.is_alive)
    print(Kiwi.__doc__)
    print(Kiwi.__init__.__doc__)
    print(Kiwi.die.__doc__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 4 - Invalid input: Empty first_name
print("Test 4 - Invalid input: Empty first_name\n")

try:
    Kiwi = Stark("", True)
    print(Kiwi.__dict__)
    print(Kiwi.is_alive)
    Kiwi.die()
    print(Kiwi.is_alive)
    print(Kiwi.__doc__)
    print(Kiwi.__init__.__doc__)
    print(Kiwi.die.__doc__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 5 - Invalid input: Invalid is_alive argument
print("Test 5 - Invalid input: Invalid is_alive argument\n")

try:
    Kiwi = Stark("Kiwi", "True")
    print(Kiwi.__dict__)
    print(Kiwi.is_alive)
    Kiwi.die()
    print(Kiwi.is_alive)
    print(Kiwi.__doc__)
    print(Kiwi.__init__.__doc__)
    print(Kiwi.die.__doc__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")
