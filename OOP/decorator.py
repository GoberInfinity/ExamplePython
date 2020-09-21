# Use the wraps decorator from the functools built-in module when you define
# your own decorators to avoid any issues.
# @wraps preserves information about the original function

import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


@decorator
def some_function():
    return True
