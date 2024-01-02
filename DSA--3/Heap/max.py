class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2

            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return node

    def heapify_down(self, index):
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            largest = index

            if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
                largest = left_child

            if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                index = largest
            else:
                break

    def build_heap(self, arr):
        n = len(arr)
        self.heap = arr

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

# Example usage:
# Example usage:
max_heap = MaxHeap()

# Insert elements into the max heap
max_heap.insert(10)
max_heap.insert(30)
max_heap.insert(40)
max_heap.insert(50)
max_heap.insert(60)

# Print the current state of the max heap
print("Max Heap:", max_heap.heap)  # Output: [60, 50, 40, 10, 30]

# Remove the maximum element (60)
max_heap.pop()
print("Max Heap after popping:", max_heap.heap)  # Output: [50, 30, 40, 10]

# Insert more elements
max_heap.insert(70)
max_heap.insert(20)
max_heap.insert(35)

# Print the current state of the max heap
print("Max Heap:", max_heap.heap)  # Output: [70, 50, 40, 10, 30, 20, 35]

# Remove the maximum element (70)
max_heap.pop()
print("Max Heap after popping:", max_heap.heap)  # Output: [50, 30, 40, 10, 20, 35]

# Build max heap from an array
array_to_heapify = [4, 10, 3, 5, 1]
max_heap.build_heap(array_to_heapify)
print("Max Heap after building from array:", max_heap.heap)  # Output: [10, 5, 3, 4, 1]

# Insert more elements
max_heap.insert(15)
max_heap.insert(8)

# Print the current state of the max heap
print("Max Heap:", max_heap.heap)  # Output: [15, 10, 3, 5, 1, 5, 8, 4]
