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
- There are additional resources at the end if you want to explore a concept in more depth

## Introduction

Module 00 is an introductory module designed to cover the fundamental building blocks of Python programming. This module progressively introduces essential concepts including:

- **Basic data types**: lists, tuples, sets, and dictionaries
- **Functions**: definitions, type hints, and documentation
- **Imports**: using built-in libraries and creating custom packages
- **Command-line arguments**: handling user input with sys.argv
- **Error handling**: managing exceptions and validating inputs
- **Advanced features**: generators, list comprehensions, and lambda functions


## 1. Exercice 00: First python script

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `set.remove()`: Method to remove element from set
- `set.add()`: Method to add element to set
- `print()`: Built-in function to display output

### III) New external functions, methods, attributes used
No new external functions used.

### IV) New theory points
- **Basic Data Types**
  - **List**: Mutable, ordered collection `["item1", "item2"]`
    - Can be modified using index assignment: `list[index] = "new_value"`
  - **Tuple**: Immutable, ordered collection `("item1", "item2")`
    - Cannot be modified; must reassign entire tuple: `tuple = ("new1", "new2")`
  - **Set**: Mutable, unordered collection of unique elements `{"item1", "item2"}`
    - Modified using methods: `add()`, `remove()`, `discard()`
  - **Dictionary**: Mutable, key-value pairs `{"key1": "value1", "key2": "value2"}`
    - Can be modified using key assignment: `dict["key"] = "new_value"`

- **Mutability vs Immutability**
  - **Mutable objects**: Can be changed after creation (list, set, dict)
  - **Immutable objects**: Cannot be changed after creation (tuple, str, int, float)
  - Attempting to modify immutable objects creates new objects instead

### V) Logic used for the exercise
1. Creating each data type with sample data
2. Modifying each type using their appropriate methods:
    - List: Direct index assignment (mutable)
    - Tuple: Complete reassignment (immutable)
    - Set: Using `remove()` and `add()` methods
    - Dictionary: Key-based assignment
3. Displaying the results to show how each modification affects the data structure


## 2. Exercice 01: First use of package

### I) New libraries used
- `sys`: Built-in library for system-specific parameters and functions
- `time`: Built-in library for time operations
- `datetime`: Built-in library for date/time manipulation

### II) New built-in functions, methods, attributes used
- `time.time()`: Time module function that returns seconds since epoch
- `datetime.now()`: Datetime class method that returns current date and time
- `strftime()`: Datetime object method that formats datetime to string
- `sys.exit()`: Sys module function that exits program with a return code

### III) New external functions, methods, attributes used
- `validate_args_for_prog()`: Custom function to validate command line arguments

### IV) New theory points
- **Library import**
  - `import lib`: Import entire library
  - `from lib import class`: Import specific class/function from library
  
- **F-string (formatted string literal)**
  - Allow you to embed expressions inside string literals using curly braces `{}`
    - Example: `f"Hello {name}, you are {age} years old"`
  - Can format numbers with specifiers:
    - `{value:,.4f}`: Comma separator with 4 decimal places
    - `{value:.2e}`: Scientific notation (exponential)

- **Tuple unpacking**
  - Assigning multiple values from tuple: `a, b, c = function_returning_tuple()`
  - Must match number of elements returned

### V) Logic used for the exercise
1. Import required libraries: `sys`, `time`, `datetime`, and custom validation module
2. Validate command line arguments using try/except block
3. Create `format_time()` function that:
   - Gets current time in seconds since epoch using `time.time()`
   - Formats seconds with comma separator and scientific notation using f-string specifiers
   - Gets current date using `datetime.now()`
   - Formats date using `strftime()` method with `"%b %d %Y"` format
   - Returns all three formatted values as a tuple
4. Unpack returned tuple using tuple unpacking: `a, b, c = format_time()`
5. Display results using `display_results()` function with f-strings
6. Exit program with appropriate return code using `sys.exit()`


