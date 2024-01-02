from collections import deque

class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edges(self, vertex1, vertex2, bi=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if bi:
            self.graph[vertex2].append(vertex1)
            
    def dispaly(self):
        for x , y in self.graph.items():
            print(x,y)
    
    def breadth_first_search(self, graph, startswith):
        visited = set()
        queue = deque()
        queue.append(startswith)
        visited.add(startswith)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end= " ")

            for x in graph[vertex]:
                if x not in visited:
                    visited.add(x)
                    queue.append(x)
                    
                    

                    
    