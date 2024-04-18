def sum_array(arr):
    '''recursively calculates the sum of an array'''

    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])
    
    
def count_recurse(arr):
    '''recusively calculated the count of an array'''

    if len(arr) == 0:
        return 0
    return 1 + count_recurse(arr[1:])
    

def max_recurse(arr):
    '''recusively calculated the maximum value of an array'''
    
    if len(arr) == 0:
        return 0
    return max(arr[0], max_recurse(arr[1:]))


def binary_search_recurse(arr, tar, start = 0, end = None):
    '''recursively halves the length of an array in search of a target'''
    
    if end is None:
        end = len(arr) - 1
    if start > end:
        return None
    mid = (start + end) // 2
    
    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_search_recurse(arr, tar, start, mid - 1)
    else:
        return binary_search_recurse(arr, tar, mid + 1, end)
    
    
def partition(arr, low_index, high_index):
    '''partitioning with end element as pivot'''
    
    # set i to be one less than beginning and pivot to last element
    i = low_index - 1
    pivot = arr[high_index]
    
    # when j is less/equal to pivot, increment i then swap i and j values
    for j in range(low_index, high_index):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # swaps i+1 with pivot
    arr[i + 1], arr[high_index] = arr[high_index], arr[i + 1]
    return (i + 1)


def quicksort(arr, low_index = 0, high_index = None):
    '''quicksort algorithm with end index sorting in-place'''
    
    if high_index is None:
        high_index = len(arr) - 1

    if low_index < high_index:
        pivot_index = partition(arr, low_index, high_index)
        quicksort(arr, low_index, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high_index)

arr = [2, 1, 4, 3, 6, 8, 5, 9, 0, 7]
quicksort(arr)        
print(arr)