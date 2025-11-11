from S1E7 import Baratheon, Lannister

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
name_info = (Jaine.first_name, type(Jaine).__name__)
print(f"Name : {name_info}, Alive : {Jaine.is_alive}")

print("\n--------------------------------\n")

# Test 2 - Invalid input: Invalid first_name type
print("Test 2 - Invalid input: Invalid first_name type\n")

try:
    Robert = Baratheon(31100207)
    print(Robert.__dict__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 3 - Invalid input: Invalid first_name for "create_lannister"
print("Test 3 - Invalid input: Invalid first_name for 'create_lannister'\n")

try:
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister([5, 11], True)
    name_info = (Jaine.first_name, type(Jaine).__name__)
    print(f"Name : {name_info}, Alive : {Jaine.is_alive}")
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 4a - Previous propreties"
print("Test 4a - Previous propreties\n")

try:
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    Robert.first_name = "Gerard"
    Robert.is_alive = 55
    print(Robert.__dict__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")

# Test 4b - Propreties"
print("Test 4b - Propreties\n")

try:
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    Robert.family_name = "Rashford"
    print(Robert.__dict__)
    Robert.eyes = 55
    print(Robert.__dict__)
except (TypeError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

print("\n--------------------------------\n")
