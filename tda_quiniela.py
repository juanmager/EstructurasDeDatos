# Ejercicio 2
# Implementar el TDA "Quiniela" que modela un juego de quiniela con dos números premiados. 
# La estructura contiene:

# Primer número premiado
# Segundo número premiado
# Multiplicador (cuánto se paga por cada peso apostado)
# Implementar las siguientes operaciones:

# Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que los números que 
# participan se encuentran entre 0 y 999.
# __repr__: Al usar la función print con una variable del tipo quiniela debe mostrar: 
# Primer número ganador: 'numero' - Segundo número ganador: 'numero' - Paga: 'multiplicador'X.
# esNumeroGanador: Operación que recibe un número por parámetros y retorna True si el número resultó ganador o 
# False en caso contrario.
# importeAPagar: Operación que recibe un número y el monto apostado por parámetros y retorna el importe a 
# pagar si la apuesta es ganadora o 0 en caso contrario. Si el número es el primer premio, se paga 'mutiplicador' 
# por cada peso apostado, si es el segundo premio se paga la mitad. Solo se aceptan apuestas hasta $1000.
# premiadosCercanos: Operación que retorna True si los números premiados están a menos de 10 números de distancia y 
# False en caso contrario.

def validatePositive(num):
    if isinstance(num, int) and num > 0 and num < 999:
        return num
    else: 
        raise Exception("Solo se puede elegir numeros entre entre 0 y 999")

class Quiniela():
    def __init__(self, firstNum, secondNum, multiplier):
        self.firstNum = validatePositive(firstNum)
        self.secondNum = validatePositive(secondNum)
        self.multiplier = validatePositive(multiplier)
        
    def __repr__(self):
        return str(self.firstNum) + " first winning number, " + str(self.secondNum) + " second winning number, " + " pay: "+ str(self.multiplier)
    
    def esNumeroGanador(self, numeroGanador):
        return numeroGanador == self.firstNum or numeroGanador == self.secondNum 
        
    def importeAPagar(self, num, amount):
        if num == self.firstNum and amount > 0 and amount <= 1000:
            return "The amount to pay is: $" + str(self.multiplier * amount)
        elif num == self.secondNum and amount > 0 and amount <=1000:
            return "The amount to pay is: $" + str((self.multiplier * amount)/2)
        else:
            return "The amount to pay is: $0" 
            
    def premiadosCercanos(self):
        if self.firstNum > self.secondNum:
            if self.firstNum - self.secondNum <= 10:
                return True
            else: 
                return "Los numeros no son premiados cercanos"
        elif self.secondNum > self.firstNum:
            if self.secondNum - self.firstNum <= 10:
                return True
            else: 
                return "Los numeros no son premiados cercanos"
            
        
loto = Quiniela(730, 738, 2)
# print(loto)
# print(loto.esNumeroGanador(23))
# print(loto.importeAPagar(10,100))
print(loto.premiadosCercanos())

