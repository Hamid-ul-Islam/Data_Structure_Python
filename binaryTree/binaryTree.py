#binary tree node
class TreeNode:
 def __init__(self, data):
  self.data = data
  self.left = None
  self.right = None


rootNode = TreeNode(5)
node2 = TreeNode(10)
node3 = TreeNode(20)

print(node2.data)