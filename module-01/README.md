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
- There are additional resources at the end if you want to explore a concept in more depth


## Introduction

This module focuses on array manipulation and visualization using two essential Python libraries:

- **NumPy**: For efficient numerical computing and array operations
- **Matplotlib**: For data visualization and image display


## 1. Exercice 00: Give my BMI

### I) New libraries used
- `numpy`: External library for numerical computing and array operations

### II) New built-in functions, methods, attributes used
- `math.isfinite()`: Math module function that checks if a float value is finite (not inf or nan)

### III) New external functions, methods, attributes used
- `np.asarray()`: Converts input (list, tuple, etc.) to NumPy array
- `array.tolist()`: Converts NumPy array back to Python list

### IV) New theory points
- **Union type hints** (`int | float`)
  - Modern Python 3.10+ syntax for multiple types
  - Equivalent to `Union[int, float]` from typing module
  - Used when parameter can be multiple types
  - Example: `def func(value: int | float) -> None:`

- **NumPy introduction**
  - Library for numerical computing with multi-dimensional arrays
  - Much faster than Python lists for numerical operations
  - Provides vectorized operations (no need for loops)
  - Essential for data science and scientific computing

- **NumPy array creation**
  - `np.asarray(list)`: Converts Python list to NumPy array
  - Creates ndarray (n-dimensional array) object
  - No copy if input is already ndarray
  - Efficient for numerical computations

- **Vectorized operations**
  - Operations applied element-wise without explicit loops
  - Example: `weight / (height ** 2)` computes BMI for all values at once
  - Much faster than Python loops
  - More readable and concise code

- **Array broadcasting**
  - NumPy automatically expands arrays for compatible operations
  - Allows operations between arrays of different shapes
  - Example: `array > scalar` compares each element to scalar
  - Rules: dimensions must be compatible or one must be 1

- **Boolean arrays**
  - Result of comparison operations on arrays
  - Contains `True`/`False` for each element
  - Example: `np.array([20, 30, 25]) > 26` → `[False, True, False]`
  - Can be used for filtering or conditional operations

- **Array to list conversion**
  - `.tolist()`: Converts NumPy array back to Python list
  - Useful for returning results in native Python format
  - Returns nested lists for multi-dimensional arrays

### V) Logic used for the exercise
1. Define multiple validation functions for input checking:
   - `validate_measurement_structure()`: Checks if input is non-empty list
   - `validate_measurement_content()`: Checks each element is int/float, finite, positive
   - `validate_measurement_length()`: Ensures height and weight lists have same length
   - `validate_limit()`: Checks limit is positive integer
2. `give_bmi()` function:
   - Validates height and weight lists with comprehensive error handling
   - Catches `ValueError` and `TypeError`, prints message, returns None
   - Converts lists to NumPy arrays using `np.asarray()`
   - Calculates BMI using vectorized operation: `weight / (height ** 2)`
   - Converts result back to list using `.tolist()`
3. `apply_limit()` function:
   - Validates BMI list and limit parameter
   - Converts BMI list to NumPy array
   - Uses boolean comparison: `array > limit`
   - Returns boolean list indicating which BMIs exceed limit
4. Main function tests with example data and displays results with types


## 2. Exercice 01: 2D array

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
- `array.shape`: NumPy array attribute returning tuple of dimensions (rows, columns)

### IV) New theory points

- **2D arrays (matrices)**
  - Arrays with two dimensions: rows and columns
  - List of lists in Python: `[[1, 2], [3, 4]]`
  - When converted to NumPy: `shape = (rows, columns)`
  - Each row must have same number of elements (rectangular structure)

- **NumPy ndarray type**
  - `np.ndarray`: N-dimensional array class
  - Base type for all NumPy arrays (1D, 2D, 3D, etc.)
  - Efficient storage and operations on homogeneous data
  - Type hint: `np.ndarray` for array parameters/returns

- **Array shape attribute**
  - `array.shape`: Returns tuple of array dimensions
  - For 2D array: `(rows, columns)` or `(height, width)`
  - Example: `array.shape = (4, 2)` means 4 rows, 2 columns
  - Can unpack: `rows, cols = array.shape`

