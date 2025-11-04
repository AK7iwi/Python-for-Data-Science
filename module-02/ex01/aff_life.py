import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from validate_args import validate_args_for_prog


def display_graph(years_clean: list[int], values_clean: list[float], country: str, ) -> None:
    """
    Display the graph of life expectancy over time for a specific country.

    Args:
        country (str): The country to display the graph for

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(12, 8))
    plt.plot(years_clean, values_clean, 'b-', linewidth=2, label=f'Life Expectancy - {country}')
    plt.title(f'Life Expectancy Over Time - {country}', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Life Expectancy (years)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def get_life_expectancy(dataset: pd.DataFrame, country: str) -> tuple[list[int], list[float]]:
    """
    Get life expectancy data for a specific country.
    
    Args:
        dataset (pd.DataFrame): The life expectancy dataset
        country (str): The country to plot
        
    Returns:
        tuple[list[int], list[float]]: Years and life expectancy values

    Raises:
        None
    """
    #Not EAFP
    if country not in dataset['country'].values:
        print(f"Error: Country '{country}' not found in dataset")
        return
    
    country_data = dataset[dataset['country'] == country]
    
    years = [col for col in dataset.columns if col != 'country']
    years = [int(year) for year in years if year.isdigit()]
    
    life_expectancy = []
    for year in years:
        if str(year) in country_data.columns:
            value = country_data[str(year)].iloc[0]
            if pd.notna(value):
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

    return years_clean, values_clean


def main() -> int:
    """
    Main function to load and display life expectancy data.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        validate_args_for_prog()
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1
        
    dataset = load("../csv_files/valid_csv/life_expectancy_years.csv")
    if dataset is None:
        return 1

    years_clean, values_clean = get_life_expectancy(dataset, "France")
    
    display_graph(years_clean, values_clean, "France")

    return 0


if __name__ == "__main__":
    sys.exit(main())
