import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from validate_args import validate_args_for_prog


def display_graph(
    country1: str, pop1: list[float], country2: str,
    pop2: list[float], years: list[int]
) -> None:
    """
    Display the graph of population comparison between two countries.

    Args:
        country1 (str): First country
        pop1 (list[float]): List of population values for first country
        country2 (str): Second country
        pop2 (list[float]): List of population values for second country
        years (list[int]): List of years

    Returns:
        None

    Raises:
        None
    """
    plt.figure(figsize=(14, 8))
    plt.plot(
        years, pop1, 'b-', linewidth=2, label=f'{country1}',
        marker='o', markersize=3
    )
    plt.plot(
        years, pop2, 'r-', linewidth=2, label=f'{country2}',
        marker='s', markersize=3
    )
    plt.title(f'Population Comparison: {country1} vs {country2} (1800-2050)',
              fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Population', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xlim(1800, 2050)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(
            lambda x, p: f'{x/1e6:.0f}M' if x < 1e9 else f'{x/1e9:.1f}B'
        )
    )
    plt.tight_layout()
    plt.show()


def parse_population_value(value: str) -> float:
    """
    Parse population value from string format (e.g., "29M", "3.25M", "40.2k").

    Args:
        value (str): Population value as string

    Returns:
        float: Population value as number

    Raises:
        None
    """
    value_str = str(value).strip()
    value_float = 0.0

    if value_str.endswith('B'):
        value_float = float(value_str[:-1]) * 1_000_000_000
    elif value_str.endswith('M'):
        value_float = float(value_str[:-1]) * 1_000_000
    elif value_str.endswith('k'):
        value_float = float(value_str[:-1]) * 1_000
    else:
        value_float = float(value_str)

    return value_float


def extract_population_values(
    country_data: pd.DataFrame, years: list[int]
) -> list[float]:
    """
    Extract population values for given years.

    Args:
        country_data (pd.DataFrame): The country's data row
        years (list[int]): List of years to extract values for

    Returns:
        list[float]: List of population values

    Raises:
        None
    """
    populations = []
    for year in years:
        if 1800 <= year <= 2050:
            value = country_data[str(year)].iloc[0]
            parsed_value = parse_population_value(value)
            populations.append(parsed_value)

    return populations


def get_country_data(
    dataset: pd.DataFrame, country: str
) -> tuple[pd.DataFrame, list[int]]:
    """
    Extract population data for a specific country.

    Args:
        dataset (pd.DataFrame): The population dataset
        country (str): The country to extract data for

    Returns:
        tuple[pd.DataFrame, list[int]]: Country data and years

    Raises:
        None
    """
    country_data = dataset[dataset['country'] == country]
    years = [
        int(year) for year in country_data.columns
        if year != 'country' and 1800 <= int(year) <= 2050
    ]

    return country_data, years


def get_data(
    dataset: pd.DataFrame, country1: str, country2: str
) -> tuple[list[int], pd.DataFrame, pd.DataFrame]:
    """
    Get population data for two countries.

    Args:
        dataset (pd.DataFrame): The population dataset
        country1 (str): First country
        country2 (str): Second country

    Returns:
        tuple[list[int], pd.DataFrame, pd.DataFrame]: Years,
        country1 data, country2 data

    Raises:
        None
    """
    country1_data, years = get_country_data(dataset, country1)
    country2_data, _ = get_country_data(dataset, country2)

    return years, country1_data, country2_data


def compare_populations(
    dataset: pd.DataFrame, country1: str, country2: str
) -> tuple[list[int], list[float], list[float]]:
    """
    Compare population between two countries from 1800 to 2050.

    Args:
        dataset (pd.DataFrame): The population dataset
        country1 (str): First country (campus country)
        country2 (str): Second country (comparison country)

    Returns:
        tuple[list[int], list[float], list[float]]: Years,
        country1 population, country2 population

    Raises:
        None
    """
    years, country1_data, country2_data = get_data(dataset, country1, country2)
    pop1 = extract_population_values(country1_data, years)
    pop2 = extract_population_values(country2_data, years)

    return years, pop1, pop2


def main() -> int:
    """
    Main function to load and display population comparison data.

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

    dataset = load("../csv_files/valid_csv/population_total.csv")
    if dataset is None:
        return 1

    years, pop1, pop2 = compare_populations(dataset, "France", "Belgium")

    display_graph("France", pop1, "Belgium", pop2, years)

    return 0


if __name__ == "__main__":
    sys.exit(main())
