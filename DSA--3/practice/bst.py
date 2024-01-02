class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.key = value
        

class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, value):
        self.root = self._insert(self.root, value)
        
    def _insert(self, node, value):
        if node is None:
            return Node(value)
        
        if value < node.key:
            node.left = self._insert(node.left, value)
        
        elif value > node.key:
            node.right = self._insert(node.right, value)
            
        return node
    
    def contains(self, value):
        return self._contains(self.root, value)
    
    def _contains(self, node, value):
        if node is None:
            return node
        
        if node.key == value:
            return True
        
        if value < node.key:
            return self.contains(node.left, value)
        
        elif value > node.key:
            return self._contains(node.right, value)
        
     
    def delete(self, value):
        self.root = self._delete(self.root, value)
        
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.key:
            node.left = self._delete(node.left, value)
            
        elif value > node.key:
            node.right = self._delete(node.right, value)
        
        else:
            if node.right is None:
                return node.left
            
            elif node.left is None:
                return node.right
            
        node.key = self.get_min(node.right).key
        node.right = self._delete(node.right, node.key)
        
        return node
    
    def get_min(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur