import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load
from validate_args import validate_args_for_prog


def display_graph(
    countries: list[str], life_expectancy: list[float],
    gdp: list[float]
) -> None:
    """
    Display the graph of life expectancy vs GDP for the year 1900.

    Args:
        countries (list[str]): List of countries
        life_expectancy (list[float]): Life expectancy values
        gdp (list[float]): GDP values

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
        'Life Expectancy vs GDP per Capita (1900)',
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
    plt.legend(['Countries (1900)'], loc='upper right', fontsize=12)
    plt.tight_layout()
    plt.show()


def parse_gdp_value(value: str) -> float | None:
    """
    Parse GDP value from string format (e.g., "1000", "1500").

    Args:
        value (str): GDP value as string

    Returns:
        float | None: GDP value as number, or None if invalid

    Raises:
        None
    """
    if pd.isna(value) or value == '':
        return None

    value_str = str(value).strip()

    try:
        return float(value_str)
    except ValueError:
        return None


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


def extract_life_expectancy_value(
    country_data: pd.DataFrame, year: str
) -> float | None:
    """
    Extract life expectancy value for a specific year.

    Args:
        country_data (pd.DataFrame): The country's data row
        year (str): The year to extract value for

    Returns:
        float | None: Life expectancy value, or None if invalid

    Raises:
        None
    """
    if year not in country_data.columns:
        return None

    value = country_data[year].iloc[0]
    if pd.notna(value) and value > 0:
        return float(value)

    return None


def extract_gdp_value(
    country_data: pd.DataFrame, year: str
) -> float | None:
    """
    Extract GDP value for a specific year.

    Args:
        country_data (pd.DataFrame): The country's data row
        year (str): The year to extract value for

    Returns:
        float | None: GDP value, or None if invalid

    Raises:
        None
    """
    if year not in country_data.columns:
        return None

    value = country_data[year].iloc[0]
    parsed_gdp = parse_gdp_value(value)

    if parsed_gdp is not None and parsed_gdp > 0:
        return parsed_gdp

    return None


def get_common_countries(
    life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame
) -> set:
    """
    Get set of countries that exist in both datasets.

    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset

    Returns:
        set: Set of common country names

    Raises:
        None
    """
    return (
        set(life_expectancy_df['country'].values) &
        set(gdp_df['country'].values)
    )


def get_1900_data(
    life_expectancy_df: pd.DataFrame, gdp_df: pd.DataFrame
) -> tuple[list[str], list[float], list[float]]:
    """
    Extract life expectancy and GDP data for the year 1900.

    Args:
        life_expectancy_df (pd.DataFrame): Life expectancy dataset
        gdp_df (pd.DataFrame): GDP dataset

    Returns:
        tuple[list[str], list[float], list[float]]: Countries,
        life expectancy, GDP

    Raises:
        None
    """
    countries = []
    life_expectancy_1900 = []
    gdp_1900 = []

    common_countries = get_common_countries(
        life_expectancy_df, gdp_df
    )

    for country in common_countries:
        life_data = get_country_data(life_expectancy_df, country)
        life_value = extract_life_expectancy_value(life_data, '1900')

        if life_value is not None:
            gdp_data = get_country_data(gdp_df, country)
            gdp_value = extract_gdp_value(gdp_data, '1900')

            if gdp_value is not None:
                countries.append(country)
                life_expectancy_1900.append(life_value)
                gdp_1900.append(gdp_value)

    return countries, life_expectancy_1900, gdp_1900


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

    countries, life_expectancy_1900, gdp_1900 = get_1900_data(
        life_expectancy_df, gdp_df
    )

    display_graph(countries, life_expectancy_1900, gdp_1900)

    return 0


if __name__ == "__main__":
    sys.exit(main())
