class Minheap:
    def _init_(self) -> None:
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = ( index - 1) // 2

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index] , self.heap[parent_index] = self.heap[parent_index] , self.heap[index]
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

            smallest = index

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest != index :
                self.heap[smallest] , self.heap[index] = self.heap[index] , self.heap[smallest]
                index = smallest
            else:
                break

    def build_heap(self, arr):
        n = len(arr)
        self.heap = arr

        for i in range(n // 2 - 1, -1 , -1):
            self.heapify_down(i)


# Example usage:
min_heap = Minheap()
min_heap.insert(10)
min_heap.insert(30)
min_heap.insert(40)
min_heap.insert(50)
min_heap.insert(60)
min_heap.pop()
min_heap.pop()
min_heap.pop()
min_heap.pop()
# array_to_heapify = [4, 10, 3, 5, 1]
# min_heap.build_heap(array_to_heapify)
print(min_heap.heap)  # Output: [1, 4, 3, 5, 10]