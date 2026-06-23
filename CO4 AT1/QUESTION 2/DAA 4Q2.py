
def min_cost_climb(cost, k):
    n = len(cost)

    dp = [0] * n

    dp[0] = cost[0]

    for i in range(1, n):
        min_prev = float('inf')

        for j in range(1, k + 1):
            if i - j >= 0:
                min_prev = min(min_prev, dp[i - j])

        dp[i] = cost[i] + min_prev

    return min(dp[n-k:])

n = 5
cost = [10, 15, 20, 5, 10]
k = 2

result = min_cost_climb(cost, k)
print("Min Cost =", result)