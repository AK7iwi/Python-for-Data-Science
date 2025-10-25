from ft_filter import ft_filter

# Test 1 - Valid input: Compare ft_filter with built-in filter
print("Test 1 - Valid input: Compare ft_filter with built-in filter\n")

list_test = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, list_test)
print("built-in filter: ", result)
print("list(result): ", list(result))

result = ft_filter(lambda x: x % 2 == 0, list_test)
print("\nft_filter: ", result)
print("list(result): ", list(result))

print("\n--------------------------------\n")

# Test 2 - Valid input: None function
print("Test 2 - Valid input: None function\n")

list_test = [1, 2, 3, 4, False, 0, True, ""]

result = filter(None, list_test)
print("built-in filter: ", result)
print("list(result): ", list(result))

result = ft_filter(None, list_test)
print("\nft_filter: ", result)
print("list(result): ", list(result))

print("\n--------------------------------\n")

# Test 3 - Valid input: others iterable types (tuple for example)
print("Test 3 - Valid input: others iterable types (tuple for example)\n")

tuple = (1, 2, 3, 4, 5)

result = filter(lambda x: x % 2 == 0, tuple)
print("built-in filter: ", result)
print("list(result): ", list(result))

result = ft_filter(lambda x: x % 2 == 0, tuple)
print("\nft_filter: ", result)
print("list(result): ", list(result))

print("\n--------------------------------\n")

# Test 4 - "Valid" input: Non-callable function
print("Test 4 - \"Valid\" input: Non-callable function\n")

list_test = [1, 2, 3, 4, 5]

result = filter("not a function", list_test)
print("built-in filter: ", result)
# print("list(result): ", list(result))

result = ft_filter("not a function", list_test)
print("\nft_filter: ", result)
# print("list(result): ", list(result))

print("\n--------------------------------\n")

# Test 5 - "Valid" input: Non-iterable
print("Test 5 - \"Valid\" input: Non-iterable\n")

result = filter(lambda x: x % 2 == 0, "not an iterable")
print("built-in filter: ", result)
# print("list(result): ", list(result))

result = ft_filter(lambda x: x % 2 == 0, "not an iterable")
print("\nft_filter: ", result)
# print("list(result): ", list(result))

print("\n--------------------------------\n")

# Test 6 - "Valid" input: contains non-valid values
print("Test 6 - \"Valid\" input: contains non-valid values\n")

list_test = [1, 2, 3, 4, "Kiwi"]

result = filter(lambda x: x % 2 == 0, list_test)
print("built-in filter: ", result)
# print("list(result): ", list(result))

result = ft_filter(lambda x: x % 2 == 0, list_test)
print("\nft_filter: ", result)
# print("list(result): ", list(result))

print("\n--------------------------------\n")
