# Write a function to write a comma-separated value (CSV) file. It should accept a filename and
# a list of tuples as parameters. The tuples should have a name, address, and age. The file
# should create a header row followed by a row for each tuple.
import csv


def write_in_csv(filename, list0):
    head_content = ('name', 'address', 'age')
    csvfile = open(filename, 'w', newline='')
    obj = csv.writer(csvfile)
    obj.writerow(head_content)
    obj.writerows(list0)
    csvfile.close()


lst = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
write_in_csv("data.csv", lst)
print("Task Completed")
