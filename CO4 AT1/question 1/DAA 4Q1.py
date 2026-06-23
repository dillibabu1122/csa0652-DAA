
INF = float('inf')
def floyd_warshall(graph, n):
    # Create a copy of the graph
    dist = [row[:] for row in graph]

    # Update distances using each node as an intermediate node
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
n = 3
graph = [
    [0, 5, INF],
    [2, 0, 3],
    [INF, INF, 0]
]

result = floyd_warshall(graph, n)
print("Shortest Distance Matrix:")
for row in result:
    for value in row:
        if value == INF:
            print("INF", end=" ")
        else:
            print(value, end=" ")
    print()