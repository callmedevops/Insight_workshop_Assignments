def binary_search(lst, item, low, high):
    if item not in lst:
        return "Not in list"
    pos = low + int(((item - lst[low]) * (high - low) / (lst[high] - lst[low])))
    if lst[pos] == item:
        return pos
    elif lst[pos] > item:
        return binary_search(lst, item, low, pos - 1)
    else:
        return binary_search(lst, item, pos + 1, high)


number_list = [int(x) for x in input("Enter list of number separated by space ").split()]
n = int(input("Enter the item to search "))
print(f'Number list: {number_list}')
print(f'Index of {n} item: {binary_search(sorted(number_list), n, 0, len(number_list) - 1)}')
