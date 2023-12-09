import csv

def employees():
    ids = {}
    id = 1
    print(f"Id,ManagerId,LastName,FirstName")

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)


        for row in header:
            employee_name = row['FirstName'] + ' ' + row['LastName']
