#binary tree node class
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#creating node with node class
rootNode = TreeNode(5)
node2 = TreeNode(10)
node3 = TreeNode(20)

#linking node with each other
rootNode.left = node2
rootNode.right = node3

#printing binary tree with recursion
def printTree(root):
  #base case
  if root is not None:
    print(root.data)
  else:
    return
  printTree(root.left)
  printTree(root.right)

#print tree function call -> 5, 10, 20
printTree(rootNode)


#print tree in details
def printTreeDetailed(root):
  #base case
  if root == None:
    return
  if root.right.data is not None:
    print("R->", root.right.data)
  print(root.data) #root node data
  if root.left.data is not None:
    print("L->",root.left.data)
  print("") #for new line after one node (with left and right node) is printed
  
  printTreeDetailed(root.left)
  printTreeDetailed(root.right)

#call detailed print
printTreeDetailed(rootNode)


#taking input for binary tree
def treeInput():
  data = int(input())
  #base case
  if(data == -1):
    return None #-1 means the node would be None and parent node will be linked to None as their left or right node
  
  rootNode = TreeNode(data)
  leftNode = TreeNode()