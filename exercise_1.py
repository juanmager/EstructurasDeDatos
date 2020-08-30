# Ejercicio 2
# Implementar el TDA "Quiniela" que modela un juego de quiniela con dos números premiados. La estructura contiene:

# Primer número premiado
# Segundo número premiado
# Multiplicador (cuánto se paga por cada peso apostado)
# Implementar las siguientes operaciones:

# Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que los números que 
# participan se encuentran entre 0 y 999.
# __repr__: Al usar la función print con una variable del tipo quiniela debe mostrar: Primer número 
# ganador: 'numero' - Segundo número ganador: 'numero' - Paga: 'multiplicador'X.
# esNumeroGanador: Operación que recibe un número por parámetros y retorna True si el número resultó 
# ganador o False en caso contrario.
# importeAPagar: Operación que recibe un número y el monto apostado por parámetros y retorna el importe
#  a pagar si la apuesta es ganadora o 0 en caso contrario. Si el número es el primer premio,
#  se paga 'mutiplicador' por cada peso apostado, si es el segundo premio se paga la mitad. 
# Solo se aceptan apuestas hasta $1000.
# premiadosCercanos: Operación que retorna True si los números premiados están 
# a menos de 10 
# números de distancia y False en caso contrario.

def validarNro(number):
  if isinstance(number, int) and number > 0 and number <= 999:
    return number
  else:
    raise Exception("El numero no es correcto") 

def validarMonto(monto):
  if isinstance(monto, int) and monto:
    return monto
  else:
    raise Exception("El numero no es correcto")  

class Quiniela:
    def __init__(self, nro, monto, first_num, second_num, multiplier):
        self.number = validarNro(nro)
        self.monto = validarMonto(monto)
        self.first_num = first_num
        self.second_num = second_num
        self.multiplier = multiplier

    def getFirstNum(self):
        return self.first_num
    
    def esNumeroGanador(self):
        return self.number == self.first_num or self.number == self.second_num
    
    def importeAPagar(self):
        if ( self.number == self.first_num):
          return self.monto * self.multiplier
        elif (self.number == self.second_num): 
          return (self.monto * self.multiplier) / 2
        else: return 0
        
    def __repr__(self):
        hoy = "Primer numero ganador: " + str(self.first_num) + " Segundo numero ganador: " + str(self.second_num) + ". Paga X: " + str(self.multiplier)
        return hoy
    
    

nocturna = Quiniela(7, 100, 7, 1, 2)
print(nocturna.importeAPagar())

    
    

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# if a < b:
#     print("The biggest number is: " ,a)

# elif a == b:
#     print( "The number " , a , " and the number" , b , " they are equal")
    
# else:
#     print("The smallest number is: " ,b)

# name = str(input("Input your name with uppercase letter: "))
# gender = str(input("Input your gender with a F or M: "))

# firstChar = name[0]
# abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

# if gender == "F" and firstChar in abc: 
#     print("You belongs to A group")

# elif gender == "M" and firstChar not in abc:
#     print("You belong to A group")
    
# else:
#     print("You belongs to B group")

# buleano = True
# one = 0

# while buleano == True:
#     if one < 100:
#         one += 1
#         print(one)
#     else:
#         buleano = False

# for a in range(1,101):
#     print(a)
        
        
# PYTHON program to find sum of first 
# n natural numbers. 

# Returns sum of first n natural 
# numbers 
# def findSum(): 
#     n = int(input("Input: "))
# 	sum = 0
# 	x = 1
# 	while x <=n : 
# 		sum = sum + x 
# 		x = x + 1
# 	return sum


# # Driver code 

# n = 5
# print findSum(n) 


# print("CONTADOR DE PARES E IMPARES")
# valores = int(input("¿Cuántos valores va a introducir? "))
# if valores < 0:
#     print("¡Imposible!")
# else:
#     pares = 0
#     for i in range(1, valores + 1):
#         numero = int(input(f"Escriba el valor {i}: "))
#         if numero % 2 == 0:
#             pares += 1
# print("Ha escrito",pares, "números pares y ",valores - pares, "números impares.")
# print("Gracias por su colaboración.")

