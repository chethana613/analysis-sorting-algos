def bucket_sort(arr):
    # Determine the range of values in the input array
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value

    # Define the number of buckets
    num_buckets = len(arr)  # Adjust the number of buckets as needed

    # Create buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        # Calculate the index for each element
        if range_of_values != 0:
            index = int((num - min_value) / (range_of_values) * (num_buckets - 1))
        else:
            index = 0
        buckets[index].append(num)

    # Sort each bucket and concatenate them
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

'''
# Test cases
test_cases = {
    "Small Array": np.random.rand(100),
    "Medium Array": np.random.rand(1000),
    "Large Array": np.random.rand(10000)
}

# Perform sorting and measure time
for case_name, case_data in test_cases.items():
    start_time = time.time()
    bucket_sort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Bucket Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds")
'''