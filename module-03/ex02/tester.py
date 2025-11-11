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

# Test 6 - Valid input: test die
print("Test 6 - Valid input: Die\n")

Joffrey.die()
print(Joffrey.is_alive)
print(Joffrey.__dict__)

print("\n--------------------------------\n")


# Test 2 - Invalid input: Invalid eyes type
print("Test 2 - Invalid input: Invalid eyes type\n")

try:
    Joffrey = King("Joffrey")
    Joffrey.set_eyes(123)
    print(Joffrey.__dict__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 3a - Properties
print("Test 3a - Properties\n")

try:
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.first_name = "Corentin"
    Joffrey.is_alive = False
    Joffrey.family_name = "Houssein"
    Joffrey.eyes = "green"
    Joffrey.hairs = "red"
    print(Joffrey.first_name)
    print(Joffrey.is_alive)
    print(Joffrey.family_name)
    print(Joffrey.eyes)
    print(Joffrey.hairs)
    print(Joffrey.__dict__)
    Joffrey.eyes = ["Ouille"]
    print(Joffrey.__dict__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")
