class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
 
    def dequeue(self):
        if self.head is None:
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        if self.head is None:
            print("Queue is empty. Cannot peek.")
            return None
        else:
            return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue after enqueue operations:")
my_queue.display()

print("Dequeue:", my_queue.dequeue())
print("Peek:", my_queue.peek())

print("Queue after dequeue and peek operations:")
my_queue.display()
