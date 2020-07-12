def linear_search(lst, item):
    for i in lst:
        if i == item:
            return lst.index(i)


number_list = [int(x) for x in input("Enter list of number separated by space ").split()]
n = int(input("Enter the item to search "))
print(f'Number list: {number_list}')
print(f'The item {n} is in index {linear_search(number_list, n)}')
