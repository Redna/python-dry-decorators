from functools import wraps
import logging
import time
from typing import Callable

log = logging.getLogger(__name__)


def logged(_func=None, level: int = logging.DEBUG):
    def decorator(func):

        func_qual_name = func.__qualname__
        func_arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter_ns()

            passed_args = [f"{name}={value}" for name,
                           value in zip(func_arg_names, args)]
            passed_kwargs = [f"{name}={value}" for name,
                             value in kwargs.items()]

            parameter_string = ", ".join(passed_args + passed_kwargs)

            log.log(
                level, f"[{'entering'.center(8)}] {func_qual_name}({parameter_string})")

            try:
                retval = func(*args, **kwargs)
                log.log(
                    level, f"[{'leaving'.center(8)}] {func_qual_name} -> {retval} | {(time.perf_counter_ns() - start)*1e-6:0.2f}ms")
            except Exception as e:
                log.log(
                    level, f"[{'leaving'.center(8)}] {func_qual_name} thrown [{repr(e)}] | {(time.perf_counter_ns() - start)*1e-6:0.2f}ms")
                raise

            return retval

        return wrapper
    return decorator(_func) if callable(_func) else decorator
