from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()
        
    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("Stack underflow error")
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None
        
    def display(self):
        print("Stack elements:", list(self.stack))
        
my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.display()


print("Top of the stack:", my_stack.peek())
my_stack.pop()
print("Top of the stack after pop:", my_stack.peek())