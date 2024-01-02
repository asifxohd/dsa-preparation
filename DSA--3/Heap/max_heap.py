class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        
    def heapify_up(self):
        idx = len(self.heap) - 1
        
        while idx > 0:
            parent_idx = (idx - 1) // 2
            
            if self.heap[idx] > self.heap[parent_idx]:
                self.heap[idx] , self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break
            
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()
        
        
    def heapify_down(self, index=0):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            
            largest = index
            
            if left < len(self.heap) and self.heap[largest] < self.heap[left]:
                largest = left
            
            if right < len(self.heap) and self.heap[largest] < self.heap[right]:
                largest = right
            
            if index != largest:
                self.heap[index], self.heap[largest] = self.heap[largest],self.heap[index]
                index = largest
                
            else:
                break
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        node = self.heap.pop()
        self.heap[0] = self.heap.pop()
        self.heapify_down()
        
        return node
    
    
    def build_heap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n//2 -1, -1, -1):
            self.heapify_down(i)
        
            
        
            
            
        
        
        
        
            
            