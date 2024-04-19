# this method sorts in-place
def selection_sort(arr, ascending = True):
    '''performs a selection sort on an array'''

    def find_extreme(arr, start, largest):
        '''finds the smallest/largest number in array''' 

        ext_value = arr[start]
        ext_index = start

        for i in range(start + 1, len(arr)):
            if largest:
                if arr[i] > ext_value:
                    ext_value = arr[i]
                    ext_index = i
            else:
                if arr[i] < ext_value:
                    ext_value = arr[i]
                    ext_index = i 
        return ext_index
   
    # outer loop iterates over original array index
    for i in range(len(arr)):
        # inner loops iterate over unsorted remaining array
        if ascending:
            ext_val_index = find_extreme(arr, i, largest = False)
        else:
            ext_val_index = find_extreme(arr, i, largest = True)
        # swaps extreme value in place of i 
        (arr[i], arr[ext_val_index]) = (arr[ext_val_index], arr[i])


# this method returns a new array
def selection_sort(arr, ascending = True):
    '''performs a selection sort on an array'''

    def find_extreme(arr, largest = True):
        '''finds the smallest/largest number in array'''

        ext_value = arr[0]
        ext_index = 0

        for i in range(1, len(arr)):
            if largest:
                if arr[i] > ext_value:
                    ext_value = arr[i]
                    ext_index = i
            else:
                if arr[i] < ext_value:
                    ext_value = arr[i]
                    ext_index = i 
        return ext_index

    # outer loop iterates over original array index
    sorted = list()
    for i in range(len(arr)):
        # inner loops iterate over unsorted remaining array
        if ascending:
            ext_val = find_extreme(arr, largest = False)
            sorted.append(arr.pop(ext_val))
        else:
            ext_val = find_extreme(arr, largest = True)
            sorted.append(arr.pop(ext_val))
    return sorted