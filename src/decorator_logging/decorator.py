
from enum import Enum, auto
from functools import wraps
import logging
import time
from typing import Callable
from uuid import uuid4

log = logging.getLogger(__name__)


class benchmark_unit(Enum):
    NANOSECONDS = auto()
    MILLISECONDS = auto()
    SECONDS = auto()


def benchmark(_function=None, level: int = logging.DEBUG, unit=benchmark_unit.MILLISECONDS):
    if unit == benchmark_unit.MILLISECONDS:
        factor = 1e-6
        unit_text = "ms"
    elif unit == benchmark_unit.SECONDS:
        factor = 1e-9
        unit_text = "s"
    else:
        factor = 1
        unit_text = "ns"

    def decorator(function):
        function_name = f"{function.__module__}.{function.__qualname__}"

        @wraps(function)
        def wrapper(*args, **kwargs):
            start = time.perf_counter_ns()
            try:
                retval = function(*args, **kwargs)
            finally:
                benchmark_text = f"[{'benchmark':<10}] {function_name}: {(time.perf_counter_ns() - start)*factor:0.4f}{unit_text}"
                log.log(level, benchmark_text)

            return retval

        return wrapper
    return decorator(_function) if callable(_function) else decorator


def logged(_function=None, level: int = logging.DEBUG):
    def decorator(function):
        function_name = f"{function.__module__}.{function.__qualname__}"
        function_arg_names = function.__code__.co_varnames[:function.__code__.co_argcount]

        @wraps(function)
        def wrapper(*args, **kwargs):

            passed_args = [f"{name}={value}" for name,
                           value in zip(function_arg_names, args)]
            passed_kwargs = [f"{name}={value}" for name,
                             value in kwargs.items()]

            parameter_string = ", ".join(passed_args + passed_kwargs)

            log.log(
                level, f"[{'entering':<10}] {function_name}({parameter_string})")

            try:
                retval = function(*args, **kwargs)
                log.log(
                    level, f"[{'leaving':<10}] {function_name} -> {retval}")
            except Exception as e:
                log.log(
                    level, f"[{'leaving':<10}] {function_name} thrown [{repr(e)}]")
                raise

            return retval

        return wrapper
    return decorator(_function) if callable(_function) else decorator
