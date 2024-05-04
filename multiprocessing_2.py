import time
from multiprocessing import process
import multiprocessing

def print_func(continent = 'Asia'):
    print('The name of continent is :',continent)


if __name__=="__main__":
 names = ['America','Europe','Africa']
 procs = []
 proc = multiprocessing.Process(target=print_func)
 procs.append(proc)
 proc.start()

 for name in names:
     proc = multiprocessing.Process(target=print_func , args=[name])
     proc.start()
     procs.append(proc)


     # Complete the procrss
     for proc in procs:
         proc.join()