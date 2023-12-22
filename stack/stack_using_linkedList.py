class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.head = None
        
    def __str__(self):
        if self.head is None:
            return "stack []"
        else:
            name = ''
            current = self.head
            while current:
                name += f" {current.value} -->"
                current = current.next
            return name[:-3]
            
        
    def push(self , value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
            
    def pop(self):
        if self.head is None:
            return "stack is empty"
        else:
            self.head = self.head.next
    
    def peek(self):
        return self.head.value if self.head is not None else "stack is empty"
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
stack.pop()
print(stack)  
print("Peek:", stack.peek())  
