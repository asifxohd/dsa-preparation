class TreeNode:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        
    def validate_bst(self, root):
        values = []
        def in_order_traversal(node):
            if node:
                in_order_traversal(node.left)
                values.append(node.key)
                in_order_traversal(node.right)
        in_order_traversal(root)
    
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        return True 
    
    
bst = BST()
bst.root = TreeNode(2)
bst.root.left = TreeNode(1)
bst.root.right = TreeNode(3)
print(bst.validate_bst(bst.root))

# 2. Invalid BST
invalid_bst = BST()
invalid_bst.root = TreeNode(5)
invalid_bst.root.left = TreeNode(1)
invalid_bst.root.right = TreeNode(4)
invalid_bst.root.right.left = TreeNode(3)
invalid_bst.root.right.right = TreeNode(6)
print(invalid_bst.validate_bst(invalid_bst.root))

# 3. Edge case - Empty Tree
empty_tree = BST()
print(empty_tree.validate_bst(empty_tree.root))

# 4. Edge case - Single Node
single_node_tree = BST()
single_node_tree.root = TreeNode(1)
print(single_node_tree.validate_bst(single_node_tree.root))
