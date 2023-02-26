import logging

from decorator_logging.decorator import logged

@logged()
def something(i):
    if i == 3: 
        raise RuntimeError("It is really something what I wanted to be thrown!")

    return i*i


@logged(level=logging.INFO)
def another(prefix, call_count=0):
    addition = 0
    for i in range(call_count):
        try:
            addition += something(i)
        except:
            pass
 
    return addition

