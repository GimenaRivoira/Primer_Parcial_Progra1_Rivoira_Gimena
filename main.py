from funciones import (mostrar_enunciado, cargar_existencias, mostrar_total_unidad_garaje, mostrar_calcular_recaudacion)
from validaciones import validaciones as opciones_numeros
from UTN_Heroes_Dataset.utn_pp import clear_console

def app(matriz_concesionaria):
    while True:
        mostrar_enunciado()
        opciones = opciones_numeros(1,8)
        match opciones:
            case 1:
                cargar_existencias(matriz_concesionaria)
            case 2:
                mostrar_total_unidad_garaje(matriz_concesionaria)
            case 3:
                pass
            case 4:
                pass
            case 5: 
                mostrar_calcular_recaudacion(matriz_concesionaria)
            case 9:
                break
        clear_console()