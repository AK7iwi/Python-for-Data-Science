# Data Science Pool - Python Learning Guide

## General Concepts

In Python, there's a distinction:

- **Built-in functions** are functions like `print()`, `len()`, `max()`, `min()`, etc. that are available globally
- **Methods** are functions that belong to specific objects/classes, like `list.append()`, `set.add()`, `dict.keys()`, etc.

---

<div align="center">

## MODULE 00 - Starting

</div>

<div align="center">

### ex00: First python script

</div>

#### I) Libraries used
No external libraries used.

#### II) Built-in functions and methods used
- `print()` - Built-in function to display output
- `list[index]` - List indexing and assignment
- `tuple` - Tuple creation and reassignment
- `set.remove()` - Method to remove element from set
- `set.add()` - Method to add element to set
- `dict[key]` - Dictionary key access and assignment

#### III) New theory points
- **Basic Data Types**: Introduction to Python's four main collection types
  - **List**: Mutable, ordered collection `["item1", "item2"]`
  - **Tuple**: Immutable, ordered collection `("item1", "item2")`
  - **Set**: Mutable, unordered collection of unique elements `{"item1", "item2"}`
  - **Dictionary**: Mutable, key-value pairs `{"key1": "value2", "key2": "value2"}`

#### IV) Logic used for the exercise
1. **Creating** each data type with sample data
2. **Modifying** each type using their appropriate methods:
   - List: Direct index assignment (mutable)
   - Tuple: Complete reassignment (immutable)
   - Set: Using `remove()` and `add()` methods
   - Dictionary: Key-based assignment
3. **Displaying** the results to show how each modification affects the data structure

<div align="center">

### ex01 - First use of package

</div>

#### I) Libraries used
- `time` - Built-in library for time operations
- `datetime` - Built-in library for date/time manipulation

#### II) Built-in functions and methods used
- `print()` (already used in ex00)
- `time.time()` - Returns seconds since epoch
- `datetime.now()` - Returns current date and time
- `strftime()` - Formats datetime objects
- `f"string"` - Check next point

#### III) New theory points
- **F-string (formatted string literal)**
  - Allow you to embed expressions inside string literals using curly braces `{}`
    - `f"Hello {name}, you are {age} years old"`
  - Can format numbers with specifiers:
    - `{value:,.4f}` - Comma separator with 4 decimal places
    - `{value:.2e}` - Scientific notation
- **Exception handling**: `try/except` blocks

#### IV) Logic used for the exercise
1. **Get current time** using `time.time()` and `datetime.now()`
2. **Format time values** using f-string specifiers for different representations
3. **Return formatted values** as tuple from function
4. **Display results** with descriptive output
5. **Handle errors** with try/except blocks
6. **Use `if __name__ == "__main__"`** for script execution

<div align="center">

### ex02 - Type Checking

</div>

#### I) `isinstance()` and `type()` built-in functions

**a) `isinstance()`**
- Returns whether an object is an instance of a class or of a subclass thereof
- Example: `isinstance(x, int)`

**b) `type()`**
- Returns the object's type
- Example: `type(x)`

<div align="center">

### ex03 - Null Values

</div>

#### I) `None` in Python = `NULL` in C
- Used to represent absence of a value
- Check with: `if value is None:`

<div align="center">

### ex04 - Command Line Arguments and Error Handling

</div>

#### I) `sys.argv`
- Gets command line arguments
- Example: `python script.py arg1 arg2`

#### II) Error Handling
- **try/except system** (like try/catch in C++)
- **raise AssertionError** like throw in C++

#### III) `__name__ = "__main__"`

**`__name__`**
- Special built-in variable in Python
- Contains the name of the current module

**What values can `__name__` have?**
- When the script is run directly: `__name__ = "__main__"`
- When the script is imported as a module: `__name__ = "module_name"`

<div align="center">

### ex05 - Code Quality and Loops

</div>

#### I) Norme: flake8
```bash
pip install flake8
# Add the local bin directory to your PATH if needed as user
```

#### II) Script vs Module
- **Script**: File run directly with `python filename.py`
- **Module**: File imported into another script

#### III) `input()`
- Gets user input from console
- Example: `name = input("Enter your name: ")`
- Synthax

#### IV) `sum`
- Built-in function that adds all items in an iterable
- Returns the sum of all items plus the optional start value
- Syntax: `sum(iterable, start=0)`

#### V) string library 

string library is built-in

#### VI) "for" Loop Syntax

## Basic `for` Loop Syntax

The basic syntax for a `for` loop in Python is:

```python
for item in iterable:
    # code block to execute
```

## Common Examples

### 1. Looping through a list:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. Looping through a range:
```python
for i in range(5):
    print(i)  # prints 0, 1, 2, 3, 4
```

