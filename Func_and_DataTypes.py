'''Functions and Data Types'''

#Exercise 1
'''Write a Python function called find_maximum that takes a list of numbers as input
and returns the maximum number from the list.'''
'''Escriba una función de Python llamada find_maximum que tome una lista de números como entrada 
y devuelva el número máximo de la lista'''

def find_maximum(n):
    '''
    Short description
    ---------------------
    Hice una función que duelve el valor máximo de una lista.
    Utilicé pop, que es un método especifico para las listas.
    ---------------------
    Parameters
    ---------------------
    n = list
    ---------------------
    Notes:
    Esta función se ejecuta solo para listas.
    ---------------------
    '''
    if len(n) > 1:
        if n[0] > n[-1]:
            return find_maximum(n[0:-1])
        elif n[0] < n[-1]:
            return find_maximum(n[1:])
        else:
            n.pop(-1)
            return find_maximum(n)
    return n[-1]
        
print(find_maximum([1, 2, 3, 55, 66, 88, 99, 6464, 1, 65, 65]))


#Exercise 2
'''Create a Python function called reverse_string that takes a string as input and returns
the reversed string.'''
'''Cree una función de Python llamada cadena_reversa que tome una cadena como entrada y devuelva la cadena invertida'''

def cadena_reversa(string):
    '''
    Short description
    ---------------------
    Hice una función que duelve un cadena de texto invertida.
    Utilicé string[0 : -1], para determinar las posiciones dentro del string.
    ---------------------
    Parameters
    ---------------------
    string = 'str'
    ---------------------
    Notes:
    Esta función se ejecuta solo para strings.
    ---------------------
    '''
    if string == '':
        return ''
    else:
        return string[-1] + cadena_reversa(string[0 : -1])

print(cadena_reversa('Hola'))
