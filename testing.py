# print "Solomon"

# print "Hello World!"
# print "Hello you"

# def print_two(*args):
#     arg1, arg2 = args
#     print "arg1: %r, arg2: %r" %(arg1, arg2)


# def print_two_again(arg1, arg2):
#     print "arg1: %r, arg2: %r" % (arg1, arg2)

# def print_one(arg1):
#     print "arg1: %r" % arg1

# def print_none():
#     print "I got nothin"


# print_two("Zed", "Shaw")
# print_two_again("Solomon", "Sunday")
# print_one("Oluwafemi")
# print_none()

####binary search####

def binary_search(list, item):
   low = 0
   high = len(list)-1

   while low <= high:
      mid = (low + high)
      guess = list[mid]
      if guess == item:
          return mid
      if guess > item:
          high = mid-1
      else:
        low = mid + 1
   return None

my_list = [1, 3, 5, 7, 9, 12, 13, 25, 26, 27, 30, 34, 35, 37, 39, 40, 43]

print binary_search(my_list, 25)
print binary_search(my_list, -1)


###### Assignment ####

# def binary_search1(list, item):
#    low = 0
#    high = len(list)-1

#    while low <= high:
#        mid = low + high
#        guess = list[mid]
#        if guess == item:
#            mid = item
#        if guess < item:
#            low = mid + 1
#        else:
#             high = mid - 1

#    return None 

# list_main = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17, 23, 24, 25, 27]
# binary_search1(list_main, 13)


### for loop ###
# elements = []
# for i in range(0, 6):
#     print i

#     elements.append(i)


# for j in elements:
#     print j


#### assignment for-loop

# def binary_search2(list, item):
#    low = 0
#    high = len(list)-1

#    while low <= high:
#       mid = (low + high)
#       guess = list(mid)

#       if guess == item:
#          return mid
#       if guess > item:
#          high = mid - 1
#       else:
#          low = mid + 1
   
#    return None

#    list1 = [1,2,3,4,5,6,7,8,9]
#    print binary_search2(list1, 6)