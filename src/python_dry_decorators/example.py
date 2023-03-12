import logging

from python_dry_decorators.decorator import logged, retryable, benchmark, benchmark_unit

@benchmark
@logged
def something(i):
    if i == 3: 
        raise RuntimeError("It is really something what I wanted to be thrown!")

    return i*i


@benchmark(unit=benchmark_unit.SECONDS)
@logged(level=logging.INFO)
def another(print_prefix, call_count=0):
    addition = 0
    for i in range(call_count):
        try:
            addition += something(i)
        except:
            pass
 
    return addition




def always_failing():
    i = 0

    @logged
    @retryable(exceptions=[RuntimeError, ConnectionError], no_of_retries=3)
    def critical_function():
        nonlocal i
        i = i + 1
        if i < 2:
            raise ConnectionAbortedError("Here was something defenitely aborted")
        if i < 3:
            raise ConnectionRefusedError("Well, not allowed")
        if i < 4:
            raise ConnectionResetError("Umm, not really working")
        if i < 5:
            raise RuntimeError("This is something severe")
        
        return "This is what I want!"

    return critical_function()

def runtime_error_failing():
    i = 0

    @logged
    @retryable(exceptions=[ConnectionError], no_of_retries=4)
    def critical_function():
        nonlocal i
        i = i + 1
        if i < 2:
            raise ConnectionAbortedError("Here was something defenitely aborted")
        if i < 3:
            raise ConnectionRefusedError("Well, not allowed")
        if i < 4:
            raise ConnectionResetError("Umm, not really working")
        if i < 5:
            raise RuntimeError("This is something severe")
        
        return "This is what I want!"

    return critical_function()


def finally_passing():
    i = 0

    @logged
    @retryable(exceptions=[Exception], no_of_retries=5)
    def critical_function():
        nonlocal i
        i = i + 1
        if i < 2:
            raise ConnectionAbortedError("Here was something defenitely aborted")
        if i < 3:
            raise ConnectionRefusedError("Well, not allowed")
        if i < 4:
            raise ConnectionResetError("Umm, not really working")
        if i < 5:
            raise RuntimeError("This is something severe")
        
        return "This is what I want!"

    return critical_function()