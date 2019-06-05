def countdown(i):
    print i

    if i == 0:
        return
    else:
        countdown(i - 1)


print countdown(24)


def sum(arr):
    total = 0
    for i in arr:
        total += i

    return total    

print sum([1,2,3,4,5,678,9,9,0,23,34,3553,46,46,6868,979,42,2323,355])
