import numpy as np
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Test 1 - Valid input: Basic input
print("Test 1 - Valid input: Basic input")

try:
    array = ft_load("../images/landscape.jpg")
    print(array)

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 2 - Invalid image array: non-numpy array
print("Test 2 - Invalid image array: non-numpy array")

try:
    array = "invalid"
    ft_invert(array)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3a - Invalid image array: non-2D array
print("Test 3a - Invalid image array: non-2D array")

try:
    array = np.array([1, 2, 3])
    ft_red(array)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")

# Test 3b - Invalid image array: empty array
print("Test 3b - Invalid image array: empty array")

try:
    array = np.array([])
    ft_grey(array)

except Exception as e:
    print(f"Error: {e}")

print("--------------------------------")
