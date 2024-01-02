class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def heapify_up(self):
        idx = len(self.heap) - 1

        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx] > self.heap[idx]:
                self.heap[parent_idx], self.heap[idx] = self.heap[idx], self.heap[parent_idx]
                idx = parent_idx
            else:
                break

    def heapify_down(self, index=0):
        n = len(self.heap)
        while True:
            left_idx = 2 * index + 1
            right_idx = 2 * index + 2

            smallest = index
            if left_idx < n and self.heap[left_idx] < self.heap[smallest]:
                smallest = left_idx
            if right_idx < n and self.heap[right_idx] < self.heap[smallest]:
                smallest = right_idx

            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()

    def pop(self):
        if len(self.heap) == 0:
            return "No element to Pop"
        if len(self.heap) == 1:
            return self.heap.pop()

        node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        return node

    def build_heap(self, arr):
        n = len(arr)
        self.heap = arr

        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)
