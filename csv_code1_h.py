import csv

# Reading CSV file where first row is column names manually
f = open('sample_h.csv')
try:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        print(dict(zip(header, row)))
finally:
    f.close()
