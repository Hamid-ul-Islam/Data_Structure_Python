#importing printing and taking input functions
from PrintTree import printTree, printTreeDetailed

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


#taking input recursively for binary tree
def treeInput():
  data = int(input())
  #base case
  if(data == -1):
    return None #-1 means the node would be None and parent node will be linked to None as their left or right node
  
  #creating a rootNode, also left and right node for the root node each time
  rootNode = TreeNode(data)
  leftNode = TreeNode(treeInput()) #treeInput() again called and it will create leftNode(it is the root that time) and ask for left and right node for it
  rightNode = TreeNode(treeInput())
  
  #linking created node with each
  rootNode.left = leftNode
  rootNode.right = rightNode
  
  return rootNode #it will return the firs-most root node of the whole tree which is needed for printing nodes

#taking input and printing
printTree(rootNode)