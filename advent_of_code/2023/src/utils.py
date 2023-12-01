from typing import Callable, TypeVar
import time


RT = TypeVar("RT")


def timer(f: Callable[..., RT]) -> Callable[..., RT]:
    def _f(*args, **kwds) -> RT:
        start_time = time.perf_counter()
        
        result = f(*args, **kwds)
        
        elapsed = time.perf_counter() - start_time
        print(f"{f.__name__} took {elapsed} seconds")

        return result

    return _f
