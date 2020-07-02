# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed?
# Sort the list. What is the first item on the list? What is the second item on the list?

lst = ["Mary", "Steph", "Harry", "Larry", "Barry", "Aqua"]
print(lst)
id1 = id(lst)
print(f'Id of list {id1}')
lst.append("Garry")
print(lst)
id2 = id(lst)
print(f'Id of list after appending {id2}')
if id1 == id2:
    print("Id of list hasn't changed")
else:
    print("Id of list has changed")
lst.sort()
print(f'Sorted list = {lst}')
print(f'After sorting the first item is {lst[0]} and the second item is {lst[1]}')
