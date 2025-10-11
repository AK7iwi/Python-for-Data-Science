<div align="center">

# MODULE 00 - Starting

</div>

## Summary

[1. Exercice 00: First python script](#1-exercice-00-first-python-script)  
[2. Exercice 01: First use of package](#2-exercice-01-first-use-of-package)  
[3. Exercice 02: First function python](#3-exercice-02-first-function-python)  
[4. Exercice 03: NULL not found](#4-exercice-03-null-not-found)  
[5. Exercice 04: The Even and the Odd](#5-exercice-04-the-even-and-the-odd)  
[6. Interlude: From now on you must follow these additional rules](#6-interlude-from-now-on-you-must-follow-these-additional-rules)  
[7. Exercice 05: First standalone program python](#7-exercice-05-first-standalone-program-python)  
[8. Exercice 06: ft_filter](#8-exercice-06-ft_filter)  
[9. Exercice 07: Dictionaries SoS](#9-exercice-07-dictionaries-sos)  
[10. Exercice 08: Loading ...](#10-exercice-08-loading-)  
[11. Exercice 09: My first package creation](#11-exercice-09-my-first-package-creation)  
[Additional Resources](#additional-resources)


## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- Cross-references like "(already used in ex00)" indicate when a concept was previously introduced
- There are additional resources at the end if you want to explore a concept in more depth

## Introduction


## 1. Exercice 00: First python script

### I) Libraries used
No external libraries used.

### II) Built-in functions and methods used
- `set.remove()`: Method to remove element from set
- `set.add()`: Method to add element to set
- `print()`: Built-in function to display output

### III) External functions
No external functions used.

### IV) New theory points
- **Basic Data Types**
  - List: Mutable, ordered collection `["item1", "item2"]`
  - Tuple: Immutable, ordered collection `("item1", "item2")`
  - Set: Mutable, unordered collection of unique elements `{"item1", "item2"}`
  - Dictionary: Mutable, key-value pairs `{"key1": "value2", "key2": "value2"}`

### V) Logic used for the exercise
1. Creating each data type with sample data
2. Modifying each type using their appropriate methods:
    - List: Direct index assignment (mutable)
    - Tuple: Complete reassignment (immutable)
    - Set: Using `remove()` and `add()` methods
    - Dictionary: Key-based assignment
3. Displaying the results to show how each modification affects the data structure


## 2. Exercice 01: First use of package

### I) Libraries used
- `time`: Built-in library for time operations
- `datetime`: Built-in library for date/time manipulation

### II) Built-in functions and methods used
- `time.time()`: Module function that returns seconds since epoch
- `datetime.now()`: Class method that returns current date and time
- `strftime()`: Method that formats datetime objects
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Library import**
  - `import lib` or just a specific class `from lib import class`
- **F-string (formatted string literal)**
  - Allow you to embed expressions inside string literals using curly braces `{}`
    - `f"Hello {name}, you are {age} years old"`
  - Can format numbers with specifiers:
    - `{value:,.4f}`: Comma separator with 4 decimal places
    - `{value:.2e}`: Scientific notation

### V) Logic used for the exercise
1. Import required libraries using `import time` and `from datetime import datetime`
2. Get current time using `time.time()` and `datetime.now()`
3. Format time values using f-string specifiers for different representations
4. Return formatted values as tuple from function
5. Display results with descriptive output


## 3. Exercice 02: First function python

### I) Libraries used
No external libraries used.

### II) Built-in functions and methods used
- `isinstance()`: Built-in function that checks if object is instance of a class
- `type()`: Built-in function that returns the type of an object
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Function definition**
  - Basic function: `def function_name(parameter):`
  - Function definition with type: `def function_name(parameter: type) -> return_type:`
  - Type hints: `object: any` and `-> int` for parameter and return type documentation
- **Function import**
  - `from module import function`
- **Conditional statements**
  - `if/elif/else` structure

### V) Logic used for the exercise
1. Define a function with type hints and documentation
2. Use isinstance() to check object types (list, tuple, set, dict, str, int)
3. Print different messages based on the object type
4. Handle special cases (strings get special message, int returns "Type not found")
5. Return a value (42) from the function
6. Import and test the function with different data types


## 4. Exercice 03: NULL not found

### I) Libraries used
No external libraries used.

### II) Built-in functions and methods used
- `isinstance()`: (already used in ex02)
- `type()`: (already used in ex02)
- `str()`: Built-in function that converts object to string
- `float()`: Built-in function that converts to float type
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **None value**
  - `None` represents absence of value (like NULL in C)
- **NaN (Not a Number)**
  - `float("NaN")` creates a special float value
- **Boolean False**
  - `False` as a null-like value
- **Zero as null**
  - Integer `0` representing empty/nothing
- **Empty string**
  - `""` representing no text
- **Identity operator**
  - `is` vs `==` for object comparison
- **String conversion**
  - `str(object)` to convert values for comparison

### V) Logic used for the exercise
1. Define function to check different null-like values
2. Use `is` operator to check for `None` (identity comparison)
3. Check for NaN using `isinstance()` and string conversion
4. Check for False using `is` operator for boolean identity
5. Check for zero using `==` operator for value comparison
6. Check for empty string using `==` operator
7. Return different codes (0 for recognized, 1 for unrecognized)
8. Test with various null-like values to demonstrate different cases


## 5. Exercice 04: The Even and the Odd

### I) Libraries used
- `sys`: Built-in library for system-specific parameters and functions

### II) Built-in functions and methods used
- `len()`: Built-in function that returns length of a sequence
- `int()`: Built-in function that converts string to integer
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Gets command line arguments**
  - `sys.argv`
  - Example: `python script.py arg1 arg2`, sys.arg[0] = script.py, sys.arg[1] = arg1, sys.arg[2] = arg2
- **Exception/Error handling**
  - Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point III)

### V) Logic used for the exercise
1. Import sys module to access command line arguments
2. Validate argument count using `len(sys.argv)` - must be exactly 2
3. Check for too many arguments and raise AssertionError if found
4. Extract argument from `sys.argv[1]` (first user argument)
5. Convert string to integer using `int()` with try/except for ValueError
6. Check odd/even using modulo operator `% 2`
7. Handle errors with specific exception messages


## 6. Interlude: From now on you must follow these additional rules

### I) Script vs Module
- **Script**
  - File run directly with `python filename.py`
- **Module**
  - File imported into another script

### II) Norme: Flake8
```bash
pip install flake8
# or
python -m pip install flake8
# Add the local bin directory to your PATH if needed as user
```

- **Adding to PATH explanation**
  - When you install packages with `pip install --user`, they are installed in your user directory
  - The executable files (like `flake8`) are placed in `~/.local/bin/` (Linux/Mac)
  - You need to add this directory to your PATH environment variable so the system can find the executable
- **Linux/Mac**
  - Add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc`
- **Alternative method**
  - You can also uncomment (remove the #) the existing PATH line in your `~/.zshrc` file that already contains this export
  - After adding to PATH, restart your terminal or run `source ~/.zshrc` (Linux/Mac)

### III) Exception/Error handling
- `try/except`: System with specific exception types (like try/catch in C++)
- `raise`: Built-in keyword that raises an exception (like throw in C++)
- `ValueError`: Built-in exception for conversion errors
- `AssertionError`: Custom exception for validation errors

### IV) `__name__`

Special built-in variable in Python that contains the name of the current module

```python
if __name__ == "__main__"
```

### V) `__doc__`

Special built-in variable that contains the documentation string (docstring) of a function, class, or module. If you write a description for your function (written with triple quotes `"""` right after function definition), you can read it with `print(function.__doc__)`


## 7. Exercice 05: First standalone program python

### I) Libraries used
- `sys`: (already used in ex04)
- `string`: Built-in library for string constants and utilities

### II) Built-in functions and methods used
- `len()`: (already used in ex04)
- `input()`: Built-in function that gets user input from console
- `sum()`: Built-in function that return the sum off all items plus the optional start value
- `char.isupper()`: Method that checks if character is uppercase
- `char.islower()`: Method that checks if character is lowercase
- `char.isdigit()`: Method that checks if character is a digit
- `char.isspace()`: Method that checks if character is whitespace
- `string.punctuation`: Module constant containing all punctuation characters
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Using `if __name__ == "__main__"`**
  - Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point IV)
- **Loop to iterate over sequences**
  - `for`
  - Loop keyword used to iterate over sequences (lists, tuples, strings, etc.)
  - Basic syntax: `for item in iterable:`

### V) Logic used for the exercise
1. Validate arguments - Handle 0, 1, or multiple arguments
2. Get input - Either from command line argument or user input prompt
3. Count character types using generator expressions with `sum()`
4. Use string methods to classify each character (upper, lower, digit, space, punctuation)
5. Return counts as tuple from the counting function
6. Display formatted results with character counts and total length


## 8. Exercice 06: ft_filter

### I) Libraries used
- `sys`: (already used in ex04)

### II) Built-in functions and methods used
- `len()`: (already used in ex04)
- `int()`: (already used in ex04)
- `lambda`: Built-in keyword that creates anonymous functions
- `str.split()`: Method that splits string into list of words
- `filter()`: Built-in function that filters iterable based on function
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Lambda functions**
  - Anonymous functions created with `lambda` keyword
  - Syntax: `lambda arguments: expression`
  - Used for simple, one-time operations
  - Example: `lambda x: len(x) > 5`
- **Higher-order functions**
  - Functions that take other functions as parameters
  - `filter(function, iterable)` pattern
- **List comprehension**
  - Concise way to create lists from iterables
  - Syntax: `[expression for item in iterable if condition]`
  - More efficient than traditional loops for simple operations
  - Example: `[item for item in iterable if function(item)]`

### V) Logic used for the exercise
1. Create custom filter function `ft_filter()` that mimics built-in `filter()`
2. Handle two cases in the filter function:
   - When function is `None`: filter out falsy values
   - When function is provided: apply function to each item
3. Use list comprehensions for filtering logic
4. Validate command line arguments - must be exactly 2 (string and integer)
5. Convert string to integer with error handling
6. Use lambda function with `ft_filter()` to filter words by length
7. Split string into words using `str.split()` method
8. Display function documentation using `__doc__` attribute. Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point V)


## 9. Exercice 07: Dictionaries SoS

### I) Libraries used
- `sys`: (already used in ex04)

### II) Built-in functions and methods used
- `len()`: (already used in ex04)
- `str.upper()`: Method that converts string to uppercase
- `str.rstrip()`: Method that removes trailing whitespace
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Dictionary mapping**
  - Using dictionaries to map characters to their representations
  - Key-value pairs for character-to-morse code conversion
- **String concatenation in loops**
  - Building strings by concatenating in loops
  - Pattern: `result += new_part`

### V) Logic used for the exercise
1. Create morse code dictionary with character-to-morse mappings
2. Validate command line arguments - must be exactly 1 string argument
3. Convert input to uppercase using `str.upper()` for case-insensitive processing
4. Iterate through each character in the input string
5. Check if character exists in morse dictionary using `in` operator
6. Convert valid characters to morse code using dictionary lookup
7. Handle invalid characters by raising AssertionError
8. Remove trailing whitespace using `str.rstrip()` from final result
9. Display encrypted message


## 10. Exercice 08: Loading ...

### I) Libraries used
- `time`: (already used in ex01)
- `tqdm`: External library for progress bars (for comparison)

### II) Built-in functions and methods used
- `len()`: (already used in ex04)
- `enumerate()`: Built-in function that returns index and value pairs
- `yield`: Built-in keyword that creates generator functions
- `range()`: Built-in function that creates sequence of numbers
- `sleep()`: Module function that pauses execution
- `print()`: (already used in ex00)

### III) External functions
- `tqdm()`: External function from tqdm library for creating progress bars

### IV) New theory points
- **Generator functions**
  - Functions that use `yield` instead of `return`
  - Create iterators that can be paused and resumed
  - Memory efficient for large data sets
- **Enumerate function**
  - `enumerate(iterable)` returns (index, value) pairs
  - Useful for tracking position in loops

### V) Logic used for the exercise
1. Create generator function `ft_tqdm()` that yields items from range
2. Calculate progress metrics - percentage and bar width
3. Build visual progress bar using string concatenation and padding
4. Use carriage return `\r` to overwrite the same line
5. Yield each item from the range while displaying progress
6. Compare with real tqdm library to show functionality
7. Handle progress display with percentage, bar, and item count
8. Add sleep delays to demonstrate real-time progress updates


## 11. Exercice 09: My first package creation

### I) Libraries used
- `setuptools`: Built-in library for package building
- `wheel`: Built-in library for package distribution

### II) Built-in functions and methods used
- `list.count()`: Method that counts occurrences of item in list
- `print()`: (already used in ex00)

### III) External functions
No external functions used.

### IV) New theory points
- **Package structure**
  - `__init__.py` file makes directory a Python package
  - `__all__` list defines public API of the package
  - `__version__` variable stores package version
- **Package configuration**
  - `pyproject.toml` file for modern Python packaging
  - Project metadata (name, version, description, license)
  - Build system requirements and classifiers
- **Package distribution**
  - Building packages with `python -m build`
  - Installing local packages with `pip install`
  - Package verification and management
- **Relative imports**
  - `from .core import function` for same-package imports
  - Using dots to indicate relative module location
- **Command summary**
  - Build: python -m build
  - Install: python -m pip install ./dist/ft_package-0.0.1.tar.gz
  - Verify: python -m pip show -v ft_package
  - Unbuild: rm -rf build/ dist/ *.egg-info
  - Uninstall: python -m pip uninstall ft_package
  - List of installed packages: python -m pip list

### V) Logic used for the exercise
1. Create package structure with `ft_package/` directory
2. Add `__init__.py` to make it a proper Python package
3. Define core functionality in `core.py` with `count_in_list()` function
4. Configure package metadata in `pyproject.toml` file
5. Set up package imports in `__init__.py` with `__all__` and `__version__`
6. Build the package using `python -m build` command
7. Install the package locally with `pip install ./dist/ft_package-0.0.1.tar.gz`
8. Test the package by importing and using the functions
9. Verify installation with `pip show -v ft_package`
10. Clean up with uninstall and remove build artifacts

---

## Additional Resources

[Python Official Documentation](https://docs.python.org/)  
[Python Style Guide](https://www.python.org/dev/peps/pep-0008/)  
[Flake8 Doc](https://flake8.pycqa.org/en/latest/)  
[Type Hints in Python](https://www.geeksforgeeks.org/python/type-hints-in-python/)  
[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)  
[Create a Package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)  

[Python Official Documentation]: https://docs.python.org/
[Python Style Guide]: https://www.python.org/dev/peps/pep-0008/
[Flake8 Doc]: https://flake8.pycqa.org/en/latest/
[Type Hints in Python]: https://www.geeksforgeeks.org/python/type-hints-in-python/
[Built-in Exceptions]: https://docs.python.org/3/library/exceptions.html
[Create a Package]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
