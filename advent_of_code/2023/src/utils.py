import time
from typing import Callable, TypeVar

RT = TypeVar("RT")


def stopwatch(f: Callable[..., RT]) -> Callable[..., RT]:
    def _f(*args, **kwds) -> RT:
        start_time = time.perf_counter()

        result = f(*args, **kwds)

        elapsed = time.perf_counter() - start_time

        for symbol in ["", "m", "μ", "n"]:
            if 1 < elapsed:
                print(f"{f.__name__}: {elapsed:.2f} {symbol}s")
                break
            else:
                elapsed *= 1000

        return result

    return _f
