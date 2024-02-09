
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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
    heap_sort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Heap Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds")
'''