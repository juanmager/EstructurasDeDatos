# Ejercicio 1
# Implementar una función que calcule el factorial de un número de forma recursiva

def validatePositive(num):
    if isinstance(num, int) and num > 0 and num < 999:
        return num
    else: 
        raise Exception("Solo se puede elegir numeros entre entre 0 y 999")

def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num-1)

num = 1
print("El factorial de:" , num , "es: " + str((factorial(num))))