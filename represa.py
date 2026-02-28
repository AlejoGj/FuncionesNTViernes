from funcionDos import crear_lista
from funciontres import calcular_promedio_lista
from funcionCinco import calcular_nivel_represa

listaMediciones = crear_lista(20,0,800)
medicionPromedio = calcular_promedio_lista(listaMediciones)
calcular_nivel_represa(medicionPromedio)