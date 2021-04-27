# Ejercicio 4
# Implementar el TDA "Tiempo" que modela una duracion en horas, minutos y segundos.

# Se deben implementar las siguientes operaciones:

# Constructor: Debe incluir las validaciones necesarias, la hora debe ser un número positivo y los minutos y segundos deben ser números 
# positivos entre 0 y 59.
# __repr__: Al usar la función print con una variable del tipo tiempo debe mostrar: 'horas':'minutos':'segundos'.
# tiempoASegundos: Operación que toma una variable de tipo tiempo y retorna la cantidad en segundos.
# tiemposDesdeSegundos: Operación que recibe un tiempo en segundos como parámetro y retorna una variable de tipo tiempo, en horas minutos 
# y segundos.
# mayorDuracion: Operación que recibe dos variables de tipo tiempo y retorna la de mayor duración.

def validatePositive(horas):
    if isinstance(horas, int) and horas >= 0:
        return horas
    else:
        raise Exception("Las horas deben ser solo numeros positivos")
    
def validateMin(minutos):
    if isinstance(minutos, int) and minutos >= 0 and minutos <= 59:
        return minutos
    else:
        raise Exception("Los minutos deben ser numeros entre 0 y 59.")

def validateSeg(segundos):
    if isinstance(segundos, int) and segundos >= 0 and segundos <= 59:
        return segundos
    else:
        raise Exception("Los segundos deben ser numeros entre 0 y 59.")

class Tiempo:
    def __init__(self, horas, minutos, segundos):
        self.horas = validatePositive(horas)
        self.minutos = validateMin(minutos)
        self.segundos = validateSeg(segundos)
    
    def __repr__(self):
        return str(self.horas) + ":" + str(self.minutos) + ":" + str(self.segundos)
    
    def tiempoASegundos(self):
        hoursToConvert = self.horas *3600
        minutesToConvert = self.minutos * 60
        self.segundos += hoursToConvert + minutesToConvert 
        return self.segundos
    
    def tiemposDesdeSegundos(self, segundos):
        hours = segundos // 3600
        remaining1 = segundos % 3600
        minutes = remaining1 // 60
        remaining2 = remaining1 % 60
        return str(hours) + ":" + str(minutes) + ":" + str(remaining2)
    
    def mayorDuracion(self, otherTime):
        if self.horas > otherTime.horas:
            higherHours = self.horas
        else:
            higherHours = otherTime.horas
        
        if self.minutos > otherTime.minutos:
            higherMinutes = self.minutos
        else:
            higherMinutes = otherTime.minutos
        
        if self.segundos > otherTime.segundos:
            higherSeconds = self.segundos
        else:
            higherSeconds = self.segundos
        
        return "El tiempo mayor es: " + str(higherHours) + ":" + str(higherMinutes) + ":" + str(higherSeconds)
        
            
            
             
    
actualTime = Tiempo(1, 2, 34)
supposedTime = Tiempo(10,3,14)
# print(actualTime.tiemposDesdeSegundos(45800))
# print(actualTime)
# print(supposedTime)
print(actualTime.mayorDuracion(supposedTime))