- **Array slicing**
  - Same syntax as Python lists: `array[start:end]`
  - Returns view (not copy) for efficiency
  - Negative indices work: `-1` is last, `-2` is second-to-last
  - Example: `array[1:-2]` from second element to third-to-last
  - NumPy slicing is much faster than list slicing for large arrays

- **Negative index normalization**
  - Negative indices converted to positive: `negative_index + length`
  - Example with length 4: `-1` → `3`, `-2` → `2`
  - Useful for accessing elements from end
  - Must validate bounds: normalized index within `[0, length]`

- **IndexError exception**
  - Raised when index is out of bounds
  - Similar to list index errors
  - Caught and handled like ValueError, TypeError

### V) Logic used for the exercise
1. Define comprehensive validation functions:
   - `validate_2d_array_structure()`: Checks input is non-empty list
   - `validate_2d_array_content()`: Validates all rows are non-empty lists with same size
   - `validate_indice_type()`: Ensures indices are integers
   - `validate_indices_bounds()`: Checks indices within valid range
     - Normalizes negative indices to positive equivalents
     - Validates start < end and within array bounds
2. `slice_me()` function:
   - Validates 2D array structure and slice indices
   - Catches `ValueError`, `TypeError`, and `IndexError`
   - Converts list to NumPy array using `np.asarray()`
   - Performs slicing: `array[start:end]` (returns view, not copy)
   - Gets shape before and after slicing using `.shape` attribute
3. `print_info()` displays original and sliced shapes
4. Returns sliced array as Python list using `.tolist()`
5. Main function tests with positive and negative indices


## 3. Exercice 02: load my image

### I) New libraries used
- `PIL` (Pillow): External library for image loading and processing

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
- `Image.open()`: Opens and identifies image file
- `image.mode`: PIL Image attribute returning color mode (e.g., 'RGB', 'L', 'RGBA')
- `image.convert()`: Converts image to different color mode

### IV) New theory points

- **PIL/Pillow library**
  - Fork of Python Imaging Library (PIL)
  - Standard library for image manipulation in Python
  - Supports many image formats: JPEG, PNG, GIF, BMP, etc.
  - Installation: `pip install Pillow`

- **Context managers with `with` statement**
  - `with Image.open(path) as image:` ensures proper file closure
  - Automatically closes file even if exception occurs
  - More reliable than manual `open()` and `close()`
  - Same pattern as `with open(file) as f:` for text files

- **Image loading**
  - `Image.open(path)`: Opens image file and returns PIL Image object
  - Lazy loading: Image data loaded on demand
  - Supports many formats automatically
  - Raises various exceptions for invalid files

- **Image color modes**
  - `'RGB'`: 3 channels (Red, Green, Blue) - most common
  - `'L'`: 1 channel (Grayscale/Luminance)
  - `'RGBA'`: 4 channels (RGB + Alpha/transparency)
  - `image.mode`: Attribute to check current mode
  - `image.convert('RGB')`: Convert to desired mode

- **Image to NumPy array**
  - `np.asarray(PIL_image)`: Converts PIL Image to NumPy array
  - Result shape for RGB: `(height, width, 3)`
  - Result shape for grayscale: `(height, width)`
  - Data type: typically `uint8` (0-255 integer values)
  - Efficient: shares memory when possible

- **Image array shape interpretation**
  - Shape for color images: `(height, width, channels)`
  - `shape[0]`: Height (Y-axis, number of rows)
  - `shape[1]`: Width (X-axis, number of columns)
  - `shape[2]`: Number of channels (3 for RGB)
  - `shape[:2]`: Gets height and width only
  - `len(shape)`: Number of dimensions (2 or 3)

- **File-related exceptions**
  - `FileNotFoundError`: File doesn't exist at specified path
  - `PermissionError`: No permission to access file
  - `IsADirectoryError`: Path points to directory, not file
  - `UnidentifiedImageError`: PIL-specific, file isn't valid image format
  - `AttributeError`: Occurs with invalid image data

### V) Logic used for the exercise
1. `ft_load()` function with comprehensive exception handling:
   - Catches `UnidentifiedImageError` for invalid image files
   - Catches `FileNotFoundError` for missing files
   - Catches `PermissionError` for access denied
   - Catches `IsADirectoryError` for directory paths
   - Catches `AttributeError` for invalid image data
   - Catches `TypeError` and `ValueError` for other errors
   - Returns None on any error with descriptive message