## 3. Exercice 02: First function python

### I) New libraries used
- `typing`: Built-in library for type hints (importing `Any` type)

### II) New built-in functions, methods, attributes used
- `isinstance()`: Built-in function that checks if object is instance of a class
- `type()`: Built-in function that returns the type of an object
- `len()`: Built-in function that returns length of an object

### III) New external functions, methods, attributes used
- `validate_args_for_test()`: Custom function to validate test arguments

### IV) New theory points
- **Function definition**
  - Basic function: `def function_name(parameter):`
  - Function with type hints: `def function_name(parameter: type) -> return_type:`
  - Type hints document expected parameter and return types
  
- **The `Any` type**
  - `Any` from `typing` module accepts any type of object
  - Usage: `def func(object: Any) -> None:`
  - Useful when function can handle multiple types

- **Conditional statements**
  - `if/elif/else` structure for branching logic
  - `elif` allows multiple conditions to be checked sequentially
  - `else` handles all remaining cases

- **Exception handling with try/except/raise**
  - Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point III) for complete exception handling documentation

### V) Logic used for the exercise
1. Import required modules: `sys`, `typing.Any`, and validation functions
2. Define `print_type_object()` function with `Any` type hint:
   - Use `isinstance()` to check if object is list, tuple, set, or dict
   - Print appropriate message with object type using `type()`
   - Special handling for strings: check if empty using `len()`, raise TypeError if empty
   - Raise TypeError for unrecognized types
3. Define `all_thing_is_obj()` function that:
   - Calls `print_type_object()` wrapped in try/except
   - Catches TypeError exceptions and prints error message
   - Always returns 42
4. Create test data with different data types
5. Validate arguments using custom validation function
6. Test function with various data types (list, tuple, set, dict, strings, integer)
7. Exit program with appropriate return code


## 4. Exercice 03: NULL not found

### I) New libraries used
- `math`: Built-in library for mathematical functions

### II) New built-in functions, methods, attributes used
- `float()`: Built-in function that converts to float type or creates special values
- `math.isnan()`: Math module function that checks if a float is NaN (Not a Number)

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points
- **Null-like values in Python**
  - **None**: Represents absence of value (like NULL in C/C++)
  - **NaN**: `float("NaN")` creates a "Not a Number" special float value
  - **False**: Boolean false value
  - **Zero**: Integer `0` representing no quantity
  - **Empty string**: `""` representing no text content

- **Identity operator `is`**
  - Checks if two variables reference the same object in memory
  - Different from `==` which checks if values are equal
  - Used for: `None`, `True`, `False` (singleton objects)
  - Example: `x is None` (correct), not `x == None`

- **Equality operator `==`**
  - Checks if two values are equal (not necessarily same object)
  - Used for comparing values: numbers, strings, etc.
  - Example: `x == 0` checks if x has value 0

- **Boolean type checking**
  - `bool` is a subclass of `int` in Python
  - `False == 0` is `True` (value equality)
  - `False is False` checks boolean identity specifically
  - Must check `isinstance(object, bool)` before checking identity to distinguish from `0`

- **Checking for NaN**
  - Cannot use `==` or `is` to check for NaN
  - `math.isnan()` is the proper way to detect NaN values
  - NaN is the only value where `x != x` is True

### V) Logic used for the exercise
1. Import required modules: `sys`, `math`, `typing.Any`, and validation functions
2. Define `print_null_type()` function to identify null-like values:
   - Check for `None` using `is` operator (identity check)
   - Check for NaN using `isinstance(object, float)` and `math.isnan()`
   - Check for `False` using `isinstance(object, bool)` and `is False` (order matters!)
   - Check for zero using `isinstance(object, int)` and `== 0`
   - Check for empty string using `isinstance(object, str)` and `len(object) == 0`
   - Raise TypeError for unrecognized types
