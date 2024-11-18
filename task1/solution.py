def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for i, (arg_name, arg_type) in enumerate(annotations.items()):
            if arg_name == "return":
                continue

            if i < len(args):
                if not isinstance(args[i], arg_type):
                    raise TypeError(
                        f"Argument '{arg_name}' must be {arg_type.__name__}, got {type(args[i]).__name__}"
                    )
            elif arg_name in kwargs:
                if not isinstance(kwargs[arg_name], arg_type):
                    raise TypeError(
                        f"Argument '{arg_name}' must be {arg_type.__name__}, got {type(kwargs[arg_name]).__name__}"
                    )
            else:
                raise TypeError(f"Missing required argument: '{arg_name}'")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# Тесты
print(sum_two(1, 2))  # >>> 3

try:
    print(sum_two(1, 2.4))  # >>> TypeError
except TypeError as e:
    print(e)

try:
    print(sum_two("1", 2))  # >>> TypeError
except TypeError as e:
    print(e)

