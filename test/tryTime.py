# refer: https://kite.com/python/answers/how-to-measure-the-execution-time-of-code-in-python
# calculate function operational time consume.

# 1. use timeit
import timeit

def func():
    pass

def func2():
    a = [0 for i in range(100)]
    for i in a:
        a[i]+=1
    return a

execution_time = timeit.timeit(func, number=100)
execution_time2 = timeit.timeit(func2, number=100)

# Time to run func once:
print('{} Took {} Seconds'.format("func",execution_time))
# func Took 3.66000000000255e-05 Seconds

print('{} Took {} Seconds'.format("func2",execution_time2))
# func2 Took 0.004912899999999998 Seconds


# 2. use process_time 
# refer: https://www.geeksforgeeks.org/time-process_time-function-in-python/
from time import process_time 
   
n = 1000  
t1_start = process_time()  # Start the stopwatch / counter
   
for i in range(n): 
    print(i, end =' ') 
  
print()  
  
t1_stop = process_time() # Stop the stopwatch / counter 
   
print("Elapsed time:", t1_stop, t1_start)  
# Elapsed time: 0.15625 0.109375
print("Elapsed time during the whole program in seconds:", 
                                         t1_stop-t1_start)  
# Elapsed time during the whole program in seconds: 0.046875


# OTHER:

# importing the required modules 
import timeit 
  
# binary search function 
def binary_search(mylist, find): 
    while len(mylist) > 0: 
        mid = (len(mylist))//2
        if mylist[mid] == find: 
            return True
        elif mylist[mid] < find: 
            mylist = mylist[:mid] 
        else: 
            mylist = mylist[mid + 1:] 
    return False
  
  
# linear search function 
def linear_search(mylist, find): 
    for x in mylist: 
        if x == find: 
            return True
    return False
  
  
# compute binary search time 
def binary_time(): 
    SETUP_CODE = ''' 
from __main__ import binary_search 
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
binary_search(mylist, find)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('Binary search time: {}'.format(min(times)))         
  
  
# compute linear search time 
def linear_time(): 
    SETUP_CODE = ''' 
from __main__ import linear_search 
from random import randint'''
      
    TEST_CODE = ''' 
mylist = [x for x in range(10000)] 
find = randint(0, len(mylist)) 
linear_search(mylist, find) 
    '''
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10000) 
  
    # priniting minimum exec. time 
    print('Linear search time: {}'.format(min(times)))   
  
if __name__ == "__main__": 
    linear_time() 
    binary_time() 