'''Advanced Python Concepts'''

#Exercise 1
'''Write a Python class called BankAccount with methods for depositing, withdrawing,
and checking the account balance.'''
'''Escriba una clase de Python llamada BankAccount con métodos para depositar, retirar 
y verificar el saldo de la cuenta.'''

class BankAccount:
    '''
    Short description
    ---------------------
    Creé una clase con el atributo Saldo, que tiene sus respectivos métodos, 'depositing' y 'withdrawing'.
    ---------------------
    Methods
    ---------------------
    depositing(deposito: int) # En esta función se deposita el dinero del usuario y se guarda en self.balance. 
    withdrawing(retiro, int)  # En esta función se retira el dinero del usuario y se guarda en self.balance. 
    ---------------------
    Parameters
    ---------------------
    saldo = int
    ---------------------
    Notes:
    Esta clase se ejecuta solo con valores numéricos.
    ---------------------
    '''

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
    '''
    Short description
    ---------------------
    Creé una función para leer un archivo de texto. Utilicé 'with open()' y lo guardé en una variable.
    Convertí las palabras en minúscula.
    Y determiné que cuando la palabras tuvieran signos de puntuación al final o 
    al inicio, me trajeran las palabras sin los signos. Lo hice para que se realizara dos veces en la misma palabra, 
    porque venian dos signos de puntuación juntos en la misma palabra.
    ---------------------
    ---------------------
    Notes:
    Esta función se ejecuta solo para archivos de texto.
    ---------------------
    '''

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
# contar()
#comenté la función porque en la terminal no aparece la respuesta del primer ejercicio, cuando ambos se ejecutan.