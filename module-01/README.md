README01:

Numpy:

import numpy as np

np.array = Function to create arrays
np.asarray = Function to create arrays
np.ndarray = Class/type of the array

Diff between np.array/np.asarray:

Feature	np.array	np.asarray
Always copies	✅ Yes	❌ No (reuses if possible)
Memory usage	Higher	Lower
Performance	Slower	Faster
Use case	When you need a copy	When you want to avoid copying 

Input Type	np.array	np.asarray
List	Creates new array	Creates new array
Numpy array	Creates new array (copy)	Reuses existing array


Exemple:

np.array (Always creates a new array):
np.asarray (Creates new array from lists, reuses if already numpy array):


From lists (both behave the same):
my_list = [1, 2, 3]

# Both create new arrays
arr1 = np.array(my_list)   # New array
arr2 = np.asarray(my_list) # New array
print(arr1 is arr2)  # False - different objects

From numpy arrays (different behavior):
my_array = np.array([1, 2, 3])

# np.array creates a copy
arr1 = np.array(my_array)   # New array (copy)
print(my_array is arr1)     # False - different objects

# np.asarray reuses the original
arr2 = np.asarray(my_array) # Same array
print(my_array is arr2)     # True - same object



Parsing with pure python before convert to numpy because convert numpy array change the values types 

import numpy as np

# Mixed int and float -> becomes float
arr1 = np.array([1, 2.5, 3])
print(arr1.dtype)  # float64

# All int -> stays int
arr2 = np.array([1, 2, 3])
print(arr2.dtype)  # int64

# All float -> stays float
arr3 = np.array([1.0, 2.0, 3.0])
print(arr3.dtype)  # float64

# Strings -> becomes string array
arr4 = np.array(["hello", "world"])
print(arr4.dtype)  # <U5 (unicode string, max 5 chars)

# Mixed strings and numbers -> becomes string
arr5 = np.array(["hello", 123, "world"])
print(arr5.dtype)  # <U5
print(arr5)  # ['hello' '123' 'world']

# This silently converts strings to numbers!
arr6 = np.array(["1", "2", "3"])
print(arr6.dtype)  # <U1 (string)

# But this converts to numbers:
arr7 = np.array([1, "2", 3])
print(arr7.dtype)  # <U1 (string)

# This is dangerous - no error!
arr8 = np.array(["1", "2", "3"])
result = arr8 * 2  # Works! Converts to numbers

---------------------------------------------------

ex00:

two type of parameter:
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

numpy 
python -m pip install numpy 
numpy important method 

ex01: 

Slicing method (compare np manip with List manipulation)
family_array = np.array(family)
sliced_array = family_array[start:end]

def slice_list(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list using list slicing.
    """
    # Slice each row, then slice each row
    sliced = [row[start:end] for row in family[start:end]]
    return sliced

ex02: 

New important lib: 
a) os: 
built-in Python library, provides a way to interact with the operating system
b) PIL:
standard library for loading and processing images in Python

Image format: 

(257, 450, 3), this represents the dimensions of your image array:
The 3 values mean:
257 = Height (number of rows/pixels vertically)
450 = Width (number of columns/pixels horizontally)
3 = Channels (color components)
Why 3 channels?
Each pixel in a color image has 3 color components:
RGB Format:
R = Red component (0-255)
G = Green component (0-255)
B = Blue component (0-255)

ex03: 

New lib: 
matplotlib 
Array manip

ex04/ex05:
Array manip



link:

Return vs exit
https://discuss.python.org/t/return-vs-sys-exit/45098/3