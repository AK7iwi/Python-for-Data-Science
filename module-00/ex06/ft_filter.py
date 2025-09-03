def ft_filter(function, iterable):
    """
    Custom filter function that behaves like the built-in filter.

    Args:
        function (callable or None): Function to apply to each element, or None
            to filter out falsy values
        iterable (iterable): The iterable to filter

    Returns:
        list: A list containing elements for which function returns True,
              or elements that are truthy if function is None

    Raises:
        None
    """
    if function is None:
        # When function is None, filter out falsy values
        return [item for item in iterable if item]
    else:
        # When function is provided, apply it to each item
        return [item for item in iterable if function(item)]
