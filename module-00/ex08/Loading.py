import sys
from time import sleep
from validate_args import validate_args_for_test


def ft_tqdm(lst: range) -> None:
    """
    Custom progress bar function that mimics tqdm behavior.
    Uses yield operator to iterate through the range and display progress.

    Args:
        lst (range): The range to iterate through and display progress for

    Returns:
        generator: A generator that yields each item from the range

    Raises:
        None
    """
    total = len(lst)

    for i, item in enumerate(lst):
        percentage = int((i + 1) / total * 100)

        bar_width = 50
        filled_width = int((i + 1) / total * bar_width)

        bar = "=" * filled_width
        if filled_width < bar_width:
            bar += ">"
        bar = bar.ljust(bar_width, " ")

        progress_line = f"\r{percentage}%|[{bar}]| {i + 1}/{total}"

        print(progress_line, end="")

        yield item

    print()


def main() -> int:
    """
    Main function to test the ft_tqdm function.
    """
    try:
        if not validate_args_for_test():
            return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    for _ in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
