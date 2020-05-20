import csv

f_in = open('C:\Data\Python\IEPUG\CSV\sample.csv')
f_out = open('C:\Data\Python\IEPUG\CSV\output.csv', 'w')

try:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out, delimiter='|', quotechar='$', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        writer.writerow( (row[0], int(row[3])) )

finally:
    f_out.close()
    f_in.close()

print open('C:\Data\Python\IEPUG\CSV\output.csv').read()
