
def test(s1):
    a = [0 for i in range(26)]
    length = len(s1)
    for i in range(0, length):
        a[ord(s1[i]) - ord('a')] += 1
        # print(a)

# # TEST:
# print(ord('a')) # 97
# print(ord('A')) # 65 
# print(ord(' ')) # 32
# print(ord('~')) # 126
# a = [0 for i in range(26)]
# print(a)
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     #  0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     #  0, 0, 0, 0, 0, 0]
# print([1 for i in range(5)]) # [1, 1, 1, 1, 1]


# MY TRY:
# refer: http://www.asciitable.com/
MAX_CHAR=94 # a to z, 0 to 9, symbol 
  
def MyCommon( s1, s2): 
    a1 = [0 for i in range(MAX_CHAR)] 
    a2 = [0 for i in range(MAX_CHAR)] 
  
    length1 = len(s1) 
    length2 = len(s2) 

    for i in range(0,length1): 
        a1[ord(s1[i]) - ord(' ')] += 1
        
    for i in range(0,length2): 
        a2[ord(s2[i]) - ord(' ')] += 1
    
    test = []
    for i in range(0,MAX_CHAR): 
        if (a1[i] != 0 and a2[i] != 0): 
            for j in range(0,min(a1[i],a2[i])): 
                ch = chr(ord(' ')+i) 
                test.append(ch)
    return test

# MT TEST:
s1 = "Testing123@email.com"
s2 = "twq1xxx@gmail.com"
print(MyCommon(s1, s2))
# ['.', '1', '@', 'a', 'c', 'g', 'i', 'l', 'm', 'm', 'o', 't']

# from other:
# refer: https://www.geeksforgeeks.org/print-common-characters-two-strings-alphabetical-order-2/

MAX_CHAR= 26 # a to z
   
def printCommon( s1, s2): 
    a1 = [0 for i in range(MAX_CHAR)] 
    a2 = [0 for i in range(MAX_CHAR)] 
  
    length1 = len(s1) 
    length2 = len(s2) 
    result = []
    for i in range(0,length1): 
        a1[ord(s1[i]) - ord('a')] += 1
        
    for i in range(0,length2): 
        a2[ord(s2[i]) - ord('a')] += 1

    print(a1)
    print(a2)
    
    for i in range(0,MAX_CHAR): 
        if (a1[i] != 0 and a2[i] != 0): 
            for j in range(0,min(a1[i],a2[i])): 
                ch = chr(ord('a')+i) 
                result.append(ch)
    return result 
              
# Driver code 
if __name__=="__main__": 
    s1 = "geeksforgeeks"
    s2 = "practiceforgeeks"
    print(printCommon(s1, s2)) 
    # ['e', 'e', 'e', 'f', 'g', 'k', 'o', 'r', 's']

    # print(printCommon("123ad","2sdgf")) # error
