import csv
# source [https://docs.python.org/3/library/csv.html#examples]

filename = "data/person.csv"
with open(filename, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
