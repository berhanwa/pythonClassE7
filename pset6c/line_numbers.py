from sys import argv

def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        lines = file.readlines()
            file.write(f"/*{line_num}*/ {lines[line_num]}")

def main():
    if len(argv) == 3:
        input_file = argv[1]
        output_file = argv[2]

    else:
        
    line_num = 0

    for line in infile:
        # outfile.write(line)
        line_num += 1
        updated_lines = f"/*{line_num}*/ {line}\n"
        outfile.write(updated_lines)
        # outfile.write("/*"line_num"*/" line"\n", file=outfile)
    infile.close()
    outfile.close()

main()

print("The task is complete.")


    # Accesses the file that the user provided the name of
    # infile = open (input_file_name, "r")
    # outfile = open (output_file_name, "w")

# input_file_name = input("Enter an input filename to read: ")
# output_file_name = input("Enter an output filename to create: ")