2. `load_image()` helper function:
   - Opens image using `with Image.open(path)` context manager
   - Checks if image mode is RGB: `image.mode != 'RGB'`
   - Converts to RGB if needed: `image.convert('RGB')`
   - Converts PIL Image to NumPy array: `np.asarray(image)`
   - Returns array for further processing
3. `print_info()` displays image information:
   - Extracts height and width from `shape[:2]`
   - Determines number of channels using `len(shape)`
   - For 2D arrays (grayscale): channels = 1
   - For 3D arrays (color): channels = `shape[2]`
4. Main function loads and displays image array


## 4. Exercice 03: zoom on me

### I) New libraries used
- `matplotlib.pyplot`: External library for data visualization and plotting

### II) New built-in functions, methods, attributes used
- `min()`: Returns smallest value from multiple arguments or iterable

### III) New external functions, methods, attributes used
- `np.dot()`: Performs dot product or matrix multiplication
- `array.astype()`: Converts array to specified data type
- `plt.figure()`: Creates new figure for plotting
- `plt.imshow()`: Displays image data as 2D array
- `plt.title()`: Sets title for plot
- `plt.xlabel()` / `plt.ylabel()`: Sets axis labels
- `plt.colorbar()`: Adds colorbar to plot
- `plt.show()`: Displays all created figures

### IV) New theory points

- **Matplotlib library**
  - Standard library for creating visualizations in Python
  - `matplotlib.pyplot` (imported as `plt`): Main plotting interface
  - Interactive plotting capabilities
  - Installation: `pip install matplotlib`

- **2D array slicing for images**
  - Syntax: `image[y_start:y_end, x_start:x_end]`
  - First index: rows (Y-axis, vertical)
  - Second index: columns (X-axis, horizontal)
  - Returns view of array (efficient, no copy)
  - Example: `image[100:300, 200:400]` crops rectangle

- **Ellipsis notation `...`**
  - Represents all remaining dimensions
  - `array[..., :3]` = `array[:, :, :3]` for 3D array
  - Useful for accessing last dimension
  - Makes code work with different dimensional arrays

- **RGB to grayscale conversion**
  - Standard luminance formula: `0.299*R + 0.587*G + 0.114*B`
  - Weights based on human eye sensitivity
  - Red: 29.9%, Green: 58.7%, Blue: 11.4%
  - Result: single channel representing brightness

- **NumPy dot product for grayscale**
  - `np.dot(image[..., :3], [0.299, 0.587, 0.114])`
  - Multiplies each RGB pixel by weights
  - Efficient vectorized operation
  - Applies formula to all pixels at once

- **Array data type conversion**
  - `array.astype(np.uint8)`: Converts to 8-bit unsigned integer
  - `np.uint8`: Data type representing 0-255 range
  - Necessary after grayscale calculation (returns float)
  - Ensures proper image display

- **Matplotlib visualization**
  - **Figure creation**: `plt.figure(figsize=(width, height))`
    - `figsize` in inches: `(10, 8)` creates 10×8 inch figure
  - **Image display**: `plt.imshow(image, cmap='gray')`
    - `cmap='gray'`: Colormap for grayscale visualization
    - Without cmap, uses default color mapping
  - **Colorbar**: Shows intensity scale mapping
  - **Labels and titles**: Annotate plot with information
  - **Show plot**: `plt.show()` renders and displays figure

- **Floor division `//`**
  - Divides and rounds down to nearest integer
  - Example: `7 // 2 = 3` (not 3.5)
  - Used for center calculations and pixel coordinates

### V) Logic used for the exercise
1. Load image using `ft_load()` from previous exercise
2. `define_zoom_area()` calculates center square region:
   - Gets image dimensions from `shape[:2]`
   - Calculates center point: `width // 2`, `height // 2`
   - Determines zoom size: `min(width, height) // 2` for square
   - Computes corners: start/end for x and y axes
3. `zoom_center_square()` crops image:
   - Uses 2D slicing: `image[start_y:end_y, start_x:end_x]`
   - Prints zoom coordinates for verification
4. `convert_to_grayscale()` transforms RGB to grayscale:
   - Checks if already grayscale: `len(shape) == 2`
   - Uses ellipsis notation: `image[..., :3]` for RGB channels
   - Applies luminance formula with `np.dot()`
   - Converts to uint8: `astype(np.uint8)`
