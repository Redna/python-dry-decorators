import logging

from decorator_logging.decorator import logged, benchmark, benchmark_unit

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

