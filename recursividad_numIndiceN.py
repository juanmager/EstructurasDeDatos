# Ejercicio 4
# Escribir una función recursiva que calcule el número triangular de índice N. 
# El número triangular de índice N es la suma de todos los números desde 1 hasta N.
# Algunos ejemplos:
# T(1) = 1
# T(2) = 1 + 2
# T(3) = 1 + 2 + 3
# T(4) = 1 + 2 + 3 + 4
# T(5) = 1 + 2 + 3 + 4 + 5
# ...
# T(N) = 1 + 2 + 3 + 4 + ... + N

def numTriangular(num):
    if num == 1:
        return 1

    else:
        return num + numTriangular(num-1)

print(numTriangular(5))
