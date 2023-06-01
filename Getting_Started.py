import re

'''Getting Started with Python'''

#Exercise 1
'''Write a Python program that takes two numbers as input from the user and prints
their sum.'''
'''Escriba un programa en Python que tome dos números como entrada del usuario e imprima su suma.'''

def suma():
    n_1 = input("Digite el primer número: ")
    n_2 = input("Digite el segundo número: ")
    
    if re.match(r'^-?\d+(?:\.\d+)$', n_1):
        n_1 = float(n_1)
    elif n_1.isnumeric():
        n_1 = int(n_1)
    else:
        return 'Digite solo valores numéricos'
 
    if re.match(r'^-?\d+(?:\.\d+)$', n_2):
        n_2 = float(n_2)
    elif n_2.isnumeric():
        n_2 = int(n_2)
    else:
        return 'Digite solo valores numéricos'

    return  f'La suma es :{ n_1 + n_2 }'  
print(suma())


#Exercise 2
'''Create a Python program that converts a temperature from Fahrenheit to Celsius.
The user should enter the temperature in Fahrenheit, and the program should print
the equivalent temperature in Celsius.'''
'''Cree un programa en Python que convierta una temperatura de Fahrenheit a Celsius. 
El usuario debe ingresar la temperatura en Fahrenheit y el programa debe imprimir 
la temperatura equivalente en Celsius.'''

def temp():

    F = input("Digite en valor numérico, la tempetura en Fahrenheit: ")

    if re.match(r'^-?\d+(?:\.\d+)$', F):
        F = float(F)
    elif F.isnumeric():
        F = int(F)
    else:
        return 'Digite solo valores numéricos'

    Celsius = (F - 32)/1.8
    Celsius =round(Celsius, 2)
    return Celsius
print(temp())

