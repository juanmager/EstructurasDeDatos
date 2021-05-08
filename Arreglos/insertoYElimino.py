# Ejercicio 3
# Desarrollar una función que inserte un elemento en un arreglo de enteros dada la posición de inserción. 
# Al insertar un elemento en una posición, se produce un desplazamiento a la derecha, si el arreglo estaba lleno,
#  el último elemento se pierde.

## vector = [1 2 4 5 3]
##Insertamos el 10 en la posicion 1
## vector = [1 10 2 4 5]

import matplotlib.pyplot as plt
import numpy as np 

def insertoYElimino(vector):
    # numInsertar = int(input("Ingrese el numero deseado: "))
    # numPosicion = int(input("Ingrese posicion: "))
    numInsertar = 333
    numPosicion = 2
    sVector = len(vector)
    for pos in reversed(range(numPosicion, sVector)):
        vector[pos] = vector[pos-1]
    vector[numPosicion] = numInsertar


vectorchu = np.array([2,20,200,2000,20000])
print(vectorchu)
insertoYElimino(vectorchu)
print(vectorchu)

