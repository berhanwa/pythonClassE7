##### The lorem.txt file is what I used to test as the input file and I created new_lorem.txt as the output result of this program #####

from sys import argv

# Created this function to open the input file and create the output file with the formatting required
def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line_num in range(len(lines)):
            file.write(f"/*{line_num}*/ {lines[line_num]}")

# Here, ensured that three arguments are passed in the command line and if not, the program prompts users to enter the files in order to proceed
def main():
    if len(argv) == 3:
        input_file = argv[1]
        output_file = argv[2]

    else:
        input_file = input("Enter an input filename to read: ")
        output_file = input("Enter an output filename to create: ")

    add_line_numbers(input_file, output_file)
    print("The task is complete.")


main()
