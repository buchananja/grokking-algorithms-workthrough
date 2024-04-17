# 4.1
- Calculating the sum of an array in Python can be done recursively as follows:

def sum_array(arr):
    '''recursively calculates the sum of an array'''

    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])

- The sum_array function first checks if an array is empty and returns zero if
it is; empty arrays cannot be summed.
- Otherwise, the function takes the zero'th element and recursively calls
itself on the remainer of the array.
- This causes a series of array segments to be checked for length of zero, when
this evaluates to TRUE, the array has been exhausted and the base case is 
reached.
- The call stack has been loaded with recursive sum_array calls with decreasing
length segments of an array. Once the base case is reached, the recursion
unwinds and the summation of each call is added to the main returned sum,
giving the full summation of the array.


# 4.2
- Calculating the count of an array in Python can be done recursively as 
follows:

def count_recurse(arr):
    '''recusively calculated the count of an array'''

    if len(arr) == 0:
        return 0
    return 1 + count_recurse(arr[1:])


# 4.3
- Calculating the maximum value of an array in Python can be done recursively
as follows:

def max_recurse(arr):
    '''recusively calculated the maximum value of an array'''
    
    if len(arr) == 0:
        return 0
    return max(arr[0], max_recurse(arr[1:]))

- The function max_recurse accepts an array (list in python) as an argument 
with the intent of returning the maximum value.
- It first checks whether the array is empty and if it is returns zero. Else, 
the function calls itself recursively on the array's second element onwards 
(arr[1:]). This is encapsulated inside a maximum comparison that cascades 
recursively for each call. 
- Given array arr = [1, 2, 3], the resulting call stack of
max_number_array(arr) will be max(1, max(2, max(3, 0))) where 0 represents 
arr[1:] not existing, which is to say the base case has been reached as the 
len(arr) is zero. 
-The following comparison is made upon unwinding: 3 > 0, 3 > 2, and 3 > 1, as 
such the maximum value of the array is 3.


# 4.4
- Performing a binary search in Python can be fone recursively as follows:

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