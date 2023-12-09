import csv

# Here, initialized the ids dictionary which stores the employee names and ids, printed the header values and accessed the csv file
def employees():
    ids = {}
    id = 1
    print(f"Id,ManagerId,LastName,FirstName")

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        # Then, iterated through each row in the csv to assign the employee and manager names. For the employees, concatenated both names into the variable.
        for row in reader:
            employee_name = row['FirstName'] + ' ' + row['LastName']
            manager_name = row['Manager']

            # Assigned id to employee if that has already not been done so
            if employee_name not in ids:
                ids[employee_name] = id
                id += 1

            # And assigned id to manager_name if that hasn't been done either
            if manager_name != '':
                if manager_name not in ids:
                    ids[manager_name] = id
                    id += 1

                # Then printed a formatted result of employees with managers
                print(f"{ids[employee_name]}, {ids[manager_name]}, {row['FirstName']}, {row['LastName']}")

            else:
                # And printed a formatted result of employees without managers
                print(f"{ids[employee_name]}, , {row['FirstName']}, {row['LastName']}")

def main():
    employees()
main()
