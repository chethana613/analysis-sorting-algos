def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result
'''
# Test cases
test_cases = {
    "Small Array": np.random.randint(0, 100, 100),
    "Medium Array": np.random.randint(0, 1000, 1000),
    "Large Array": np.random.randint(0, 10000, 10000)
}

# Perform sorting and measure time
for case_name, case_data in test_cases.items():
    start_time = time.time()
    merge_sort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Merge Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds")
    '''
