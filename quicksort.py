def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot =  array[0]
        less = [i for i in array[1:] if  i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10,5,2,3,4,5,67,46, 57,57,68,5757])        

print quicksort([23,34,64,2,13,46,757,57,42])