input_file_name = input("Enter an input filename to read: ")
output_file_name = input("Enter an output filename to create: ")

def main():

    # Accesses the file that the user provided the name of
    infile = open (input_file_name, "r")
    outfile = open (output_file_name, "w")

    for line in infile:
        outfile.write(line)
        print(f'The sum of the args is: {result_sum}')

    infile.close()
    outfile.close()

main()
print("The task is complete.")
