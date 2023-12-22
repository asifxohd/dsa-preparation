from collections import deque
stack = deque()

stack.append(10)
stack.append(1)
stack.append(120)
stack.append(104)

print(stack)
print(stack.pop())
print(stack.pop())

print(stack)

print(stack[-1])