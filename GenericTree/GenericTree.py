#Generic tree can have many children for a single node so the node will contains data and a list of the child addresses
class Node:
    def __init__(self, data) -> None:#here None is the return type of the function and it's optional in python
        self.data = data
        self.children = [] #addresses of the child nodes

#creating nodes
n1 = Node(5)
n2 = Node(3)
n3 = Node(4)
n = Node(7)
n6 = Node(9)
n7 = Node(10)

#linking nodes
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
