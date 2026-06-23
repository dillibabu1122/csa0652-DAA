def subset_sum_range(arr, index, current_subset,
                     current_sum, low, high):

    if current_sum > high:
        return

    if low <= current_sum <= high:
        print(current_subset)

    if index == len(arr):
        return
    current_subset.append(arr[index])

    subset_sum_range(arr,
                     index + 1,
                     current_subset,
                     current_sum + arr[index],
                     low,
                     high)

    current_subset.pop()
    subset_sum_range(arr,
                     index + 1,
                     current_subset,
                     current_sum,
                     low,
                     high)


arr = [2, 3, 5, 7]
low = 5
high = 10

print("Valid Subsets:")

subset_sum_range(arr, 0, [], 0, low, high)
