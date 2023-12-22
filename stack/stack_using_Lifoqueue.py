from queue import LifoQueue

stack = LifoQueue(maxsize=5)
print(stack.qsize())

stack.put(2)
stack.put("e")
stack.put(4)

print(stack.get())
print(stack.get())
print(stack.get())
