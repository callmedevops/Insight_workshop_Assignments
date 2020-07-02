# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
lst = [("Miss", "Aqua", 16), ("Harry", "Springfield", 11), ("Larry", "Summerfield", 20), ("Barrel", "Titor", 15)]
age_list = [lst[i][2] for i in range(len(lst))]
avg = sum(age_list) / len(lst)
age_description = ["Young" if i < avg else "Old" for i in age_list]
print(lst)
for i in range(len(lst)):
    lst[i] = list(lst[i])
    lst[i][2] = age_description[i]
    lst[i] = tuple(lst[i])
print(lst)
