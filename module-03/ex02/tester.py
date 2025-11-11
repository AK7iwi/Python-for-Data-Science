from DiamondTrap import King

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

print("\n--------------------------------\n")

# Test 2 - Invalid input: Invalid eyes type
print("Test 2 - Invalid input: Invalid eyes type\n")

try:
    Joffrey.set_eyes(123)
    print(Joffrey.__dict__)
except TypeError as e:
    print(f"TypeError: {e}")

print("\n--------------------------------\n")

# Test 3 - Valid input: Properties
print("Test 3 - Valid input: Properties\n")

print(Joffrey.eyes)
print(Joffrey.hairs)
Joffrey.eyes = "green"
Joffrey.hairs = "red"
print(Joffrey.eyes)
print(Joffrey.hairs)
print(Joffrey.__dict__)

print("\n--------------------------------\n")

# Test 4 - Invalid input: Invalid hairs type
print("Test 4 - Invalid input: Invalid hairs type\n")

try:
    Joffrey.hairs = 123
    print(Joffrey.hairs)
except TypeError as e:
    print(f"TypeError: {e}")

print("\n--------------------------------\n")

# Test 5 - Invalid input: 


# Test 6 - Valid input: Die
print("Test 6 - Valid input: Die\n")

Joffrey.die()
print(Joffrey.is_alive)
print(Joffrey.__dict__)

print("\n--------------------------------\n")
