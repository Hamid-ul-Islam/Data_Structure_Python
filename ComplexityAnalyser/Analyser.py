import time
from memory_profiler import profile

class ComplexityCalculator:
    @staticmethod
    def measure_time(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result, elapsed_time

    @staticmethod
    @profile(precision=4)
    def measure_space(func, *args, **kwargs):
        result = func(*args, **kwargs)
        return result
