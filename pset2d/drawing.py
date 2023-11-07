# First, I recreated the shape for both top and bottom definitions with '.'s in place of blank spaces to visualize them (down below)
# And to print out the actual \s on the right side of the shape, I had to place them twice so they won't be disregarded
def top ():
    print ("  _______  ")
    print (" /       \\ ")
    print ("/         \\")

def bottom ():
    print ("\\         /")
    print (" \\       / ")
    print ("  _______  ")

# Here, I included \s because I was getting an error without them. I believe \ makes the print statement view the -s as text
def mid ():
    print ("-\"-\'-\"-\'-\"-")

def main ():
    top ()
    mid ()
    bottom ()
main ()



# def top ():
#     print (".._______..")
#     print ("./.......\\.")
#     print ("/.........\\")
# top ()

# def bottom ():
#     print ("\\........./")
#     print (".\\......./.")
#     print (".._______..")
# bottom ()
