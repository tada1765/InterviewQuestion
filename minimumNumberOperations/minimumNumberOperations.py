""" Hi, here's your problem today. This problem was recently asked by LinkedIn:
You are only allowed to perform 2 operations, multiply a number by 2, 
or subtract a number by 1. Given a number x and a number y, 
find the minimum number of operations needed to go from x to y.
 """

""" MY THOUGHT...
            x
          /  \
         /    \
        /      \
       /        \
     x-1        x*2
    /   \      /   \
  x-1  x*2   x-1   x*2

  reach x == y stop, then find min path and count,N=?
"""

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"[{self.value}, {self.left}, {self.right}]"
    if self.left:
      return f"[{self.value}, {self.left}]"
    if self.right:
      return f"[{self.value}, None, {self.right}]"
    return f"[{self.value}]"

def _insert(root, key):
    temp = []
    temp.append(root)
    # flag = 0
    while (len(temp)):  
        root = temp[0]  
        temp.pop(0)  
  
        if (not root.left): 
            root.left = Node(key)
            # flag = 0  
            break
        else: 
            temp.append(root.left)  
  
        if (not root.right): 
            root.right = Node(key)
            # flag = 1  
            break
        else: 
            temp.append(root.right)  
    # return flag

# # testing _insert function      
# root = Node(1) 
# root.left      = Node(2) 
# root.right     = Node(3) 
# root.left.left  = Node(4) 
# root.left.right  = Node(5)

# '''
#              1
#             / \
#            2   3
#           / \
#          4   5
# '''
# print(root) # [1, [2, [4], [5]], [3]]
# _insert(root,7)
# print(root) # [1, [2, [4], [5]], [3, [7]]]

      
# root = Node(1) 
# root.left      = Node(2) 
# root.right     = Node(3) 
# root.left.left  = Node(4) 
# root.left.right  = Node(5)
# root.right.left  = Node(6) 
# root.right.right  = Node(7)

# '''
#              1
#             / \
#            2   3
#           / \
#          4   5
# '''
# print(root) # [1, [2, [4], [5]], [3, [6], [7]]]
# _insert(root,8)
# print(root) # [1, [2, [4, [8]], [5]], [3, [6], [7]]]

# refer: https://www.geeksforgeeks.org/get-level-of-a-node-in-a-binary-tree/

def getLevelUntil(node, data, level): 
    if (node == None): 
        return 0
    if (node.value == data): 
        return level  

    downlevel = getLevelUntil(node.left, data, level+1)  
    if (downlevel != 0): 
        return downlevel  
  
    downlevel = getLevelUntil(node.right, data, level+1)  
    return downlevel  
  
# Returns level of given data value  
def getLevel(node, data): 
    return getLevelUntil(node, data, 1)  

# MY CODE:
import queue 

def min_operations(x, y):
    q = queue.Queue() 
    root = Node(x) 
    q.put(root)  
    resultTree = Node(x) # cause "root" data is not store as tree
    while(1):

      root = q.get()
      val = root.value
      if (x <= 0): # fix 0 and neg value as input data
        return 0

      if (x != val): # skip the 1st insertion
        _insert(resultTree,val)

      if (val != y):
        if ((val-1) >= 0): # fix if neg value occur
          root.left = Node(val-1) # left = -1
          q.put(root.left)
        root.right = Node(val*2) # right = *2
        q.put(root.right)

      else:break
    
    # print(resultTree) # [6, [5, [4, [3], [8]], [10, [9], [20]]], [12, [11], [24]]]
    return getLevel(resultTree, y) - 1 # 3

# ''' resultTree:
#                6
#               /  \
#              /    \
#             /      \
#            5        12
#           / \      /  \
#          4   10   11  24
#         / \ /  \
#        3  8 9  20 
# '''

print(min_operations(6, 20)) # 3
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3

# CODE Testing (fix neg value & 0 value)
print(min_operations(1, 20)) # 6
print(min_operations(0, 20)) # 0
print(min_operations(-1, 20)) # 0


# # from https://www.geeksforgeeks.org/minimum-number-operation-required-convert-number-x-y/
# # steps needed to convert a number x into y  
# # with two operations allowed :  
# # (1) multiplication with 2  
# # (2) subtraction with 1.
# import queue 
  
# # A node of BFS traversal  
# class node: 
#     def __init__(self, val, level): 
#         self.val = val  
#         self.level = level 
  
# # Returns minimum number of operations  
# # needed to convert x into y using BFS  
# def minOperations(x, y): 
      
#     # To keep track of visited numbers  
#     # in BFS.  
#     visit = set()  
  
#     # Create a queue and enqueue x into it.  
#     q = queue.Queue() 
#     n = node(x, 0)  
#     q.put(n)  
  
#     # Do BFS starting from x  
#     while (not q.empty()): 
          
#         # Remove an item from queue  
#         t = q.get()  
  
#         # If the removed item is target  
#         # number y, return its level  
#         if (t.val == y): 
#             return t.level  
  
#         # Mark dequeued number as visited  
#         visit.add(t.val)  
  
#         # If we can reach y in one more step  
#         if (t.val * 2 == y or t.val - 1 == y):  
#             return t.level+1
  
#         # Insert children of t if not visited  
#         # already  
#         if (t.val * 2 not in visit): 
#             n.val = t.val * 2
#             n.level = t.level + 1
#             q.put(n) 
#         if (t.val - 1 >= 0 and t.val - 1 not in visit): 
#             n.val = t.val - 1
#             n.level = t.level + 1
#             q.put(n) 

# # Driver code  
# if __name__ == '__main__': 
  
#     x = 4
#     y = 7
#     print(minOperations(x, y)) # 2
#     # print(minOperations(6, 20)) # 5 hmm why not 3
#     # print(minOperations(0, 20)) # None
#     # print(minOperations(2, 20)) # too long runing