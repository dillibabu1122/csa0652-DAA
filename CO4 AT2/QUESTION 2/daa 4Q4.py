
temperature = [28, 30, 29, 31, 27]
rainfall = [120, 100, 110, 90, 130]
soil_quality = [8, 7, 9, 6, 8]

dp = []

for i in range(len(temperature)):
    yield_prediction = (
        temperature[i] * 0.3 +
        rainfall[i] * 0.2 +
        soil_quality[i] * 10
    )

    dp.append(yield_prediction)
print("Predicted Crop Yields:")
for i in range(len(dp)):
    print("Field", i + 1, "=", round(dp[i], 2))