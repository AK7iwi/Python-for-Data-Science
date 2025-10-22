import sys
from validate_args import validate_args_for_prog
import time
from datetime import datetime


def display_results(formatted_seconds: str, scientific_notation: str,
                    formatted_date: str) -> None:
    """
    Display the formatted time results.

    Args:
        formatted_seconds (str): Formatted seconds since epoch
        scientific_notation (str): Scientific notation of seconds
        formatted_date (str): Formatted current date

    Returns:
        None

    Raises:
        None
    """
    print(f"Seconds since January 1, 1970: {formatted_seconds} "
          f"or {scientific_notation} in scientific notation")
    print(formatted_date)


def format_time() -> tuple[str, str, str]:
    """
    Format current time in seconds since epoch and current date.

    Args:
        None

    Returns:
        tuple: A tuple containing (formatted_seconds, scientific_notation,
               formatted_date)
            - formatted_seconds (str): Seconds since epoch with comma
              separators
            - scientific_notation (str): Seconds in scientific notation
            - formatted_date (str): Current date in "Month Day Year" format

    Raises:
        None
    """
    # Get current time in seconds since epoch
    # and format it with comma separators and scientific notation
    current_time = time.time()
    formatted_seconds = f"{current_time:,.4f}"
    scientific_notation = f"{current_time:.2e}"

    # Get current date and format it in "Month Day Year" format
    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")

    return formatted_seconds, scientific_notation, formatted_date


def main() -> int:
    """
    Main function that formats and prints current time information.
    Takes no command line arguments.

    Args:
        None

    Returns:
        int: 0 on success, 1 on error

    Raises:
        None
    """
    try:
        validate_args_for_prog()

        formatted_seconds, scientific_notation, formatted_date = format_time()
        display_results(formatted_seconds, scientific_notation, formatted_date)

        return 0

    except ValueError as e:
        print(f"ValueError: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
