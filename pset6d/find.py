keyword_name = input("Enter a keyword to search for: ")
input_file_name = input("Enter a file to search it in: ")

# Accesses the file that the user provided the name of
f = open (input_file_name, "r")

# Initialized the line and number_of_line variables
line = f.readline()
number_of_line = 0

# In the while loop where the length of the file isn't empty, it's checking which line the keyword is on and if it's found on a line, it gets printed out
while len(line) != 0:
    if keyword_name in line:
        number_of_line += 1
        print (input_file_name,':', '\t', line, end='')
    line = f.readline()

f.close()
