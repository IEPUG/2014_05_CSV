import csv

f = open('sample.csv')
try:
    reader = csv.reader(f)
    for row in reader:
        print(row)
finally:
    f.close()
