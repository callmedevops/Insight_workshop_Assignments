# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.


def binary_search(lst, item, first, last):
    if item not in lst:
        return -1
    else:
        mid = (first + last) // 2
        if lst[mid] == item:
            print(mid)
            return mid
        elif lst[mid] > item:
            return binary_search(lst, item, first, mid)
        elif lst[mid] < item:
            return binary_search(lst, item, mid, last)


num_lst = [int(x) for x in input("Enter any Number list ").split()]
itemToBeSearched = int(input("Enter number to search "))
index = binary_search(sorted(num_lst), itemToBeSearched, 0, (len(num_lst)-1))
if index == -1:
    print("Number is not in list")
else:
    print(f'After sorting the number is in index {index}')
