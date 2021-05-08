import matplotlib.pyplot as plt
import numpy as np 

# Ejercicio 2
# Escribir una función que recibe un arreglo de enteros por parámetro y lo retorna con el contenido desplazado
# una posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. 
# El último pasa a ser el primero.

# Luego, escribir un programa que cargue un arreglo con valores ingresados por el usuario y llame a la función con ese arreglo. 
# Mostrar el contenido del arreglo por pantalla, antes y después de la función.

def desplazarVectorDerecha(vector):
    nVector = len(vector)
    aux = vector[nVector-1]
    print(nVector)
    print(aux)
    for pos in reversed(range(1,nVector)):
        vector[pos] = vector[pos - 1]
    vector[0] = aux


vectorete = np.array([1,10,100,1000,10000])

print(vectorete)
desplazarVectorDerecha(vectorete)
print(vectorete)
