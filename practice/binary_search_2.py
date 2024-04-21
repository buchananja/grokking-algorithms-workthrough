def binary_search(arr, tar, left = 0, right = None):
    '''performs recursive binary search on an array'''

    # sets right to end of array
    if right is None:
        right = len(arr) - 1
    # ensures invalid index returned if target not found
    if left > right:
        return -1
    # recursively searches for target
    mid = (left + right) // 2
    if arr[mid] == tar:
        return mid
    elif arr[mid] < tar:
        return binary_search(arr, tar, mid + 1, right)
    else:
        return binary_search(arr, tar, left, mid - 1)


arr = [0, 1, 2, 7, 10]
print(binary_search(arr, 1))