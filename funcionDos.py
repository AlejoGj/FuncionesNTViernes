#crear una lista de 20 notas
import random
"""def crear_lista_notas(cantidadNotas):
    notas=[]
    for _ in range(cantidadNotas):
        notas.append(random.randint(1,5))
    return notas"""

"""def crear_lista_medidasAgua(cantidadMedidas):
    mediciones=[]
    for _ in range(cantidadMedidas):
        mediciones.append(random.randint(0,800))
    return mediciones"""

def crear_lista (cantidadElementos, rangoInicial, rangoFinal): 
    lista=[]
    for _ in range(cantidadElementos):
        lista.append(random.randint(rangoInicial,rangoFinal))
    return lista