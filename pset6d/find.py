
keyword_name = input("Enter a keyword to search for: ")
input_file_name = input("Enter a python file to search it in: ")

f = open (input_file_name, "r")

line = f.readline()

while len(line) != 0:
    if keyword_name in line:
        print (line, end='')
    line = f.readline()

f.close()

