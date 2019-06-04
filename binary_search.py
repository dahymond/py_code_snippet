def binary_search2(list, item):
   low = 0
   high = len(list)-1

   while low <= high:
       mid  = (low + high)
       guess = list[mid]

   if guess == item:
       return mid
   if guess > item:
       high = mid-1
   else:
       low = mid+1       
    #   mid = (low + high)
    #   guess = list(mid)

    #   if guess == item:
    #      return mid

    #   if guess > item:
    #      high = mid-1
    #   else:
    #      low = mid+1

   
   return None

   list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   print binary_search2(list1, 6)

# def binary_search(list, item):
#     low = 0
#     high = len(list)-1

#     while low <= high:
#         mid = low + high
#         guess = list[mid]

#         if guess == item:
#             return mid

#         if guess > item:
#             high = mid-1
#         else:
#             low = mid+1

#     return None 

# list2 = [1,2 ,3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78]

# print binary_search(list2, 56)
# print binary_search(list2, 199)
