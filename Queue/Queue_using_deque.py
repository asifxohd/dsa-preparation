from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue size:", my_queue.size())

print("Dequeue:", my_queue.dequeue())
print("Dequeue:", my_queue.dequeue())

print("Peek:", my_queue.peek())

print("Is empty?", my_queue.is_empty())
