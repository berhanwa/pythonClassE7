input_file_name = input("Enter a filename to read: ")
output_file_name = input("Enter a filename to send the previous file to: ")

def main():

    # Accesses the file that the user provided the name of
    infile = open (input_file_name, "r")
    outfile = open (output_file_name, "w")

    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()