3. Define `NULL_not_found()` function that:
   - Calls `print_null_type()` wrapped in try/except
   - Returns 0 for recognized null-like values
   - Returns 1 for unrecognized types
4. Create test variables with different null-like values
5. Test with: None, NaN, 0, empty string, False, and a non-null value
6. Exit program with appropriate return code


## 5. Exercice 04: The Even and the Odd

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `int()`: Built-in function that converts string to integer

### III) New external functions, methods, attributes used
No new external functions used.

### IV) New theory points
- **Command line arguments with `sys.argv`**
  - `sys.argv` is a list containing command line arguments
  - `sys.argv[0]` is always the script name
  - `sys.argv[1]`, `sys.argv[2]`, etc. are user-provided arguments
  - Example: `python script.py arg1 arg2`
    - `sys.argv[0]` = `"script.py"`
    - `sys.argv[1]` = `"arg1"`
    - `sys.argv[2]` = `"arg2"`
  - All arguments are received as strings

- **Modulo operator `%`**
  - Returns the remainder of division
  - Syntax: `a % b` returns remainder when a is divided by b
  - Common use: Check if number is even/odd
    - `number % 2 == 0` → even
    - `number % 2 == 1` → odd

- **Exception handling with try/except**
  - Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point III) for complete exception handling documentation

### V) Logic used for the exercise
1. Import `sys` module to access command line arguments
2. Define `validate_args()` function that:
   - Checks if no arguments provided (`len(args) == 1`) → raise ValueError (silent)
   - Checks if too many arguments (`len(args) > 2`) → raise AssertionError with message
   - Extracts first user argument from `sys.argv[1]`
   - Converts string to integer using `int()` in try/except block
   - Catches ValueError and raises AssertionError if conversion fails
   - Returns validated integer
3. Define `check_odd_even()` function that:
   - Uses modulo operator `% 2` to check remainder
   - Prints "I'm Even." if remainder is 0
   - Prints "I'm Odd." if remainder is not 0
4. Main function handles exceptions:
   - Catches ValueError silently (no arguments provided)
   - Catches AssertionError and prints error message
   - Returns appropriate exit codes
5. Exit program using `sys.exit()` with return code


## 6. Interlude: From now on you must follow these additional rules

### I) Script vs Module

**Script:**
- File run directly with `python filename.py`
- Contains executable code that runs when the file is executed
- Typically includes `if __name__ == "__main__":` block

**Module:**
- File imported into another script using `import` or `from ... import ...`
- Provides reusable functions, classes, or variables
- Code at module level runs when imported

### II) Norme: Flake8

**Installation:**
```bash
pip install flake8
# or
python -m pip install flake8
```

**Adding to PATH (if needed for user installation):**

When you install packages with `pip install --user`, executables are placed in `~/.local/bin/` (Linux/Mac) and need to be in your PATH.

**Linux/Mac Setup:**
1. Add to your shell configuration file (`~/.bashrc` or `~/.zshrc`):
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

2. Alternative: Uncomment the existing PATH line in your `~/.zshrc` if it already contains this export

3. Apply changes:
   ```bash
   source ~/.zshrc   # or source ~/.bashrc
   ```
   Or restart your terminal

### III) Exception/Error handling

**Basic Syntax:**
- **`try/except`**: System for handling exceptions (like try/catch in C++)
  - `try:` block contains code that might raise exceptions
  - `except ExceptionType:` catches specific exception types
  - Multiple except blocks can handle different exceptions
  - `except ExceptionType as e:` captures exception object for error messages

**Raising Exceptions:**
- **`raise`**: Built-in keyword that raises an exception (like throw in C++)
  - Syntax: `raise ExceptionType("error message")`
  - Used to signal errors or invalid states

**Common Exception Types:**
- **`ValueError`**: Raised when a function receives correct type but inappropriate value
  - Example: `int("abc")` raises ValueError
  - Common in type conversion failures
  
