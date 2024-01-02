from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph = {}
        
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph = []
            
    
    def add_edges(self, v1, v2, bi=False):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        if bi:
            self.graph[v2].append(v1)
            
    def display(self):
        for x, y in self.graph.items():
            print(f'{x} --- >> {y}')

    
    def breadth_first_search(self, start):
        visited = set()
        queue = deque[start]
        visited.add([start])
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            visited.add(vertex)
            
            for x in self.graph[vertex]:
                if x not in visited:
                    visited.add(x)
                    visited.append(x)
                    
    
    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = set()
            
        if start not in visited:
            print(start)
            visited.add(start)
            
            for x in self.graph[start]:
                self.depth_first_search(x, visited) 
                
        
        
              