import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load
from validate_args import validate_args_for_prog


def display_graph(
    countries: list[str], life_expectancy: list[float],
    gdp: list[float], year: str
) -> None:
    """
    Display the graph of life expectancy vs GDP.

    Args:
        countries (list[str]): List of countries
        life_expectancy (list[float]): Life expectancy values
        gdp (list[float]): GDP values
        year (str): Year of the data

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(12, 8))
    plt.scatter(
        gdp, life_expectancy, alpha=0.7, s=50, c='blue',
        edgecolors='black', linewidth=0.5
    )

    for i in range(0, len(countries), 10):
        plt.annotate(
            countries[i], (gdp[i], life_expectancy[i]),
            xytext=(5, 5), textcoords='offset points',
            fontsize=8, alpha=0.7
        )

    plt.title(
        f'Life Expectancy vs GDP per Capita ({year})',
        fontsize=16, fontweight='bold'
    )
    plt.xlabel(
        'GDP per Capita (PPP, inflation-adjusted, log scale)',
        fontsize=14
    )
    plt.ylabel('Life Expectancy (years)', fontsize=14)
    plt.xscale('log')
    plt.grid(True, alpha=0.3, which='both')
    plt.ylim(min(life_expectancy) * 0.9, max(life_expectancy) * 1.1)

    correlation = np.corrcoef(gdp, life_expectancy)[0, 1]
    plt.text(
        0.02, 0.98, f'Correlation: {correlation:.3f}',
        transform=plt.gca().transAxes, fontsize=12,
        bbox=dict(
            boxstyle='round', facecolor='wheat', alpha=0.8
        ),
        verticalalignment='top'
    )
    plt.legend(['Countries'], loc='upper right', fontsize=12)
    plt.tight_layout()
    plt.show()


def parse_gdp_value(value: str) -> float:
    """
    Parse GDP value from string format (e.g., "1000", "1000.00", "1000.00k").

    Args:
        value (str): GDP value as string

    Returns:
        float: GDP value as number
    """
    value_str = value.strip()
    value_float = 0.0

    if value_str.endswith('k'):
        value_float = float(value_str[:-1]) * 1_000
    else:
        value_float = float(value_str)

    return value_float


def extract_value(
    country_data: pd.DataFrame, year: str
) -> float:
    """
    Extract value for a specific year.

    Args:
        country_data (pd.DataFrame): The country's data row
        year (str): The year to extract value for

    Returns:
        float: The extracted value

    Raises:
        None
    """
    return country_data[year].iloc[0]


def get_country_data(
    dataset: pd.DataFrame, country: str
) -> pd.DataFrame:
    """
    Get the data row for a specific country.

    Args:
        dataset (pd.DataFrame): The dataset
        country (str): The country to get data for

    Returns:
        pd.DataFrame: The filtered dataset containing only
        the country's data

    Raises:
        None
    """
    return dataset[dataset['country'] == country]


def extract_countries_data(
    life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame,
    year: str, countries: list[str]
) -> tuple[list[str], list[float], list[float]]:
    """
    Extract life expectancy and GDP data for a list of countries.

    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset
        year (str): Year to extract data for
        countries (list[str]): List of countries to extract data for

    Returns:
        tuple[list[str], list[float], list[float]]: Countries,
        life expectancy, GDP

    Raises:
        None
    """
    countries_list = []
    life_expectancy = []
    gdp = []

    for country in countries:
        life_data = get_country_data(life_expectancy_df, country)
        life_value = extract_value(life_data, year)

        gdp_data = get_country_data(gdp_df, country)
        gdp_value = extract_value(gdp_data, year)
        gdp_value = parse_gdp_value(gdp_value)

        countries_list.append(country)
        life_expectancy.append(life_value)
        gdp.append(gdp_value)

    return countries_list, life_expectancy, gdp


def get_common_countries(
    life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame, year: str
) -> list[str]:
    """
    Get list of countries that exist in both datasets and have valid
    life expectancy data for the given year.

    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset
        year (str): Year to check for valid life expectancy data

    Returns:
        list[str]: List of common country names with valid life expectancy

    Raises:
        None
    """
    common_countries = (
        set(life_expectancy_df['country'].values) &
        set(gdp_df['country'].values)
    )

    valid_countries = []
    for country in common_countries:
        country_data = get_country_data(life_expectancy_df, country)
        value = country_data[year].iloc[0]
        if pd.notna(value):
            valid_countries.append(country)

    return valid_countries


def get_year_data(
    life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame, year: str
) -> tuple[list[str], list[float], list[float]]:
    """
    Extract life expectancy and GDP data for a specific year.

    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset
        year (str): Year to extract data for

    Returns:
        tuple[list[str], list[float], list[float]]: Countries,
        life expectancy, GDP

    Raises:
        None
    """
    common_countries = get_common_countries(
        life_expectancy_df, gdp_df, year
    )

    return extract_countries_data(
        life_expectancy_df, gdp_df, year, common_countries
    )


def main() -> int:
    """
    Main function to load and display life expectancy vs GDP data.

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

    life_expectancy_df = load(
        "../csv_files/valid_csv/life_expectancy_years.csv"
    )
    if life_expectancy_df is None:
        return 1

    gdp_df = load(
        "../csv_files/valid_csv/"
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    if gdp_df is None:
        return 1

    year = '2025'
    countries, life_expectancy, gdp = get_year_data(
        life_expectancy_df, gdp_df, year
    )

    display_graph(countries, life_expectancy, gdp, year)

    return 0


if __name__ == "__main__":
    sys.exit(main())
