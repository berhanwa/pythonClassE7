import csv

# Here, initialized the ids dictionary which stores the employee names and ids, assigned the id variable with an initializing value, printed the header values and accessed the csv file as a dictionary
def employees():
    ids = {}
    id = 1
    print(f"Id,ManagerId,LastName,FirstName")

    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)

        # Then, iterated through each row in the csv to gather the employee and manager names. For the employees, concatenated both names into the variable to get their full names.
        for row in reader:
            employee_name = row['FirstName'] + ' ' + row['LastName']
            manager_name = row['Manager']

            # Assigned id to employee if that has already not been done so, and if found, assigns an id to their name and incremented the id counter
            if employee_name not in ids:
                ids[employee_name] = id
                id += 1

            # And assigned id to manager_name if that hasn't been done either and if found, assigns an id to their name and incremented the id counter
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
