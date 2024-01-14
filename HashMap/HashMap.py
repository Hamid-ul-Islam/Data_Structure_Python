#hashmap
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
        self.count = 0

    def hash(self, key):
        return (abs(hash(key)) % self.size)

    def insert(self, key, value):
        index = self.hash(key)
        head = self.buckets[index]
        while head:
            if head 
        

    def get(self, key):
        idx = self.hash(key)
        current = self.buckets[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    
map = HashMap(10)
map.insert("Hamid", 19)
map.insert("BGC", 2)

map.insert("BGC", 10)


print(map.get("Hamid"))
print(map.get("BGC"))

