def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key in correct position
        arr[j + 1] = key

    return arr
arr = [12, 11, 13, 5, 6]
print("Original Array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted Array:", sorted_arr)

