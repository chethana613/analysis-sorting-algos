#Quick sort implementation - Pivot is placed on the last element

import sys
sys.setrecursionlimit(10**6)
def partition(array, low, high):

	pivot = array[high]

	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1

def quicksort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quicksort(array, low, pi - 1)
		quicksort(array, pi + 1, high)
		
def quick_sort(array):
	return quicksort(array, 0, len(array)-1)
