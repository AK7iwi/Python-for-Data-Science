import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load
from validate_args import validate_args


def parse_gdp_value(value: str) -> float:
    """
    Parse GDP value from string format (e.g., "1000", "1500").
    
    Args:
        value (str): GDP value as string
        
    Returns:
        float: GDP value as number
    """
    if pd.isna(value) or value == '':
        return None
    
    value_str = str(value).strip()
    
    try:
        return float(value_str)
    except ValueError:
        return None


def get_1900_data(life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame) -> tuple[list[str], list[float], list[float]]:
    """
    Extract life expectancy and GDP data for the year 1900.
    
    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset
        
    Returns:
        tuple[list[str], list[float], list[float]]: Countries, life expectancy, GDP
    """
    countries = []
    life_expectancy_1900 = []
    gdp_1900 = []
    
    # Get countries that exist in both datasets
    common_countries = set(life_expectancy_df['country'].values) & set(gdp_df['country'].values)
    
    for country in common_countries:
        # Get life expectancy for 1900
        life_data = life_expectancy_df[life_expectancy_df['country'] == country]
        if '1900' in life_data.columns:
            life_value = life_data['1900'].iloc[0]
            if pd.notna(life_value) and life_value > 0:
                # Get GDP for 1900
                gdp_data = gdp_df[gdp_df['country'] == country]
                if '1900' in gdp_data.columns:
                    gdp_value = gdp_data['1900'].iloc[0]
                    parsed_gdp = parse_gdp_value(gdp_value)
                    if parsed_gdp is not None and parsed_gdp > 0:
                        countries.append(country)
                        life_expectancy_1900.append(float(life_value))
                        gdp_1900.append(parsed_gdp)
    
    return countries, life_expectancy_1900, gdp_1900


def plot_life_expectancy_vs_gdp(countries: list[str], life_expectancy: list[float], gdp: list[float]) -> None:
    """
    Plot life expectancy vs GDP for the year 1900.
    
    Args:
        countries (list[str]): List of countries
        life_expectancy (list[float]): Life expectancy values
        gdp (list[float]): GDP values
        
    Returns:
        None
    """
    if not countries:
        print("Error: No valid data found for 1900")
        return
    
    # Create the scatter plot
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot
    scatter = plt.scatter(gdp, life_expectancy, alpha=0.7, s=50, c='blue', edgecolors='black', linewidth=0.5)
    
    # Add country labels for some points (to avoid overcrowding)
    # Only label every 10th country to keep the plot readable
    for i in range(0, len(countries), 10):
        plt.annotate(countries[i], (gdp[i], life_expectancy[i]), 
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=8, alpha=0.7)
    
    # Customize the plot
    plt.title('Life Expectancy vs GDP per Capita (1900)', fontsize=16, fontweight='bold')
    plt.xlabel('GDP per Capita (PPP, inflation-adjusted)', fontsize=14)
    plt.ylabel('Life Expectancy (years)', fontsize=14)
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3)
    
    # Set axis limits with some padding
    plt.xlim(min(gdp) * 0.8, max(gdp) * 1.2)
    plt.ylim(min(life_expectancy) * 0.9, max(life_expectancy) * 1.1)
    
    # Add some statistics
    correlation = np.corrcoef(gdp, life_expectancy)[0, 1]
    plt.text(0.02, 0.98, f'Correlation: {correlation:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, 
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             verticalalignment='top')
    
    # Add legend
    plt.legend(['Countries (1900)'], loc='upper right', fontsize=12)
    
    # Add some styling
    plt.tight_layout()
    
    # Show the plot
    plt.show()


def main() -> int:
    """
    Main function to load and display life expectancy vs GDP data for 1900.
    """
    try:
        validate_args()
        
        # Load the life expectancy dataset
        print("Loading life expectancy dataset...")
        life_expectancy_df = load("../csv_files/life_expectancy_years.csv")
        if life_expectancy_df is None:
            print("Error: Failed to load life expectancy dataset")
            return 1
        
        # Load the GDP dataset
        print("Loading GDP dataset...")
        gdp_df = load("../csv_files/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if gdp_df is None:
            print("Error: Failed to load GDP dataset")
            return 1
        
        # Extract 1900 data
        print("Extracting data for year 1900...")
        countries, life_expectancy_1900, gdp_1900 = get_1900_data(life_expectancy_df, gdp_df)
        
        if not countries:
            print("Error: No valid data found for 1900")
            return 1
        
        print(f"Found data for {len(countries)} countries in 1900")
        print("Creating visualization...")
        
        # Plot the data
        plot_life_expectancy_vs_gdp(countries, life_expectancy_1900, gdp_1900)
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
