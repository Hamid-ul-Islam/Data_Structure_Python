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

def numOfLeafNodes(root):
    if root is None:
        return 1
    leafNodeOnLeft = numOfLeafNodes(root.left)
    leafNodeOnRight = numOfLeafNodes(root.right)
    
    return leafNodeOnLeft + leafNodeOnRight

print(numOfLeafNodes(rootNode))