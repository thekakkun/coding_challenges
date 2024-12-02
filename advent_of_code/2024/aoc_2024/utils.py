import time
from typing import Callable


def stopwatch[T](f: Callable[..., T]) -> Callable[..., T]:
    def _f(*args, **kwds) -> T:
        start_time = time.perf_counter()
        result = f(*args, **kwds)

        elapsed = time.perf_counter() - start_time
        for unit in ["", "m", "μ", "n"]:
            if 1 < elapsed:
                print(f"{f.__name__}: {elapsed:.2f} {unit}s")
                break
            else:
                elapsed *= 1000

        return result

    return _f
