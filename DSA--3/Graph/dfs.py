class Graph:
    def __init__(self) -> None:
        self.graph = {}
        
    def add_vartex(self, vertax):
        if vertax not in self.graph:
            self.graph[vertax] = []
            
    def add_edges(self, vertax1, vertax2, bidirection=False):
        self.add_vartex(vertax1)
        self.add_vartex(vertax2)
        self.graph[vertax1].append(vertax2)
        if bidirection:
            self.graph[vertax2].append(vertax1)
            
    def dispaly(self):
        for x, y in self.graph.items():
            print(x, y)
            
    
    def depth_first_search(self, graph, startswith):
        pass
        
            