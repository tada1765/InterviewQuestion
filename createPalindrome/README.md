Hi, here's your problem today. This problem was recently asked by Google:

Given a string, determine if you can remove any character to create a palindrome.

Here's some examples and some starter code:

```

def create_palindrome(s):
  # Fill this in.

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False

```


MY SOLUTION:
-------------

```

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

```
