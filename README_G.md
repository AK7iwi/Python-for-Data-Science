- General
Python  is typed or not 
__pycache__
Status code of a program: python script.py ; echo $pipestatus


- ###def 
No need return type for raise exception 
The type hints are just documentation
two type of parameter:
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:


- ###if/elif/else
Test the diff between if,if and if,elif,...
if not (maybe in other section)
if/else in one line 
or (keyword) 


- ###import 
precisez que import execute du code 

 
- Exemple 
Cut exemple code in multiple exemple 
Add "exemple" title 

- Basic data types

I) List: 

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]


[1:2]

# Print the entire array
print("Print the entire array")
print(family[::])

# Print every 2nd element starting from index 0
print("Print every 2nd element starting from index 0")
print(family[::2])

# Print every 2nd element starting from index 1
print("Print every 2nd element starting from index 1")
print(family[1::2])

# Print the array in reverse order
print("Print the array in reverse order")
print(family[::-1])

# Print every 2nd element in reverse order
print("Print every 2nd element in reverse order")
print(family[::-2])

# Print every 2nd element, then reverse that result
print("Print every 2nd element, then reverse that result")
print(family[::2][::-1])

# Print every 2nd element, then take every 2nd element of that in reverse
print("Print every 2nd element, then take every 2nd element of that in reverse")
print(family[::2][::-2])

# Print every 2nd element starting from index 1, then reverse that result
print("Print every 2nd element starting from index 1, then reverse that result")
print(family[1::2][::-1])

# Print every 2nd element starting from index 1, then take every 2nd element of that in reverse
print("Print every 2nd element starting from index 1, then take every 2nd element of that in reverse")
print(family[1::2][::-2])
 
- Numpy array

Compare Numpy vs List: Create a tester file to compare
Add performance tester 

Slicing method (compare np manip with List manipulation)
family_array = np.array(family)
sliced_array = family_array[start:end]

def slice_list(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list using list slicing.
    """
    # Slice each row, then slice each row ??
    sliced = [row[start:end] for row in family[start:end]]
    return sliced


arr = np.array([1, 2, 3])
print("arr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1, 2, 3]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1], [2], [3]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\narr =", arr)
print("arr.shape =", arr.shape)

- try and except
finally, else
raise

- pass (keyword)
- zip (keyword)
- with (keyword)





Uses super() to call the parent constructor
self reference to the current instance of the class. 
@abstractmethod to create ... abstract methods
obj.__dict__. ex print(Ned.__dict__)


__str__ and __repr__ are special methods (also called "dunder methods" or "magic methods") just like __init__

__str__:
Creates a user-friendly string representation
Meant for end users
Called by str() and print()

__repr__:
Creates an unambiguous string representation
Meant for developers/debugging
Should ideally contain enough information to recreate the object
Called by repr() and in the interactive Python shell

from datetime import datetime

now = datetime.now()

# __str__ gives user-friendly output:
print(str(now))
# Output: 2025-11-06 10:30:45.123456

# __repr__ gives developer-friendly output:
print(repr(now))
# Output: datetime.datetime(2025, 11, 6, 10, 30, 45, 123456)


@classmethod: class method that can be called on the class itself
cls parameter: In class methods, cls refers to the class itself, allowing you to create instances using cls


self → The instance (the specific object created)
cls → The class itself (the blueprint)

Ex:

Benefit #1: Inheritance support

class Lannister(Character):
    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        return cls(first_name, is_alive)  # Uses the actual class

class SpecialLannister(Lannister):
    """A special subclass"""
    pass

# This creates a SpecialLannister, not a Lannister!
tywin = SpecialLannister.create_lannister("Tywin", True)
print(type(tywin))  # <class 'SpecialLannister'>


Benefit #2: Access to class attributes

class Lannister(Character):
    house_words = "Hear Me Roar!"
    
    @classmethod
    def create_with_motto(cls, first_name: str):
        character = cls(first_name, True)
        print(f"Created {first_name}. Motto: {cls.house_words}")
        return character

cersei = Lannister.create_with_motto("Cersei")
# Output: Created Cersei. Motto: Hear Me Roar!




- Others

- Improve the struct, more coherence (sort the point)
- Summary (link)
- Add subject in the folder
- Improve english level (orthographe, synthax, ...)