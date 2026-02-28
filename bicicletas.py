from funcionUno import crear_lista_estudiantes
from funcionDos import crear_lista
from funciontres import calcular_promedio_notas
from funcionCuatro import evaluar_bicicleta

#Equipo 1
equipoUno= crear_lista_estudiantes(1)
notasEficienciaEquipoUno = crear_lista(20)
notasParecidoEquipoUno = crear_lista(20)
notasEstabilidadEquipoUno = crear_lista(20)

promedioEficienciaUno= calcular_promedio_notas(notasEficienciaEquipoUno)
promedioParecidoUno= calcular_promedio_notas(notasParecidoEquipoUno)
promedioEstabilidadUno = calcular_promedio_notas(notasEstabilidadEquipoUno)

evaluacionUno = evaluar_bicicleta(promedioEstabilidadUno,promedioEficienciaUno,promedioParecidoUno)

print(f"El resultado global del equipo uno fue: {evaluacionUno}")

#Equipo 2
equipoDos= crear_lista_estudiantes(1)
notasEficienciaEquipoDos = crear_lista(20)
notasParecidoEquipoDos = crear_lista(20)
notasEstabilidadEquipoDos = crear_lista(20)

promedioEficienciaDos= calcular_promedio_notas(notasEficienciaEquipoDos)
promedioParecidoDos= calcular_promedio_notas(notasParecidoEquipoDos)
promedioEstabilidadDos = calcular_promedio_notas(notasEstabilidadEquipoDos)

evaluacionDos = evaluar_bicicleta(promedioEstabilidadDos,promedioEficienciaDos,promedioParecidoDos)

print(f"El resultado global del equipo uno fue: {evaluacionDos}")