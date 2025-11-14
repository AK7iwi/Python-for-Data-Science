<div align="center">

# MODULE 03 - OOP

</div>

## Summary

[1. Exercice 00: GOT S1E9](#1-exercice-00-got-s1e9)  
[2. Exercice 01: GOT S1E7](#2-exercice-01-got-s1e7)  
[3. Exercice 02: Now it's weird!](#3-exercice-02-now-its-weird)  
[4. Exercice 03: Calculate my vector](#4-exercice-03-calculate-my-vector)  
[5. Exercice 04: Calculate my dot product](#5-exercice-04-calculate-my-dot-product)  
[Additional Resources](#additional-resources)


## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- There are additional resources at the end if you want to explore a concept in more depth


## Introduction

This module focuses on Object-Oriented Programming (OOP) in Python:

- **Classes and Objects**: Creating and using custom data types
- **Inheritance**: Building class hierarchies and code reuse
- **Encapsulation**: Data hiding and access control
- **Special Methods**: Customizing object behavior with dunder methods


## 1. Exercice 00: GOT S1E9

### I) New libraries used
- `abc`: Built-in module for abstract base classes

### II) New built-in functions, methods, attributes used
- `super()`: Built-in function that returns proxy object for parent class methods
- `object.__dict__`: Special attribute containing object's attribute dictionary

### III) New external functions, methods, attributes used
- `ABC`: Abstract base class from abc module
- `abstractmethod`: Decorator from abc module marking method as abstract

### IV) New theory points

- **Object-Oriented Programming (OOP) basics**
  - Paradigm based on "objects" that contain data (attributes) and code (methods)
  - Objects are instances of classes (blueprints/templates)
  - Four main principles: Encapsulation, Abstraction, Inheritance, Polymorphism
  - Python is multi-paradigm: supports OOP, procedural, and functional programming

- **Class definition**
  - `class ClassName:` defines new class (custom type)
  - Class names use PascalCase convention (e.g., `Character`, `MyClass`)
  - Classes can have docstrings immediately after definition
  - Blueprint for creating objects with shared structure and behavior

- **Instance attributes and `self`**
  - `self`: Reference to current instance of class
  - First parameter of instance methods (automatically passed)
  - Used to access instance attributes: `self.attribute_name`
  - Each instance has its own copy of attributes
  - Convention: could be named differently but `self` is standard

- **The `__init__` method (constructor)**
  - Special method called when creating new instance
  - Syntax: `def __init__(self, parameters):`
  - Initializes instance attributes
  - Not required (Python provides default if absent)
  - Example: `def __init__(self, first_name: str):`
  - Can have default parameter values

- **Creating instances**
  - Syntax: `instance = ClassName(arguments)`
  - Calls `__init__` automatically
  - Returns new instance object
  - Example: `ned = Stark("Ned")`

- **Instance methods**
  - Functions defined inside class
  - Always take `self` as first parameter
  - Called on instances: `instance.method()`
  - Can access and modify instance attributes via `self`
  - Example: `def die(self) -> None:`

- **Inheritance**
  - Mechanism for creating new class based on existing class
  - Syntax: `class ChildClass(ParentClass):`
  - Child inherits all attributes and methods from parent
  - Can override parent methods with same name
  - Promotes code reuse and hierarchical relationships
  - Example: `class Stark(Character):` - Stark inherits from Character

- **The `super()` function**
  - Returns proxy object that delegates method calls to parent class
  - Syntax: `super().method_name(arguments)`
  - Common use: `super().__init__(arguments)` calls parent constructor
  - Allows access to overridden parent methods
  - Useful in inheritance hierarchies

- **Abstract Base Classes (ABC)**
  - Classes that cannot be instantiated directly
  - Serve as templates/interfaces for derived classes
  - Define methods that must be implemented by child classes
  - From `abc` module: `from abc import ABC, abstractmethod`
  - Syntax: `class MyClass(ABC):`
  - Enforces contract: child classes must implement abstract methods

- **The `@abstractmethod` decorator**
  - Marks method as abstract (must be implemented by child class)
  - Applied above method definition: `@abstractmethod`
  - Abstract methods can have implementation (optional)
  - Child class cannot be instantiated unless all abstract methods implemented
  - Useful for defining interfaces
  - **Note**: In this exercise, `die()` is abstract for learning purposes, but in real-world scenarios, if all subclasses have the same behavior, it should be a normal method in the parent class instead

- **Properties with `@property` decorator**
  - Converts method into "managed attribute"
  - Syntax: `@property` above getter method
  - Allows method to be accessed like attribute: `instance.attribute` (not `instance.attribute()`)
  - Enables validation and computed attributes
  - Read-only by default unless setter defined

- **Property setters**
  - Syntax: `@property_name.setter` above setter method
  - Allows validation when setting attribute value
  - Called automatically: `instance.attribute = value`
  - Paired with `@property` getter
  - Example: `@first_name.setter`

- **Private attributes convention**
  - Python has no true private attributes
  - Single underscore prefix: `_attribute` indicates "internal use"
  - Convention: "protected" - shouldn't be accessed outside class
  - Used with properties: store in `_attribute`, access via property
  - Not enforced by Python, just a convention

- **The `@staticmethod` decorator**
  - Defines method that doesn't require instance (`self`) or class reference
  - Syntax: `@staticmethod` above method definition
  - Called on class or instance: `Class.method()` or `instance.method()`
  - No automatic `self` parameter
  - Used for utility functions related to class but not needing instance data
  - Example: Validation helpers

- **The `__dict__` attribute**
  - Special attribute containing dictionary of object's attributes
  - Keys: attribute names (strings)
  - Values: attribute values
  - Syntax: `instance.__dict__`
  - Doesn't include methods or class attributes
  - Useful for debugging and introspection

- **Module docstrings**
  - Triple-quoted string at beginning of module file
  - Describes purpose of entire module
  - Accessible via module's `__doc__` attribute
  - Convention: One-line summary

### V) Logic used for the exercise
1. Import abc module for abstract base classes
2. Define `Character` abstract base class:
   - Inherits from `ABC` to make it abstract
   - Add class docstring describing purpose
   - Define `__init__` method:
     - Takes `first_name` (str) and `is_alive` (bool, default True)
     - Assigns to instance attributes using property setters
   - Define `first_name` property:
     - `@property` getter returns `_first_name` private attribute
     - `@first_name.setter` validates and sets value
     - Calls `_validate_string_attribute()` for validation
   - Define `is_alive` property:
     - `@property` getter returns `_is_alive` private attribute
     - `@is_alive.setter` validates and sets value
     - Calls `_validate_boolean_attribute()` for validation
   - Define `_validate_string_attribute()` static method:
     - Takes value and attribute name
     - Checks if value is string with `isinstance()`
     - Checks if value is non-empty with `str.strip()`
     - Raises `TypeError` or `ValueError` if invalid
   - Define `_validate_boolean_attribute()` static method:
     - Takes value and attribute name
     - Checks if value is boolean
     - Raises `TypeError` if invalid
   - Define abstract `die()` method:
     - Marked with `@abstractmethod` decorator
     - Must be implemented by child classes
     - Only has docstring and `pass`
3. Define `Stark` class inheriting from `Character`:
   - Syntax: `class Stark(Character):`
   - Add class docstring
   - Define `__init__` method:
     - Takes same parameters as parent
     - Calls parent constructor: `super().__init__(first_name, is_alive)`
   - Implement required `die()` method:
     - Sets `self.is_alive` to `False`
     - Fulfills abstract method requirement
4. Main function demonstrates usage:
   - Create `Ned` instance: `Stark("Ned")`
   - Print `__dict__` to see instance attributes
   - Access `is_alive` property
   - Call `die()` method
   - Print docstrings using `__doc__` attribute
   - Create `Lyanna` instance with custom `is_alive` value
   - Print `__dict__` again


## 2. Exercice 01: GOT S1E7

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `__str__`: Special method that returns human-readable string representation
- `__repr__`: Special method that returns official string representation
- `type()`: Built-in function that returns type of object (already used in module-00, but new usage with `__name__` attribute)

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **Special methods (dunder methods)**
  - Methods with double underscores before and after name: `__method__`
  - Called "magic methods" or "dunder methods" (double underscore)
  - Automatically called by Python in specific situations
  - Allow customization of object behavior
  - **Purpose**: Rewrite/override default Python functions and operators for custom classes
  - Examples: `__init__`, `__str__`, `__repr__`, `__add__`, etc.
  - Enable objects to work with built-in functions and operators

- **The `__str__` method**
  - Defines human-readable string representation of object
  - Called by `str(object)` and `print(object)`
  - Should return user-friendly, readable string
  - Signature: `def __str__(self) -> str:`
  - If not defined, Python uses `__repr__` instead
  - Example return: `"Vector: ('Baratheon', 'brown', 'dark')"`

- **The `__repr__` method**
  - Defines official string representation of object
  - Called by `repr(object)` and in interactive interpreter
  - Should return unambiguous, developer-focused string
  - Ideally: string that could recreate object
  - Signature: `def __repr__(self) -> str:`
  - If `__str__` not defined, `__repr__` used for `print()`
  - Example return: `"Vector: ('Lannister', 'blue', 'light')"`

- **Difference between `__str__` and `__repr__`**
  - `__str__`: For end users (readable, friendly)
  - `__repr__`: For developers (unambiguous, debugging)
  - Best practice: implement both
  - In this exercise: both return same format for simplicity

- **The `@classmethod` decorator**
  - Creates method that receives class as first argument instead of instance
  - Syntax: `@classmethod` above method definition
  - First parameter conventionally named `cls` (refers to class itself)
  - Can be called on class or instance: `ClassName.method()` or `instance.method()`
  - Used for alternative constructors or factory methods
  - Cannot access instance attributes (no `self`), only class-level data

- **Class methods vs static methods**
  - **Class method** (`@classmethod`): Takes `cls`, can access/modify class state
  - **Static method** (`@staticmethod`): Takes neither `self` nor `cls`, utility function
  - **Instance method** (regular): Takes `self`, can access/modify instance state
  - Choose based on what needs to be accessed

- **Factory methods**
  - Methods that create and return new instances of class
  - Often implemented as class methods
  - Provide alternative ways to construct objects
  - Example: `create_lannister(cls, first_name, is_alive)`
  - More descriptive than multiple `__init__` signatures

- **The `type().__name__` pattern**
  - `type(object)`: Returns type/class of object
  - `type(object).__name__`: Returns class name as string
  - Useful for getting class name dynamically
  - Example: `type(Jaine).__name__` returns `"Lannister"`
  - Alternative to hardcoding class names

- **Importing from custom modules**
  - `from module_name import ClassName`: Import specific class from another file
  - Module name = filename without `.py` extension
  - Example: `from S1E9 import Character`
  - Classes in same directory can import each other
  - Enables code organization and reusability

### V) Logic used for the exercise
1. **File: S1E9.py** - Same as ex00, defines Character and Stark classes
2. **File: S1E7.py** - Defines new classes importing from S1E9:
   - Import Character class: `from S1E9 import Character`
   - Define `Baratheon` class:
     - Inherits from `Character`
     - Add class docstring
     - `__init__` method:
       - Calls parent constructor with `super().__init__()`
       - Sets additional attributes: `family_name`, `eyes`, `hairs`
     - Define properties for new attributes:
       - `family_name`, `eyes`, `hairs` with getters and setters
       - Each uses validation from parent class
     - Implement `die()` method (required by abstract parent)
     - Implement `__str__` method:
       - Returns formatted string with family attributes
       - Format: `"Vector: ('Baratheon', 'brown', 'dark')"`
     - Implement `__repr__` method:
       - Returns same format as `__str__` for this exercise
   - Define `Lannister` class:
     - Similar structure to Baratheon
     - Different default values: family_name="Lannister", eyes="blue", hairs="light"
     - Implements same methods: properties, `die()`, `__str__`, `__repr__`
     - Add class method `create_lannister()`:
       - Decorated with `@classmethod`
       - Takes `cls` as first parameter
       - Returns new instance: `return cls(first_name, is_alive)`
       - Alternative constructor for creating Lannister instances
3. Main function demonstrates:
   - Create `Robert` (Baratheon instance)
   - Print `__dict__` to see attributes
   - Print `__str__` and `__repr__` method references
   - Test `die()` method
   - Create `Cersei` (Lannister instance) using regular constructor
   - Create `Jaine` (Lannister instance) using class method factory
   - Use `type().__name__` to get class name dynamically


## 3. Exercice 02: Now it’s weird!

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **Multiple inheritance**
  - Class can inherit from multiple parent classes
  - Syntax: `class ChildClass(Parent1, Parent2, Parent3):`
  - Child inherits attributes and methods from all parents
  - Order matters: leftmost parent takes precedence
  - Example: `class King(Baratheon, Lannister):`
  - Powerful but can be complex - use carefully

- **The diamond problem**
  - Occurs when class inherits from multiple classes with common ancestor
  - Diamond shape in inheritance diagram:
    ```
         Character (top)
            /  \
      Baratheon  Lannister (middle)
            \  /
           King (bottom)
    ```
  - Problem: Which parent's method to use when both define same method?
  - Which `__init__` to call? In what order?
  - Python solves this with Method Resolution Order (MRO)

- **Method Resolution Order (MRO)**
  - Defines order in which Python searches for methods/attributes
  - Uses C3 linearization algorithm (also called C3 superclass linearization)
  - Ensures:
    - Child classes appear before parents
    - Parents appear in order specified in class definition
    - Each class appears only once
  - Can view with `ClassName.__mro__` or `ClassName.mro()`
  - Example MRO for King: `King → Baratheon → Lannister → Character → ABC → object`

- **C3 linearization**
  - Algorithm Python uses to calculate MRO
  - Guarantees consistent, predictable method resolution
  - Respects local precedence order (left-to-right in inheritance list)
  - Prevents ambiguous inheritance hierarchies
  - Ensures `super()` works correctly in complex inheritance

- **`super()` in multiple inheritance**
  - `super()` follows MRO chain, not just immediate parent
  - Calls next method in MRO, not necessarily parent class method
  - In `King.__init__`, `super().__init__()` calls `Baratheon.__init__`
  - `Baratheon.__init__` uses `super()` → calls `Character.__init__`
  - This ensures all ancestors get initialized exactly once
  - Critical for diamond inheritance to work correctly

- **Accessor methods (getters/setters)**
  - Methods that access or modify object attributes
  - **Getter**: Returns attribute value (e.g., `get_eyes()`)
  - **Setter**: Sets attribute value (e.g., `set_eyes(color)`)
  - In this exercise: wrapper methods around property access
  - Example: `get_eyes()` returns `self.eyes` (which uses property getter)
  - Note: In Python, properties are preferred over explicit getters/setters
  - Here used for demonstration purposes

### V) Logic used for the exercise
1. **Files: S1E9.py and S1E7.py** - Same as ex01, define Character, Stark, Baratheon, and Lannister classes
2. **File: DiamondTrap.py** - Demonstrates multiple inheritance:
   - Import both parent classes: `from S1E7 import Baratheon, Lannister`
   - Define `King` class with multiple inheritance:
     - Syntax: `class King(Baratheon, Lannister):`
     - Baratheon listed first (takes precedence in MRO)
     - Add class docstring explaining diamond problem
   - Define `__init__` method:
     - Takes `first_name` and `is_alive` parameters
     - Calls `super().__init__(first_name, is_alive)`
     - `super()` follows MRO → calls `Baratheon.__init__`
     - Baratheon's `super()` calls `Character.__init__`
     - Character's `super()` eventually reaches `Lannister.__init__` via MRO
     - All classes initialized correctly without duplication
   - Define accessor methods:
     - `get_eyes()`: Returns `self.eyes` (uses inherited property)
     - `set_eyes(color)`: Sets `self.eyes = color` (uses property setter)
     - `get_hairs()`: Returns `self.hairs` (uses inherited property)
     - `set_hairs(color)`: Sets `self.hairs = color` (uses property setter)
     - Methods demonstrate access to inherited properties
3. Main function demonstrates:
   - Create `Joffrey` instance of King class
   - Print initial `__dict__` showing inherited attributes
   - Attributes come from Baratheon (first in MRO): family_name="Baratheon", eyes="brown", hairs="dark"
   - Use setter methods to modify attributes
   - Change eyes to "blue" and hairs to "light"
   - Use getter methods to retrieve modified values
   - Print final `__dict__` showing changes
   - Demonstrates that King inherits and can modify Baratheon/Lannister attributes


## 4. Exercice 03: Calculate my vector

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `__add__`: Special method for addition operator (`+`)
- `__mul__`: Special method for multiplication operator (`*`)
- `__sub__`: Special method for subtraction operator (`-`)
- `__truediv__`: Special method for true division operator (`/`)

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **Operator overloading**
  - Defining custom behavior for operators (`+`, `-`, `*`, `/`, etc.)
  - Uses special methods (dunder methods) to override default behavior
  - Makes custom objects work with Python's built-in operators
  - Example: `vector + 5` calls `vector.__add__(5)`
  - Enables intuitive, mathematical syntax for custom classes
  - **Important**: Requires creating an instance (object) because we need to modify the same object's state
  - Each instance maintains its own vector that gets modified by operations
  - Contrast with ex04: no object needed when just computing results without maintaining state

- **Arithmetic operator special methods**
  - **`__add__(self, other)`**: Called for `object + other`
  - **`__sub__(self, other)`**: Called for `object - other`
  - **`__mul__(self, other)`**: Called for `object * other`
  - **`__truediv__(self, other)`**: Called for `object / other`
  - `other` parameter receives right-hand operand
  - Can return new object or modify `self` (in-place)
  - Should handle appropriate types for `other`

- **The `__add__` method**
  - Implements addition operator: `+`
  - Signature: `def __add__(self, other):`
  - Called when using `instance + value`
  - In this exercise: adds scalar to each vector element
  - Example: `v1 + 5` calls `v1.__add__(5)`

- **The `__sub__` method**
  - Implements subtraction operator: `-`
  - Signature: `def __sub__(self, other):`
  - Called when using `instance - value`
  - In this exercise: subtracts scalar from each vector element
  - Example: `v3 - 5` calls `v3.__sub__(5)`

- **The `__mul__` method**
  - Implements multiplication operator: `*`
  - Signature: `def __mul__(self, other):`
  - Called when using `instance * value`
  - In this exercise: multiplies each vector element by scalar
  - Example: `v2 * 5` calls `v2.__mul__(5)`

- **The `__truediv__` method**
  - Implements true division operator: `/`
  - Signature: `def __truediv__(self, other):`
  - Called when using `instance / value`
  - Always returns float result (unlike `//` floor division)
  - In this exercise: divides each vector element by scalar
  - Example: `v3 / 5` calls `v3.__truediv__(5)`
  - Should handle `ZeroDivisionError` when dividing by zero

- **In-place operations**
  - Operations that modify object directly instead of creating new one
  - In this exercise: methods modify `self.vector` directly
  - Pattern: `self.vector = [expression for x in self.vector]`
  - More memory efficient for large data
  - Note: Python also has in-place variants: `__iadd__`, `__imul__`, etc.

- **Vector-scalar operations**
  - Mathematical operations between vector (list of numbers) and scalar (single number)
  - Each element of vector operated with scalar independently
  - Examples:
    - `[1, 2, 3] + 5 = [6, 7, 8]` (add 5 to each element)
    - `[2, 4, 6] * 3 = [6, 12, 18]` (multiply each by 3)
  - Implemented using list comprehensions
  - Common in linear algebra and data science

- **ZeroDivisionError handling**
  - Exception raised when dividing by zero
  - Should be caught in `__truediv__` method
  - Pattern: `try/except ZeroDivisionError`
  - Return `None` or raise exception depending on design
  - Prevents program crash from invalid division

### V) Logic used for the exercise
1. Define `calculator` class:
   - Add class docstring
   - `__init__` method:
     - Takes `vector` parameter (list of floats)
     - Stores as instance attribute: `self.vector = vector`
   - Implement `__add__` method:
     - Takes scalar value (`object`) as parameter
     - Uses list comprehension: `[x + object for x in self.vector]`
     - Updates `self.vector` with result
     - Prints modified vector
   - Implement `__mul__` method:
     - Takes scalar value as parameter
     - Uses list comprehension: `[x * object for x in self.vector]`
     - Updates `self.vector` with result
     - Prints modified vector
   - Implement `__sub__` method:
     - Takes scalar value as parameter
     - Uses list comprehension: `[x - object for x in self.vector]`
     - Updates `self.vector` with result
     - Prints modified vector
   - Implement `__truediv__` method:
     - Takes scalar value as parameter
     - Uses try/except to catch `ZeroDivisionError`
     - Uses list comprehension: `[x / object for x in self.vector]`
     - Updates `self.vector` with result if successful
     - Returns `None` if division by zero occurs
     - Prints modified vector or error message
2. Main function demonstrates:
   - Create `v1` calculator with vector `[0.0, 1.0, 2.0, 3.0, 4.0, 5.0]`
   - Use addition operator: `v1 + 5` adds 5 to each element
   - Create `v2` calculator with same initial vector
   - Use multiplication operator: `v2 * 5` multiplies each element by 5
   - Create `v3` calculator with vector `[10.0, 15.0, 20.0]`
   - Use subtraction operator: `v3 - 5` subtracts 5 from each element
   - Use division operator: `v3 / 5` divides each element by 5
   - Each operation modifies vector in-place and prints result


## 5. Exercice 04: Calculate my dot product

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `zip()`: Built-in function that pairs elements from multiple iterables

### III) New external functions, methods, attributes used
No new external functions, methods, or attributes used.

### IV) New theory points

- **The `zip()` function**
  - Combines multiple iterables (lists, tuples) into pairs/tuples
  - Syntax: `zip(iterable1, iterable2, ...)`
  - Returns iterator of tuples: `(item1, item2, ...)`
  - Stops at shortest iterable if lengths differ
  - Example: `zip([1, 2, 3], [4, 5, 6])` → `[(1, 4), (2, 5), (3, 6)]`
  - Common use: Iterate over multiple lists simultaneously
  - Perfect for element-wise operations on vectors

- **Tuple unpacking with `zip()`**
  - Can unpack values in for loop
  - Syntax: `for x, y in zip(list1, list2):`
  - `x` receives element from first list
  - `y` receives element from second list
  - Example: `for x, y in zip([1, 2], [3, 4]):` → iterations: `(1, 3)`, `(2, 4)`
  - Cleaner than using indices

- **Generator expressions with `zip()`**
  - Combine `zip()` with generator expressions
  - Syntax: `(expression for x, y in zip(V1, V2))`
  - Memory efficient - generates values on-demand
  - Example: `(x * y for x, y in zip([1, 2], [3, 4]))` → `3, 8`
  - Can be used with `sum()`, `list()`, etc.

- **Dot product (scalar product)**
  - Mathematical operation on two vectors producing scalar (single number)
  - Formula: `V1 · V2 = sum(v1[i] * v2[i] for all i)`
  - Example: `[5, 10, 2] · [2, 4, 3] = (5×2) + (10×4) + (2×3) = 10 + 40 + 6 = 56`
  - Implementation: `sum(x * y for x, y in zip(V1, V2))`
  - Fundamental operation in linear algebra
  - Used in machine learning (neural networks, similarity calculations)

- **Vector-vector operations (element-wise)**
  - Operations between two vectors of same length
  - Each element operated with corresponding element from other vector
  - **Addition**: `[a, b, c] + [x, y, z] = [a+x, b+y, c+z]`
  - **Subtraction**: `[a, b, c] - [x, y, z] = [a-x, b-y, c-z]`
  - Different from vector-scalar operations (ex03)
  - Requires vectors of same length
  - Implementation: `[x + y for x, y in zip(V1, V2)]`

- **Static-only classes (utility classes)**
  - Classes with only static methods, no instance attributes
  - No `__init__` method needed
  - Called directly on class: `ClassName.method()`
  - Don't need to create instance
  - Used for grouping related utility functions
  - Example: `calculator.dotproduct(a, b)` - no instantiation required
  - Serves as namespace for related functions
  - **Difference from ex03**: 
    - Ex03: Must create object (`v1 = calculator([...])`) because we need to store and modify the same vector across multiple operations
    - Ex04: No object needed (`calculator.dotproduct(a, b)`) because we just compute and return results without maintaining state
    - Choice depends on whether you need to maintain and modify object state

### V) Logic used for the exercise
1. Define `calculator` class:
   - Add class docstring noting all methods are static
   - No `__init__` method (not needed for static-only class)
   - Define `dotproduct()` static method:
     - Decorated with `@staticmethod`
     - Takes two vectors `V1` and `V2` as parameters
     - Uses generator expression with `zip()`: `(x * y for x, y in zip(V1, V2))`
     - Pairs corresponding elements and multiplies them
     - Uses `sum()` to add all products together
     - Prints result with descriptive message
     - Implements mathematical dot product formula
   - Define `add_vec()` static method:
     - Decorated with `@staticmethod`
     - Takes two vectors as parameters
     - Uses list comprehension with `zip()`: `[float(x + y) for x, y in zip(V1, V2)]`
     - Adds corresponding elements from both vectors
     - Converts to float explicitly
     - Prints result vector
   - Define `sous_vec()` static method:
     - Decorated with `@staticmethod`
     - Takes two vectors as parameters
     - Uses list comprehension with `zip()`: `[float(x - y) for x, y in zip(V1, V2)]`
     - Subtracts V2 elements from V1 elements
     - Converts to float explicitly
     - Prints result vector
2. Main function demonstrates:
   - Create two vectors: `a = [5, 10, 2]` and `b = [2, 4, 3]`
   - Call static methods directly on class (no instantiation):
     - `calculator.dotproduct(a, b)` calculates dot product: 56
     - `calculator.add_vec(a, b)` adds vectors element-wise: `[7.0, 14.0, 5.0]`
     - `calculator.sous_vec(a, b)` subtracts vectors: `[3.0, 6.0, -1.0]`
   - Demonstrates utility class pattern with static methods


## Additional Resources

- [Python Official Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
