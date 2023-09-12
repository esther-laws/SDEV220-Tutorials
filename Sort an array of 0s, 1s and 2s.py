def sort012(arr, N):
    low = 0  # Initialize a pointer for 0
    high = N - 1  # Initialize a pointer for 2
    mid = 0  # Initialize a pointer for 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage:
arr = [0, 1, 2, 0, 1, 2]
N = len(arr)
sort012(arr, N)
# Output should be [0, 0, 1, 1, 2, 2]
print(arr)  