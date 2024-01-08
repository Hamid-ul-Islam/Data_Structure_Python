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

#logic: only lastNode will return 0 (according to base case) as it's right and left is None then we add +1 to left and rightCount so that every node will return 1
def numOfNodes(root):
    if root is None:
        return 0
    leftNodeCount = numOfNodes(root.left) #numOfNodes() function will keep calling for left node untill it's reached to the None. then it will start calling root.right and if right has left
    rightNodeCount = numOfNodes(root.right)
    
    return leftNodeCount + rightNodeCount + 1 #adding +1 for every return


