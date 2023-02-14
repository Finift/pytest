def measure_time(func):
    from timeit import default_timer as timer
    import math
    import time


    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Function {func.__name__} took {end - start} for execution')
    return inner

# или:
def timer(func):
    import time


    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator