import csv

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        print('Employee', row['FirstName'], row['LastName'], 'has manager', row['Manager'])
