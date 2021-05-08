import numpy as np

def mezcla(vector,mitadIzq,mitadDer):
    indiceDer=0
    indiceIzq=0
    indiceVector=0

    copiaIzq= mitadIzq.copy()
    copiaDer =mitadDer.copy()

    while indiceIzq < len(mitadIzq) and indiceDer < len(mitadDer):
        if mitadIzq[indiceIzq] < mitadDer[indiceDer]:
            vector[indiceVector]=mitadIzq[indiceIzq]
            indiceIzq+=1
        else:
            vector[indiceVector]=mitadDer[indiceDer]
            indiceDer+=1
        indiceVector+=1

    while indiceIzq < len(mitadIzq):
        vector[indiceVector]=mitadIzq[indiceIzq]
        indiceIzq+=1
        indiceVector+=1

    while indiceDer < len(mitadDer):
        vector[indiceVector]=mitadDer[indiceDer]
        indiceDer+=1
        indiceVector+=1


def ordenamientoPorMezcla(vector):
    #print("diviendo",vector)
    if len(vector)>1:
        medio= len(vector)//2
        mitadIz = vector[:medio].copy() #copia para que no se pisen los valores.
        mitadDe = vector[medio:].copy() #copia para que no se pisen los valores.
        ordenamientoPorMezcla(mitadIz)
        ordenamientoPorMezcla(mitadDe)
        mezcla(vector,mitadIz,mitadDe)

vecti = np.array([88,2,120,45,8,150,7,19])
print("Vector antes de ser ordenado: ",vecti)
ordenamientoPorMezcla(vecti)
print("Vector luego de ser ordenado: ", vecti)

            