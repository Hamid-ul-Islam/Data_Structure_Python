class TreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
        

root = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(3)

root.left = node2
root.right = node3

#logic: only lastNode will return 0 as it's right and left is None
def numOfNodes(root):
    if root is None:
        return 0
    leftNodeCount = numOfNodes(root.left)
    rightNodeCount = numOfNodes(root.right)
    
    return leftNodeCount + rightNodeCount + 1