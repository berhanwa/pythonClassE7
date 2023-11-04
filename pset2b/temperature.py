

# def f_to_k(fahrenheit):
#     fahrenheit = int(input())
#     return (5/9(fahrenheit-32)+277.16)
# f_to_k()

print ('Input a Fahrenheit temperature to be converted:')
fahrenheit = int(input())

# kelvin= 5/9*(fahrenheit-32)+273.16
kelvin= (fahrenheit-32)*5/9+273.16

# print (fahrenheit + 'degrees Farenheit equals' + def f_to_k() + "degrees Kelvin")

# print(int(fahrenheit) + ' degrees Fahrenheit equals ' + kelvin + ' degrees Kelvin')

print(f'{fahrenheit}  degrees Fahrenheit equals {kelvin} degrees Kelvin')

