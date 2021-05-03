# Ejercicio 10
# En un edificio alto, las cucarachas se van distribuyendo por pisos de esta forma:

# En el primer piso hay una cucaracha
# En los pisos pares el doble del número de piso (por ejemplo en el piso 8 hay 16 cucarachas)
# El resto de los pisos tienen la suma de las cucarachas de los dos pisos anteriores.
# Escribir una función recursiva que calcule la cantidad de cucarachas en un edificio en función de la cantidad de pisos.

def cucasEnPiso(nPiso):
    nCucas = 0
    if nPiso == 1:
        nCucas = 1
    elif nPiso % 2 == 0:
        nCucas = nPiso * 2
    else:
        nCucas = cucasEnPiso(nPiso-1) + cucasEnPiso(nPiso-2)
    return nCucas


def cucasEnEdificio(nPisos):
    cucasTotales = 0
    if nPisos == 1:
        cucasTotales = 1
    else:
        cucasTotales = cucasEnPiso(nPisos) + cucasEnPiso(nPisos - 1)
    return cucasTotales
print(cucasEnEdificio(5))