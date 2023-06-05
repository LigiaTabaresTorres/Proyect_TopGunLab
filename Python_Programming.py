'''Python Programming Best Practices'''

# Exercise 1
'''Write a Python function called is_palindrome that checks if a given word is a palindrome. 
The function should have proper error handling and be tested with
unittest'''
'''Escriba una función de Python llamada is_palindrome que verifique si una palabra dada es un palíndromo.
La función debe tener un manejo de errores adecuado y probarse con
prueba de unidad'''

def is_palindrome(word):
    '''
    Short description
    ---------------------
    Un Palindromo, es una palabra o frase que se lee igual en un sentido y en el otro.
    Se lee igual de izquierda a derecha que de derecha a izquierda.
    ---------------------

    Parameters
    ---------------------
    word : 'Str'
    ---------------------

    Notes:
    El manejo de errores probado con unittest, está en el archivo Test_PP.py.
    
    '''

    word = word.lower()
    size = len(word)
    word_1 = ''

    for i in range(1, size + 1):
        word_1 += word[i*-1]

    if word == word_1:
        return f"Es un palindromo=>, {word_1}"
    else: 
        return f"No es un palindromo =>, {word}"

n = is_palindrome('Ana')
print(n)



# Exercise 2
'''Create a Python decorator called timer that measures the time taken to execute a
function. Use this decorator on a function that sorts a list of random numbers and
prints the sorted list.'''
'''Cree un decorador de Python llamado temporizador que mida el tiempo necesario para ejecutar una función. 
Utilice este decorador en una función que ordene una lista de números aleatorios e imprima la lista ordenada'''

import time

def temporizador(func):
    '''
    Short description
    ---------------------
    La decorador llamado 'temporizador', se usó en una función, para medir el tiempo necesario
    en la ejecución de dicha función, que ordena una lista de números y la imprime de manera ordenada.  
    ---------------------

    Parameters
    ---------------------
    *args
    **Kwargs
    --------------------
    Notes:
    Deje el parámetro **Kwargs, por si se quiere trabajar un diccionario.
    
    '''
    def Tiempo(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo de ejecución: {func.__name__}: {tiempo_total} segundos")
        return resultado
    return Tiempo

@temporizador
def ordenar(lista):
    lista.sort()
    print(f"Lista ordenada: {lista}")

# Ejemplo 
lista_numeros = [5, 2, 8, 1, 9, 3, 10, 15, 6, 11, 16, 22, 18, 30, 35, 19, 7]
ordenar(lista_numeros)
