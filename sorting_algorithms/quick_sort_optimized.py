#Quick sort implementation - Pivot is placed on the middle element, Array is Divided instead of partitioning

def quick_sort_optimized(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort_optimized(left) + middle + quick_sort_optimized(right)
