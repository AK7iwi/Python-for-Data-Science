import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load
from validate_args import validate_args


def get_campus_country() -> str:
    """
    Get the country name for the campus.
    For 42 campuses, this would typically be 'France'.
    
    Returns:
        str: Country name for the campus
    """
    # You can modify this to return the appropriate country
    # For 42 campuses in France:
    return "France"


def get_comparison_country() -> str:
    """
    Get the comparison country (Belgium as specified in the exercise).
    
    Returns:
        str: Comparison country name
    """
    return "Belgium"


def filter_years_1800_2050(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Filter dataset to include only years from 1800 to 2050.
    
    Args:
        dataset (pd.DataFrame): The population dataset
        
    Returns:
        pd.DataFrame: Filtered dataset with years 1800-2050
    """
    # Get all columns except 'country'
    year_columns = [col for col in dataset.columns if col != 'country']
    
    # Filter to years 1800-2050
    filtered_columns = ['country']  # Always include country column
    for col in year_columns:
        try:
            year = int(col)
            if 1800 <= year <= 2050:
                filtered_columns.append(col)
        except ValueError:
            # Skip non-numeric columns
            continue
    
    return dataset[filtered_columns]


def parse_population_value(value: str) -> float:
    """
    Parse population value from string format (e.g., "29M", "3.25M", "40.2k").
    
    Args:
        value (str): Population value as string
        
    Returns:
        float: Population value as number
    """
    if pd.isna(value) or value == '':
        return None
    
    value_str = str(value).strip()
    
    # Handle millions (M)
    if value_str.endswith('M'):
        try:
            return float(value_str[:-1]) * 1_000_000
        except ValueError:
            return None
    
    # Handle thousands (k)
    elif value_str.endswith('k'):
        try:
            return float(value_str[:-1]) * 1_000
        except ValueError:
            return None
    
    # Handle regular numbers
    else:
        try:
            return float(value_str)
        except ValueError:
            return None


def get_country_data(dataset: pd.DataFrame, country: str) -> tuple[list[int], list[float]]:
    """
    Extract population data for a specific country.
    
    Args:
        dataset (pd.DataFrame): The population dataset
        country (str): The country to extract data for
        
    Returns:
        tuple[list[int], list[float]]: Years and population values
    """
    if country not in dataset['country'].values:
        print(f"Error: Country '{country}' not found in dataset")
        return [], []
    
    # Filter data for the specific country
    country_data = dataset[dataset['country'] == country]
    
    # Get years (columns excluding 'country')
    years = []
    populations = []
    
    for col in dataset.columns:
        if col != 'country':
            try:
                year = int(col)
                if 1800 <= year <= 2050:  # Filter years 1800-2050
                    value = country_data[col].iloc[0]
                    parsed_value = parse_population_value(value)
                    if parsed_value is not None and parsed_value > 0:  # Only include valid positive values
                        years.append(year)
                        populations.append(parsed_value)
            except (ValueError, TypeError):
                continue
    
    return years, populations


def plot_population_comparison(dataset: pd.DataFrame, country1: str, country2: str) -> None:
    """
    Plot population comparison between two countries from 1800 to 2050.
    
    Args:
        dataset (pd.DataFrame): The population dataset
        country1 (str): First country (campus country)
        country2 (str): Second country (comparison country)
        
    Returns:
        None
    """
    # Filter dataset to years 1800-2050
    filtered_dataset = filter_years_1800_2050(dataset)
    
    # Get data for both countries
    years1, pop1 = get_country_data(filtered_dataset, country1)
    years2, pop2 = get_country_data(filtered_dataset, country2)
    
    if not years1 and not years2:
        print(f"Error: No valid data found for {country1} or {country2}")
        return

    # Create the plot
    plt.figure(figsize=(14, 8))
    
    # Plot both countries
    if years1:
        plt.plot(years1, pop1, 'b-', linewidth=2, label=f'{country1}', marker='o', markersize=3)
    if years2:
        plt.plot(years2, pop2, 'r-', linewidth=2, label=f'{country2}', marker='s', markersize=3)
    
    # Customize the plot
    plt.title(f'Population Comparison: {country1} vs {country2} (1800-2050)', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Population', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Set x-axis limits to show the full range
    plt.xlim(1800, 2050)
    
    # Format y-axis to show population in millions or billions
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e6:.0f}M' if x < 1e9 else f'{x/1e9:.1f}B'))
    
    # Add some styling
    plt.tight_layout()
    
    # Show the plot
    plt.show()


def main() -> int:
    """
    Main function to load and display population comparison data.
    """
    try:
        validate_args()
        
        # Load the dataset
        dataset = load("../csv_files/population_total.csv")
        if dataset is None:
            print("Error: Failed to load dataset")
            return 1
        
        # Get the countries to compare
        campus_country = get_campus_country()
        comparison_country = get_comparison_country()
        
        print(f"Comparing population data: {campus_country} vs {comparison_country}")
        print("Displaying years 1800-2050")
        
        # Plot the comparison
        plot_population_comparison(dataset, campus_country, comparison_country)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
