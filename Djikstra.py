class Graph:
    def minDistance(self, dist, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    def printPath(self, parent, j, l):
    # Returns a list from destination to source
    # Base case when j = source
        if parent[j] == -1:
           return l
        else:
           l.append(j)
           return self.printPath(parent, parent[j], l)  


    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        
        for i in range(1, len(dist)):
            st = f"\n{src}  --> {i}\t\t{dist[i]}\t\t\t\t\t{self.printPath(parent,i,[])[::-1]}"
            #print(("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])), end=' ')
            #self.printPath(parent, i)
            print (st)


    def dijkstra(self, graph, src):
        row = len(graph)
        col = len(graph[0])        
        dist = [float("Inf")] * row        
        parent = [-1] * row        
        dist[src] = 0  
        queue = []
        for i in range(row):
            queue.append(i)        
        while queue:            
            u = self.minDistance(dist, queue)            
            queue.remove(u)            
            for i in range(col):                
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u        
        self.printSolution(dist, parent)
# Driver program
g = Graph()
graph = [[0, 3, 0, 0, 1, 20],
           [0, 0, 8, 0, 0, 2],
           [0, 0, 0, 6, 8, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 4, 0, 3],
           [0, 0, 5, 13, 0, 0]
           ]
 
g.dijkstra(graph,0)
 
# This code is contributed by Divyanshu Mehta