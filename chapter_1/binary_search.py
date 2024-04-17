def binary_search(target_list, target_value):
    '''this function performs a binary search on an array and returns the index of the target item'''

    low = 0
    high = len(target_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = target_list[mid]
        if guess == target_value:
            return mid
        if guess > target_value:
            high = mid - 1
        else:
            low = mid + 1
    return None
    

numbers = [0, 2, 4, 8, 10, 22, 45, 46, 77, 86, 90, 101, 200]
print(binary_search(numbers, 22))


def binary_search_recurse(arr, tar, start = 0, end = None):
    
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