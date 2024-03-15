import random as r
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    com = r.randint(0,2)
    eleccion = ["piedra","papel","tijera"]
    player = int(input("Elige una opción (0 = Piedra, 1 = Papel, 2 = Tijera): "))
    if com == player:
        print("Empate! Los dos escogieron",eleccion[com])
    elif (com == 0 and player == 1) or (com == 1 and player == 2) or (com ==2 and player == 1):
        print("Has Ganado!! El computador eligió",eleccion[com])
    else:
        print("Perdiste :c El computador eligió",eleccion[com])
