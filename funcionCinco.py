# Crear una funcion que nos permita generar 20 mediciones de una represa 
# (0-800) y calcular el promedio de esas mediciones
# debemos ser capaces de indicar cual es el nivel de operacion de la represa


def calcular_nivel_represa (promedioNivel):

    if promedioNivel>0 and promedioNivel<=250:
        print("Operando bajo nivel, se recomienda apagar algunas turbinas")
    elif promedioNivel>250 and promedioNivel<=400:
        print("Operando con normalidad")
    elif promedioNivel>400: 
        print("Operando sobre el nivel, cuidado abrir compuertas")
    else: 
        print("Medicion promedio ingresada es invalida")