### 3. Looping through a string:
```python
for char in "Hello":
    print(char)  # prints H, e, l, l, o
```

## `for` Loop with Conditions

### 1. Using `if` statements inside the loop:
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
```

### 2. Using `continue` to skip iterations:

`continue`:

- Skips the current iteration and continues with the next one
- Example: Skip even numbers in a loop

```python
for i in range(10):
    if i == 5:
        continue  # skip when i equals 5
    print(i)
```

### 3. Using `break` to exit the loop:

`break`:

- Exits the loop entirely
- Example: Stop when a condition is met

```python
for i in range(10):
    if i == 5:
        break  # exit loop when i equals 5
    print(i)
```

## List Comprehensions with Conditions

### 1. Basic list comprehension:
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
```

### 2. List comprehension with condition:
```python
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in numbers if x % 2 == 0]
```

### 3. List comprehension with if-else:
```python
numbers = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
```

## Dictionary Looping

### 1. Looping through keys:
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)
```

### 2. Looping through items:
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```

## Enumerate (with index)

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

The `for` loop is one of Python's most fundamental constructs and is used extensively for iterating over sequences, collections, and other iterable objects.

<div align="center">

### ex06 - ft_filter

</div>

#### I) Lambda Functions

**What is `lambda`?**

`lambda` is a keyword that creates **anonymous functions** (functions without a name) in Python.

**Basic Syntax:**
```python
lambda arguments: expression
```

**Comparison: Regular Function vs Lambda**

**Regular Function:**
```python
def add_five(x):
    return x + 5

result = add_five(3)  # result = 8
```

**Lambda Function (equivalent):**
```python
add_five = lambda x: x + 5

result = add_five(3)  # result = 8
```

**Key Characteristics:**

1. **Anonymous** - No function name (unless assigned to a variable)
2. **Single expression** - Can only contain one expression
3. **Implicit return** - The expression is automatically returned
4. **Concise** - Shorter than regular functions

**Examples:**

**1. Simple lambda:**
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25
```

**2. Lambda with multiple arguments:**
```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add = lambda x, y: x + y

print(add(3, 4))  # 7
```

**3. Lambda with no arguments:**
```python
# Regular function
def get_five():
    return 5

# Lambda equivalent
get_five = lambda: 5

print(get_five())  # 5
```

**Common Use Cases:**

**1. In `filter()` function:**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```

**2. In `map()` function:**
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

**3. In `sorted()` function:**
```python
students = [('Alice', 20), ('Bob', 18), ('Charlie', 22)]
sorted_by_age = sorted(students, key=lambda student: student[1])
print(sorted_by_age)  # [('Bob', 18), ('Alice', 20), ('Charlie', 22)]
```

**When to Use Lambda:**

**Use lambda when:**
- ✅ Function is simple (one expression)
- ✅ Function is used only once
- ✅ Function is passed as an argument to another function

**Don't use lambda when:**
- ❌ Function is complex (multiple expressions)
- ❌ Function needs to be reused multiple times
- ❌ Function needs documentation or type hints

**Limitations:**
- Can only contain **one expression**
- Cannot contain **multiple statements**
- Cannot have **docstrings**
- Cannot have **type hints**

Lambda functions are perfect for simple, one-time operations like filtering, mapping, or sorting.

#### II) __doc__ 

<div align="center">

### ex07 - Morse encryption

</div>

#### I) rstrip() removes trailing whitespace (spaces, tabs, newlines) from the right side of a string.

<div align="center">

### ex08

</div>

#### I) ljust

#### II) yield

yield is a keyword that creates a generator function. It allows a function to return values one at a time instead of all at once

Comparison: return vs yield

return - Returns all values at once:

```python
def get_numbers():
    return [1, 2, 3, 4, 5]

numbers = get_numbers()  # Returns the entire list at once
print(numbers)  # [1, 2, 3, 4, 5]
```

yield - Returns values one by one:

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()  # Returns a generator object
print(numbers)
```

How yield works:

```python
def count_up_to(n):
    for i in range(n):
        yield i  # Pauses here and returns i

# Usage:
for num in count_up_to(5):
    print(num)
# Output: 0, 1, 2, 3, 4
```

#### III) enumerate

<div align="center">

### ex09

</div>

I) https://packaging.python.org/en/latest/tutorials/packaging-projects/

II) cmd to build/install + verify all good

build: 

python3 -m build

install: 

python3 -m pip install ./dist/ft_package-0.0.1.tar.gz

verify:

python3 -m pip show -v ft_package

"unbuild":

rm -rf build/ dist/ *.egg-info

uninstall:

python3 -m pip uninstall package_name

list of package:

python3 -m pip list


IV)

<div align="center">

## MODULE 01

</div>

---

## Additional Resources

- [Python Official Documentation](https://docs.python.org/)
- [Python Style Guide (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

