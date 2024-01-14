#hashmap : simply a list where every block contains a LinkedList. when we try to insert a key value pair into the list we module  HashCod(key) % size of the buckets/list and we find a specific index. we try to insert into the index. if any other keys (HashCod(key) % size) returns same index we maintain a linkend list chain

class MapNode: #Linkedlist node with key and value
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap: #a list containing a linkedlist in each blocks (initialiezed with None first)
    def __init__(self, size):
        self.buckets = [None] * size
        self.bucketSize = size
        self.count = 0

    def hash(self, key): # this returns index within the bucketsize
        return (abs(hash(key)) % self.bucketSize)

    def insert(self, key, value):
        index = self.hash(key)
        head = self.buckets[index] #first find the head of first entry of the list and try to traverse the linkedlist of it
        while head: #while head is not None
            if head.key == key: #if any linkedlist nodes.key == givenKey, we simply have to update the value
                head.value = value
                return
            head = head.next #else head will point to next node

        newNode = MapNode(key, value)
        self.buckets[index] = newNode
        self.count += 1
        head = self.buckets[index] #head will traversed to None by doing head.next so we have re
    
    def remove(self, key):
        index = self.hash(key)
        head = self.buckets[index]
        prev = None
        while head:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = None
                    self.count -= 1
                else:
                    prev.next = head.next
                    self.count -= 1
            
            prev = head
            head = head.next
        return None

    def size(self):
        return self.count

    def get(self, key):
        idx = self.hash(key)
        current = self.buckets[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
#creating map of size 10 initialized with None
map = HashMap(10)

#inserting
map.insert("Hamid", 19)
map.insert("BGC", 2)

#printing
print(map.get("Hamid"))
print(map.get("BGC"))

#replace/update
map.insert("BGC", 10) #update BGC value with 10
print(map.get("BGC"))

#removing element
map.remove("Hamid")

#try to get after removing
print(map.get("Hamid")) #returns None