# Ejercicio 1
# Escribir un programa que le pida al usuario que ingrese 10 números enteros (primero uno, luego otro, 
# y así hasta que el usuario ingrese 10 numeros). 
# Al final, el programa debe imprimir los números que fueron ingresados en orden inverso, la suma total de los valores y el promedio.

import matplotlib.pyplot as plt
import numpy as np 

def diezNumeros():
    vector1 = np.zeros((10), int)

    for x in reversed((range(len(vector1)))):
        # np.append(vector1, int(input("Ingrese 10 numeros enteros: "))) // asi, no me agregaba los valores.
        vector1[x] = int(input("Ingrese 1 numero entero: "))
        print("En posicion: ", x)
        
    print(vector1)

    print("La suma de todos los elementos es: ", vector1.sum())
    print("El promedio de todos los elementos es: ", vector1.mean())


diezNumeros()