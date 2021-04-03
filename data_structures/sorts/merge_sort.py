def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		arrays_left = arr[:mid]
		arrays_right = arr[mid:]
		merge_sort(arrays_left)
		merge_sort(arrays_right)


	#Merge
		i=0
		j=0
		index=0

		while i < len(arrays_left) and j < len(arrays_right):
			if arrays_left[i] < arrays_right[j]:
				arr[index] = arrays_left[i]
				i += 1
				index += 1
			else:
				arr[index] = arrays_right[j]
				j += 1
				index += 1

		while i < len(arrays_left):
			arr[index] = arrays_left[i]
			i += 1
			index += 1

		while j < len(arrays_right):
			arr[index] = arrays_right[j]
			j += 1
			index += 1

def print_array(array):
	for i in range(len(array)):
		print(array[i], end=" ")
	print()



if __name__ == '__main__':
	array = [20, 2, 10, 0, 55, 6, 9, 8, 7, 4, 0, 3, -5]
	print_array(array)
	merge_sort(array)
	print("Sorted array is: ")
	print_array(array)


