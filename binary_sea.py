def binary_search(list, item):
    low = 0 
    high = len(list)-1


    while (low < high):
        mid = low + high
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1

        else:
             low = mid + 1

    return None



list = [1,2,3,4,5,6,7,8,9]
list1 = [ 12,13,14,35,46,54,56,57,57,346,347,654,655,787,789,889]

print binary_search(list, 5)
print binary_search(list1, 654)
print binary_search(list, 45)


# selection  and sorting using python
def  find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)

        newArr.append(arr.pop(smallest))

    return newArr, arr 
print selectionSort([34, 12, 34, 13, 53, 534, 45, 32, 13, 535, 53, 64])