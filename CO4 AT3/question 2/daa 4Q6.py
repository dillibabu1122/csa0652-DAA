
from itertools import permutations
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cities = len(graph)
def tsp_dp(graph):
    vertices = list(range(1, cities))
    min_cost = float('inf')
    best_path = []
    for perm in permutations(vertices):
        current_cost = 0
        current_path = [0]
        k = 0
        for j in perm:
            current_cost += graph[k][j]
            current_path.append(j)
            k = j

        current_cost += graph[k][0]
        current_path.append(0)

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path
    return min_cost, best_path
def tsp_greedy(graph):
    visited = [False] * cities
    current = 0
    visited[current] = True

    path = [0]
    total_cost = 0

    for _ in range(cities - 1):
        next_city = -1
        min_distance = float('inf')

        for city in range(cities):
            if not visited[city] and graph[current][city] < min_distance:
                min_distance = graph[current][city]
                next_city = city

        visited[next_city] = True
        path.append(next_city)
        total_cost += min_distance
        current = next_city

    total_cost += graph[current][0]
    path.append(0)
    return total_cost, path
dp_cost, dp_path = tsp_dp(graph)
greedy_cost, greedy_path = tsp_greedy(graph)

print("Dynamic Programming Solution")
print("Path:", dp_path)
print("Minimum Cost =", dp_cost)

print("\nGreedy Nearest Neighbor Solution")
print("Path:", greedy_path)
print("Tour Cost =", greedy_cost)