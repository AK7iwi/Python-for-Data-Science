import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from validate_args import validate_args_for_prog


def display_graph(
    years_clean: list[int], values_clean: list[float], country: str
) -> None:
    """
    Display the graph of life expectancy over time for a specific country.

    Args:
        years_clean (list[int]): List of years
        values_clean (list[float]): List of life expectancy values
        country (str): The country to display the graph for

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(12, 8))
    plt.plot(
        years_clean, values_clean, 'b-', linewidth=2,
        label=f'Life Expectancy - {country}'
    )
    plt.title(
        f'Life Expectancy Over Time - {country}',
        fontsize=16, fontweight='bold'
    )
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Life Expectancy (years)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def extract_life_expectancy_values(
    country_data: pd.DataFrame, years: list[int]
) -> tuple[list[int], list[float]]:
    """
    Extract life expectancy values for given years.

    Args:
        country_data (pd.DataFrame): The country's data row
        years (list[int]): List of years to extract values for

    Returns:
        tuple[list[int], list[float]]: List of years and life expectancy values

    Raises:
        None
    """
    years_clean = []
    values_clean = []
    for year in years:
        value = country_data[str(year)].iloc[0]
        if pd.notna(value):
            years_clean.append(year)
            values_clean.append(float(value))

    return years_clean, values_clean


def get_country_data(
    dataset: pd.DataFrame, country: str
) -> tuple[pd.DataFrame, list[int]]:
    """
    Get the data row for a specific country.

    Args:
        dataset (pd.DataFrame): The life expectancy dataset
        country (str): The country to get data for

    Returns:
        tuple[pd.DataFrame, list[int]]: The filtered dataset containing
        only the country's data and the years

    Raises:
        None
    """
    country_data = dataset[dataset['country'] == country]
    years = [int(year) for year in country_data.columns if year != 'country']

    return country_data, years


def get_life_expectancy_data(
    dataset: pd.DataFrame, country: str
) -> tuple[list[int], list[float]]:
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
    country_data, years = get_country_data(dataset, country)

    return extract_life_expectancy_values(country_data, years)


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

    country = "France"
    years_clean, values_clean = get_life_expectancy_data(dataset, country)

    display_graph(years_clean, values_clean, country)

    return 0


if __name__ == "__main__":
    sys.exit(main())
