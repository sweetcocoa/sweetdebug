import time
import typing
import inspect
import sys


class sweettimer:
    times = []

    def __init__(
        self, name: typing.Optional[str] = None, unit: typing.Optional[str] = None
    ) -> None:
        self.unit = "s" if unit is None else unit
        self.unit_multiplier = 1

        if self.unit == "s":
            pass
        elif self.unit == "ms":
            self.unit_multiplier *= 1_000
        elif self.unit == "us":
            self.unit_multiplier *= 1_000_000
        elif self.unit == "ns":
            self.unit_multiplier *= 1_000_000_000
        elif self.unit == "min":
            self.unit_multiplier /= 60
        elif self.unit == "hour":
            self.unit_multiplier /= 3600
        else:
            raise ValueError(f"Unknown unit :: {self.unit}")

        self.name = name

    def __call__(self, func):
        try:
            file = inspect.getfile(func)
        except TypeError:
            file = sys.executable

        name = func.__name__ if self.name is None else self.name

        def wrapped_func(*args, **kwargs):
            st = time.time()
            ret_val = func(*args, **kwargs)
            elapsed = time.time() - st
            print(
                "\033[94m"
                f"({file})"
                "\033[0m"
                f"[{name}] :: elapsed {elapsed*self.unit_multiplier} {self.unit}"
            )
            sweettimer.times.append((name, elapsed, self.unit))
            return ret_val

        return wrapped_func

    def __enter__(self):
        self.st = time.time()
        frame = inspect.stack()[1].frame
        self.frame_desc = f"{frame.f_code.co_filename}, line {frame.f_lineno}"

    def __exit__(
        self, exc_type: typing.Any, exc_value: typing.Any, traceback: typing.Any
    ):
        elapsed = time.time() - self.st

        print(
            "\033[94m"
            f"({self.frame_desc})"
            "\033[0m"
            f"{f'[{self.name}]' if self.name is not None else ''} :: elapsed {elapsed*self.unit_multiplier} {self.unit}"
        )
        sweettimer.times.append((self.name, elapsed, self.unit))
