Hi, here's your problem today. This problem was recently asked by Uber:

Given a binary tree, find all duplicate subtrees (subtrees with the same value and same structure) and return them as a list of list [subtree1, subtree2, ...] where subtree1 is a duplicate of subtree2 etc.

Here's an example and some starter code:

```

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"

def dup_trees(root):
  # Fill this in.

n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3

print(dup_trees(n1))
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3

```
# My solution:

```


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"

def collect(node,temp,ans): # add some # dk why code to meet the requirement 
    prev = () # dk why
    m = [] # dk why
    if not node: return "#"
    serial = f"{node.value},{collect(node.left,temp,ans)},{collect(node.right,temp,ans)}"
    if serial in temp:
        temp[serial] += 1
        prev = node
    else:
        temp[serial] = 1       
    # print(serial)
    # print(temp)
    if temp[serial] == 2:
        m.append(node) # dk why
        m.append(prev) # dk why
        ans.append(m) # dk why
    return serial

def dup_trees(root): # Fill this in.
  ans = []
  temp = {}
  collect(root,temp,ans)
  return ans

n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3

print(dup_trees(n1)) # ans = [[(3), (3)], [(2, (3)), (2, (3))]]
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3

# print(n1) # (1, (2, (3)), (2, (3)))
# print(n1.left) # (2, (3))
# print(n1.right) # (2, (3))
# print(n1.right.right) # None



# l3 = Node(3)
# r3 = Node(3)
# l2 = Node(2, l3, r3)
# r2 = Node(2, l3, r3)
# n1_full3 = Node(1, l2, r2)

# l4 = Node(4)
# r4 = Node(4)
# l3 = Node(3,l4,r4)
# r3 = Node(3,l4,r4)
# l2 = Node(2, l3, r3)
# r2 = Node(2, l3, r3)
# n1_full4 = Node(1, l2, r2)
# print(n1_full4)

# l4 = Node(4)
# r4 = Node(4)
# l3 = Node(3,1,r4) # 1 is not a Node
# r3 = Node(3,0,r4) # no left Node
# l2 = Node(2, l3, r3)
# r2 = Node(2, l3, r3)
# n1_notfull4 = Node(1, l2, r2)

# print(n1_notfull4)
# print(n1_notfull4.__repr__())

'''
         1             1 
       /   \         /   \
      2     3       2     3
     / \   / \     /     / \
    4   5 2   4   4     2   4
         /             /
        4             4
'''
l4 = Node(4)
l3_3 = Node(2, l4, 0)
l3_2 = Node(5)
l2_1 = Node(2,l4,0) #Node(2,l4,l3_2)
l2_2 = Node(3,l3_3,l4)
root = Node(1,l2_1,l2_2)
# print(root)
print(dup_trees(root))


```

# Try to understand:

print tree:
------------

```

l3 = Node(3)
r3 = Node(3)
l2 = Node(2, l3, r3)
r2 = Node(2, l3, r3)
n1_full3 = Node(1, l2, r2)

print(n1_full3)

```

**result:**
(1, (2, (3), (3)), (2, (3), (3)))


```

l4 = Node(4)
r4 = Node(4)
l3 = Node(3,l4,r4)
r3 = Node(3,l4,r4)
l2 = Node(2, l3, r3)
r2 = Node(2, l3, r3)
n1_full4 = Node(1, l2, r2)

print(n1_full4)

```

**result:**
(1, (2, (3, (4), (4)), (3, (4), (4))), (2, (3, (4), (4)), (3, (4), (4))))

```

l4 = Node(4)
r4 = Node(4)
l3 = Node(3,1,r4) # 1 is not a Node
r3 = Node(3,0,r4) # no left Node
l2 = Node(2, l3, r3)
r2 = Node(2, l3, r3)
n1_notfull4 = Node(1, l2, r2)

print(n1_notfull4)

```

**result:**
(1, (2, (3, 1, (4)), (3, None, (4))), (2, (3, 1, (4)), (3, None, (4))))

# My test dupSubtreeTest.py :

