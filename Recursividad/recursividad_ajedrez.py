# Problema del trigo en el tablero de ajedrez:
# Si se colocase sobre un tablero de ajedrez, un grano de trigo en el primer casillero, dos en el segundo, 
# cuarto en el tercero y asi sucesivamente, doblando la cantidad de granos en cada casilla 
# ¿Cuantos granos de trigo habría en el tablero en total al final? Resolver el problema con una función recursiva.#

def granosPorCasillero(casillero):
    cantGranos = 0
    if casillero == 1:
        cantGranos = 1

    else:
        cantGranos = 2 * granosPorCasillero(casillero-1)
    return cantGranos


print(granosPorCasillero(3))
