# Was a bit of trial and error, but I took my learnings from the temp assignment and added the f'{}' within the print statement
# Assigned the data type of int to the studs response
# Also defined the teaching assistants separately and used // instead of %
# Lastly, I corrected the syntax error on the print by making the P lowercase and corrected the mismatched "'s in the print statement
def main():
    print ('How many students are enrolled?')
    studs = int(input())
    tf = (studs)//15
    print ('We need' " " f'{studs//15} teaching assistants')
main()
