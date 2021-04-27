# Ejercicio 3
# Implementar el TDA "Cuenta" que modela una cuenta bancaria, la estructura de datos esta compuesta por los siguientes componentes:

# Número de cuenta
# DNI del titular
# Saldo de cuenta actual
# Interés anual
# Implementar las siguientes operaciones:

# Constructor: Debe incluir las validaciones necesarias.
# __repr__: Al usar la función print con una variable del tipo cuenta debe mostrar: Cuenta Nro: 'numero' - Titular: 'dni' ($'saldo').
# actualizarSaldo: Operación que actualiza el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365).
# ingresarDinero: Operación que recibe un número e ingresa esa cantidad en la cuenta.
# retirarDinero: Operación que recibe un número y extrae esa cantidad de la cuenta (si hay saldo disponible), sino debe lanzar una excepción.

def validateAccount(cuentaNumero):
    if isinstance(cuentaNumero, int):
        return cuentaNumero
    
def validateDni(dni):
    if isinstance(dni, int):
        dniNumbers = str(dni)
        lenghtDni = len(dniNumbers)
        if lenghtDni == 8:
            return dni
        else:
            raise Exception("Invalid. You must have at least 8 digits.")
    
def validateSaldo(saldoActual):
    if isinstance(saldoActual, int):
        return saldoActual
    
def validateInt(interesAnual):
    if isinstance(interesAnual, int):
        return interesAnual
    

class Cuenta():
    def __init__(self, cuentaNumero, dni, saldoActual, interesAnual):
        self.cuentaNumero = validateAccount(cuentaNumero)
        self.dni = validateDni(dni)
        self.saldoActual = saldoActual
        self.interesAnual = validateInt(interesAnual)
        
    def __repr__(self):
        return "Cuenta numero: " + str(self.cuentaNumero) + ", Titular: " + str(self.dni) + ", Saldo actual: " + str("{0:.2f}".format(self.saldoActual))
    
    def actualizarSaldo(self):
        self.saldoActual += (self.interesAnual / 365)
        
    def ingresarDinero(self, amount):
        self.saldoActual += amount
        
    def retirarDinero(self, amount):
        if self.saldoActual > amount:
            self.saldoActual -= amount
            return "The operation was realized with success. Your account balance is: " + str(self.saldoActual)
        else:
            raise Exception ("You dont have enough money. Please try again.")
        
        
hsbc = Cuenta(100608265, 36981630, 10000, 40000)
print(hsbc)
# hsbc.ingresarDinero(5000)
# print(hsbc)
# print(hsbc.retirarDinero(3000))
# print(hsbc)
hsbc.actualizarSaldo()
print(hsbc)
        