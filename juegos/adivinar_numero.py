import random as ran
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    a = ran.randint(1,10)
    num = int(input("Escoge un numero del 1 al 10: "))
    if num == a:
        print("Adivinaste Correctamente!!")
    else:
        print("Perdiste :c")
        print("El número correcto era",a)
