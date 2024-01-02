class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._contains(root.left, key)
        else:
            return self._contains(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self._min_value_node(root.right)
            root.key = successor.key
            root.right = self._delete(root.right, successor.key)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def post_order_traversal(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result

    def _post_order_traversal(self, node, result):
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.key)


# Example Usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("In-order traversal:", bst.in_order_traversal())
print("Pre-order traversal:", bst.pre_order_traversal())
print("Post-order traversal:", bst.post_order_traversal())

key_to_delete = 30
print(f"\nDeleting node with key {key_to_delete}")
bst.delete(key_to_delete)
print("In-order traversal after deletion:", bst.in_order_traversal())
