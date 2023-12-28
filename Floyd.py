# The number of vertices
nV = 6

INF = 999

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        print("Matrix after adding vertex", k + 1)
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        # Print the current matrix
        print_solution(distance)
        print()

# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")

G = [[0, 8, 8, 8, 8, 2],
     [8, 0, -2, 7, 6, 2],
     [8, 4, 0, 3, 2, 3],
     [8, 4, INF, 0, -1, 4],
     [8, 2, 2, 3, 0, 8],
     [8, 3, 2, -1, 4, 0]]

floyd_warshall(G)
