# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.
from operator import itemgetter

lst = [("Karuna", "Shrestha", 18)]
lst.append(("Miss", "Aqua", 100))
lst.append(("Harry", "Springfield", 11))
lst.append(("Larry", "Summerfield", 20))
lst.append(("Barrel", "Titor", 35))
print(lst)
lst.sort(key=itemgetter(2))
print(f'After Sorting list by age(third item) = {lst}')
