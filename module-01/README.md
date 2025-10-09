<div align="center">

# MODULE 01 - Array

</div>

## Summary

[1. Exercice 00: Give my BMI](#1-exercice-00-give-my-bmi)  
[2. Exercice 01: Array2D](#2-exercice-01-array2d)  
[3. Exercice 02: Load image](#3-exercice-02-load-image)  
[4. Exercice 03: Zoom](#4-exercice-03-zoom)  
[5. Exercice 04: Rotate](#5-exercice-04-rotate)  
[6. Exercice 05: Pimp my image](#6-exercice-05-pimp-my-image)  
[Additional Resources](#additional-resources)

## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- Cross-references like "(already used in ex00)" indicate when a concept was previously introduced
- There are additional resources at the end if you want to explore a concept in more depth

## 1. Exercice 00: Give my BMI

### I) Libraries used
- `numpy`: External library for numerical computing
- `math`: Built-in library for mathematical functions
- `sys`: Built-in library for system-specific parameters

### II) Built-in functions and methods used
- `isinstance()`: **Built-in function** that checks if object is instance of a class
- `math.isfinite()`: **Module function** that checks if value is finite
- `len()`: **Built-in function** that returns length of a sequence
- `print()`: (already used in module00) //Explain 

### III) New theory points
- **NumPy array operations**
  - `np.asarray()`: Converts Python lists to NumPy arrays efficiently
  - Vectorized operations: `array1 / array2` performs element-wise division
  - Array broadcasting: Automatic expansion of arrays for operations
- **Data validation patterns**
  - Type checking: `isinstance(value, (int, float))`
  - Finite value checking: `math.isfinite(value)`
  - Positive value validation: `value > 0`
- **BMI calculation formula**
  - BMI = weight / (height²)
  - Vectorized calculation using NumPy arrays
- **Boolean array operations**
  - `array > limit`: Creates boolean array
  - `.tolist()`: Converts NumPy array back to Python list

### IV) Logic used for the exercise
1. **Validate input data** - Check types, finiteness, and positivity
2. **Convert Python lists to NumPy arrays** using `np.asarray()`
3. **Perform vectorized BMI calculation** using NumPy operations
4. **Apply limit comparison** using boolean array operations
5. **Return results as Python lists** using `.tolist()`
6. **Handle comprehensive error cases** with specific exception messages


## 2. Exercice 01: Array2D

### I) Libraries used
- `numpy`: (already used in ex00)
- `sys`: (already used in ex00)

### II) Built-in functions and methods used
- `isinstance()`: (already used in ex00)
- `len()`: (already used in ex00)
- `print()`: (already used in ex00)

### III) New theory points
- **2D array validation**
  - Structure validation: Check if input is list of lists
  - Content validation: Ensure all rows have same size
  - Empty row detection: Prevent empty sublists
- **Array slicing operations**
  - `array[start:end]`: Slice NumPy arrays efficiently
  - Negative indexing: `array[-2]` for second-to-last element
  - Bounds checking: Validate slice indices
- **NumPy array properties**
  - `.shape`: Returns dimensions of array
  - `.tolist()`: Converts NumPy array to Python list
  - Array slicing: More efficient than Python list slicing
- **Index normalization**
  - Convert negative indices to positive equivalents
  - Validate index bounds before slicing
  - Handle edge cases for array boundaries

### IV) Logic used for the exercise
1. **Validate 2D array structure** - Check if input is proper list of lists
2. **Validate array content** - Ensure consistent row sizes
3. **Validate slice indices** - Check bounds and types
4. **Convert to NumPy array** using `np.asarray()` for efficient slicing
5. **Perform array slicing** using NumPy's optimized slicing
6. **Display shape information** before and after slicing
7. **Return sliced data as Python list** using `.tolist()`


## 3. Exercice 02: Load image

### I) Libraries used
- `numpy`: (already used in ex00)
- `PIL`: External library for image processing
- `os`: Built-in library for operating system interface
- `sys`: (already used in ex00)

### II) Built-in functions and methods used
- `os.path.exists()`: **Module function** that checks if file exists
- `os.path.splitext()`: **Module function** that splits filename and extension
- `Image.open()`: **Class method** that opens image files
- `image.convert()`: **Method** that converts image color modes
- `print()`: (already used in ex00)

### III) New theory points
- **Image file handling**
  - File existence validation: `os.path.exists()`
  - File format validation: Check supported extensions
  - Path string validation: Ensure non-empty paths
- **PIL (Python Imaging Library)**
  - `Image.open()`: Load image files
  - Color mode conversion: `image.convert('RGB')`
  - Image properties: `.mode`, `.size`
- **NumPy array conversion**
  - `np.asarray(image)`: Convert PIL Image to NumPy array
  - Preserves data types: uint8 for image data
  - Memory efficient conversion
- **Image array properties**
  - Shape: `(height, width, channels)` for color images
  - Data type: uint8 (0-255 range)
  - Channel interpretation: RGB format

### IV) Logic used for the exercise
1. **Validate file path** - Check existence, format, and string validity
2. **Load image using PIL** with `Image.open()`
3. **Convert to RGB mode** if necessary using `image.convert()`
4. **Convert PIL Image to NumPy array** using `np.asarray()`
5. **Display image information** including dimensions and channels
6. **Return NumPy array** for further processing


## 4. Exercice 03: Zoom

### I) Libraries used
- `numpy`: (already used in ex00)
- `matplotlib`: External library for plotting and visualization
- `sys`: (already used in ex00)

### II) Built-in functions and methods used
- `plt.figure()`: **Function** that creates new figure
- `plt.imshow()`: **Function** that displays image data
- `plt.title()`: **Function** that sets plot title
- `plt.xlabel()`: **Function** that sets x-axis label
- `plt.ylabel()`: **Function** that sets y-axis label
- `plt.colorbar()`: **Function** that adds color bar
- `plt.show()`: **Function** that displays the plot
- `print()`: (already used in ex00)

### III) New theory points
- **Image visualization**
  - `matplotlib.pyplot`: Library for creating plots and visualizations
  - `plt.imshow()`: Display 2D image data
  - Color mapping: `cmap='gray'` for grayscale display
  - Figure sizing: `figsize=(width, height)`
- **Image processing operations**
  - Center calculation: `width // 2, height // 2`
  - Zoom area definition: Calculate crop boundaries
  - Array slicing: `image[start_y:end_y, start_x:end_x]`
- **Grayscale conversion**
  - RGB to grayscale: Manual conversion using dot product
  - Luminance formula: `0.299*R + 0.587*G + 0.114*B`
  - Data type conversion: `.astype(np.uint8)`
- **Array manipulation**
  - Shape analysis: `image.shape[:2]` for height and width
  - Channel handling: Check for 2D vs 3D arrays
  - Array copying: `array.copy()` for safe manipulation

### IV) Logic used for the exercise
1. **Load image** using previous `ft_load()` function
2. **Calculate zoom area** - Define center square region
3. **Crop image** using array slicing operations
4. **Convert to grayscale** using manual RGB conversion
5. **Display results** using matplotlib visualization
6. **Handle different image dimensions** and channel counts


## 5. Exercice 04: Rotate

### I) Libraries used
- `numpy`: (already used in ex00)
- `matplotlib`: (already used in ex03)
- `sys`: (already used in ex00)

### II) Built-in functions and methods used
- `plt.figure()`: (already used in ex03)
- `plt.imshow()`: (already used in ex03)
- `plt.title()`: (already used in ex03)
- `plt.xlabel()`: (already used in ex03)
- `plt.ylabel()`: (already used in ex03)
- `plt.axis()`: **Function** that controls axis display
- `plt.show()`: (already used in ex03)
- `print()`: (already used in ex00)

### III) New theory points
- **Array transposition**
  - Manual transpose: `transposed[j, i] = image[i, j]`
  - NumPy transpose: `array.T` (not used - manual implementation required)
  - Shape transformation: `(rows, cols)` → `(cols, rows)`
- **Manual array operations**
  - Nested loops: `for i in range(rows): for j in range(cols):`
  - Index swapping: `transposed[j, i] = image[i, j]`
  - Array initialization: `np.zeros((cols, rows, channels))`
- **Image rotation concepts**
  - Transpose vs rotation: Transpose swaps dimensions
  - Channel preservation: Maintain RGB channel structure
  - Data type preservation: Keep uint8 format
- **Array validation**
  - Dimension checking: `len(image.shape) < 2`
  - Shape analysis: Handle 2D and 3D arrays
  - Type validation: Ensure NumPy array input

### IV) Logic used for the exercise
1. **Load and zoom image** using previous functions
2. **Validate array dimensions** for proper processing
3. **Implement manual transpose** using nested loops
4. **Handle different array shapes** (2D vs 3D)
5. **Preserve data types** during transformation
6. **Display rotated image** using matplotlib
7. **Show shape changes** before and after rotation


## 6. Exercice 05: Pimp my image

### I) Libraries used
- `numpy`: (already used in ex00)
- `matplotlib`: (already used in ex03)
- `sys`: (already used in ex00)

### II) Built-in functions and methods used
- `plt.figure()`: (already used in ex03)
- `plt.imshow()`: (already used in ex03)
- `plt.title()`: (already used in ex03)
- `plt.axis()`: (already used in ex04)
- `plt.show()`: (already used in ex03)
- `print()`: (already used in ex00)

### III) New theory points
- **Image filtering operations**
  - Color channel isolation: `array[:, :, channel] = 0`
  - Channel indexing: RGB = [0, 1, 2] for [Red, Green, Blue]
  - Array copying: `array.copy()` for safe manipulation
- **Color space manipulation**
  - Red filter: Keep only red channel, zero others
  - Green filter: Keep only green channel, zero others
  - Blue filter: Keep only blue channel, zero others
  - Grayscale conversion: Average RGB channels
- **Array operations**
  - In-place modification: `array[:, :, 1] = 0`
  - Array copying: `array.copy()` for independent copies
  - Data type preservation: Maintain uint8 format
- **Image processing pipeline**
  - Load → Validate → Copy → Filter → Display
  - Non-destructive operations: Preserve original data
  - Independent filtering: Each filter creates separate copy

### IV) Logic used for the exercise
1. **Load image** using `ft_load()` function
2. **Validate array properties** for image processing
3. **Create independent copies** using `array.copy()`
4. **Apply color filters** by zeroing specific channels
5. **Implement grayscale conversion** using manual averaging
6. **Display filtered images** using matplotlib
7. **Preserve original data** throughout processing pipeline

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