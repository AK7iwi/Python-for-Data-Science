import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from validate_args import validate_args


def get_campus_country() -> str:
    """
    Get the country name for the campus.
    For 42 campuses, this would typically be 'France'.
    
    Returns:
        str: Country name for the campus
    """
    return "France"


def plot_life_expectancy(dataset: pd.DataFrame, country: str) -> None:
    """
    Plot life expectancy data for a specific country.
    
    Args:
        dataset (pd.DataFrame): The life expectancy dataset
        country (str): The country to plot
        
    Returns:
        None
    """
    if country not in dataset['country'].values:
        print(f"Error: Country '{country}' not found in dataset")
        return
    
    # Filter data for the specific country
    country_data = dataset[dataset['country'] == country]
    
    # Get years (columns excluding 'country')
    years = [col for col in dataset.columns if col != 'country']
    years = [int(year) for year in years if year.isdigit()]
    
    # Get life expectancy values for the country
    life_expectancy = []
    for year in years:
        if str(year) in country_data.columns:
            value = country_data[str(year)].iloc[0]
            if pd.notna(value):  # Only include non-NaN values
                life_expectancy.append(value)
            else:
                life_expectancy.append(None)
        else:
            life_expectancy.append(None)
    
    # Filter out None values and corresponding years
    valid_data = [(year, value) for year, value in zip(years, life_expectancy) if value is not None]
    if not valid_data:
        print(f"Error: No valid data found for {country}")
        return
    
    years_clean, values_clean = zip(*valid_data)
    
    # Display function
    plt.figure(figsize=(12, 8))
    plt.plot(years_clean, values_clean, 'b-', linewidth=2, label=f'Life Expectancy - {country}')
    plt.title(f'Life Expectancy Over Time - {country}', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Life Expectancy (years)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main() -> int:
    """
    Main function to load and display life expectancy data.
    """
    try:
        validate_args()
        
        dataset = load("../csv_files/life_expectancy_years.csv")
        if dataset is None:
            print("Error: Failed to load dataset")
            return 1
        
        country = get_campus_country()
        print(f"Displaying life expectancy data for: {country}")
        
        plot_life_expectancy(dataset, country)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
