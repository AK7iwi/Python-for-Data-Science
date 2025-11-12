from statistics import ft_statistics

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

print("\n--------------------------------\n")

# Test 2 - Invalid input: Non-numeric values in args
print("Test 2 - Invalid input: Non-numeric values in args\n")

ft_statistics(1, "He non", 360, 11, 64, toto="mean", tutu="median", tata="quartile")

print("\n--------------------------------\n")

# Test 3 - Invalid input: Invalid values in kwargs
print("Test 3 - Invalid input: Invalid values in kwargs\n")

ft_statistics(1, 42, 360, 11, 64, toto="heheh", tutu="median", tata="mean")

print("\n--------------------------------\n")
