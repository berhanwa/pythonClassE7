from sys import argv

# Created this function to open the input file and create the output file
def add_line_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line_num in range(len(lines)):
            file.write(f"/*{line_num}*/ {lines[line_num]}")

def main():
    if len(argv) == 3:
        input_file = argv[1]
        output_file = argv[2]

    else:
        input_file = input("Enter an input filename to read: ")
        output_file = input("Enter an output filename to create: ")

    add_line_numbers(input_file, output_file)
    print("The task is complete.")

    # for line in infile:
    #     # outfile.write(line)
    #     line_num += 1
    #     updated_lines = f"/*{line_num}*/ {line}\n"
    #     outfile.write(updated_lines)
    #     # outfile.write("/*"line_num"*/" line"\n", file=outfile)
    # infile.close()
    # outfile.close()

main()

