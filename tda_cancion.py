# Las plataformas de música online como YouTube y Spotify almacenan la información asociada a las canciones en estructuras de datos 
# complejas para hacer las búsquedas de manera eficiente. Para esto se deben modelar las canciones. 
# Implementar el TDA "Cancion" con los siguientes componentes:

# Nombre
# Artista
# Duración
# Género musical (6 posibles: Rock, Jazz, Blues, Funk, Reggae y Rap).
# Año de edición
# Número de likes
# Implementar las siguientes operaciones:

# Constructor: Debe incluir las validaciones necesarias.
# __repr__: Al usar la función print con una variable del tipo canción debe mostrar: 'nombre' - 'artista' ('duracion').
# mayorDuracion: Operación que recibe dos canciones por parámetros y retorna la de mayor duración.
# agregaLikes: Operación que recibe un número e incrementa la cantidad de likes de la canción en ese número.
# masVotada: Operacion que recibe dos canciones y sin son del mismo artista y del mismo género musical, retorna la que tiene mayor
# cantidad de likes. En caso contrario debe lanzar una excepción.


# Here, I will add a part of exercise 4, because I need to use the class called Tiempo() to get the duration of the Cancion() in the same format

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

def validateName(nombre):
    if isinstance (nombre, str):
        return nombre
    else:
        raise Exception("El nombre de la cancion deben ser solo letras")
    
def validateArtist(artista):
    if isinstance(artista, str):
        return artista
    else:
        raise Exception("El nombre del artista deben ser solo letras")
    
def validateDuration(duracion):
    if isinstance (duracion, Tiempo):
        return duracion
    else:
        raise Exception("La duracion de la canción debe ser del tipo Tiempo")
    
def validateGenders(genero_musical): #Deberia ser una lista, pero como aun no lo vimos, no lo implementamos aqui.
    if isinstance (genero_musical, str):
        return genero_musical
    else:
        raise Exception("El genero musical debe ser solo letras")

def validateYear(anio_edicion):
    if isinstance(anio_edicion, int):
        return anio_edicion
    else:
        raise Exception("El anio_edicion debe ser solo numeros")
    
def validateNLikes(nLikes):
    if isinstance(nLikes, int):
        return nLikes
    else:
        raise Exception("La cantidad de likes deben ser solo numeros")
    
class Cancion:
    def __init__(self, nombre, artista, duracion, genero_musical, anio_edicion, nLikes):
        self.nombre = validateName(nombre)
        self.artista = validateArtist(artista)
        self.duracion = validateDuration(duracion)
        self.genero_musical = validateGenders(genero_musical)
        self.anio_edicion = validateYear(anio_edicion)
        self.nLikes = validateYear(nLikes)
    
    def __repr__(self):
        return str(self.nombre) + "-" + str(self.artista) + "(" + str(self.duracion) + ")"
    
    def mayorDuracion(self, otherSong):
        if self.duracion > otherSong.duracion:
            higherDuration = self.duracion
        else:
            higherDuration = otherSong.duracion
        
    #     if self.minutos > otherSong.minutos:
    #         higherMinutes = self.minutos
    #     else:
    #         higherMinutes = otherSong.minutos
        
    #     if self.segundos > otherSong.segundos:
    #         higherSeconds = self.segundos
    #     else:
    #         higherSeconds = self.segundos
        
    #     return "El tiempo mayor es: " + str(higherHours) + ":" + str(higherMinutes) + ":" + str(higherSeconds)
        
    
pinguinosEnLaCama = Cancion("Pinguinos", "Arjona", Tiempo(0,3,30), "Melodica", 1999, 34350)
dimeQueNo = Cancion("dimeQueNo", "Arjona", Tiempo(0,4,15), "Melodica", 1999, 34350)
print(pinguinosEnLaCama.mayorDuracion(dimeQueNo))