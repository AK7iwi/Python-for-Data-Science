"""
Module statistics: Data and StatisticsCalculator classes implementation.
"""
import sys
from typing import Any
from validate_args import validate_args_for_test, MissingArgumentsError


class Data:
    """
    Class representing validated and formatted statistical data.

    This class handles data validation, formatting, and storage.

    Attributes:
        values (list[float]): Sorted data values.
        size (int): Number of data points.
    """

    def __init__(self, raw_data: list[Any]) -> None:
        """
        Initialize the Data instance with validation and formatting.

        Args:
            raw_data (list[Any]): Raw input data to be validated and
                formatted.
        """
        self.values = raw_data

    # ==================== Properties ==================== #
    @property
    def values(self) -> list[float]:
        """
        Get the sorted data values.

        Returns:
            list[float]: Sorted data values.
        """
        return self._values

    @values.setter
    def values(self, raw_data: list[Any]) -> None:
        """
        Set and validate the data values.

        Args:
            raw_data (list[Any]): Raw input data to validate and format.

        Raises:
            None
        """
        self._validate_data(raw_data)
        self._values = sorted(float(x) for x in raw_data)

    @property
    def size(self) -> int:
        """
        Get the number of data points.

        Returns:
            int: Number of data points.
        """
        return len(self._values)

    # ==================== Methods ==================== #
    @staticmethod
    def _validate_data(raw_data: list[Any]) -> None:
        """
        Validate the raw data input.

        Args:
            raw_data (list[Any]): Raw input data to validate.

        Returns:
            None

        Raises:
            ValueError: If raw_data is empty.
            TypeError: If raw_data contains non-numeric values.
        """
        if len(raw_data) == 0:
            raise ValueError()

        for item in raw_data:
            if not isinstance(item, (int, float)):
                raise TypeError()


class StatisticsCalculator:
    """
    Class for calculating statistical measures on data.

    This class encapsulates statistical calculations using
    object-oriented programming principles.

    Attributes:
        data (Data): The Data instance containing validated data.
    """

    def __init__(self, data: Data) -> None:
        """
        Initialize the calculator with validated Data instance.

        Args:
            data (Data): The Data instance to calculate statistics on.
        """
        self.data = data

    # ==================== Methods ==================== #

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
        return sum(self.data.values) / self.data.size

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
        n = self.data.size
        values = self.data.values

        if n % 2 == 0:
            mid1 = values[n // 2 - 1]
            mid2 = values[n // 2]
            return (mid1 + mid2) / 2

        return values[n // 2]

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
        n = self.data.size
        values = self.data.values

        q1_index = int(n * 0.25)
        q3_index = int(n * 0.75)

        return [float(values[q1_index]), float(values[q3_index])]

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

        return sum((x - mean) ** 2 for x in self.data.values) / self.data.size

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

    def get_statistic(self, stat_name: str) -> float | list[float]:
        """
        Get a statistic by name.

        Args:
            stat_name (str): Name of the statistic to calculate.

        Returns:
            float | list[float]: The calculated statistic value.

        Raises:
            None
        """
        stat_methods = {
            "mean": self.calculate_mean,
            "median": self.calculate_median,
            "quartile": self.calculate_quartile,
            "var": self.calculate_variance,
            "std": self.calculate_std,
        }

        return stat_methods[stat_name]()


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics on the provided data.

    Uses OOP principles internally via Data and StatisticsCalculator classes.

    Args:
        *args: Variable number of numeric values to calculate statistics on.
        **kwargs: Keyword arguments where keys are labels and values are
            statistic names: "mean", "median", "quartile", "std", "var".

    Returns:
        None

    Raises:
        None
    """
    try:
        data = Data(list(args))
    except (ValueError, TypeError):
        for _ in kwargs.values():
            print("ERROR")
        return None

    calculator = StatisticsCalculator(data)
    for stat_name in kwargs.values():
        try:
            result = calculator.get_statistic(stat_name)
        except KeyError:
            continue

        print(f"{stat_name} : {result}")


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
