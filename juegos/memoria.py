from random import randint
def memoria():
    N=int(input('Elige el nivel del desafío: '))
    print('Memoriza la siguiente secuencia: ')
    sec=''
    for i in range(N):
        num=randint(0,9)
        sec+=str(num)+' '
    sec=sec[:-1]
    print(sec)
    print('Ahora repite la secuencia')
    resp=input()
    if resp==sec:
        print('Felicidades! Has acertado')
    else:
        print('Incorrecto :c')

    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
