Hi, here's your problem today. This problem was recently asked by AirBNB:

Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of the Pascal's Triangle of size 5.

```

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

```

Given an integer n, generate the n-th row of the Pascal's Triangle.

Here's an example and some starter code.

```

def pascal_triangle_row(n):
  # Fill this in.

print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]

```


# MY SOLUTION

```

def cal(arr):
    if len(arr) == 0:
        return [1]
    result = []
    for i in range(0,len(arr)):
        if i == 0:
            result.append(arr[i])
        else: 
            result.append(arr[i-1]+arr[i])
    result.append(arr[len(arr)-1])
    return result
# print(cal([1, 4, 6, 4, 1])) # [1, 5, 10, 10, 5, 1]
# print(cal([])) # [1]

def pascal_triangle_row(n):
    if isinstance(n, int) == False:
        return False
    arr = []
    for i in range(0,n):
        arr = cal(arr)
        print(arr)
    return arr

print(pascal_triangle_row(6)) # [1, 5, 10, 10, 5, 1]
# print(pascal_triangle_row(5.0)) # False
# print(pascal_triangle_row("6")) # False

```


```

# # not using this shit, cause it pass decimal although is .0 but still
# # not work since for loop not accept .0 data.
# def is_integer_num(n):
#     if isinstance(n, int):
#         return True
#     if isinstance(n, float):
#         return n.is_integer()
#     return False

# print(is_integer_num(100.0)) # True
# print(is_integer_num("100")) # False


# # test isdigit is Attribute for string
# x = "122"
# y = "-122"
# print(x.isdigit()) # True
# print(y.replace('-','').isdigit()) # True
# print(y.replace('.','')) # -122
# print(y.replace('.','').isdigit()) # False
# print(y.replace('/','').isdigit()) # False
# print(y.replace(':','').isdigit()) # False

```

