class BubbleSort:
    """ BubbleSort Algorithm Implementation in Python 3.0+
        arr : Unorded list
        output : Return list in ascending order.
        time complexity : O(n2)
        Example :
        >>> sort = BubbleSort()
        >>> sort([4, 2, 6, 5, 9, 8])
        [2, 4, 5, 6, 8, 9]
    """

    def __init__(self):
        print("Bubble Sort Algorithm is Initialized")

    def __call__(self, arr):
        len_arr = len(arr)

		# Iterate over each element of arr and compare it to adjacent element.
		# For each loop one element of the arr is sorted.
        for outer in range(len_arr):
            already_sorted = True # Let arr is sorted.
			
			# Iterate over each element in the unsorted arr.
            for inner in range(len_arr - outer - 1): # compare the adjacent elements in arr.
                if arr[inner] > arr[inner + 1]: # if adjacent elements are not sorted then 
					# swap those elements and make already_sorted to be false.
                    arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
                    already_sorted = False
			# if any swap does not happen , means the arr is sorted and break out of outer loop
            if already_sorted:
                break
        return arr


sort = BubbleSort()
print(sort([10, 9, 5, 11, 2]))