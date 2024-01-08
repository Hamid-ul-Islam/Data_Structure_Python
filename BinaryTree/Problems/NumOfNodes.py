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

