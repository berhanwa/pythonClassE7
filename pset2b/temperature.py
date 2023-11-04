

def f_to_k(fahrenheit):
    fahrenheit = int(input())
    return (5/9(fahrenheit-32)+277.16)
# f_to_k()

# k= 5/9(fahrenheit-32)+277.16

print ('Input a Fahrenheit temperature to be converted:')
fahrenheit = int(input())
# print (fahrenheit + 'degrees Farenheit equals' + def f_to_k() + "degrees Kelvin")

print(str(fahrenheit) + ' degrees Fahrenheit equals ' + float(f_to_k(fahrenheit)) + ' degrees Kelvin')