- **`TypeError`**: Raised when operation is performed on inappropriate type
  - Example: Calling non-callable object, wrong number of arguments
  
- **`AssertionError`**: Raised for assertion failures
  - Used to signal invalid program state or bad input
  - Commonly used for input validation

### IV) `__name__`

**Definition:**
- Special built-in variable in Python that contains the name of the current module

**Usage:**
- When a Python file is run directly: `__name__` is set to `"__main__"`
- When a Python file is imported as a module: `__name__` is set to the module's name

**Purpose:**
- Allows code to be both importable (as a module) and executable (as a script)
- Functions can be imported without running the script's main code

### V) `__doc__`

**Definition:**
- Special built-in variable that contains the documentation string (docstring) of a function, class, or module

**Docstring Format:**
- Written with triple quotes `"""..."""`
- Placed immediately after function, class, or module definition
- First line should be a brief summary

**Purpose:**
- Documents code behavior and usage
- Accessible at runtime via `__doc__` attribute (print(my_function.__doc__))
- Used by help() function and documentation generators


## 7. Exercice 05: First standalone program python

### I) New libraries used
- `string`: Built-in library for string constants and utilities

### II) New built-in functions, methods, attributes used
- `input()`: Built-in function that gets user input from console
- `sum()`: Built-in function that returns sum of all items in an iterable
- `str.isupper()`: String method that checks if character is uppercase
- `str.islower()`: String method that checks if character is lowercase
- `str.isdigit()`: String method that checks if character is a digit
- `str.isspace()`: String method that checks if character is whitespace
- `string.punctuation`: String module constant containing all punctuation characters

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points
- **Using `if __name__ == "__main__"`**
  - Check [Interlude](#6-interlude-from-now-on-you-must-follow-these-additional-rules) (point IV)

- **For loop**
  - Used to iterate over sequences (lists, tuples, strings, etc.)
  - Basic syntax: `for item in iterable:`
  - Each iteration, `item` takes the next value from the iterable
  
- **While loop**
  - Repeats code block while condition is True
  - Syntax: `while condition:`
  - Useful for input validation with user prompts
  - Can create infinite loop with `while True:` (use `break` to exit a loop prematurely)

- **Generator expressions**
  - Compact way to create iterables on-the-fly
  - Syntax: `(expression for item in iterable if condition)`
  - Memory efficient - generates values one at a time
  - Example: `sum(1 for char in text if char.isupper())`
  - Similar to list comprehensions but with parentheses instead of brackets

- **Membership operator `in`**
  - Checks if value exists in a sequence
  - Returns `True` or `False`
  - Example: `'a' in 'apple'` returns `True`
  - Works with strings, lists, tuples, sets, dictionaries

- **Additional exception types**
  - **EOFError**: Raised when `input()` hits end-of-file (Ctrl+D on Unix, Ctrl+Z on Windows)
  - **KeyboardInterrupt**: Raised when user interrupts execution (Ctrl+C)
  - Used to handle input interruptions gracefully

### V) Logic used for the exercise
1. Import required modules: `sys` and `string`
2. Define `validate_args()` function that:
   - Checks if no argument or empty string provided → prompt user with `input()`
   - Uses `while True:` loop to repeatedly prompt until valid input
   - Catches `EOFError` and `KeyboardInterrupt` exceptions for input interruptions
   - Uses `break` to exit loop when valid text is entered
   - Checks if too many arguments → raise AssertionError
   - Returns validated text string
3. Define `count_characters()` function that:
   - Uses generator expressions with `sum()` to count each character type
   - Iterates through text once for each type: upper, lower, digit, space
   - Uses `in` operator to check if character is in `string.punctuation`
   - Returns tuple with all five counts
4. Define `print_results()` function to display formatted output
5. Main function orchestrates:
   - Validates arguments with try/except
   - Unpacks tuple from `count_characters()`
   - Calls `print_results()` with all counts
6. Exit program using `sys.exit()` with return code


## 8. Exercice 06: ft_filter

### I) New libraries used
- `typing`: Built-in library for type hints (importing `Iterator` type)

### II) New built-in functions, methods, attributes used
- `str.split()`: Method that splits string into list of words
- `filter()`: Built-in function that filters iterable based on function
- `list()`: Built-in function that converts an iterable to a list

### III) New external functions, methods, attributes used
No new external functions used.

### IV) New theory points
- **Lambda functions**
  - Anonymous functions created with `lambda` keyword
  - Syntax: `lambda arguments: expression`
  - Can take multiple arguments: `lambda x, y: x + y`
  - Returns result of expression automatically (no `return` statement)
  - Used for simple, one-time operations
  - Example: `lambda x: len(x) > 5`

- **Higher-order functions**
  - Functions that take other functions as parameters
  - `filter(function, iterable)` returns iterator of items where function returns True
  - Common pattern: `filter(lambda x: condition, iterable)`
  - Can also accept `None` as function: filters out falsy values

- **Iterators and the `Iterator` type**
  - Iterator: Object that produces values one at a time
  - Can be converted to list using `list(iterator)`
  - Generator expressions return iterators
  - `Iterator` type hint from `typing` module documents iterator return types

- **Falsy values**
  - Values that evaluate to `False` in boolean context
  - Include: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`
  - Used with `if item:` or `filter(None, iterable)` to remove falsy values

### V) Logic used for the exercise
1. **File: ft_filter.py** - Create custom filter function:
   - Define `ft_filter(function, iterable)` with `Iterator` return type hint
   - Handle two cases using conditional expression:
     - If `function is None`: return generator expression filtering falsy values `(item for item in iterable if item)`
     - If function provided: return generator expression applying function `(item for item in iterable if function(item))`
   - Return iterator (generator expression), not a list
   
2. **File: filterstring.py** - Main program:
   - Import `ft_filter` from ft_filter module
   - Define `validate_args()` function:
     - Check exactly 3 arguments (script name + 2 args)
     - Extract string and integer arguments from `sys.argv`
     - Convert second argument to integer with try/except
     - Return tuple of validated arguments
   - In main function:
     - Validate arguments with exception handling
     - Split input string into list of words using `str.split()`
     - Create lambda function `lambda x: len(x) > integer_arg` to check word length
     - Apply `ft_filter()` with lambda and word list
     - Convert iterator result to list using `list()` for display
3. Test function demonstrates usage and compares with built-in `filter()`


## 9. Exercice 07: Dictionaries SoS

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `str.upper()`: Method that converts string to uppercase
- `str.rstrip()`: Method that removes trailing whitespace

### III) New external functions, methods, attributes used
No new external functions used.

### IV) New theory points
- **Dictionary as lookup table**
  - Dictionaries used to map keys to values for fast lookups
  - Access values using square bracket notation: `dict[key]`
  - Raises `KeyError` if key doesn't exist
  - Common use: translation tables, configuration mappings
  - Example: `morse_code = {"A": ".-", "B": "-..."}`

- **String concatenation with `+=`**
  - Augmented assignment operator: `result += new_part`
  - Shorthand for `result = result + new_part`
  - Builds strings incrementally in loops
  - Example: Building morse code character by character

- **KeyError exception**
  - Raised when accessing non-existent dictionary key
  - Can be caught with try/except to handle invalid lookups
  - Alternative: use `dict.get(key, default)` to avoid exception

### V) Logic used for the exercise
1. Import `sys` module for command line arguments
2. Define `validate_args()` function:
   - Check exactly 2 arguments (script name + 1 string argument)
   - Raise AssertionError if wrong number of arguments
   - Return string argument
3. Define `get_dict()` function:
   - Create dictionary mapping uppercase letters, digits, and space to morse code
   - Each morse code representation includes trailing space for separation
   - Return morse code dictionary
4. Define `encrypt()` function:
   - Get morse code dictionary
   - Initialize empty result string
   - Convert input message to uppercase using `str.upper()`
   - Iterate through each character with for loop
   - For each character:
     - Try to look up morse code using `dict[key]` access
     - Concatenate morse code to result using `+=` operator
     - Catch `KeyError` for invalid characters and raise AssertionError
   - Remove trailing whitespace using `str.rstrip()` from final result
   - Return encrypted message
5. Main function orchestrates:
   - Validate arguments with try/except for AssertionError
   - Call encrypt function
   - Display encrypted message
6. Exit program using `sys.exit()` with return code


## 10. Exercice 08: Loading ...

### I) New libraries used
- `time`: Built-in library for time operations (importing `sleep` function)
- `tqdm`: External library for progress bars (for comparison only)

### II) New built-in functions, methods, attributes used
- `enumerate()`: Built-in function that returns (index, value) pairs from iterable
- `range()`: Built-in function that creates sequence of numbers
- `str.ljust()`: String method that left-justifies string with padding
- `print()`: Built-in function (using `end` parameter for inline printing)
- `time.sleep()`: Time module function that pauses execution for specified seconds

### III) New external functions, methods, attributes used
- `tqdm()`: External function from tqdm library for creating progress bars (comparison only)

### IV) New theory points
- **Generator functions with `yield`**
  - Functions that use `yield` instead of `return`
  - Create iterators that can be paused and resumed
  - Each call to `yield` produces one value and suspends execution
  - Function state is preserved between yields
  - Memory efficient - generates values on-demand rather than storing all at once
  - Perfect for progress bars, data streams, large datasets
  - Example: Generator can process millions of items using minimal memory

- **The `enumerate()` function**
  - `enumerate(iterable)` returns (index, value) pairs
  - Starts counting from 0 by default
  - Syntax: `for i, item in enumerate(iterable):`
  - Useful for tracking position while iterating
  - Can specify start value: `enumerate(iterable, start=1)`

- **String multiplication and formatting**
  - String multiplication: `"x" * n` creates string repeated n times
  - `str.ljust(width, fillchar)`: Left-justifies string with padding
  - Example: `"abc".ljust(10, " ")` → `"abc       "`
  - Useful for creating visual elements like progress bars

- **Print parameters**
  - `print(text, end="")`: Prevents automatic newline after printing
  - Default `end="\n"` adds newline; `end=""` prints inline
  - Allows continuous updates on same line when combined with `\r`

### V) Logic used for the exercise
1. Import required modules: `sys`, `time.sleep`, and validation functions
2. Define `ft_tqdm()` generator function with `range` parameter:
   - Get total count using `len(lst)` on range object
   - Use `enumerate(lst)` to iterate with both index and item
   - For each iteration:
     - Calculate percentage: `(i + 1) / total * 100`
     - Calculate filled width for visual bar: `(i + 1) / total * bar_width`
     - Build bar string:
       - Use string multiplication: `"=" * filled_width` for filled portion
       - Add `">"` at the end if not complete
       - Use `str.ljust(bar_width, " ")` to pad to full width
     - Create progress line with f-string: `"\r{percentage}%|[{bar}]| {i + 1}/{total}"`
     - Print with `end=""` to avoid newline (allows overwriting with `\r`)
     - **Yield** item to calling code (makes this a generator)
   - Print final newline after loop completes
3. Main function:
   - Validate arguments with try/except
   - Use `ft_tqdm(range(333))` in for loop
   - Each iteration calls `sleep(0.005)` to simulate work
   - Progress bar updates automatically on each yield
4. Demonstrates generator function creating live-updating progress display


## 11. Exercice 09: My first package creation

### I) New libraries used
No new libraries used in the package code itself.

**Build tools required (installed separately):**
- `setuptools`: Tool for package building
- `wheel`: Tool for creating wheel distributions
- `build`: Modern Python package build tool

### II) New built-in functions, methods, attributes used
- `list.count()`: Method that counts occurrences of item in list

### III) New external functions, methods, attributes used
No new external functions used.

### IV) New theory points

- **Python Package Structure**
  - **Package directory**: Contains `__init__.py` to mark as package
  - **`__init__.py`**: Makes directory importable as Python package
    - Can be empty or contain initialization code
    - Defines package's public API with `__all__`
    - Can set `__version__` for version tracking
  - **Module docstring**: Triple-quoted string at top of `__init__.py` documenting package
  
- **Relative imports**
  - `from .module import function`: Import from same package
  - `.` refers to current package directory
  - `..` would refer to parent package
  - Example: `from .core import count_in_list`

- **`__all__` list**
  - Defines public API of package/module
  - Lists names that are exported when using `from package import *`
  - Example: `__all__ = ["count_in_list"]`
  - Good practice for controlling what users can access

- **`__version__` attribute**
  - Convention for storing package version
  - Typically set in `__init__.py`
  - Accessible as `package.__version__`
  - Should match version in `pyproject.toml`

- **`pyproject.toml` configuration**
  - Modern standard for Python project configuration (PEP 518)
  - Replaces old `setup.py` approach
  - **Key sections:**
    - `[build-system]`: Specifies build requirements (setuptools, wheel)
    - `[project]`: Project metadata (name, version, description, license)
    - `requires-python`: Minimum Python version
    - `classifiers`: Package categorization for PyPI

- **Package building and distribution**
  - **Build command**: `python -m build`
    - Creates both `.tar.gz` (source) and `.whl` (wheel) distributions
    - Output goes to `dist/` directory
  - **Install command**: `pip install ./dist/package-version.tar.gz`
  - **Verify installation**: `pip show -v package_name`
  - **Uninstall**: `pip uninstall package_name`
  - **List packages**: `pip list`

- **Build artifacts**
  - `dist/`: Contains built package files (.tar.gz and .whl)
  - `build/`: Temporary build directory
  - `*.egg-info/`: Package metadata directory
  - Clean up with: `rm -rf build/ dist/ *.egg-info`

### V) Logic used for the exercise

**1. Create package structure:**
```
ex09/
├── ft_package/
│   ├── __init__.py      # Package initialization
│   └── core.py          # Core functionality
├── pyproject.toml       # Package configuration
├── README.md            # Package documentation
└── LICENSE              # License file
```

**2. File: `ft_package/core.py`**
- Import `Any` type from `typing` module
- Define `count_in_list(lst: list, item: Any) -> int` function
- Function wraps `list.count()` method
- Add docstring with Args, Returns, and Raises sections

**3. File: `ft_package/__init__.py`**
- Add module-level docstring describing package
- Import function from core module: `from .core import count_in_list`
- Define `__all__ = ["count_in_list"]` to expose public API
- Set `__version__ = "0.0.1"` for version tracking

**4. File: `pyproject.toml`**
- Configure `[build-system]` with setuptools and wheel requirements
- Define `[project]` metadata:
  - Package name, version, description
  - README file, Python version requirement
  - License and classifiers for package categorization

**5. Build and distribute:**
- Install build tools: `python -m pip install --upgrade build wheel`
- Build package: `python -m build` (creates `dist/` directory)
- Install locally: `pip install ./dist/ft_package-0.0.1.tar.gz`
- Test by importing: `from ft_package import count_in_list`
- Verify: `pip show -v ft_package`

**6. Package lifecycle commands:**
- Build: `python -m build`
- Install: `pip install ./dist/ft_package-0.0.1.tar.gz`
- Verify: `pip show -v ft_package`
- Uninstall: `pip uninstall ft_package`
- Clean: `rm -rf build/ dist/ *.egg-info`
- List installed: `pip list`

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
