Hi, here's your problem today. This problem was recently asked by Amazon:

Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.

Here's some examples and some starter code.

```

def reverse_integer(num):
  # Fill this in.
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123

```

# MY THOUGHT:

```

1. check NEG value or not.
2. identify data with number digit:
like:
123 = 100+20+3 -> 300+20+1 = 321
result = 135 - 5 / 10 = 13
result = 5*10^(3-1) = 500

```

# MY SOLUTION

```

def reverse_integer(num):
    # deal with neg value:
    negFlag = 0
    temp = num
    if (num < 0): # check neg value:
        negFlag = 1
        temp = temp*-1

    # Cal: result = 135 - 5 / 10 = 13
    digit = []    
    prev = 0
    while(1):
        modulus = temp % 10
        # print(modulus)
        temp = (temp - modulus) / 10
        # print(temp)
        digit.append(int(modulus)) # get rid of decimals 
        
        if(temp < 1):
            break
    
    # get arrange data from digit:
    # result = 5*10^(3-1)
    temp = 0
    lenght = len(digit)
    for i in range(0, len(digit)):
        temp = temp + (digit[i]*10**(lenght-1))
        lenght-=1

    if (negFlag): # bring back neg value
        temp = temp*-1
    return temp

print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123

print(reverse_integer(0)) # 0

```