input_file_name = input("Enter an input filename to read: ")
output_file_name = input("Enter an output filename to create: ")

def main():

    # Accesses the file that the user provided the name of
    infile = open (input_file_name, "r")
    outfile = open (output_file_name, "w")

    line_num = 0

    for line in infile:
        # outfile.write(line)
        line_num += 1
        updated_lines = f"/*{line_num}*/ {line}\n"
        outfile.write(updated_lines, \n)
        # outfile.write("/*"line_num"*/" line"\n", file=outfile)
    infile.close()
    outfile.close()

main()

print("The task is complete.")
