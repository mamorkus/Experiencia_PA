"""
Esta función representa el juego de adivinar si un número es par o impar.
Tienes que permitir que el usuario ingrese una de las dos opciones y
generar un número aleatorio para ver si es par o impar.
Se debe mostrar si el usuario adivina correctamente o no.
"""
import random

def adivinar_par_o_impar():
    number = random.randint(1,100)
    print(number)
    x = input('¿Es par o impar? ')

    if number % 2 == 0:                       # par
        if x == 'par':
            print('Muy bien, es par')
        elif x == 'impar':
            print('Muy mal, es impar')
    else:                                     # impar
        if x == 'impar':
            print('Muy bien, es impar')
        elif x == 'par':
            print('Muy mal, es par')