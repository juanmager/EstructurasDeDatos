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


print("CONTADOR DE PARES E IMPARES")
valores = int(input("¿Cuántos valores va a introducir? "))
if valores < 0:
    print("¡Imposible!")
else:
    pares = 0
    for i in range(1, valores + 1):
        numero = int(input(f"Escriba el valor {i}: "))
        if numero % 2 == 0:
            pares += 1
print("Ha escrito",pares, "números pares y ",valores - pares, "números impares.")
print("Gracias por su colaboración.")