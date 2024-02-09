
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge(arr, left, middle, right):
    left_copy = arr[left:middle + 1]
    right_copy = arr[middle + 1:right + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        sorted_index = sorted_index + 1

    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

    return arr


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            middle = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, middle, end)
        size *= 2

    return arr

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
    timsort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Tim Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds") '''
