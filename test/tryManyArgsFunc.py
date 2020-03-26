
def Many(*args, **kwargs):
    print('arguments are:')
    for i in args:
        print(i)

    print('\nkeywords are:')
    for j in kwargs:
        print(j)

a1 = "Bob"      #string
a2 = [1,2,3]    #list
a3 = {'a': 222, #dictionary
      'b': 333,
      'c': 444}

Many(a1, a2, a3, param1=True, param2=12, param3=None)

""" Output:
arguments are:
Bob
[1, 2, 3]
{'a': 222, 'b': 333, 'c': 444}

keywords are:
param1
param2
param3
"""