```

import collections

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"

n3_1 = Node(3)
n2_1 = Node(2, n3_1)
n3_2 = Node(3)
n2_2 = Node(2, n3_2)
n1 = Node(1, n2_1, n2_2)
# Looks like
#     1
#    / \
#   2   2
#  /   /
# 3   3
# ans:
# [[(3), (3)], [(2, (3)), (2, (3))]]
# There are two duplicate trees
#
#     2
#    /
#   3
# and just the leaf
#
# 3

class Solution(object): # from online
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def collect(node):
          if not node: return "#"
          serial = "{},{},{}".format(node.value, collect(node.left), collect(node.right))
          count[serial] += 1
          if count[serial] == 2:
            ans.append(node)
          return serial
        collect(root)
        return ans

def findDuplicateSubtrees1(root): # no class pls
    count = collections.Counter()
    ans = []
    def collect(node):
        # print("howManyTimeCall")
        if not node: return "#"
        serial = f"{node.value},{collect(node.left)},{collect(node.right)}"
        count[serial] += 1
        # print(serial)
        # print(count)
        if count[serial] == 2:
            ans.append(node)
        return serial
    collect(root)
    return ans



def findDuplicateSubtrees2(root): # not using collections module
    ans = []
    temp = {}
    def collect(node):
        # print("howManyTime")
        if not node: return "#"
        serial = f"{node.value},{collect(node.left)},{collect(node.right)}"
        if serial in temp:
            temp[serial] += 1
        else:
            temp[serial] = 1
        # print(serial)
        # print(temp)
        if temp[serial] == 2:
            ans.append(node)
        return serial
    collect(root)
    return ans

# Why function inside a function? try split it out.
def collect(node,temp,ans):
    # print("howManyTime")
    if not node: return "#"
    serial = f"{node.value},{collect(node.left,temp,ans)},{collect(node.right,temp,ans)}"
    if serial in temp:
        temp[serial] += 1
    else:
        temp[serial] = 1
    # print(serial)
    # print(temp)
    if temp[serial] == 2:
        ans.append(node)
    return serial

def findDuplicateSubtrees3(root): # not using collections module too
    ans = []
    temp = {}
    collect(root,temp,ans)
    return ans

print("from online")
print(Solution.findDuplicateSubtrees(n1,n1)) # [(3), (2, (3))]
print("Why class? no class.")
print(findDuplicateSubtrees1(n1))  # [(3), (2, (3))]
print("not using collections module") 
print(findDuplicateSubtrees2(n1))  # [(3), (2, (3))]
print("Why function inside a function? try split it out")
print(findDuplicateSubtrees3(n1))  # [(3), (2, (3))]

'''
         1             1 
       /   \         /   \
      2     3       2     3
     / \   / \     /     / \
    4   5 2   4   4     2   4
         /             /
        4             4
'''
l4 = Node(4)
l3_3 = Node(2, l4, 0)
l3_2 = Node(5)
l2_1 = Node(2,l4,0) #Node(2,l4,l3_2)
l2_2 = Node(3,l3_3,l4)
root = Node(1,l2_1,l2_2)
print(root) # (1, (2, (4)), (3, (2, (4)), (4)))
print(findDuplicateSubtrees1(root)) # [(4), (2, (4))]

```

# My test dupSubtreeTest2.py :

```


# ans: [[(3), (3)], [(2, (3)), (2, (3))]]
class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = self.right = None


def Inorder(root): # using stack
  current = root  
  stack = [] 
  temp = {}
  Str = ""
  while True:
    if current is not None:
      stack.append(current)
      current = current.left
    elif(stack):
        current = stack.pop()
        Str = ""
        Str += str(current.data)
        if current.left is None:Str += "x"
        # else:Str += str(current.left.data)
        if current.right is None:Str += "y"
        # else:Str += str(current.right.data)
        if (Str in temp and temp[Str] >= 1):  
            print(current.data)
        if Str in temp: 
            temp[Str] += 1
        else: 
            temp[Str] = 1 
        current = current.right
    else:
        return temp

def inorder(node, m): # using recursion
    # print(node) 
    if (not node):  
        return ""  
    # print(node.data)
    Str = "("
    Str += inorder(node.left, m)  
    Str += str(node.data)  
    Str += inorder(node.right, m)  
    Str += ")" 
    # Subtree already present (Note that  
    # we use unordered_map instead of  
    # unordered_set because we want to print 
    # multiple duplicates only once, consider  
    # example of 4 in above subtree, it  
    # should be printed only once. 
    if (Str in m and m[Str] == 1):  
        print(node.data)#, end = " ")  
    if Str in m: 
        m[Str] += 1
    else: 
        m[Str] = 1
  
    return Str
  
# Wrapper over inorder()  
def printAllDups(root): 
    m = {}  
    inorder(root, m) 
  

def _printAllDups(root): 
    m = {}  
    result = inorder(root, m) 
    print(result)

# Driver code  
if __name__ == '__main__':
    '''
         1 
       /   \
      2     3
     / \   / \
    4   5 2   4
         /
        4
    '''
    # root = None
    root = newNode(1)  
    root.left = newNode(2) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
    root.right = newNode(3)  
    root.right.left = newNode(2)  
    root.right.left.left = newNode(4)  
    root.right.right = newNode(4) 
    print(Inorder(root))
    # printAllDups(root)
    print("end")

    '''
       1
      / \
     2   2
     /   /
    3   3
    '''
    root1 = None
    root1 = newNode(1)  
    root1.left = newNode(2)  
    root1.right = newNode(2)  
    root1.left.left = newNode(3)  
    root1.right.left = newNode(3)  
    # printAllDups(root1)
    print(Inorder(root1))
    print("end")

```

**result:**

```

4
4
{'4xy': 3, '2': 1, '5xy': 1, '1': 1, '2y': 1, '3': 1}
end
3
2
{'3xy': 2, '2y': 2, '1': 1}
end

```
