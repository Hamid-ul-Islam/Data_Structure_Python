from BinaryTree import TreeNode

#taking input recursively for binary tree
def treeInput(TreeNode):
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
