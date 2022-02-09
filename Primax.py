import csv

with open('input.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if row == ['0;0']:
            break
        print(row)     
