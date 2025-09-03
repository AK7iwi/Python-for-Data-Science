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
        # Calculate progress percentage
        percentage = int((i + 1) / total * 100)

        # Calculate progress bar width (50 characters)
        bar_width = 50
        filled_width = int((i + 1) / total * bar_width)

        # Create progress bar
        bar = "=" * filled_width
        if filled_width < bar_width:
            bar += ">"
        bar = bar.ljust(bar_width, " ")

        # Create the progress display
        progress_line = f"\r{percentage}%|[{bar}]| {i + 1}/{total}"

        # Print progress (overwrite the same line)
        print(progress_line, end="")

        # Yield the current item
        yield item

    # Print newline at the end
    print()
