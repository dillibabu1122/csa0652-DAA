
def knapsack(capacity, resources, priorities, n):

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if resources[i - 1] <= w:
                dp[i][w] = max(
                    priorities[i - 1] + dp[i - 1][w - resources[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


resources = [10, 20, 30, 40]
priorities = [60, 100, 120, 150]
capacity = 50

n = len(resources)

max_priority = knapsack(capacity, resources, priorities, n)

print("Maximum Priority Value =", max_priority)

