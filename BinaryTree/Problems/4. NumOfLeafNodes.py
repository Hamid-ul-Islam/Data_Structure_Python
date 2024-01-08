#creating treenode
class TreeNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
        

rootNode = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(15)
node5 = TreeNode(20)

rootNode.left = node2
rootNode.right = node3
node2.left = node4
node2.right = node5

def numOfLeafNodes(root):
    if root.left is None and root.right is None:
        return 1

    leafNodeOnLeft = numOfLeafNodes(root.left)
    leafNodeOnRight = numOfLeafNodes(root.right)

    return leafNodeOnLeft + leafNodeOnRight

print(numOfLeafNodes(rootNode))