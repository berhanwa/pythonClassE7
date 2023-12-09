import csv

def employees():
    ids = {}
    id = 1
    print(f"Id,ManagerId,LastName,FirstName")

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)


        for row in reader:
            employee_name = row['FirstName'] + ' ' + row['LastName']
            manager_name = row['Manager']

            if employee_name not in ids:
                ids[employee_name] = id
                id += 1

            if manager_name != '':
                if manager_name not in ids:
                    ids[manager_name] = id
                    id += 1

                print(f"{ids[employee_name]}, {ids[manager_name]}, {row['FirstName']}, {row['LastName']}")

            else:
                print(f"{ids[employee_name]}, , {row['FirstName']}, {row['LastName']}")

def main():
    employees()
main()
