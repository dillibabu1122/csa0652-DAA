import time

# -----------------------------
# Binary Search for Integers
# -----------------------------
def binary_search_int(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons

# -----------------------------
# Binary Search for Floats
# -----------------------------
def binary_search_float(arr, target, epsilon=1e-6):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if abs(arr[mid] - target) < epsilon:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons

# -----------------------------
# Dataset Creation
# -----------------------------
sizes = [1000, 10000, 100000]

print("\nBINARY SEARCH PERFORMANCE ANALYSIS")
print("-" * 80)
print(f"{'Size':<12}{'Data Type':<15}{'Time(us)':<15}{'Comparisons':<15}")

for size in sizes:

    # Integer Dataset
    int_data = list(range(size))
    target_int = int_data[size // 2]

    start = time.perf_counter()
    _, int_comp = binary_search_int(int_data, target_int)
    int_time = (time.perf_counter() - start) * 1_000_000

    print(f"{size:<12}{'Integer':<15}{int_time:<15.3f}{int_comp:<15}")

    # Float Dataset
    float_data = [float(i) + 0.5 for i in range(size)]
    target_float = float_data[size // 2]

    start = time.perf_counter()
    _, float_comp = binary_search_float(float_data, target_float)
    float_time = (time.perf_counter() - start) * 1_000_000

    print(f"{size:<12}{'Float':<15}{float_time:<15.3f}{float_comp:<15}")

print("-" * 80)