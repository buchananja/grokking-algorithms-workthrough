def quicksort(arr):

    def partition(arr, low, high):
        '''partitions array about a pivot'''
        
        # set i to be before first element and pivot at end
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            # increment i and swap i & j if j <=pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]



    if len(arr) < 2:
        return arr
    
    
