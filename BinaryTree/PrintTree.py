#simple printing binary tree with recursion
def printTree(root):
  #base case
  if root != None:
    print(root.data)
  else:
    return
  printTree(root.left)
  printTree(root.right)


#print tree in details
def printTreeDetailed(root):
  #base case
  if root == None:
    return
  if root.right is not None:
    print(" R->", root.right.data)
  print(root.data) #root node data
  if root.left is not None:
    print(" L->",root.left.data)
  print("") #for new line after one node (with left and right node) is printed
  
  printTreeDetailed(root.left)
  printTreeDetailed(root.right)
