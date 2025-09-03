import time
from datetime import datetime


def format_time():
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
    current_time = time.time()

    # Format the seconds with comma separators and scientific notation
    formatted_seconds = f"{current_time:,.4f}"
    scientific_notation = f"{current_time:.2e}"

    # Get current date and format it
    current_date = datetime.now()
    formatted_date = current_date.strftime("%b %d %Y")

    return formatted_seconds, scientific_notation, formatted_date


def display_results(formatted_seconds, scientific_notation, formatted_date):
    """
    Display the formatted time results.

    Args:
        formatted_seconds (str): Formatted seconds since epoch
        scientific_notation (str): Scientific notation of seconds
        formatted_date (str): Formatted current date

    Returns:
        None: This function only prints to stdout

    Raises:
        None
    """
    print(f"Seconds since January 1, 1970: {formatted_seconds} "
          f"or {scientific_notation} in scientific notation")
    print(formatted_date)


def main():
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
        formatted_seconds, scientific_notation, formatted_date = format_time()
        display_results(formatted_seconds, scientific_notation, formatted_date)
        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    main()
