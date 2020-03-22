Hi, here's your problem today. This problem was recently asked by Twitter:

Given a matrix, transpose it. Transposing a matrix means the rows are now the column and vice-versa.

Here's an example:

```

def transpose(mat):
  # Fill this in.

mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5], 
#  [3, 6]]

```


# MY SOLUTION

```

# let say that all're same column.
def transpose(mat):
    row = len(mat)
    if row == 0:return False
    column = len(mat[0])
    if column == 0:return False
        
    temp = []
    Tmat = []
    for j in range(0,column):
        for i in range(0,row):
            temp.append(mat[i][j])
        Tmat.append(temp)
        temp =[]
    return Tmat

mat = [
    [1, 2, 3],
    [4, 5, 6]
]

# [[1, 4],
#  [2, 5], 
#  [3, 6]]
print(transpose(mat)) # [[1, 4], [2, 5], [3, 6]]

```

```

# RANDOM TESTING
mat2 = [[1, 4],
        [2, 5], 
        [3, 6]]
print(transpose(mat2)) # [[1, 2, 3], [4, 5, 6]]

mat21 = [[1],
        [2], 
        [3]]
print(transpose(mat21)) # [[1, 2, 3], [4, 5, 6]]

mat3 = []
print(transpose(mat3)) # False

mat4 = [[],
        [],
        []]
print(transpose(mat3)) # False

```