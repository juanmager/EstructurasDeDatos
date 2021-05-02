# Ejercicio 2
# Una canilla de una casa pierde agua de forma que todos los días pierde 2 gotas más que el día anterior. 
# Escribir una función recursiva que calcule cuantas gotas perderá la canilla el día N. El primer día solo perdía dos gotas.

def validatePositive(dias):
    if isinstance(dias, int) and dias > 0 and dias < 999:
        return dias
    else: 
        raise Exception("Solo se puede elegir numeros entre entre 0 y 999")


def gotasDia(dias):
    cantGotas = 0
    if dias == 1:
        cantGotas = 2
        
    else:
        cantGotas = 2 + gotasDia(dias-1)
    return cantGotas

dias = 5
print("En" , dias , "dias, cayeron: " + str((gotasDia(dias))))

    

    