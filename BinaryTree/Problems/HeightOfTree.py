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

#logic: 
def heightOfTree(root):
    if root is None:
        return 0
    leftHeight = heightOfTree(root.left)
    rightHeight = heightOfTree(root.right)
    
    return max(leftHeight, rightHeight) + 1
    