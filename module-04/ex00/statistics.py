"""
Module statistics: Statistical calculations using OOP principles.
"""
import sys
from typing import Any
from validate_args import validate_args_for_test, MissingArgumentsError


class StatisticsCalculator:
    """
    Class for calculating statistical measures on data.

    This class encapsulates statistical calculations using
    object-oriented programming principles.
    """

    def __init__(self, data: list[float]) -> None:
        """
        Initialize the calculator with data.

        Args:
            data (list[float]): The data to calculate statistics on.

        Returns:
            None

        Raises:
            None
        """
        self.data = sorted(data)
        self.n = len(self.data)

    def calculate_mean(self) -> float:
        """
        Calculate the mean (average) of the data.

        Args:
            None

        Returns:
            float: The mean value.

        Raises:
            None
        """
        return sum(self.data) / self.n

    def calculate_median(self) -> float:
        """
        Calculate the median of the data.

        Args:
            None

        Returns:
            float: The median value.

        Raises:
            None
        """
        if self.n % 2 == 0:
            mid1 = self.data[self.n // 2 - 1]
            mid2 = self.data[self.n // 2]
            return (mid1 + mid2) / 2

        return self.data[self.n // 2]

    def calculate_quartile(self) -> list[float]:
        """
        Calculate the first and third quartiles (25% and 75%).

        Args:
            None

        Returns:
            list[float]: [Q1, Q3] quartile values.

        Raises:
            None
        """
        q1_index = int(self.n * 0.25)
        q3_index = int(self.n * 0.75)
        q1_index = min(q1_index, self.n - 1)
        q3_index = min(q3_index, self.n - 1)

        return [float(self.data[q1_index]), float(self.data[q3_index])]

    def calculate_variance(self) -> float:
        """
        Calculate the variance of the data.

        Args:
            None

        Returns:
            float: The variance value.

        Raises:
            None
        """
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.data) / self.n

    def calculate_std(self) -> float:
        """
        Calculate the standard deviation of the data.

        Args:
            None

        Returns:
            float: The standard deviation value.

        Raises:
            None
        """
        return self.calculate_variance() ** 0.5

    def get_statistic(self, stat_name: str) -> Any:
        """
        Get a statistic by name.

        Args:
            stat_name (str): Name of the statistic to calculate.

        Returns:
            Any: The calculated statistic value.

        Raises:
            ValueError: If stat_name is not a valid statistic.
        """
        stat_methods = {
            "mean": self.calculate_mean,
            "median": self.calculate_median,
            "quartile": self.calculate_quartile,
            "var": self.calculate_variance,
            "std": self.calculate_std,
        }

        if stat_name not in stat_methods:
            raise ValueError(f"Unknown statistic: {stat_name}")

        return stat_methods[stat_name]()


def validate_args(args: list[Any], kwargs: dict[str, Any]) -> None:
    """
    Validate the arguments and keyword arguments.
    """
    if len(args) == 0:
        for _ in kwargs.values():
            print("ERROR")
        return



def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics on the provided data.

    Uses OOP principles internally via StatisticsCalculator class.

    Args:
        *args: Variable number of numeric values to calculate statistics on.
        **kwargs: Keyword arguments where keys are labels and values are
            statistic names: "mean", "median", "quartile", "std", "var".

    Returns:
        None

    Raises:
        None
    """
    #validate fct, data class
    if len(args) == 0:
        for _ in kwargs.values():
            print("ERROR")
        return

    try:
        data = [float(x) for x in args]
    except (ValueError, TypeError):
        for _ in kwargs.values():
            print("ERROR")
        return

    if len(data) == 0:
        for _ in kwargs.values():
            print("ERROR")
        return

    calculator = StatisticsCalculator(data)

    valid_stats = {"mean", "median", "quartile", "std", "var"}

    for stat_name in kwargs.values():
        if stat_name not in valid_stats:
            continue

        try:
            result = calculator.get_statistic(stat_name)
            print(f"{stat_name} : {result}")
        except Exception:
            print("ERROR")


def main() -> int:
    """
    Main function to test the ft_statistics function.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                  world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

    return 0


if __name__ == "__main__":
    sys.exit(main())
