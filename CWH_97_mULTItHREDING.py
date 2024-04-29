import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds,minuts):
    print(f"Sleeping for {seconds} seconds and {minuts} minuts")
    time.sleep(seconds)
    return seconds
time1 = time.perf_counter()
# Normal code
# func(4)
# func(2)
# func(1)

def main():
  t1 = threading.Thread(target=func,args=[4,2])
  t2 = threading.Thread(target=func,args=[2,5])
  t3 = threading.Thread(target=func,args=[1,7])

  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()

  time2 = time.perf_counter()
  print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3,4)
        future2 = executor.submit(func,2,2)
        future3 = executor.submit(func,4,2)
        print(future1.result())
        print(future2.result())
        print(future3.result())
poolingDemo()

def function():
    with ThreadPoolExecutor() as executor:
     lst = [3,2,4,1]
     lst2 = [5,6,6,1]
     results = executor.map(func,lst,lst2)
     for result in results:
         print(result)

function()
