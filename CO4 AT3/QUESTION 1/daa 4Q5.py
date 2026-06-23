
def dice_throw(num_dice, faces, target_sum):
    dp = [[0] * (target_sum + 1) for _ in range(num_dice + 1)]

    dp[0][0] = 1

    for d in range(1, num_dice + 1):
        for s in range(1, target_sum + 1):
            for face in range(1, faces + 1):
                if s - face >= 0:
                    dp[d][s] += dp[d - 1][s - face]

    return dp[num_dice][target_sum]
def coin_change(coins, amount):
    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

num_dice = 2
faces = 6
target_sum = 7

dice_result = dice_throw(num_dice, faces, target_sum)

coins = [1, 2, 5]
amount = 5

coin_result = coin_change(coins, amount)
print("Dice Throw Problem")
print("-------------------")
print("Number of Ways =", dice_result)

print("\nCoin Change Problem")
print("-------------------")
print("Number of Ways =", coin_result)