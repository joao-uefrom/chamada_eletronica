from time import time


def execution_time(show=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            init = time()
            r = func(*args, **kwargs)
            final = time()

            if show:
                print(f"[{func.__name__}] Tempo total de execução: {final - init}s")

            return r

        return wrapper

    return decorator
