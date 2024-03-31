from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_Edge(self,u, v):
        self.graph[u].append(v)
    def BFS(self,s):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s,end = " ")
            for neighbor in self.graph[s]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor]=True    

if __name__ == "__main__":
    graph = Graph()
    graph.add_Edge(0,1)
    graph.add_Edge(0,2)
    graph.add_Edge(1,0)
    graph.add_Edge(1,3)
    graph.add_Edge(2,1)
    graph.add_Edge(3,0)
    graph.BFS(0)
