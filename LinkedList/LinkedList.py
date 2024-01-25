#node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#basic nodes
n1 = Node(5)
n2 = Node(6)
n3 = Node(7)

#linking nodes
n1.next = n2
n2.next = n3

def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
        if head is None:
            print("None")

printLL(n1)



#taking input for linkedlist
def takeInput():
    head = None
    tail = None
    inputList = [int(ele) for ele in input().split()]
    
    for currData in inputList:
        if currData == -1:
            break
        
        if head is None:
            head = 