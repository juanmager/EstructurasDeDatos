# Ejercicio 3
# Implementar una función recursiva que calcule los números de la serie de Fibonacci. 
# La función para generar la serie de Fibonacci es la siguiente (donde N es el índice 
# del número en la serie):
# alt text
# Luego escribir un programa que pida un número N (mayor o igual a 0) al usuario e imprima por 
# pantalla los primeros N números de la serie de Fibonacci
# Sobre la sucesion de Fibonacci:
#  https://www.vix.com/es/btg/curiosidades/4461/que-es-la-sucesion-de-fibonacci

def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
       return 1

    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(9))

repeats = int(input("Ingrese un numero entero positivo: "))
for x in range(repeats):
    print(fibonacci(x))
