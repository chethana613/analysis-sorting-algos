def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

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
    radix_sort(case_data.copy())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("********* Radix Sort ***********")
    print(f"{case_name}: {elapsed_time:.5f} seconds")
    '''
