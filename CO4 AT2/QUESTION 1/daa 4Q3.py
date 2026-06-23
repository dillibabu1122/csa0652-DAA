# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(capacity, memory, revenue, n):
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if memory[i - 1] <= w:
                dp[i][w] = max(
                    revenue[i - 1] + dp[i - 1][w - memory[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
memory = [10, 20, 30, 40, 50]
revenue = [60, 100, 120, 150, 200]

capacity = 100
n = len(memory)
max_revenue = knapsack(capacity, memory, revenue, n)

print("Maximum Revenue =", max_revenue)