#Generic tree can have many children for a single node so the node will contains data and a list of the child addresses
class Node:
    def __init__(self, data) -> None:#here None is the return type of the function and it's optional in python
        self.data = data
        self.children = [] #addresses of the child nodes

