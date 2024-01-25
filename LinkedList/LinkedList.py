#node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
n1 = Node(5)
n2 = Node(6)
n3 = Node(7)

n1.next = n2
n2.next = n3


def printLL(head):
    while head is not None:
        print(head.data)
        