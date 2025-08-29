import time
from datetime import datetime


def format_time():
    """
    Format and display current time in seconds since epoch and current date.
    Returns formatted strings for seconds and date.
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


def main():
    """
    Main function that formats and prints current time information.
    """
    try:
        formatted_seconds, scientific_notation, formatted_date = format_time()

        # Print the results
        print(f"Seconds since January 1, 1970: {formatted_seconds} "
              f"or {scientific_notation} in scientific notation")
        print(formatted_date)

        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    main()
