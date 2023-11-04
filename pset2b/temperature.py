# Made the program start by asking users to enter the f value, assign an input to the response
print ('Input a Fahrenheit temperature to be converted:')
fahrenheit = int(input())

# Then writing in the calculation portion and assigning it the value kelvin, to then print the conversion down below.
kelvin= (fahrenheit-32)*5/9+273.16

# Took me a while, but I realized I needed to place the values within {}s and that I didn't need to explicitly concatenate them with the strings by a + symbol.
print(f'{fahrenheit}  degrees Fahrenheit equals {kelvin} degrees Kelvin')
