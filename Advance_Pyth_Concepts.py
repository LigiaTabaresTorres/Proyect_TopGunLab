'''Advanced Python Concepts'''

#Exercise 1
'''Write a Python class called BankAccount with methods for depositing, withdrawing,
and checking the account balance.'''
'''Escriba una clase de Python llamada BankAccount con métodos para depositar, retirar 
y verificar el saldo de la cuenta.'''

class BankAccount:
    balance = {}
    def __init__(self, saldo):
        self.saldo = saldo
        self.balance = {
            'Ingresos': 0,
            'Egresos': 0,
            'Saldo': self.saldo,
        }
    def depositing(self, deposito):
        self.balance['Ingresos'] += deposito
        self.saldo += deposito 
    def withdrawing(self, retiro):
        self.balance['Egresos'] += retiro
        self.saldo -= retiro 
        retiro -= self.saldo
    def checking(self):
        self.balance['Saldo'] += self.balance['Ingresos'] - self.balance['Egresos']
        return self.balance
    

a = BankAccount(600)
b = a.depositing(1000)
c = a.withdrawing(250)
d = a.checking()
print('*'*60)
print('******************** BANK ACCOUNT **************************')
print('*'*60)
print('*****', d,'****')
print('*'*60)


#Exercise 2
'''Create a Python program that reads a text file and counts the occurrences of each
word using a dictionary. The program should print the words and their counts.'''
'''Cree un programa de Python que lea un archivo de texto y cuente las ocurrencias de cada palabra usando un diccionario. 
El programa debe imprimir las palabras y sus cuentas.'''

def contar():

    with open('./text.txt', 'r') as file:
        ocurrencias = {}
        var = ['.', ',', ';', ':', '"', '"']

        for linea in file:
            linea = linea.lower()
            palabras = linea.split()
            for palabra in palabras:
                if palabra[-1] in var:
                    palabra = palabra[:-1]
                    if palabra[-1] in var:
                      palabra = palabra[:-1]
                if palabra[0] in var:
                    palabra = palabra[1:]
                if palabra in ocurrencias:
                    ocurrencias[palabra] += 1
                else:
                    ocurrencias[palabra] = 1
            for palabra, cuenta in ocurrencias.items():
                print(f'{palabra}: {cuenta}')
contar()