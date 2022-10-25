import functools


def compare_cast_function(cf, ocf):
    return cf == ocf


def compare_with_int(op):
    def comparison(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cf = args[0].cast_function
            if len(args) >= 2:
                ocf = args[1].cast_function
                if not (compare_cast_function(cf, int) and compare_cast_function(ocf, int)):
                    raise Exception(
                        f'Unsupported operation {op} between {args[0].cast_function} and {args[1].cast_function}')
            else:
                if not compare_cast_function(cf, int):
                    raise Exception(
                        f'Unsupported unary operation {op} for {args[0].cast_function}')

            return func(*args, **kwargs)

        return wrapper

    return comparison
