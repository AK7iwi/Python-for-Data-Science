"""
Module callLimit: Decorator for limiting function calls.
"""
import sys
from typing import Any, Callable
from validate_args import validate_args_for_test, MissingArgumentsError


def callLimit(limit: int) -> Callable:
    """
    Decorator factory that limits the number of times a function can be called.

    Args:
        limit (int): Maximum number of times the decorated function can
            be called.

    Returns:
        Callable: The decorator function.

    Raises:
        None
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
        Decorator that wraps a function to limit its calls.

        Args:
            function (Callable): The function to wrap.

        Returns:
            Callable: The wrapped function.

        Raises:
            None
        """
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            Wrapper function that enforces the call limit.

            Args:
                *args: Positional arguments for the wrapped function.
                **kwds: Keyword arguments for the wrapped function.

            Returns:
                Any: The result of the wrapped function if within limit.

            Raises:
                None
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


def main() -> int:
    """
    Main function to test the callLimit decorator.
    """
    try:
        validate_args_for_test()
    except MissingArgumentsError:
        return 1
    except ValueError as e:
        print(f"ValueError: {e}")
        return 1

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()

    return 0


if __name__ == "__main__":
    sys.exit(main())
