from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
   
    def add_edges(self, vertex1, vertex2,bi=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if bi:
            self.graph[vertex2].append(vertex1)
            
    def display(self):
        for x, y in self.graph.items():
            print(f'{x}--{y}')
            
    
    def bredth_first_search(self, graph, start_node):
        visited = set() 
        q = deque()
        q.append(start_node)
        visited.add(start_node)
        
        while q:
            vertex = q.popleft()
            print(vertex, end=" ")
            
            for x in graph[vertex]:
                if x not in visited:
                    q.append(x)
                    visited.add(x)
                    