5. `display_image()` visualizes result:
   - Creates figure with specified size
   - Displays grayscale image with colorbar
   - Adds title, axis labels, and intensity scale
   - Shows plot with `plt.show()`
6. Main function orchestrates pipeline and prints array data


## 5. Exercice 04: rotate me

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `range()`: Creates sequence of numbers for iteration

### III) New external functions, methods, attributes used
- `np.zeros()`: Creates new array filled with zeros
- `array.dtype`: NumPy array attribute returning data type

### IV) New theory points

- **Array transposition**
  - Mathematical operation that flips array over its diagonal
  - Swaps rows and columns: `(rows, cols)` → `(cols, rows)`
  - Element at position `[i, j]` moves to `[j, i]`
  - For images: effectively rotates by 90° when combined with flips
  - NumPy has `array.T` but manual implementation required here

- **Creating arrays with `np.zeros()`**
  - Syntax: `np.zeros(shape, dtype=type)`
  - `shape`: Tuple defining dimensions `(rows, cols)` or `(rows, cols, channels)`
  - `dtype`: Data type for array elements (e.g., `np.uint8`)
  - Initializes all elements to 0
  - Efficient way to pre-allocate array before filling

- **Array dtype attribute**
  - `array.dtype`: Returns data type of array elements
  - Common types: `uint8`, `float64`, `int32`
  - Preserving dtype: `np.zeros(shape, dtype=image.dtype)`
  - Ensures consistency when creating new arrays

- **Manual array manipulation with loops**
  - Nested loops for 2D array traversal:
    ```python
    for i in range(rows):      # Iterate over rows
        for j in range(cols):  # Iterate over columns
            new_array[j, i] = old_array[i, j]
    ```
  - Index swapping: `[j, i]` instead of `[i, j]` performs transpose
  - Slower than vectorized NumPy operations
  - Useful for understanding underlying mechanics

- **Transpose vs rotation**
  - **Transpose**: Swaps dimensions, reflects over diagonal
  - **90° rotation**: Transpose + flip (not just transpose)
  - This exercise: transpose only (swaps width/height)
  - Full rotation would need additional flip operation

- **Multi-dimensional array handling**
  - Grayscale shape: `(height, width)` or `(height, width, 1)`
  - RGB shape: `(height, width, 3)`
  - Must preserve channel dimension in transpose
  - `shape[:2]` gets height and width regardless of channels

### V) Logic used for the exercise
1. Load image using `ft_load()` from exercise 02
2. Zoom and convert to grayscale using `zoom_center_square_to_grayscale()` from exercise 03
3. `manual_transpose()` function performs transposition:
   - Gets original dimensions: `rows, cols = image.shape[:2]`
   - Creates empty array with swapped dimensions: `np.zeros((cols, rows, 1), dtype=image.dtype)`
     - New shape: `(cols, rows, 1)` instead of `(rows, cols, 1)`
     - Preserves original data type with `dtype=image.dtype`
     - Maintains single channel for grayscale (1)
   - Uses nested for loops to copy elements:
     - Outer loop: `for i in range(rows)` iterates through rows
     - Inner loop: `for j in range(cols)` iterates through columns
     - Swaps indices: `transposed[j, i] = image[i, j]`
     - Each element moves from `(row, col)` to `(col, row)`
4. `rotate_image()` wrapper function:
   - Calls `manual_transpose()`
   - Prints shape information showing dimension swap
5. `display_image()` visualizes transposed result:
   - Shows rotated grayscale image
   - Matplotlib handles new dimensions automatically
6. Main function demonstrates complete pipeline from loading to display


## 6. Exercice 05: Pimp my image

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
- `array.copy()`: Creates independent copy of array (not a view)
- `array.mean()`: Calculates mean along specified axis
- `np.stack()`: Stacks arrays along new axis
- `plt.axis()`: Controls axis display (e.g., `'off'` to hide axes)

### IV) New theory points

- **RGB color channels**
  - Images stored as 3D arrays: `(height, width, 3)`
  - Channel 0: Red values (0-255)
  - Channel 1: Green values (0-255)
  - Channel 2: Blue values (0-255)
  - Each pixel: combination of RGB values creates color

