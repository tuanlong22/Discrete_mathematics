from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add_Edge(self,u, v):
        self.graph[u].append(v)
    def DFSutil(self, v, visited):
        visited.add(v)
        print(v, end= " ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSutil(neighbor,visited)
    def DFS(self, v):
        visited = set()
        self.DFSutil(v,visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_Edge(0,1)
    graph.add_Edge(0,2)
    graph.add_Edge(1,0)
    graph.add_Edge(1,3)
    graph.add_Edge(2,1)
    graph.add_Edge(3,0)
    graph.DFS(0)