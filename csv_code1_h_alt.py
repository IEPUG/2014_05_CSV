import csv

# Reading CSV file where first row is column names using DictReader
f = open('sample_h.csv')
try:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))
finally:
    f.close()
