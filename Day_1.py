#  Linear Search

def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#  Binary Search

def BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1