- **Array copying vs views**
  - **View**: Reference to same data, changes affect original
  - **Copy**: Independent duplicate, changes don't affect original
  - `array.copy()`: Creates deep copy with separate memory
  - Important for preserving original when applying filters
  - Slicing creates views; need explicit `.copy()` for independence

- **Color inversion**
  - Inverts colors by subtracting from maximum value
  - Formula: `inverted = 255 - original`
  - Each pixel: `255 - pixel_value`
  - Vectorized operation: applies to entire array at once
  - White (255) becomes black (0), black becomes white

- **Color channel filtering**
  - Isolating channels by zeroing others
  - **Red filter**: Keep `[:, :, 0]`, set `[:, :, 1]` and `[:, :, 2]` to 0
  - **Green filter**: Keep `[:, :, 1]`, set `[:, :, 0]` and `[:, :, 2]` to 0
  - **Blue filter**: Keep `[:, :, 2]`, set `[:, :, 0]` and `[:, :, 1]` to 0
  - Result: image shows only specified color channel

- **In-place array modification**
  - Syntax: `array[:, :, channel] = value`
  - `:, :` selects all rows and columns
  - `channel` selects specific color channel
  - Direct modification without creating new array
  - Efficient for large arrays

- **Array mean operation**
  - `array.mean(axis=n)`: Calculates mean along specified axis
  - `axis=0`: Mean across rows (column-wise)
  - `axis=1`: Mean across columns (row-wise)
  - `axis=2`: Mean across channels (for grayscale)
  - Returns array with reduced dimensions

- **Grayscale conversion methods**
  - **Simple averaging**: `mean(axis=2)` averages RGB channels
  - Equal weights: each channel contributes equally
  - Result: 2D array with single intensity value per pixel
  - Different from luminance formula (weighted average)

- **Array stacking**
  - `np.stack([arr1, arr2, arr3], axis=n)`: Combines arrays
  - `axis=2`: Stacks along channel dimension
  - Creates 3D array from multiple 2D arrays
  - Used to convert grayscale back to 3-channel format
  - All input arrays must have same shape

- **Matplotlib axis control**
  - `plt.axis('off')`: Hides axis ticks and labels
  - Cleaner display for images
  - Other options: `'on'`, `'equal'`, `'tight'`

### V) Logic used for the exercise
1. Load RGB image using `ft_load()` from exercise 02
2. Validate image is proper NumPy array with at least 2 dimensions
3. **`ft_invert()` function** - Color inversion:
   - Validates image array
   - Applies inversion: `255 - array` (vectorized operation)
   - Subtracts each pixel value from 255
   - Displays inverted image
4. **`ft_red()` function** - Red channel filter:
   - Creates independent copy: `array.copy()`
   - Sets green channel to 0: `red_filtered[:, :, 1] = 0`
   - Sets blue channel to 0: `red_filtered[:, :, 2] = 0`
   - Keeps red channel unchanged
   - Displays red-filtered image
5. **`ft_green()` function** - Green channel filter:
   - Creates copy of original
   - Sets red channel to 0: `green_filtered[:, :, 0] = 0`
   - Sets blue channel to 0: `green_filtered[:, :, 2] = 0`
   - Keeps green channel unchanged
   - Displays green-filtered image
6. **`ft_blue()` function** - Blue channel filter:
   - Creates copy of original
   - Sets red channel to 0: `blue_filtered[:, :, 0] = 0`
   - Sets green channel to 0: `blue_filtered[:, :, 1] = 0`
   - Keeps blue channel unchanged
   - Displays blue-filtered image
7. **`ft_grey()` function** - Grayscale conversion:
   - Calculates mean across channels: `array.mean(axis=2)`
   - Result shape: `(height, width)` - single channel
   - Converts to uint8: `astype(np.uint8)`
   - Stacks to create 3-channel grayscale: `np.stack([grayscale, grayscale, grayscale], axis=2)`
   - Final shape: `(height, width, 3)` with identical channels
   - Displays grayscale image
8. `display_image()` helper function:
   - Creates figure without axes: `plt.axis('off')`
   - Shows image with custom title
   - Clean visualization without distracting axis labels
9. Main function demonstrates all five filters on same image

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