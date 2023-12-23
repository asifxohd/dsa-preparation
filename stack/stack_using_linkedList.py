class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack underflow error. Cannot pop.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

my_stack = StackLinkedList()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Top of the stack:", my_stack.peek())

popped_item = my_stack.pop()
print("Popped item:", popped_item)

print("Is stack empty?", my_stack.is_empty())
