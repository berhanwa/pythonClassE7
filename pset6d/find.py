
keyword_name = input("Enter a keyword to search for: ")
input_file_name = input("Enter a file to search it in: ")

f = open (input_file_name, "r")

line = f.readline()
number_of_line = 0

while len(line) != 0:
    if keyword_name in line:
        number_of_line += 1
        print (input_file_name,':', '\t', line, end='')
    line = f.readline()

f.close()
