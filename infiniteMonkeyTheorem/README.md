Sample Input:
    - 314159265358979323846263383279
    - ['314','49','9001','15926535897','14','9323','846263383279','4','793']

Sample Output:
    -3(314 15926535897 9323 846263383279)

Code:
--------------

```

PI = "314159265358979323846263383279"
IN = ['314','49','9001','15926535897','14','9323',
        '846263383279','4','793']
A = "95073093100301051542794729"
B = ['0','950730','07','4729','931003','010515','4279']

def findMatch(a,b):
    index = []
    pos_a = 0
    count_match = 0
    for i in range(0, len(b)):
        if pos_a >= len(a):
            break
        if checkStr(a,pos_a,b,i) == True:
            pos_a += len(b[i]) 
            count_match+=1
            index.append(b[i])
            # print("ya")
            # # print(pos_a)
        else:
            pos_a = pos_a
            # print("no")
            # print(pos_a)

    return f"{count_match-1}({' '.join(index)})"

def checkStr(strA,pos_a,listB,pos_b):
    for i in range(0, len(listB[pos_b])):
        if strA[pos_a+i] != listB[pos_b][i]:
            return False
        else:
            return True

# print(checkStr(PI,13,IN,4))
print(findMatch(PI,IN))
print(findMatch(A,B))

```

**result:**

```

3(314 15926535897 9323 846263383279)
3(950730 931003 010515 4279) hmm seem bug occur



```
