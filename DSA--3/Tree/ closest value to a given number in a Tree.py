class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.key = value

class BST:
    def __init__(self) -> None:
        self.root = None  
        
    def closest_value_to_the_target(self, target):
        closest = self.root.key
        current = self.root
        while current:
            if abs(current.key - target) < abs(closest - target):
                closest = current.key
            if current.key == target:
                return target
            elif current.key > target:
                current = current.left
            else:
                current = current.right
                
        return closest
            
                
        
        
new  = BST()
print(new.closest_value_to_the_target(10))