def binary_search(lst, item, first, last):
    if item not in lst:
        return "Not in list"
    mid = (first + last) // 2
    if lst[mid] == item:
        return mid
    elif lst[mid] > item:
        return binary_search(lst, item, first, mid - 1)
    else:
        return binary_search(lst, item, mid + 1, last)


number_list = [int(x) for x in input("Enter list of number separated by space ").split()]
n = int(input("Enter the item to search "))
print(f'Number list: {number_list}')
print(f'Index of {n} item: {binary_search(sorted(number_list), n, 0, len(number_list))}')
