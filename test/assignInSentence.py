import timeit

def func(mydata,find):
    if mydata == 1:
        # print(1)
        return True
    return False


def func_time():

    SETUP_CODE = '''
from __main__ import func
Count = 0
    '''

    TEST_CODE = '''
mydata = 1
find = 9
func(mydata, find)'''

    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 10) 

    # time not consistance?
    # refer: https://stackoverflow.com/questions/24762030/inconsistent-execution-time-in-python-on-all-systems
    print('func time: {}'.format(min(times)))         
  
if __name__ == "__main__":
    func_time()
