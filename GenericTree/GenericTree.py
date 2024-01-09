#Generic tree can have many children for a single node so the node will contains 
class Node:
    def __init__(self, data) -> None:#here None is the return type of the function and it's optional in python
        self.data = data
        self.children = []