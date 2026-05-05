import time 

def measure_elapsed_time(func, *args):
    if not callable(func):
        raise TypeError("The provided func must be callable")
    
    #precise time set
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()

    return end - start