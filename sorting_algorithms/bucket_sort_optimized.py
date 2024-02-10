def bucket_sort_optimized(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value

    num_buckets = len(arr) 

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        if range_of_values != 0:
            index = int((num - min_value) / (range_of_values) * (num_buckets - 1))
        else:
            index = 0
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key