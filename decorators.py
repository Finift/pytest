from timeit import default_timer as timer
import math
import time



def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Function {func.__name__} took {end - start} for execution')
    return inner