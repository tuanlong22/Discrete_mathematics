tsp_g = [
   [0, 3, 93, 13, 33,9],
   [4, 0, 77, 42, 21,16],
   [15, 17, 0, 36, 16,28],
   [39, 90, 80, 0, 56,7],
   [28, 46, 88, 33, 0,25],
   [3,88,18,46,92,0]
]
visited = [0] * 12
n = 6
cost = 0
def travellingsalesman(c):
    global cost
    adj_vertex = 999
    min_val = 999
    visited[c] = 1
    print(c + 1, end = " ")
    for k in range(n):
        if (tsp_g[c][k] != 0 and visited[k] == 0):
            if (tsp_g[c][k] < min_val):
                min_val = tsp_g[c][k]
                adj_vertex = k
    if (min_val != 999):
        cost = cost + min_val
    if (adj_vertex == 999):
        adj_vertex = 0
        print(adj_vertex + 1, end = " ")
        cost += tsp_g[c][adj_vertex]
        return 
    travellingsalesman(adj_vertex)
print("Shortest Path: ", end = " ")
travellingsalesman(0)
print("\nMinimum Cost: ", cost)
