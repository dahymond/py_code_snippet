def binary_search(list, item):
    low  = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
             low = mid + 1
    return None            


random_num = [23,24,35,45,46,47,55,56,57,75]

print binary_search(random_num, 46)