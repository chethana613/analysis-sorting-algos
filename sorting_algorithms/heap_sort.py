#Heap sort implementation

def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapifying the root.
		heapify(arr, n, largest)


def heap_sort(arr):
	n = len(arr)

	# Building a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# Extracting elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

