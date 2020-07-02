# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

lst = ["Mary", "Steph", "Harry", "Larry", "Barry", "Aqua", "Tarry", "Cary"]

for i in lst:
    if i == "John":
        status = True
        break
    else:
        status = False

if status:
    print("Name Found")
else:
    print("Not Found")