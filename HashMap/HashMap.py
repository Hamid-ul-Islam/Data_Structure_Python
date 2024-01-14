class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = Node(key, value)
        else:
            current = self.buckets[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.buckets[index] = current.next
                return
            previous = current
            current = current.next

# Example usage:
hash_map = HashMap(10) #creating map of size 10 filled with None
hash_map.put("key1", "Hamid")
hash_map.put("key2", "BGC")
hash_map.put("key3", "Robot")

print(hash_map.get("key1"))  # Output: Hamid
print(hash_map.get("key2"))  # Output: value2

hash_map.put("key1", "new_value1")  # Update existing key
print(hash_map.get("key1"))  # Output: new_value1

hash_map.remove("key2")
print(hash_map.get("key2"))  # Output: None (key2 is removed)
