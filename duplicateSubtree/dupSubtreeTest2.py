
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