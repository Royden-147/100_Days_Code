def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    mer = []
    a = b = 0

    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            mer.append(left[a])
            a += 1
        else:
            mer.append(right[b])
            b += 1

    mer.extend(left[a:])
    mer.extend(right[:b])
    return mer

# quick sort

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    x = arr[0]
    l = [a for a in arr[1:] if a <= x]
    g = [a for a in arr[1:] if a > x]

    return quicksort(l) + x + quicksort(g)

