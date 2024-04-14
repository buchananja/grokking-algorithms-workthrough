def find_smallest_element(arr):
    '''returns the index of the smallest element in an array'''

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def find_largest_element(arr):
    '''returns the index of the largest element in an array'''

    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index


def selection_sort(arr, ascending = True):
    '''sorts an array in ascending/descending numerical order'''

    def find_extreme_element(arr, smallest = True):
        '''returns the index of the smallest/largest element in an array'''

        extreme_element = arr[0]
        extreme_index = 0
        for i in range(1, len(arr)):
            if smallest:
                if arr[i] < extreme_element:
                    extreme_element = arr[i]
                    extreme_index = i
            else:
                if arr[i] > extreme_element:
                    extreme_element = arr[i]
                    extreme_index = i
        return extreme_index


    sorted_arr = list()
    for i in range (len(arr)):
        if ascending:
            smallest = find_extreme_element(arr, smallest = True)
            sorted_arr.append(arr.pop(smallest))
        else:
            largest = find_extreme_element(arr, smallest = False)
            sorted_arr.append(arr.pop(largest))
    return sorted_arr


# code demonstration
numbers = [0, 2, 5, 6, 8, 2, 1]
print(f'\nSorted Array: {selection_sort(numbers)}')