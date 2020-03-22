'''
Hi, here's your problem today. This problem was recently asked by Uber:

Given a binary tree, find all duplicate subtrees 
(subtrees with the same value and same structure) 
and return them as a list of list [subtree1, subtree2, ...] 
where subtree1 is a duplicate of subtree2 etc.

Here's an example and some starter code:
'''

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
         1 
       /   \
      2     3
     / \   / \
    4   5 2   4
         /
        4
'''
l4 = Node(4)
l3_3 = Node(2, l4, 0)
l3_2 = Node(5)
l2_1 = Node(2,l4,0) #Node(2,l4,l3_2)
l2_2 = Node(3,l3_3,l4)
root = Node(1,l2_1,l2_2)
print(root)
print(dup_trees(root)) # ans = [[(4), (4)], [(2, (4)), (2, (4))]]
