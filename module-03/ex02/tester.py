from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# Test properties
print("Test properties:")
print(Joffrey.eyes)
print(Joffrey.hairs)
Joffrey.eyes = "green"
Joffrey.hairs = "brown"
print(Joffrey.eyes)
print(Joffrey.hairs)
print(Joffrey.__dict__)
