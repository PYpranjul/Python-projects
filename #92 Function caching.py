import functools
import time
@functools.lru_cache(maxsize=None)
def fx(x):
    x=(x**2)+(x+1)
    time.sleep(2)
    return x
t=fx(10)
print(t)
print(fx(30))
print(fx(7))
print(fx(5))


print(fx(30))
print(fx(7))
print(fx(5))
