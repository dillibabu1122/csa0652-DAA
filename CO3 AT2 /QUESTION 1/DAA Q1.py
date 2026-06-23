
def binary_search(flights, target):
    low = 0
    high = len(flights) - 1

    while low <= high:
        mid = (low + high) // 2

        if flights[mid] == target:
            return mid
        elif target < flights[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
flight_records = [
    "AI101",
    "AI205",
    "AI310",
    "AI420",
    "AI525",
    "AI630",
    "AI740"
]
flight_number = input("Enter Flight Number to Search: ")
result = binary_search(flight_records, flight_number)
if result != -1:
    print(f"Flight {flight_number} found at index {result}.")
else:
    print(f"Flight {flight_number} not found.")