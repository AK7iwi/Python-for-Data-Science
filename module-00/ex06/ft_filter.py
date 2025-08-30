def ft_filter(function, iterable):
    """
    Custom filter function that behaves like the built-in filter.
    Returns an iterator of elements for which function returns True.
    """
    if function is None:
        # When function is None, filter out falsy values
        return [item for item in iterable if item]
    else:
        # When function is provided, apply it to each item
        return [item for item in iterable if function(item)]
