class Node:
    def __init__(self, value) -> None:
        self.key = value
        self.left = None
        self.right = None
    
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
            node.right = self._insert(node.right ,value)
        
        return node
    
    def contains(self,value):
        return self._contains(self.root, value)
    
    def _contains(self, node, value):
        if node is None:
            return False
        
        if node.key == value:
            return True

        elif value < node.key:
            return self._contains(node.left , value)
        
        elif value > node.key:
            return self._contains(node.right, value)
        
    def in_order(self):
        result = []
        self._in_order(self.root)
        return result
    
    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.key)
            self._in_order(node.right, result)
            
    def pre_order(self):
        result = []
        self._pre_order(self.root)
        return result
    
    def _pre_order(self, node, result):
        if node:
            result.append(node.key)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)
    
    def post_order(self):
        result = []
        self._post_order(self.root)
        return result
    
    def _post_order(self, node, result):
        if node:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.key)
            
    def delete(self, value):
        self.root = self._delete(self.root , value)
        
    def _delete(self, node, value):
        if node is None:
            return
        
        if value < node.key :
            node.left = self._delete(node.left , value)
        
        elif value > node.key:
            node. right = self._delete(node.right, value)
            
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
        node.key = self.get_min(node.right).key
        node.right = self._delete(node.right and node.key)
        
        return node
    
    def get_min(self, node):
        current = node 
        while current:
            current = current.left
        return current
    
    
            
            
    