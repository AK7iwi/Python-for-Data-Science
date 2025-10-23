from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Test 1 - Valid input: Compare ft_tqdm with tqdm
print("Test 1 - Valid input: Compare ft_tqdm with tqdm\n")

for elem in tqdm(range(333)):
    sleep(0.005)
print()

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print("\n--------------------------------\n")

# Test 2 - "Valid" input: Negative range
print("Test 2 - \"Valid\" input: Negative range\n")

for elem in tqdm(range(-333)):
    sleep(0.005)
print()

for elem in ft_tqdm(range(-333)):
    sleep(0.005)
print()

print("\n--------------------------------\n")

# Test 3 - Valid input: Non iterable object
print("Test 3 - Valid input: Non iterable object\n")

for elem in tqdm("not an iterable"):
    sleep(0.005)
print()

for elem in ft_tqdm("not an iterable"):
    sleep(0.005)
print()

# Test 4 - Valid input: Non-range object
print("Test 4 - Valid input: Non-range object\n")

for elem in tqdm([5, "Kiwi", 3.14]):
    sleep(0.005)
print()

for elem in ft_tqdm([5, "Kiwi", 3.14]):
    sleep(0.005)
print()

print("\n--------------------------------\n")
