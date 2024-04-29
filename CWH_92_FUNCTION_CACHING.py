from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n * n


print(fx(2))
print("Done for 2")
print(fx(5))
print("Done for 5")
print(fx(10))
print("Done for 10")

print("\r")
print(fx(2))
print("Done for 2")
print(fx(5))
print("Done for 5")
print(fx(10))
print("Done for 10")
print(fx(30))
print("Done for 30")
