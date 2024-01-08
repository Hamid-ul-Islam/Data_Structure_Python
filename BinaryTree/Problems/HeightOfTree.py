#creating treenode
class TreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
        

rootNode = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(3)

rootNode.left = node2
rootNode.right = node3

#logic: lastNode will return 0 and 0 from left and right as they are None. then we find max of them. and we add +1 and return. so last node will return 1. Recursively continues for left side and every 
def heightOfTree(root):
    if root is None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    
    return max(leftHeight, rightHeight) + 1
    