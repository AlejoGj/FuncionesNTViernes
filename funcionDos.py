# Crear una lista de 20 nnotas

import random
def CrearNotas(cantidadNotas):
    notas = []
    
    for _ in range(cantidadNotas):
        notas.append(random.randint(1,5))
    return notas

listaNotas = CrearNotas(20)