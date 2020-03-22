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
