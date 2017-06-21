

from timeit import timeit

def func():
    return 1 + 1

time = timeit(func, number=1)
print(time)



