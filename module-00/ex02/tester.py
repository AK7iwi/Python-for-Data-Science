from find_ft_type import all_thing_is_obj

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input\n")

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

print("\n--------------------------------\n")

# Test 2 - Invalid input: Type not found
print("Test 2 - Invalid input: Type not found\n")

all_thing_is_obj(10.5)
all_thing_is_obj(True)
all_thing_is_obj(None)
all_thing_is_obj(float("NaN"))
all_thing_is_obj(float("-inf"))

print("\n--------------------------------\n")

# Test 3 - Invalid input: Empty string
print("Test 3 - Invalid input: Empty string\n")

all_thing_is_obj("")
