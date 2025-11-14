<div align="center">

# MODULE 02 - DataTable

</div>

## Summary

[1. Exercice 00: Load my Dataset](#1-exercice-00-load-my-dataset)  
[2. Exercice 01: draw my country](#2-exercice-01-draw-my-country)  
[3. Exercice 02: compare my country](#3-exercice-02-compare-my-country)  
[4. Exercice 03: draw my year](#4-exercice-03-draw-my-year)  
[Additional Resources](#additional-resources)


## Warning

This learning guide follows a progressive and logical structure where concepts are introduced when they are most relevant to the exercise context.

So:
- Theory points and some advanced concepts may be used before their detailed explanation appears in later exercises
- There are additional resources at the end if you want to explore a concept in more depth


## Introduction

This module focuses on data manipulation and visualization using CSV files and the Pandas library:

- **CSV Files**: Reading and processing comma-separated value files
- **Pandas**: Powerful data analysis and manipulation library
- **Data Visualization**: Creating plots and charts from real-world datasets


## 1. Exercice 00: Load my Dataset

### I) New libraries used
- `pandas`: External library for data manipulation and analysis (imported as `pd`)

### II) New built-in functions, methods, attributes used
- `open()`: Built-in function to open files for reading/writing
- `str.lower()`: String method that converts string to lowercase
- `str.endswith()`: String method that checks if string ends with specified suffix

### III) New external functions, methods, attributes used
- `pd.read_csv()`: Reads CSV file and returns DataFrame
- `pd.DataFrame`: Pandas primary data structure (2D labeled table)
- `dataframe.shape`: DataFrame attribute returning tuple `(rows, columns)`
- `pd.errors.EmptyDataError`: Pandas exception raised when CSV file is empty
- `pd.errors.ParserError`: Pandas exception raised when CSV parsing fails

### IV) New theory points

- **Pandas library**
  - Most popular Python library for data analysis and manipulation
  - Built on top of NumPy for efficient numerical operations
  - Provides DataFrame: 2D labeled data structure with columns of potentially different types
  - Installation: `pip install pandas`
  - Convention: imported as `pd`

- **DataFrame data structure**
  - 2D labeled table with rows and columns (like spreadsheet or SQL table)
  - Each column can have different data type (int, float, string, etc.)
  - Has row indices and column labels
  - Powerful methods for filtering, grouping, merging, and analyzing data
  - Type hint: `pd.DataFrame`

- **Reading CSV files with Pandas**
  - `pd.read_csv(path)`: Loads CSV file into DataFrame
  - Automatically detects column names from first row
  - Handles missing values, different delimiters, and various CSV formats
  - Returns DataFrame object ready for analysis
  - Much more convenient than manual CSV parsing

- **DataFrame shape attribute**
  - `dataframe.shape`: Returns tuple `(number_of_rows, number_of_columns)`
  - Similar to NumPy array shape
  - Useful for understanding dataset dimensions
  - Example: `(259, 302)` means 259 rows and 302 columns
  - Read-only attribute (cannot be modified directly)

- **CSV file validation**
  - Check file extension: `path.lower().endswith('.csv')`
  - `str.lower()`: Ensures case-insensitive comparison
  - `str.endswith()`: Checks if string ends with specified suffix
  - Important to validate before attempting to parse

- **File opening with context manager**
  - `with open(path, 'r'):` opens file for reading
  - Used here to check if path is valid and readable
  - Automatically closes file even if exception occurs
  - Can detect if path is directory vs file

- **Pandas-specific exceptions**
  - **EmptyDataError**: Raised when CSV file has no data (empty or only whitespace)
  - **ParserError**: Raised when CSV structure is malformed or inconsistent
  - Both from `pd.errors` module
  - Should be caught separately from standard Python exceptions
  - Allow specific error handling for data issues

### V) Logic used for the exercise
1. Import pandas library and custom validation modules
2. Define `validate_path_string()` function:
   - Checks if path parameter is a string using `isinstance()`
   - Raises `TypeError` if not a string
3. Define `validate_csv_format()` function:
   - Opens file with context manager to verify it exists and is accessible
   - Converts path to lowercase and checks if it ends with `.csv`
   - Raises `ValueError` if not a CSV file
4. Define `validate_path()` wrapper function:
   - Calls both validation functions in sequence
   - Ensures path is valid string pointing to CSV file
5. Define `print_dataset_info()` function:
   - Takes DataFrame as parameter
   - Prints dimensions using `dataset.shape` attribute
   - Format: "Loading dataset of dimensions (rows, columns)"
6. Define `load()` function as main CSV loader:
   - Takes file path as parameter
   - Validates path with `validate_path()`
   - Reads CSV with `pd.read_csv(path)`
   - Catches multiple exceptions with separate except blocks:
     - `pd.errors.EmptyDataError`: Empty CSV file
     - `pd.errors.ParserError`: Malformed CSV structure
     - `TypeError`: Invalid path type
     - `ValueError`: Invalid CSV format
     - `IsADirectoryError`: Path is directory, not file
     - `FileNotFoundError`: File doesn't exist
     - `PermissionError`: No read permission
   - Returns `None` on any error (with printed error message)
   - On success: prints dataset info and returns DataFrame
7. Main function demonstrates usage:
   - Validates command line arguments
   - Loads and prints example dataset from CSV file
   - Returns appropriate exit code


## 2. Exercice 01: draw my country

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
No new built-in functions, methods, or attributes used.

### III) New external functions, methods, attributes used
- `plt.plot()`: Creates line plot with x and y data
- `plt.legend()`: Displays legend on the plot
- `plt.grid()`: Adds grid lines to the plot
- `plt.tight_layout()`: Adjusts plot layout to prevent label cutoff
- `dataframe['column_name']`: DataFrame column selection using bracket notation
- `dataframe.columns`: DataFrame attribute that returns list of column names
- `dataframe.iloc[]`: Integer-location based indexing for DataFrames
- `pd.notna()`: Checks if value is not NaN (Not a Number) or missing
- `load()`: Custom function imported from load_csv module

### IV) New theory points

- **Line plots with plt.plot()**
  - `plt.plot(x, y, format_string, **kwargs)`: Creates line plot
  - `x`: List/array of x-axis values
  - `y`: List/array of y-axis values
  - Format string: Combines color and line style (e.g., `'b-'` = blue solid line)
  - Common kwargs:
    - `linewidth`: Line thickness in points
    - `label`: Label for legend
    - `marker`: Marker style for data points
  - Multiple plots can be drawn on same figure

- **Adding legend with plt.legend()**
  - `plt.legend(fontsize=size)`: Displays legend on plot
  - Shows labels from `label` parameter in `plt.plot()`
  - Automatically positioned by default (can be customized)
  - Helps identify multiple data series on same plot
  - `fontsize` parameter controls text size

- **Adding grid with plt.grid()**
  - `plt.grid(True, alpha=transparency)`: Adds grid lines to plot
  - Makes it easier to read values from plot
  - `alpha` controls transparency (0.0 to 1.0)
  - Can specify which axis to show grid on
  - Useful for data-dense visualizations

- **Layout adjustment with plt.tight_layout()**
  - Automatically adjusts subplot/plot spacing
  - Prevents label cutoff at edges of figure
  - Should be called before `plt.show()`
  - Ensures all elements (title, labels, legend) are visible
  - No manual margin adjustment needed

- **DataFrame column selection**
  - **Bracket notation**: `dataframe['column_name']` returns Series (single column)
  - Returns `pd.Series` object (1D labeled array)
  - Column names are strings (year columns need conversion)
  - Can chain operations: `dataframe['col'].iloc[0]` gets first value
  - Similar to dictionary key access syntax

- **DataFrame filtering/selection**
  - **Boolean filtering**: `dataframe[dataframe['column'] == value]`
  - Creates boolean mask (True/False for each row)
  - Returns new DataFrame with only matching rows
  - Example: `dataset[dataset['country'] == 'France']` returns France's data
  - Efficient way to filter large datasets

- **DataFrame.columns attribute**
  - Returns Index object with all column names
  - Can be iterated over like a list
  - Useful for dynamic column processing
  - Example: `[int(year) for year in df.columns if year != 'country']`
  - Read-only attribute

- **DataFrame.iloc indexer**
  - Integer-location based indexing (like NumPy arrays)
  - `dataframe.iloc[row_index]`: Select row by position
  - `dataframe.iloc[row_index, col_index]`: Select specific cell
  - Zero-based indexing
  - `.iloc[0]` gets first element from Series
  - Different from `.loc[]` which uses labels

- **Handling missing data with pd.notna()**
  - Checks if value is NOT NaN (Not a Number) or missing
  - Returns `True` for valid values, `False` for NaN/None
  - Opposite of `pd.isna()` or `pd.isnull()`
  - Essential for data cleaning before plotting
  - Example: `if pd.notna(value): years_clean.append(year)`
  - Prevents plotting errors from missing data

- **Data cleaning pattern**
  - Iterate through raw data
  - Check each value with `pd.notna()`
  - Keep only valid (non-NaN) values
  - Build separate "clean" lists for plotting
  - Ensures aligned x and y data (same length)

### V) Logic used for the exercise
1. Import matplotlib, pandas, and custom load function from ex00
2. Define `display_graph()` function:
   - Takes cleaned years, values, and country name as parameters
   - Creates figure with specified size
   - Plots line with `plt.plot()` using blue solid line (`'b-'`), linewidth 2, and label
   - Adds title, axis labels with custom font sizes
   - Adds legend with `plt.legend()` for identifying data series
   - Adds grid with `plt.grid()` for easier reading (alpha=0.3 for subtle appearance)
   - Applies `plt.tight_layout()` to prevent label cutoff
   - Displays plot
3. Define `extract_life_expectancy_values()` function:
   - Takes country's DataFrame row and list of years
   - Initializes empty lists for cleaned years and values
   - Loops through years and extracts values using `country_data[str(year)].iloc[0]`
   - Filters out NaN values using `pd.notna()`
   - Converts valid values to float and appends to clean lists
   - Returns tuple of cleaned years and values
4. Define `get_country_data()` function:
   - Filters dataset to get specific country's row using boolean filtering
   - Extracts years from column names using list comprehension
   - Excludes 'country' column from years list
   - Returns filtered DataFrame and years list
5. Define `get_life_expectancy_data()` wrapper function:
   - Calls `get_country_data()` to filter by country
   - Calls `extract_life_expectancy_values()` to clean data
   - Returns cleaned years and values ready for plotting
6. Main function:
   - Validates command line arguments
   - Loads life expectancy dataset using `load()` from ex00
   - Checks if dataset loaded successfully (not None)
   - Sets country to "France"
   - Gets cleaned data with `get_life_expectancy_data()`
   - Displays line graph with `display_graph()`
   - Returns appropriate exit code


## 3. Exercice 02: compare my country

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `str.strip()`: Removes leading and trailing whitespace from string

### III) New external functions, methods, attributes used
- `plt.xlim()`: Sets limits for x-axis (minimum and maximum values)
- `plt.gca()`: Gets current axes object for further customization
- `plt.FuncFormatter()`: Creates custom formatter for axis labels
- `ax.yaxis.set_major_formatter()`: Sets custom formatter for y-axis tick labels

### IV) New theory points

- **Plotting multiple data series on same figure**
  - Call `plt.plot()` multiple times before `plt.show()`
  - Each plot can have different color, line style, and label
  - Example: Blue line with circles (`'b-'`, `marker='o'`) vs red line with squares (`'r-'`, `marker='s'`)
  - Legend automatically shows all labeled series
  - Useful for comparing trends between datasets

- **Plot markers**
  - `marker` parameter in `plt.plot()` adds markers at each data point
  - Common marker styles:
    - `'o'`: Circle
    - `'s'`: Square
    - `'^'`: Triangle up
    - `'*'`: Star
  - `markersize` parameter controls marker size in points
  - Helps distinguish data points and series

- **Setting axis limits with plt.xlim()**
  - `plt.xlim(min, max)`: Sets minimum and maximum values for x-axis
  - Forces plot to show specific range regardless of data
  - Example: `plt.xlim(1800, 2050)` shows years from 1800 to 2050
  - Similar function exists: `plt.ylim()` for y-axis
  - Useful for focusing on specific data range or maintaining consistent scale

- **Getting current axes with plt.gca()**
  - `plt.gca()`: Returns current axes object
  - GCA stands for "Get Current Axes"
  - Allows access to advanced axes properties and methods
  - Returns `matplotlib.axes.Axes` object
  - Necessary for low-level customization like custom formatters

- **Custom axis formatting**
  - **plt.FuncFormatter()**: Creates formatter from function
    - Takes function with signature: `func(x, p)` where `x` is value, `p` is position
    - Returns formatted string for display
    - Can use lambda functions or regular functions
  - **ax.yaxis.set_major_formatter()**: Applies formatter to y-axis tick labels
    - Takes formatter object as parameter
    - Changes how numbers are displayed (e.g., `1000000` → `1M`)
    - Similar exists: `ax.xaxis.set_major_formatter()` for x-axis
  - Useful for making large numbers more readable
  - Example with lambda: `lambda x, p: f'{x/1e6:.0f}M' if x < 1e9 else f'{x/1e9:.1f}B'`

- **Numeric literals with underscores**
  - Python allows underscores in numeric literals for readability
  - `1_000_000` is same as `1000000`
  - `1_000_000_000` is same as `1000000000`
  - Underscores ignored by Python, only for human readability
  - Can place underscores anywhere in number
  - Particularly useful for large numbers

- **Scientific notation shortcuts**
  - `1e6` means `1 × 10^6` = `1000000` (1 million)
  - `1e9` means `1 × 10^9` = `1000000000` (1 billion)
  - More compact than writing full numbers
  - Commonly used in scientific computing
  - Can be used in comparisons and arithmetic

- **String parsing for population data**
  - Population data often stored with suffix: `"29M"`, `"3.25B"`, `"40.2k"`
  - Need to parse string and convert to numeric value
  - Process:
    1. Strip whitespace with `str.strip()`
    2. Check suffix with `str.endswith()`
    3. Extract numeric part with string slicing `[:-1]` (all except last character)
    4. Convert to float and multiply by appropriate factor
  - Suffix meanings: `'B'` (billion = ×1e9), `'M'` (million = ×1e6), `'k'` (thousand = ×1e3)

### V) Logic used for the exercise
1. Import matplotlib, pandas, and custom load function
2. Define `display_graph()` function:
   - Takes two countries' names, populations, and years
   - Creates figure with size 14x8 inches
   - Plots first country with blue line, circle markers
   - Plots second country with red line, square markers
   - Adds title showing comparison and year range
   - Adds axis labels and legend
   - Sets x-axis limits to 1800-2050 with `plt.xlim()`
   - Gets current axes with `plt.gca()`
   - Creates custom y-axis formatter using lambda function
   - Formatter displays values as "XM" (millions) or "X.XB" (billions)
   - Applies formatter to y-axis with `ax.yaxis.set_major_formatter()`
   - Applies tight layout and displays plot
3. Define `parse_population_value()` function:
   - Takes population string (e.g., "29M", "3.25B")
   - Strips whitespace
   - Checks if ends with 'B', 'M', or 'k'
   - Extracts numeric part with `[:-1]` slicing
   - Converts to float and multiplies by appropriate factor
   - Returns numeric population value
4. Define `extract_population_values()` function:
   - Takes country DataFrame and list of years
   - Loops through years and gets string values
   - Parses each value with `parse_population_value()`
   - Returns list of numeric population values
5. Define `get_country_data()` function:
   - Filters dataset by country name
   - Extracts years from columns with list comprehension
   - Filters years to range 1800-2050
   - Returns country data and years list
6. Define `get_populations_data()` wrapper function:
   - Gets data for both countries
   - Extracts population values for both
   - Returns years and both population lists
7. Main function:
   - Validates command line arguments
   - Loads population dataset
   - Sets countries to "France" and "Belgium"
   - Gets population data for both countries
   - Displays comparison graph
   - Returns appropriate exit code


## 4. Exercice 03: draw my year

### I) New libraries used
No new libraries used.

### II) New built-in functions, methods, attributes used
- `set()`: Creates set from iterable (unordered collection of unique elements)
- `max()`: Returns maximum value from iterable or multiple arguments

### III) New external functions, methods, attributes used
- `plt.scatter()`: Creates scatter plot with individual data points
- `plt.annotate()`: Adds text annotations to specific points on plot
- `plt.xscale()`: Sets scale type for x-axis (linear, log, etc.)
- `plt.ylim()`: Sets limits for y-axis (minimum and maximum values)
- `plt.text()`: Adds text at specific position on plot
- `ax.transAxes`: Coordinate system for axes (0-1 range for positioning)
- `np.corrcoef()`: Computes correlation coefficient matrix between variables
- `dataframe['column'].values`: Returns underlying NumPy array from Series

### IV) New theory points

- **Scatter plots with plt.scatter()**
  - `plt.scatter(x, y, **kwargs)`: Plots individual data points
  - Different from line plots - shows discrete points, not connected
  - Useful for showing relationship between two variables
  - Common parameters:
    - `alpha`: Transparency (0.0 to 1.0)
    - `s`: Marker size in points²
    - `c`: Color (single color or array of colors per point)
    - `edgecolors`: Color of marker edge/border
    - `linewidth`: Width of marker edge
  - Perfect for correlation and distribution visualization

- **Logarithmic scale with plt.xscale()**
  - `plt.xscale('log')`: Sets x-axis to logarithmic scale
  - Useful when data spans multiple orders of magnitude
  - Each tick represents multiplication by constant factor (e.g., 10×)
  - Example: 100, 1000, 10000 instead of 100, 200, 300
  - Makes exponential relationships appear linear
  - Similar function: `plt.yscale('log')` for y-axis
  - GDP data often displayed on log scale due to huge variance

- **Y-axis limits with plt.ylim()**
  - `plt.ylim(min, max)`: Sets minimum and maximum values for y-axis
  - Similar to `plt.xlim()` but for vertical axis
  - Can use expressions: `plt.ylim(min(data) * 0.9, max(data) * 1.1)` adds 10% padding
  - Forces specific range for consistency or focus
  - Useful for zooming into data range

- **Adding annotations with plt.annotate()**
  - `plt.annotate(text, xy, xytext, textcoords, **kwargs)`: Adds label to specific point
  - `text`: String to display
  - `xy`: Tuple `(x, y)` of point to annotate
  - `xytext`: Offset for text position
  - `textcoords`: Coordinate system for xytext
    - `'offset points'`: Offset in points from xy position
    - Allows fine-tuning text placement
  - Parameters: `fontsize`, `alpha` for styling
  - Useful for labeling specific data points (countries, outliers)

- **Adding text with plt.text()**
  - `plt.text(x, y, text, transform, **kwargs)`: Adds text at position
  - `x, y`: Position coordinates
  - `text`: String to display
  - `transform`: Coordinate system to use
    - `plt.gca().transAxes`: Uses axes coordinates (0-1 range)
    - `(0, 0)` = bottom-left, `(1, 1)` = top-right
    - Independent of data range
  - `bbox`: Dictionary for text box styling
    - `boxstyle`: Shape (e.g., `'round'`)
    - `facecolor`: Background color
    - `alpha`: Transparency
  - `verticalalignment`: Vertical alignment (`'top'`, `'bottom'`, `'center'`)
  - Useful for displaying statistics or notes on plot

- **Grid control with which parameter**
  - `plt.grid(True, alpha=0.3, which='both')`: Enhanced grid control
  - `which` parameter controls which grid lines to show:
    - `'major'`: Only major tick marks (default)
    - `'minor'`: Only minor tick marks
    - `'both'`: Both major and minor tick marks
  - Especially useful with logarithmic scales
  - Provides finer visual guidance for reading values

- **Set operations in Python**
  - `set()`: Creates unordered collection of unique elements
  - Set intersection: `set1 & set2` returns common elements
  - Fast membership testing and deduplication
  - Example: `set(df1['country'].values) & set(df2['country'].values)`
  - Other operations: union (`|`), difference (`-`), symmetric difference (`^`)
  - Useful for finding common countries between datasets

- **DataFrame.values attribute**
  - Returns underlying NumPy array from DataFrame or Series
  - Strips away labels and returns raw data
  - Type: `numpy.ndarray`
  - Faster for certain operations (like set creation)
  - Example: `dataframe['country'].values` returns array of country names
  - Direct access to data without pandas overhead

- **range() with step parameter**
  - `range(start, stop, step)`: Generates sequence with custom step
  - `step`: Increment between numbers (default is 1)
  - Example: `range(0, len(countries), 10)` gives 0, 10, 20, 30...
  - Useful for sampling or skipping elements
  - Can be negative for counting down
  - Used here to annotate every 10th country (avoid cluttered labels)

- **Correlation coefficient**
  - `np.corrcoef(x, y)`: Computes Pearson correlation coefficient
  - Returns 2×2 matrix: `[[1, corr], [corr, 1]]`
  - Access coefficient with `[0, 1]` or `[1, 0]`
  - Value range: -1 to +1
    - +1: Perfect positive correlation (as x↑, y↑)
    - 0: No correlation
    - -1: Perfect negative correlation (as x↑, y↓)
  - Measures linear relationship strength between variables
  - Example: GDP vs life expectancy shows how they relate

- **NumPy data types**
  - NumPy has specific integer types: `np.int8`, `np.int16`, `np.int32`, `np.int64`
  - `np.int64`: 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
  - Pandas often returns NumPy types from DataFrames
  - Type hints: Can use union type `np.int64 | str`
  - Convert to Python types with `int()`, `float()`, `str()`
  - More memory-efficient and faster than Python's built-in types

- **Dictionary literals in function calls**
  - Can create dictionary inline using `dict()` constructor
  - Syntax: `dict(key1=value1, key2=value2)`
  - Example: `dict(boxstyle='round', facecolor='wheat', alpha=0.8)`
  - Equivalent to: `{'boxstyle': 'round', 'facecolor': 'wheat', 'alpha': 0.8}`
  - Cleaner syntax when keys are valid Python identifiers
  - Used here for bbox parameter in `plt.text()`

### V) Logic used for the exercise
1. Import matplotlib, pandas, numpy, and custom load function
2. Define `display_graph()` function:
   - Takes lists of countries, life expectancy, GDP, and year
   - Creates figure with specified size
   - Creates scatter plot with `plt.scatter()`:
     - X-axis: GDP values, Y-axis: life expectancy values
     - Blue points with black edges, alpha 0.7 for transparency
     - Size 50 points², edge linewidth 0.5
   - Annotates every 10th country using `range(0, len(countries), 10)`
   - Each annotation offset by (5, 5) points from data point
   - Adds title showing year
   - Sets x-axis to logarithmic scale with `plt.xscale('log')`
   - Sets y-axis limits with 10% padding above/below data range
   - Adds grid for both major and minor ticks
   - Computes correlation coefficient with `np.corrcoef()`
   - Displays correlation in text box using `plt.text()`
     - Positioned at (0.02, 0.98) in axes coordinates (top-left)
     - Formatted to 3 decimal places
     - Styled with rounded box, wheat background
   - Adds legend and displays plot
3. Define `parse_gdp_value()` function:
   - Takes GDP value as NumPy int64 or string
   - Converts to string and strips whitespace
   - Checks if ends with 'k' suffix
   - Extracts numeric part and multiplies by 1000 if 'k'
   - Returns float value
4. Define `get_country_data()` function:
   - Filters DataFrame by country name using boolean filtering
   - Returns filtered DataFrame
5. Define `extract_countries_data()` function:
   - Takes both datasets, year, and list of countries
   - Loops through countries list
   - For each country:
     - Gets life expectancy value for year
     - Gets GDP value for year and parses it
     - Appends country name, life expectancy, and GDP to lists
   - Returns three aligned lists
6. Define `get_common_countries()` function:
   - Gets country lists from both datasets using `.values`
   - Converts to sets and finds intersection with `&` operator
   - Loops through common countries
   - Filters out countries with NaN life expectancy for the year
   - Returns list of valid countries
7. Define `get_year_data()` wrapper function:
   - Gets common countries between datasets
   - Extracts data for all common countries
   - Returns countries, life expectancy, and GDP lists
8. Main function:
   - Validates command line arguments
   - Loads both life expectancy and GDP datasets
   - Checks both loaded successfully
   - Sets year to '1900'
   - Gets data for all countries in that year
   - Displays scatter plot showing GDP vs life expectancy
   - Returns appropriate exit code


## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [CSV File Format](https://en.wikipedia.org/wiki/Comma-separated_values)
- [Data Visualization Best Practices](https://www.tableau.com/learn/articles/data-visualization)
- [Correlation and Causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
