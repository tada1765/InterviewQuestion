""" Hi, here's your problem today. 
This problem was recently asked by Apple:

Given a list of strings, find the list 
of characters that appear in all strings.

"""


# MY SOLUTION:
MAX_CHAR=94 # a to z, 0 to 9, symbol 
  
def _MyCommon( s1, s2): 

    # for looping purpose
    if(s1 == ""):
        return s2
    if(s2 == ""):
        return s1

    a1 = [0 for i in range(MAX_CHAR)] 
    a2 = [0 for i in range(MAX_CHAR)] 
    length1 = len(s1) 
    length2 = len(s2) 

    for i in range(0,length1): 
        a1[ord(s1[i]) - ord(' ')] += 1
        
    for i in range(0,length2): 
        a2[ord(s2[i]) - ord(' ')] += 1
    
    resultStr = ""
    for i in range(0,MAX_CHAR): 
        if (a1[i] != 0 and a2[i] != 0): 
            for j in range(0,min(a1[i],a2[i])): 
                ch = chr(ord(' ')+i) 
                resultStr+=ch
    return resultStr

# # MT TEST:
# s1 = "Testing123@email.com"
# s2 = "twq1xxx@gmail.com"
# print(_MyCommon(s1, s2))# .1@acgilmmot in string

def common_characters(strs):
    resultStr = ""
    result = []
    for i in strs:
        resultStr = _MyCommon(resultStr,i)

    for j in range(0, len(resultStr)):
        result.append(resultStr[j])

    return result

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']





# # MY attempt (fail):
# # MY THOUGHT:
# # 0. find lessest len data.
# # 1. take that data put in table.
# # 2. count the other data,store if same. 
# # 3. the most same val is the result.

# def _getSameLetters(strA,strB):
#     strSame = ""
#     if(strA == ""):
#         strSame = strB
#     if(strB == ""):
#         strSame = strA
    
#     for i in range(0,len(strA)):
#         temp = strA[i]
#         for j in range(0,len(strB)):
#             if (temp == strB[j]):
#                 strSame+=temp
#                 break # to prevent adff 
#     return strSame

# # Testing:
# # print(_getSameLetters("afgdh","afsdff")) #adff, hmm i want adf
# # print(_getSameLetters("afgdh","asdff")) # affd not problem too
# # print(_getSameLetters("aadff","afgdh")) # aadff
# # print(_getSameLetters("","asdff")) # asdff
# # print(_getSameLetters("asdff","")) # asdff
# # print(ord("a")) # 97
# # print(ord("A")) # 65
# # print(ord("?")) # 63
# # print(chr(65)) # A

# def _common_characters(strs):
#     result = ""
#     for i in strs:
#         result = _getSameLetters(result,i)
#     return result

# print(_common_characters(['google', 'facebook', 'youtube']))
# # ['e', 'o'] but i get # ooe





# # FROM OTHER:......
# # "googleA", "asdfk1232", "hdafjh#$$%" is not work.
# # only accept small letter, not number, not symbol.
# # refer: https://www.geeksforgeeks.org/print-common-characters-two-strings-alphabetical-order-2/
# # Python3 program to print common characters 
# # of two Strings in alphabetical order 
# MAX_CHAR=26
  
# # Function to find similar characters 
# def printCommon( s1, s2): 
#     # two arrays of length 26 to store occurrence 
#     # of a letters alphabetically for each string 
#     a1 = [0 for i in range(MAX_CHAR)] 
#     a2 = [0 for i in range(MAX_CHAR)] 
  
#     length1 = len(s1) 
#     length2 = len(s2) 
#     result = []
#     for i in range(0,length1): 
#         a1[ord(s1[i]) - ord('a')] += 1
#         # print(a1)
  
#     for i in range(0,length2): 
#         a2[ord(s2[i]) - ord('a')] += 1
  
#     # If a common index is non-zero, it means 
#     # that the letter corresponding to that 
#     # index is common to both strings 
#     print(a1)
#     print(a2)
    
#     for i in range(0,MAX_CHAR): 
#         if (a1[i] != 0 and a2[i] != 0): 
#             # Find the minimum of the occurrence 
#             # of the character in both strings and print 
#             # the letter that many number of times 
#             for j in range(0,min(a1[i],a2[i])): 
#                 ch = chr(ord('a')+i) 
#                 # print (ch, end='') 
#                 result.append(ch)
#     return result 
              
# # Driver code 
# if __name__=="__main__": 
#     s1 = "geeksforgeeks"
#     s2 = "practiceforgeeks"
#     # printCommon(s1, s2); 
#     # print("")
#     print(printCommon("ssa", "saaa")) # ['a', 's']


  