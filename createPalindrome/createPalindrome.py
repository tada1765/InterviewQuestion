'''
Hi, here's your problem today. This problem was 
recently asked by Google:
    Given a string, determine if you can remove any 
    character to create a palindrome.
'''

'''
my thought:
check the string both side from(start and end),
string length check,
 
remove a character for example:
1. abcdcbea = abccbea(d removed)
2. abccaa = bcc(a removed)
'''

def reverse(s): 
    return s[::-1] 
'''
@brief  check palindrome string.
@param  s: a string. 
@retval True: the string is palindrome. 
        string: string return after deleted a character 
'''
def noMoreCharDelete(s):
  rev = reverse(s)
  i = 0
  while (i <= len(s)-1):
    if rev[i] == s[i]:
      i+=1
    elif rev[i] != s[i]:
      return s.replace(rev[i],'')
  return True

def create_palindrome(s):
  rev = reverse(s)
  if (s == rev): 
        return False

  result = noMoreCharDelete(s)
  while result != True:
    result = noMoreCharDelete(result)
    if result == True:
      return True
    if len(result) == 1: # check End of string
      break
  return False

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False

# a = 'abedebea'
# b = 'abedbea'
# c = 'abcdcba'
# print(True if len(a)%2 == 0 else False)
# le = len(a)
# print(le)
# for i in range(0,le//2):
#     print(a[i:le-i])

# def demo(s):
#   if len(a)%2 == 0:
#     for i in range(0,le//2):
#       print(a[i:le-i])
    
#   else:
#     return False


# print(demo(a))
# print(a.translate({ord('a'): None}))
# print(a)
# print(a.replace('a',''))
# s = a.replace('a','')
# print(s)
# print(a[len(a)-2]) # e
