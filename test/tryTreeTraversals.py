class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

  
def printInorder(root): 
    if root:  
        printInorder(root.left) 
        print(root.val,end = " ") 
        printInorder(root.right) 
  
def printPostorder(root): 
    if root:  
        printPostorder(root.left)  
        printPostorder(root.right)
        print(root.val,end = " ") 
        
def printPreorder(root): 
    if root: 
        print(root.val,end = " ")
        printPreorder(root.left) 
        printPreorder(root.right)

def preOrder(root):
  current = root  
  stack = [] 
  done = 0 
  while True:
    if current is not None:
      stack.append(current)
      print(current.val,end = " ")
      current = current.left
    elif(stack):
      current = stack.pop()
      current = current.right
      
    else:
      break

def inOrder(root):
  current = root  
  stack = [] 
  done = 0 
  while True:
    if current is not None:
      stack.append(current)
      current = current.left
    elif(stack):
      current = stack.pop()
      print(current.val,end = " ")
      current = current.right
    else:
      break

def postOrderReverse(root): # doing reverse
  current = root  
  stack = [] 
  done = 0 
  while True:
    if current is not None:
      stack.append(current)
      print(current.val,end = " ")
      current = current.right
      # print(stack[len(stack)-1].val) #test
      # print(True if stack else False) #test
    elif(stack):
      current = stack.pop()
      current = current.left
    else:
      print('c')
      break

def postOrder(root): # doing...
  current = root  
  stack = []
  result = []
  done = 0 
  while True:
    if current is not None:
      stack.append(current)
      # print(current.val,end = " ")
      result.append(current.val)
      current = current.right
    elif(stack):
      current = stack.pop()
      current = current.left
    else:
      break
    
  while result:
    print(result.pop(),end=" ")

# Iterative Postorder Traversal | Set 1 (Using two Stack)
def postOrderIterative(root):  
    if root is None: 
      return        
    s1 = [] 
    s2 = [] 
    s1.append(root) 
    while s1: 
      node = s1.pop() 
      s2.append(node) 
      if node.left: 
        s1.append(node.left)
        print("le")
      if node.right: 
        print("re")
        s1.append(node.right) 
    while s2: 
      node = s2.pop() 
      print(node.val) 

# Iterative Postorder Traversal | Set 2 (Using One Stack)
ans = [] 
def peek(stack): 
    if len(stack) > 0: 
      return stack[-1] 
    return None
def postOrderIterativeOneStack(root): 
  if root is None: 
    return  
  stack = [] 
  while(True): 
    while (root): 
      if root.right is not None: 
        stack.append(root.right) 
      stack.append(root) 
      root = root.left 
    root = stack.pop()  
    if (root.right is not None and peek(stack) == root.right): 
      stack.pop()   
      stack.append(root) 
      root = root.right 
    else: 
      ans.append(root.val)  
      root = None
    if (len(stack) <= 0): 
      break


if __name__ == "__main__":
  root = Node(1) 
  root.left      = Node(2) 
  root.right     = Node(3) 
  root.left.left  = Node(4) 
  root.left.right  = Node(5) 

  '''
             1
            / \
           2   3
          / \
         4   5
  '''
  # print(root.val)
  # print(root.left.val)
  # print(root.right.val)
  # print(root.left.left.val)
  # print(root.left.right.val)


  printPreorder(root) 
  print("Preorder")
  printInorder(root)
  print("inorder")
  printPostorder(root) 
  print("Postorder")

  preOrder(root)
  print("preorder no recursion")
  inOrder(root)
  print("inorder no recursion")
  postOrder(root)
  print("postorder no recursion")
    
  print('postorder no recursion use one stack:')
  postOrderIterativeOneStack(root)
  print(ans)
# # test something (elif):
# # elif is using like a case:
# # only choose one to run
# def tryelif(inp):
#   i = 0
#   while True:
#     if len(inp) <= i:
#       print("4th")
#       break
#     if inp[i] == 2:
#       print("1st")
#       i+=1
#     elif inp[i] <= 4:
#       print("2nd")
#       i+=1
#     elif inp[i] > 4:
#       print("3rd")
#       i+=1
#     else:
#       print("break...")
#       break
#   print("test...")
    
# tryelif([2,4,1,9,2,4])