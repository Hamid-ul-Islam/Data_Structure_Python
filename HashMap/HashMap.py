#hashmap
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size):
        self.buckets = [None] * size
        self.bucketSize = size
        self.count = 0

    def hash(self, key):
        return (abs(hash(key)) % self.bucketSize)

    def insert(self, key, value):
        index = self.hash(key)
        head = self.buckets[index]
        while head:
            if head.key == key:
                head.value = value
                return
            head = head.next
        newNode = MapNode(key, value)
        self.buckets[index] = newNode
        self.count += 1
    
    def remove(self, key):
        index = self.hash(key)
        head = self.buckets[index]
        prev = None
        while head:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = None
                else:
                    prev.next = head.next
            
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
    
#creating map of size 10 initialized with 0
map = HashMap(10)

#inserting
map.insert("Hamid", 19)
map.insert("BGC", 2)

#printing
print(map.get("Hamid"))
print(map.get("BGC"))

#
map.insert("BGC", 10) #update BGC value with 10

map.remove("Hamid")

print(map.get("Hamid"))

map.insert("Hamid", 19)

print(map.get("Hamid"))