<div align="center">

# MODULE 04 - Dunder

</div>

## Summary

[1. Exercice 00: Calculate my statistics](#1-exercice-00-calculate-my-statistics)  
[2. Exercice 01: Outer_inner](#2-exercice-01-outer_inner)  
[3. Exercice 02: my first decorating](#3-exercice-02-my-first-decorating)  
[4. Exercice 03: data class](#4-exercice-03-data-class)  
[Additional Resources](#additional-resources)


## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- There are additional resources at the end if you want to explore a concept in more depth


## Introduction

This module focuses on advanced Python concepts including decorators and special methods:

- **Decorators**: Functions that modify or enhance other functions
- **Variable arguments**: Handling flexible function parameters
- **Function introspection**: Examining function properties at runtime
- **Advanced dunder methods**: More special methods for custom behavior


## 1. Exercice 00: Calculate my statistics

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `sorted()`: Built-in function that returns sorted list from iterable

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **Variable positional arguments (`*args`)**
  - Allows function to accept any number of positional arguments
  - Syntax: `def function(*args):`
  - `*args` collects all positional arguments into a tuple
  - Example: `func(1, 2, 3)` → `args = (1, 2, 3)`
  - Can iterate over: `for arg in args:`
  - Useful when number of arguments unknown in advance
  - Convert to list: `list(args)`

- **Variable keyword arguments (`**kwargs`)**
  - Allows function to accept any number of keyword arguments
  - Syntax: `def function(**kwargs):`
  - `**kwargs` collects all keyword arguments into a dictionary
  - Example: `func(a=1, b=2)` → `kwargs = {'a': 1, 'b': 2}`
  - Access values: `kwargs['key']` or `kwargs.values()`
  - Access keys: `kwargs.keys()`
  - Useful for flexible function interfaces

- **Combining `*args` and `**kwargs`**
  - Can use both in same function
  - Order matters: `def func(*args, **kwargs):`
  - `*args` must come before `**kwargs`
  - Example: `func(1, 2, x=3, y=4)` → `args=(1,2)`, `kwargs={'x':3, 'y':4}`
  - Very flexible function signatures
  - Common in decorators and wrapper functions

- **The `sorted()` function**
  - Returns new sorted list from any iterable
  - Syntax: `sorted(iterable, key=None, reverse=False)`
  - Does not modify original (unlike `list.sort()`)
  - Returns list even if input is tuple, set, etc.
  - Example: `sorted([3, 1, 2])` → `[1, 2, 3]`
  - Can sort generator expressions: `sorted(x for x in data)`

- **Statistical measures**
  - **Mean (average)**: Sum of all values divided by count
    - Formula: `mean = sum(values) / len(values)`
    - Center point of data
  - **Median**: Middle value when data is sorted
    - For odd count: middle element
    - For even count: average of two middle elements
    - Less affected by outliers than mean
  - **Quartiles**: Divide sorted data into quarters
    - Q1 (25th percentile): Value at 25% position
    - Q3 (75th percentile): Value at 75% position
    - Index calculation: `int(n * 0.25)`, `int(n * 0.75)`
  - **Variance**: Average of squared differences from mean
    - Formula: `sum((x - mean)² for x in values) / n`
    - Measures spread of data
  - **Standard deviation**: Square root of variance
    - Formula: `variance ** 0.5`
    - Same units as original data
    - Common measure of dispersion

- **Square root using power operator**
  - `value ** 0.5` computes square root
  - Equivalent to `math.sqrt(value)` but doesn't need import
  - Power operator `**` for exponentiation
  - Example: `16 ** 0.5 = 4.0`
  - Already covered in module-00, but used here for square root

- **Dictionary as method dispatcher**
  - Store methods as dictionary values
  - Keys are strings identifying methods
  - Syntax: `methods = {"name": self.method}`
  - Call dynamically: `methods[key]()`
  - Cleaner than long if/elif chains
  - Pattern: `stat_methods = {"mean": self.calculate_mean, "median": self.calculate_median}`
  - Flexible dispatching based on string input

- **Computed properties**
  - Properties that calculate value instead of storing it
  - Example: `size` property returns `len(self._values)`
  - No setter needed - read-only computed value
  - Keeps code clean: access like attribute, computed like method
  - Pattern: `@property` without corresponding setter

- **Separation of concerns (OOP pattern)**
  - Different classes handle different responsibilities
  - `Data` class: validation and storage
  - `StatisticsCalculator` class: calculations
  - Wrapper function: user interface
  - Makes code modular, testable, maintainable
  - Single Responsibility Principle

### V) Logic used for the exercise
1. Define `Data` class:
   - Handles data validation and storage
   - `__init__` method takes raw data list
   - `values` property with getter and setter:
     - Setter validates data with `_validate_data()`
     - Converts and sorts: `sorted(float(x) for x in raw_data)`
     - Stores as `_values`
     - Getter returns sorted values
   - `size` computed property:
     - Returns `len(self._values)`
     - No setter - read-only
   - `_validate_data()` static method:
     - Checks if data is non-empty
     - Validates all items are numeric (int or float)
     - Raises `ValueError` or `TypeError` on failure
2. Define `StatisticsCalculator` class:
   - Takes `Data` instance in `__init__`
   - Stores as `self.data`
   - `calculate_mean()`:
     - Returns `sum(self.data.values) / self.data.size`
   - `calculate_median()`:
     - Gets sorted values and size
     - If even count: average of two middle elements
     - If odd count: middle element
   - `calculate_quartile()`:
     - Calculates Q1 at 25% position: `int(n * 0.25)`
     - Calculates Q3 at 75% position: `int(n * 0.75)`
     - Returns list `[Q1, Q3]`
   - `calculate_variance()`:
     - Gets mean
     - Calculates sum of squared differences: `sum((x - mean) ** 2 for x in values)`
     - Divides by size
   - `calculate_std()`:
     - Gets variance
     - Returns square root: `variance ** 0.5`
   - `get_statistic()`:
     - Creates dictionary mapping stat names to methods
     - Calls and returns appropriate method: `stat_methods[stat_name]()`
3. Define `ft_statistics()` function:
   - Takes `*args` (data values) and `**kwargs` (stat names)
   - Wraps OOP classes in user-friendly interface
   - Try to create `Data` instance from `list(args)`
   - If validation fails, print "ERROR" for each requested stat
   - Create `StatisticsCalculator` with validated data
   - Loop through `kwargs.values()` (stat names)
   - Try to get each statistic with `get_statistic()`
   - Catch `KeyError` for invalid stat names
   - Print results: `"{stat_name} : {result}"`
4. Main function demonstrates:
   - Call with data and multiple stat requests
   - Uses keyword arguments for stat names
   - Handles invalid data (empty args)
   - Handles invalid stat names (ignored)


## 2. Exercice 01: Outer_inner

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **Closures**
  - Function defined inside another function that captures variables from outer scope
  - Inner function "closes over" variables from enclosing function
  - Outer function returns inner function
  - Inner function remembers outer variables even after outer function completes
  - Powerful pattern for data encapsulation and state preservation
  - Example: `outer()` returns `inner()` which remembers `x` and `count`

- **Functions as first-class objects**
  - Functions can be passed as arguments to other functions
  - Functions can be returned from other functions
  - Functions can be assigned to variables
  - Functions can be stored in data structures
  - Enables functional programming patterns
  - Example: `outer(3, square)` passes `square` function as argument

- **The `nonlocal` keyword**
  - Allows nested function to modify variables from enclosing (non-global) scope
  - Syntax: `nonlocal variable_name`
  - Without `nonlocal`, assignment creates new local variable
  - With `nonlocal`, assignment modifies enclosing scope variable
  - Can specify multiple variables: `nonlocal count, x`
  - Only works for enclosing function scopes (not global)
  - Essential for closures that need to modify captured variables

- **Variable scopes in Python**
  - **Local**: Variables defined inside current function
  - **Enclosing**: Variables in outer (enclosing) function scopes
  - **Global**: Variables defined at module level
  - **Built-in**: Python built-in names
  - **LEGB rule**: Python searches in order: Local → Enclosing → Global → Built-in
  - `nonlocal` accesses Enclosing scope
  - `global` accesses Global scope

- **Stateful functions**
  - Functions that maintain state between calls
  - Closures provide state without classes
  - Each closure instance has independent state
  - Example: `my_counter` and `another_counter` have separate states
  - Alternative to class-based state management
  - Lightweight compared to full classes

- **Factory functions**
  - Functions that create and return other functions
  - Each call creates new closure with independent state
  - Pattern: outer function is factory, inner function is product
  - Example: `outer(3, square)` creates new counter starting at 3
  - Useful for creating customized functions dynamically
  - Common in functional programming

### V) Logic used for the exercise
1. Define `MathOperations` class with static methods:
   - `square(x)`: Returns `x * x`
   - `pow(x)`: Returns `x ** x` (x to the power of x)
   - `outer(x, function)`: Factory function that creates closures
     - Takes initial value `x` and a function to apply
     - Initializes `count = 0` in outer scope
     - Defines nested `inner()` function:
       - Uses `nonlocal count, x` to access outer scope variables
       - Increments `count += 1`
       - Applies function: `x = function(x)`
       - Returns new value of `x`
     - Returns `inner` function (closure)
2. Define wrapper functions at module level:
   - `square(x)`: Calls `MathOperations.square(x)`
   - `pow(x)`: Calls `MathOperations.pow(x)`
   - `outer(x, function)`: Calls `MathOperations.outer(x, function)`
   - Provide convenient interface without class prefix
3. Main function demonstrates closures:
   - Create first closure: `my_counter = outer(3, square)`
     - `my_counter` is `inner` function with `x=3`, `count=0`
     - First call: `x = 3*3 = 9`, returns 9
     - Second call: `x = 9*9 = 81`, returns 81
     - Third call: `x = 81*81 = 6561`, returns 6561
   - Create second closure: `another_counter = outer(1.5, pow)`
     - Independent state from `my_counter`
     - `another_counter` has `x=1.5`, `count=0`
     - First call: `x = 1.5**1.5 ≈ 1.837`, returns ~1.837
     - Second call: `x = 1.837**1.837 ≈ 2.028`, returns ~2.028
     - Third call: continues applying `pow` to result
   - Demonstrates:
     - State preservation across calls
     - Independent closure instances
     - Functions as arguments
     - Flexible behavior based on passed function


## 3. Exercice 02: my first decorating

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **`Callable` type hint** (from `typing` module)
  - Type hint for callable objects (functions, methods, classes)
  - Syntax: `Callable[[arg_types], return_type]` or just `Callable`
  - `Callable` alone means any callable object
  - `Callable[[int, str], bool]` means function taking (int, str) and returning bool
  - Used for function parameters and return types
  - Example: `def callLimiter(function: Callable) -> Callable:`

- **Decorators**
  - Functions that modify or enhance other functions
  - Takes a function as input, returns a modified function
  - Wraps original function to add behavior before/after/around it
  - Pattern: Decorator returns wrapper function that calls original
  - Used for: logging, timing, access control, caching, validation
  - Example: `callLimiter` decorator wraps functions to limit calls

- **The `@` decorator syntax**
  - Syntactic sugar for applying decorators to functions
  - `@decorator` placed above function definition
  - Equivalent to: `function = decorator(function)`
  - Example:
    ```python
    @callLimit(3)
    def f():
        pass
    # Equivalent to: f = callLimit(3)(f)
    ```
  - Can stack multiple decorators (applied bottom-to-top)
  - Cleaner and more readable than manual application

- **Decorator factories (decorators with arguments)**
  - Functions that return decorators
  - Allows parameterizing decorator behavior
  - Requires three levels of nesting:
    1. **Factory**: Takes decorator arguments, returns decorator
    2. **Decorator**: Takes function to wrap, returns wrapper
    3. **Wrapper**: Takes function arguments, calls original with added behavior
  - Example: `callLimit(3)` is factory, returns `callLimiter` decorator
  - Pattern:
    ```python
    def factory(param):          # Level 1: Factory with params
        def decorator(func):     # Level 2: Actual decorator
            def wrapper(*args):  # Level 3: Wrapper function
                # Use param and func here
                return func(*args)
            return wrapper
        return decorator
    ```

- **Function wrapping pattern**
  - Wrapper function intercepts calls to original function
  - Can execute code before calling original
  - Can execute code after calling original
  - Can modify arguments before passing to original
  - Can modify return value before returning
  - Can conditionally call or skip original function
  - Example: `limit_function` checks count before calling original

- **Decorator state with closures**
  - Decorators can maintain state using closure variables
  - State persists across multiple function calls
  - Each decorated function gets independent state
  - Example: `count` variable tracks calls per decorated function
  - Combines closure and decorator patterns

### V) Logic used for the exercise
1. Define `callLimit(limit)` decorator factory:
   - Takes `limit` parameter (maximum allowed calls)
   - Initializes `count = 0` in factory scope (closure variable)
   - Returns `callLimiter` decorator function
2. Define `callLimiter(function)` decorator:
   - Takes `function` to be wrapped
   - Defines `limit_function(*args, **kwds)` wrapper:
     - Uses `nonlocal count` to access factory scope variable
     - Checks if `count < limit`:
       - If true: increments count, calls and returns `function(*args, **kwds)`
       - If false: prints error message with function name
     - No return value when limit exceeded (implicitly returns `None`)
   - Returns `limit_function` wrapper
3. Main function demonstrates decorator usage:
   - Define `f()` with `@callLimit(3)` decorator:
     - Can be called maximum 3 times
     - Each call prints "f()"
   - Define `g()` with `@callLimit(1)` decorator:
     - Can be called maximum 1 time
     - Each call prints "g()"
   - Loop 3 times calling both functions:
     - Iteration 0: `f()` succeeds (count=1), `g()` succeeds (count=1)
     - Iteration 1: `f()` succeeds (count=2), `g()` fails (prints error)
     - Iteration 2: `f()` succeeds (count=3), `g()` fails (prints error)
   - Demonstrates:
     - Independent state for each decorated function
     - Call limiting behavior
     - Decorator syntax with arguments
     - Graceful handling when limit exceeded


## 4. Exercice 03: data class

### I) New libraries used
- `random`: Built-in module for generating random numbers and making random selections
- `dataclasses`: Built-in module providing decorator and functions for creating dataclasses (Python 3.7+)

### II) New built-in functions, methods, attributes used
- `random.choices(sequence, k)`: Random module function that returns list of k elements chosen from sequence with replacement
- `str.capitalize()`: String method that returns string with first character capitalized and rest lowercased

### III) New external functions, methods, attributes used
- `@dataclass`: Decorator from dataclasses module that automatically generates special methods (`__init__()`, `__repr__()`, `__eq__()`) for classes
- `field()`: Function from dataclasses module that customizes individual field behavior (default, default_factory, init, repr parameters)

### IV) New theory points

- **Dataclasses**
  - Special classes primarily for storing data
  - Introduced in Python 3.7 via `dataclasses` module
  - Reduce boilerplate code compared to regular classes
  - Automatically generate common methods based on class attributes
  - Use type hints to declare fields
  - Benefits:
    - Less code to write and maintain
    - Cleaner and more readable
    - Consistent implementation of common methods
    - Built-in support for default values and factories

- **Auto-generated methods in dataclasses**
  - **`__init__()`**: Automatically generated from type-hinted attributes
    - Takes parameters for each field (unless `init=False`)
    - Assigns values to instance attributes
  - **`__repr__()`**: Automatically generated string representation
    - Format: `ClassName(field1=value1, field2=value2, ...)`
    - Useful for debugging and logging
  - **`__eq__()`**: Automatically generated equality comparison
    - Compares all fields for equality
    - Returns `True` if all fields match

- **Default values in dataclasses**
  - **Simple defaults**: Assign value directly
    - Example: `active: bool = True`
    - All instances share same default
    - Only for immutable types (int, str, bool, tuple, etc.)
  - **`default_factory` for mutable defaults**: Use function to create value
    - Example: `id: str = field(default_factory=generate_id)`
    - Function called once per instance
    - Creates new object for each instance
    - Required for mutable types (list, dict, etc.)
    - Prevents shared mutable default bug

- **`init=False` parameter**
  - Excludes field from `__init__()` parameters
  - Field must have default value or `default_factory`
  - Used for computed or generated fields
  - Value set in `__post_init__()` or via `default_factory`
  - Example: `login` computed from `name` and `surname`
  - Example: `id` generated randomly

- **`__post_init__()` method**
  - Special method called after `__init__()`
  - Allows custom initialization logic after dataclass initialization
  - Can access all fields (including those with `init=False`)
  - Used for:
    - Computing derived fields
    - Validation
    - Complex initialization
  - Example: Computing `login` from `name[0]` and `surname`

- **Field ordering in dataclasses**
  - Fields without defaults must come before fields with defaults
  - Same rule as function parameters
  - Example order:
    1. `name: str` (no default)
    2. `surname: str` (no default)
    3. `active: bool = True` (has default)
    4. `login: str = field(init=False)` (excluded from init)

### V) Logic used for the exercise
1. Define `generate_id()` helper function:
   - Uses `random.choices()` to select 15 random characters
   - Source: `string.ascii_lowercase` (letters a-z)
   - Returns 15-character random string
   - Example: `"xkcdpqrmnoabcxy"`
   - Used as `default_factory` for `id` field
2. Define `Student` dataclass with `@dataclass` decorator:
   - **Required fields** (no defaults, must be provided):
     - `name: str` - student's first name
     - `surname: str` - student's last name
   - **Optional field** (has default):
     - `active: bool = True` - whether student is active
   - **Computed field** (`init=False`, set in `__post_init__`):
     - `login: str = field(init=False)` - generated from name and surname
   - **Generated field** (`init=False`, has `default_factory`):
     - `id: str = field(init=False, default_factory=generate_id)` - random ID
3. Implement `__post_init__()` method:
   - Called automatically after `__init__()`
   - Computes `login` from:
     - First letter of `name`, capitalized
     - Full `surname`, lowercased
   - Example: `name="Edward"`, `surname="agle"` → `login="Eagle"`
4. Main function demonstrates dataclass usage:
   - Create student: `Student(name="Edward", surname="agle")`
   - Only need to provide `name` and `surname`
   - `active` defaults to `True`
   - `login` computed automatically as `"Eagle"`
   - `id` generated automatically (random 15-char string)
   - Print uses auto-generated `__repr__()`
   - Output: `Student(name='Edward', surname='agle', active=True, login='Eagle', id='...')`
5. Demonstrates dataclass benefits:
   - Minimal code for full-featured class
   - No manual `__init__()`, `__repr__()`, `__eq__()` needed
   - Clean syntax with type hints
   - Flexible field customization with `field()`
   - Custom post-initialization logic


## Additional Resources

- [Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python *args and **kwargs](https://realpython.com/python-kwargs-and-args/)
- [Functools Module](https://docs.python.org/3/library/functools.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

