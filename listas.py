# Necesito crear un programa que almanece una lista de 200 notas de estudiantes

#[] --> listas --> plural --> mismo tipo
#       indice(0.....n) posiciones

#{} -->  Diccionarios --> singular --> != (diferentes)
        #clave (llave, propiedad key): valor

import random

notas = []

for i in range (5):
    notaSimulada = random.randint(1,5)
    notas.append(notaSimulada)


#Métodos para transformar, modificar o administrar listas
notas.insert(0,80)  #indice, valor
notas.remove(80)     #valor a eliminar
notas.pop(0)         # elimina un índice
notas.sort(reverse=True)    #organizar de menos a mayor y mayor a menor 
notas.clear()       #Limpiar 
print(notas)