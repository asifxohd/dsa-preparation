class Node:
    def __init__(self, key, value) -> None:
        self.key = key 
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
        
    def _hash(self,key):
        return hash(key) % self.capacity
    
    def insertion(self,key,value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key,value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            
    def deletion(self, key):
        
        index = self._hash(key)
        if self.table[index] is None:
            raise KeyError("key not found")
        
        current = self.table[index]
        
        if current.key == key:
            self.table[index] = current.next
            return
        
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
            
        raise KeyError("not found")
    
    def search(self,key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError("key not found")
            
            