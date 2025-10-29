import numpy as np
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

array = ft_load("../images/valid_images/landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)

print("\n--------------------------------\n")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

array = "invalid"
ft_invert(array)

print("\n--------------------------------\n")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

array = np.array([1, 2, 3])
ft_red(array)

print("\n--------------------------------\n")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

array = np.array([])
ft_grey(array)

print("\n--------------------------------\n")
