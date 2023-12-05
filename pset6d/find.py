
keyword_name = input("Enter a keyword to search for: ")
input_file_name = input("Enter a python file to search it in: ")

f = open (input_file_name, "r")

line = f.readline()

while len(line) != 0:
    if keyword_name in line:
        print (line, end='')
    # else:


# def main():

#     # Opens the file and then saves the external text in this program as input_text
#     with open('romeo_and_juliet_data.txt', 'r') as f:
#         input_text = f.readlines()
