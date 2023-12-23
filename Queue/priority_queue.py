import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []  
        
    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            return item
        else:
            print("Priority queue is empty. Cannot dequeue.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]  # Return the item with the highest priority
        else:
            print("Priority queue is empty. Cannot peek.")
            return None

    def display(self):
        items = [item for priority, item in self.heap]
        print(items)

# Example usage:
my_priority_queue = PriorityQueue()

my_priority_queue.enqueue("Task 1", 3)
my_priority_queue.enqueue("Task 2", 1)
my_priority_queue.enqueue("Task 3", 2)

print("Priority queue after enqueue operations:")
my_priority_queue.display()

print("Dequeue:", my_priority_queue.dequeue())
print("Peek:", my_priority_queue.peek())

print("Priority queue after dequeue and peek operations:")
my_priority_queue.display()
