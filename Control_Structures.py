import re
'''Control Structures and Loops'''

#Exercise 1
'''Write a Python program that prints the first 10 Fibonacci numbers using a loop.'''
'''Escriba un programa en Python que imprima los primeros 10 números de Fibonacci usando un bucle'''

def func(n):
    a = 0
    b = 0
    for i in range(1, n):
        if i == 1:
            a += 1
            print(a)
        elif i == 2:
            b += 1
            print(b)
        else:
            c = a
            a = a + b
            b = c
            print(a)
func(10)


# a = 1
# b = 1
# a = a + b = 2
# c = a

# a = 2
# c = a = 1
# a = a + b = 2 + 1 = 3
# b = c = 1



#Exercise 2
'''Create a Python program that checks if a given number is prime or not. The user
should input a number, and the program should print whether it is prime or not.'''
'''Cree un programa en Python que verifique si un número dado es primo o no. 
El usuario debe ingresar un número y el programa debe imprimir si es primo o no.'''

def primo():

    num = input('Digite un número: ')

    if num.isnumeric():
        b = int(num)
    else:
        return 'Digite solo valores numéricos'
    a = ''
    c = int(b/2)
    for i in range(2, c + 1):
        if b % i == 0:
            a = True
    if a:
        return f"El número {num} , no es un número primo. "
    else:
        return f"El número {num} , es un número primo. "
    
print(primo())
