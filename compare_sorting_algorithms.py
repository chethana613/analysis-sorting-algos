import numpy as np
import time
import matplotlib.pyplot as plt
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.quick_sort_optimized import quick_sort_optimized
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.bucket_sort_optimized import bucket_sort_optimized
from sorting_algorithms.bucket_sort import bucket_sort
from sorting_algorithms.tim_sort import tim_sort

def generate_test_arrays(criteria, n):
    test_arrays = []
    if criteria == 1:
        test_arrays.append(np.random.randint(0, n, n))
    elif criteria == 2:
        test_arrays.append(np.random.randint(0, 1000, n))
    elif criteria == 3:
        test_arrays.append(np.random.randint(0, n**3, n))
    elif criteria == 4:
        test_arrays.append(np.random.randint(0, int(np.log(n)), n))
    elif criteria == 5:
        test_arrays.append(np.arange(0, n)*1000)
    elif criteria == 6:
        arr = np.arange(0, n)
        indices_to_swap = np.random.choice(n, size=int(np.log(n)/2), replace=False)
        for i in range(len(indices_to_swap)):
            j = np.random.randint(0, n)
            arr[indices_to_swap[i]], arr[j] = arr[j], arr[indices_to_swap[i]]
        test_arrays.append(arr)
    return test_arrays

# Define criteria
criteria = {
    "Rand Int[0...n]": 1,
    "Rand Int[0...1000]": 2,
    "Rand Int[0...n^3]": 3,
    "Rand Int[0...log n]": 4,
    "Rand Int(Multiples of 1000) [0...n]": 5,
    "In-order Integers": 6,
}

sorting_algorithms = {
    "Quick Sort": quick_sort,
    "Quick Sort - Optimized": quick_sort_optimized,
    "Heap Sort": heap_sort,
    "Merge Sort": merge_sort,
    "Radix Sort": radix_sort,
    "Bucket Sort": bucket_sort,
    "Bucket Sort - Optimized": bucket_sort_optimized,
    "TimSort": tim_sort,
}

optimized_sorting_algorithms = {
    "Quick Sort - Optimized": quick_sort_optimized,
    "Heap Sort": heap_sort,
    "Merge Sort": merge_sort,
    "Radix Sort": radix_sort,
    "Bucket Sort - Optimized": bucket_sort_optimized,
    "TimSort": tim_sort,
}

def compare_algorithms(algorithms, input_sizes):
    # Run sorting algorithms and measure execution time
    execution_times = {algo_name: {criterion_name: [] for criterion_name in criteria} for algo_name in algorithms}

    for algo_name, sorting_algo in algorithms.items():
        print("******************" + str(algo_name) + "******************")
        for criterion_name, criterion_value in criteria.items():
            for n in input_sizes:
                test_arrays = generate_test_arrays(criterion_value, n)
                start_time = time.time()
                for test_array in test_arrays:
                    sorting_algo(test_array.copy())
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(criterion_name +":"+ str(elapsed_time))
                execution_times[algo_name][criterion_name].append(elapsed_time)

    # Plotting
    plt.figure(figsize=(16, 10))
    plot_index = 1

    for criterion_name in criteria:
        plt.subplot(3, 3, plot_index)
        for algo_name in algorithms:
            plt.plot(input_sizes, execution_times[algo_name][criterion_name], label=algo_name)
        plt.title(criterion_name)
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time (seconds)')
        plt.legend()
        plt.grid(True)
        plot_index += 1

    plt.tight_layout()
    plt.show()

# input_sizes = [1000, 5000, 7500]
# compare_algorithms(sorting_algorithms, input_sizes)

input_sizes = [250000,500000,750000,1000000]
compare_algorithms(optimized_sorting_algorithms, input_sizes)