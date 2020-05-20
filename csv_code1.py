import csv

f = open('C:\Data\Python\IEPUG\CSV\sample.csv')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()
