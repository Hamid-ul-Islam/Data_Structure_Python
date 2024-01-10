#Generic tree can have many children for a single node so the node will contains data and a list of the child addresses
class Node:
    def __init__(self, data):#here None is the return type of the function and it's optional in python
        self.data = data
        self.children = list() #addresses list of the child nodes

#creating nodes
n1 = Node(5)
n2 = Node(3)
n3 = Node(4)
n4 = Node(7)
n5 = Node(9)
n6 = Node(10)
n7 = Node(20)

#linking nodes
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n2.children.append(n6)
n2.children.append(n7)


#finding the number of nodes logic: every leaf nodes has no child(None) and it should return 0 and we will add +1 with every recursive return of the function

def number 