import numpy as np

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

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
    quick_sort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Quick Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds")
'''