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