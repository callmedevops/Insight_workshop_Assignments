# Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names,
# and each subsequent row as values for those keys.
import csv

result_list = []


def read_csv(filename):
    csvfile = open(filename, 'r', newline='')
    obj = csv.DictReader(csvfile)
    for row in obj:
        result_list.append(dict(row))
    print(result_list)


read_csv("data.csv")
