from random import randint
def juego_del_dado():
    empezar=input('Apreta enter para lanzar el dado: ')
    s1=0
    s2=0
    if empezar=='':
        while s1<30 and s2<30:
            score=randint(0,10)
            s2+=score
            print('Obtuviste',score,'puntos')
            score=randint(0,10)
            s1+=score
            print('Obtuve',score,'puntos')
        if s2>=30:
            print('Has ganado!')
        elif s1>=30:
            print('Te gané')


    
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
