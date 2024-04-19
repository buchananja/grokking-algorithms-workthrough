# implementation with early return guard clause
def binary_search_1(arr, tar, left, right):
    '''recursively binary searches an array for target index'''

    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_search_1(arr, tar, left, mid - 1)
    else:
        return binary_search_1(arr, tar, mid + 1, right)
    

# implementation with late return guard clause
def binary_search_2(arr, tar, left, right):
    '''recursively binary searches an array for target index'''

    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            return binary_search_2(arr, tar, left, mid - 1)
        else:
            return binary_search_2(arr, tar, mid + 1, right)
    else:
        return -1


arr = [2, 4, 5, 9, 11]
print(binary_search_1(arr, 2, left = 0, right = len(arr) - 1))