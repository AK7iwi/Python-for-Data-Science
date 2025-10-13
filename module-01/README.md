<div align="center">

# MODULE 01 - Array

</div>

## Summary

[1. Exercice 00: Give my BMI](#1-exercice-00-give-my-bmi)  
[2. Exercice 01: 2D array](#2-exercice-01-2d-array)  
[3. Exercice 02: load my image](#3-exercice-02-load-my-image)  
[4. Exercice 03: zoom on me](#4-exercice-03-zoom-on-me)  
[5. Exercice 04: rotate me](#5-exercice-04-rotate-me)  
[6. Exercice 05: Pimp my image](#6-exercice-05-pimp-my-image)  
[Additional Resources](#additional-resources)


## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- Cross-references like "(already used in ex00)" indicate when a concept was previously introduced
- There are additional resources at the end if you want to explore a concept in more depth


## Introduction

This module focuses on array manipulation and visualization using two essential Python libraries:

- **NumPy**: For efficient numerical computing and array operations
- **Matplotlib**: For data visualization and image display

The exercises progressively introduce concepts from basic array operations (BMI calculations) to advanced image processing (filtering, rotation, and visualization). Each exercise builds upon previous knowledge, demonstrating how NumPy arrays enable vectorized operations and how Matplotlib provides powerful visualization capabilities for data science applications.


## 1. Exercice 00: Give my BMI

### I) New libraries used
- `numpy`: External library for numerical computing
- `math`: Built-in library for mathematical functions

### II) New built-in functions and methods used
- `math.isfinite()`: Module function that checks if value is finite

### III) New external functions
- `np.asarray()`: NumPy function that converts Python lists to NumPy 
- `array.tolist()`: NumPy array method that converts arrays back to Python lists

### IV) New theory points
- **NumPy array operations**
  - `np.asarray()`: Converts Python lists to NumPy arrays efficiently
  - Array broadcasting: Automatic expansion of arrays for operations
    - Allows arrays with different shapes to perform element-wise operations
    - NumPy automatically aligns dimensions and expands arrays as needed
    - Enables vectorized operations without manual loops
  - Vectorized operations: `array1 / array2` performs element-wise division
  - Boolean array operations: `array > limit` creates boolean array
  - `.tolist()`: Converts NumPy array back to Python list

### V) Logic used for the exercise
1. Validate input data - Check types, finiteness, positivity, ...
2. Convert Python lists to NumPy arrays using `np.asarray()`
3. Perform vectorized BMI calculation using NumPy operations
4. Apply limit comparison using boolean array operations
5. Return results as Python lists using `.tolist()`


## 2. Exercice 01: 2D array

### I) New libraries used
No new libraries used.

### II) New built-in functions and methods used
No new built-in functions and methods used

### III) New external functions
- `array.shape`: NumPy array attribute that returns the dimensions of the array 

### IV) New theory points
- **Array slicing operations**
  - `array[start:end]`: Slice NumPy arrays efficiently
  - Negative indexing: `array[-1]` for last element, `array[-2]` for second-to-last element, ...
  - Array slicing: More efficient than Python list slicing
- **NumPy array properties**
  - `array.shape`: Returns dimensions of array
  - `y, x = array.shape`
- **NumPy array type**
  - `np.ndarray`: NumPy's main array class for n-dimensional arrays
  - Base class for all NumPy arrays (1D, 2D, 3D, etc.)

### V) Logic used for the exercise
1. Validate 2D array - Check if input is proper list of lists, ensure consistent row sizes, ...
2. Validate slice indices - Check bounds and types (Index normalization: Convert negative indices to positive equivalents, e.g., -2 becomes len(array) - 2)
3. Convert to NumPy array using `np.asarray()` for efficient slicing
4. Perform array slicing using NumPy's optimized slicing
5. Display shape information before and after slicing
6. Return sliced data as Python list using `.tolist()`


## 3. Exercice 02: load my image

### I) New libraries used
- `os`: Built-in library for operating system interface
- `PIL`: External library for loading and processing images

### II) New built-in functions and methods used
- `str.strip()`: Built-in string method that removes whitespace from both ends
- `os.path.splitext()`: Module function that splits filename and extension
- `os.path.exists()`: Module function that checks if file exists

### III) New external functions
- `image.open()`: Class method that opens image files
- `image.mode`: PIL Image attribute that returns the color mode of the image 
- `image.convert()`: Method that converts image color modes

### IV) New theory points
- **Image file handling**
  - File format validation: Check supported extensions
  - File existence validation: `os.path.exists()`
- **PIL (Python Imaging Library)**
  - `Image.open()`: Load image files
  - Image properties: `.mode`, `.size`
  - Color mode conversion: `image.convert('RGB')`
- **NumPy array conversion**
  - `np.asarray(image)`: Convert PIL Image to NumPy array
  - Preserves data types: uint8 for image data
  - Memory efficient conversion
- **Image array properties**
  - Shape: `(height, width, channels)` for color images
  - Data type: uint8 (0-255 range)
  - Channel interpretation: RGB format
- **Array manipulation**
  - Shape analysis: `image.shape[:2]` for height and width
  - Channel handling: Check for 2D vs 3D arrays

### V) Logic used for the exercise
1. Validate file path - Check existence, format, and string validity
2. Load image using PIL with `Image.open()`
3. Convert to RGB mode if necessary using `image.convert()`
4. Convert PIL Image to NumPy array using `np.asarray()`
5. Display image information including dimensions and channels
6. Return NumPy array for further processing


## 4. Exercice 03: zoom on me

### I) Libraries used
- `matplotlib`: External library for plotting and visualization

### II) Built-in functions and methods used
- `min()`: Built-in function that returns the smallest value from iterable

### III) External functions
- `np.dot()`: NumPy function that performs matrix multiplication or dot product
  - Applies formula: `0.299*R + 0.587*G + 0.114*B`
- `np.uint8`: NumPy data type for 8-bit unsigned integers (0-255 range)
  - Used with `.astype(np.uint8)` for data type conversion
- `np.astype()`: NumPy array method that converts data type
- `plt.figure()`: Function that creates new figure
- `plt.imshow()`: Function that displays image data
- `plt.title()`: Function that sets plot title
- `plt.xlabel()`: Function that sets x-axis label
- `plt.ylabel()`: Function that sets y-axis label
- `plt.colorbar()`: Function that adds color bar
- `plt.show()`: Function that displays the plot

### IV) New theory points
- **Image processing operations**
  - Array slicing: `image[start_y:end_y, start_x:end_x]`
- **Grayscale conversion**
  - RGB to grayscale: Manual conversion using dot product
  - Luminance formula: `0.299*R + 0.587*G + 0.114*B`
  - Data type conversion: `.astype(np.uint8)`
- **Image visualization**
  - `matplotlib.pyplot`: Library for creating plots and visualizations
  - `figsize=(width, height)`: Figure sizing
  - `plt.imshow()`: Display 2D image data
  - `cmap='gray'`: Grayscale display

### V) Logic used for the exercise
1. Load image using previous `ft_load()` function
2. Calculate zoom area - Define center square region
3. Crop image using array slicing operations
4. Convert to grayscale using manual RGB conversion (Luminance formula)
5. Display results using matplotlib visualization


## 5. Exercice 04: rotate me

### I) New libraries used
No new libraries used.

### II) New built-in functions and methods used
No new built-in functions and methods used

### III) External functions
- `np.zeros()`: NumPy function that creates array filled with zeros

### IV) New theory points
- **Array transposition**
  - Manual transpose: `transposed[j, i] = image[i, j]`
  - NumPy transpose: `array.T` (not used - manual implementation required)
  - Shape transformation: `(rows, cols)` → `(cols, rows)`
- **Manual array operations**
  - Array initialization: `np.zeros((cols, rows, channels))`
  - Nested loops: `for i in range(rows): for j in range(cols):`
  - Index swapping: `transposed[j, i] = image[i, j]`
- **Image rotation concepts**
  - Transpose vs rotation: Transpose swaps dimensions
  - Channel preservation: Maintain RGB channel structure
  - Data type preservation: Keep uint8 format

### V) Logic used for the exercise
1. Load and zoom image using previous functions
2. Validate array dimensions for proper processing
3. Implement manual transpose using nested loops
4. Handle different array shapes (2D vs 3D)
5. Preserve data types during transformation
6. Display rotated image using matplotlib
7. Show shape changes before and after rotation


## 6. Exercice 05: Pimp my image

### I) New libraries used
No new libraries used.

### II) New built-in functions and methods used
No new built-in functions and methods used

### III) External functions
- `array.copy()`: NumPy array method that creates independent copy of array
- `np.stack()`: NumPy function that stacks arrays along new axis
  - Combines multiple arrays into single array
  - Used for creating composite images or channel operations
  - Maintains array dimensions and data types
- `plt.axis()`: Matplotlib function that controls axis display properties

### IV) New theory points
- **Image filtering operations**
  - Color channel isolation: `array[:, :, channel] = 0`
  - Channel indexing: RGB = [0, 1, 2] for [Red, Green, Blue]
- **Color space manipulation**
  - Red filter: Keep only red channel, zero others
  - Green filter: Keep only green channel, zero others
  - Blue filter: Keep only blue channel, zero others
  - Grayscale conversion: Average RGB channels
- **Array operations**
  - Array copying: `array.copy()` for independent copies
  - In-place modification: `array[:, :, 1] = 0`
  - Data type preservation: Maintain uint8 format
- **Image processing pipeline**
  - Load → Validate → Copy → Filter → Display
  - Non-destructive operations: Preserve original data
  - Independent filtering: Each filter creates separate copy

### V) Logic used for the exercise
1. Load image using `ft_load()` function
2. Validate array properties for image processing
3. Create independent copies using `array.copy()`
4. Apply color filters by zeroing specific channels
5. Implement grayscale conversion using manual averaging
6. Display filtered images using matplotlib
7. Preserve original data throughout processing pipeline

---

## Additional Resources

[NumPy Official Documentation](https://numpy.org/doc/stable/)  
[PIL/Pillow Documentation](https://pillow.readthedocs.io/)  
[Matplotlib Documentation](https://matplotlib.org/stable/)  
[Data Science with NumPy](https://numpy.org/doc/stable/user/quickstart.html)  
[Image Processing with Python](https://scikit-image.org/docs/stable/user_guide/)  
[Array Broadcasting in NumPy](https://numpy.org/doc/stable/user/basics.broadcasting.html)

[NumPy Official Documentation]: https://numpy.org/doc/stable/
[PIL/Pillow Documentation]: https://pillow.readthedocs.io/
[Matplotlib Documentation]: https://matplotlib.org/stable/
[Data Science with NumPy]: https://numpy.org/doc/stable/user/quickstart.html
[Image Processing with Python]: https://scikit-image.org/docs/stable/user_guide/
[Array Broadcasting in NumPy]: https://numpy.org/doc/stable/user/basics.broadcasting.html