import functools


def squeak_decorator(func):
    @functools.wraps(func)
    def wrapper(*argc, **kwargs):
        print("SQUEAK")
        return func(*argc, **kwargs)

    return wrapper
