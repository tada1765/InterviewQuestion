""" Hi, here's your problem today. 
This problem was recently asked by Facebook:

Reshaping a matrix means to take the same elements 
in a matrix but change the row and column length. 
This means that the new matrix needs to have the 
same elements filled in the same row order as the 
old matrix. Given a matrix, a new row size x and 
a new column size y, reshape the matrix. 
If it is not possible to reshape, return None.
"""

# x = row
# y = column
def reshape_matrix(mat, x, y):
    row = len(mat)
    elem = []
    count = 0
    
    for i in range(0,row):
        column = (len(mat[i]))
        for j in range(0,column):
            elem.append(mat[i][j])# get all data in mat
            count+=1 # count total elem in mat

    if (x*y != count): # check mat reshapable or not
        return None

    newMat = []
    n = 0 
    for k in range(0,y):
        InMat = []
        for l in range(0,x):
            InMat.append(elem[n])
            n+=1
        newMat.append(InMat)

    return newMat

"""
  (2x2)         (2x3)             (1x4)
[[1, 2],   [[0, 0, 0],  [[0, 0, 0, 0,]]
 [3, 4]]    [0, 0, 0]]

"""
mat = [[1, 2],
       [3, 4]] 

mat2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10,11,12]] 
#                                     row column
print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None

print(reshape_matrix([[1, 2], [3, 4]], 4, 1))
# [[1, 2, 3, 4]]

print(reshape_matrix(mat2, 4,3))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]





# function _reshapable and _getValueFromMatrix
# is doing same thing twict not efficiency. 
def _reshapable(mat,x,y):
    row = len(mat)
    column = []
    total = 0
    for i in range(0,row):
        column.append(len(mat[i]))
        total = total + len(mat[i])
    if ((x*y) == total):
        return True
    return False 

def _getValueFromMatrix(mat):
    row = len(mat)
    elem = []
    for i in range(0,row):
        column = (len(mat[i]))
        for j in range(0,column):
            elem.append(mat[i][j])
    return elem

# # testing:
# print(_reshapable(mat2,6,2)) # True
# print(_reshapable(mat,1,4)) # True
# print(_reshapable(mat,2,3)) # False
# print(_getValueFromMatrix(mat)) # [1, 2, 3, 4]

