# Crear una funcion que reciba una lista de notas y calcula su promedio
"""def calcular_promedio_notas (notas) : 

    Recorrer la lista
    CICLO FOR (FOR EACH) para recorrer listas
    sumatoria = 0
    for nota in notas: 
        sumatoria+= nota
    promedio = sumatoria / len(notas)
    print(promedio)

    sumatoria = sum(notas)
    cantidadNotas = len(notas)
    promedio = sumatoria/cantidadNotas
    print(promedio)

    return (sum(notas)/len(notas))"""


def calcular_promedio_lista (lista):
    return(sum(lista)/len(lista))

