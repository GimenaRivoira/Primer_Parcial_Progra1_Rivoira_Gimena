from UTN_Heroes_Dataset.utn_pp import get_original_matrix
matriz_concesionaria = get_original_matrix()

from UTN_Heroes_Dataset.utn_pp import (mostrar_matriz_texto_tabla, get_original_matrix, )
def recorer_matriz(lista_matriz: list[list]) -> list[list]:
    nueva_lista = []
    for fila in range(len(lista_matriz[0])):
        lista_unitaria = []
        for columnas in range(len(lista_matriz)):
            dato = f"{lista_matriz[columnas][fila]}"
            lista_unitaria.append(dato)
        nueva_lista.append(lista_unitaria)
    return nueva_lista

def cargar_existencias(lista_matriz: list[list]) -> None:
    print(mostrar_matriz_texto_tabla(recorer_matriz(lista_matriz), ['Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']))

def total_unidad_garaje(lista_matriz: list[list], indice: int) -> int:
    matriz = lista_matriz[indice]
    suma_unidad = 0
    for unidades in matriz:
        suma_unidad = suma_unidad + unidades
    return suma_unidad

def mostrar_total_unidad_garaje (lista_matriz: list[list]) -> int:
    total_garaje_unidad = total_unidad_garaje(lista_matriz, 2)
    print(f"La cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria es: {total_garaje_unidad}")

def obtener_minimo(lista_matriz: list[list]) -> int:
    matriz = lista_matriz[2]
    numero_minimo = 0

    for unidad in matriz:
        if numero_minimo == 0 or unidad <= numero_minimo:
            numero_minimo = unidad
    return numero_minimo

def obtener_maximo(lista_matriz: list[list]) -> int:
    matriz = lista_matriz[2]
    numero_maximo = 0

    for unidad in matriz:
        if numero_maximo == 0 or unidad <= numero_maximo:
            numero_maximo = unidad
    return numero_maximo

def mostrar_datos_unidad_minina(lista_matriz: list[list]):
    matriz = recorer_matriz(lista_matriz)
    unidad_minima = obtener_minimo(lista_matriz, "minimo")

    for unidad in matriz:
        if unidad[2] == unidad_minima:
            print(unidad)
            
def calcular_recaudacion(lista_matriz: list[list]) -> list[list]:
    nueva_lista = []
    for fila in range(len(lista_matriz[0])):
        lista_unitaria = []
        for columnas in range(len(lista_matriz)):
            precio = lista_matriz[3][fila]
            unidades = lista_matriz[2][fila]
            calculo = precio * unidades
            lista_matriz[4][fila] = calculo
            dato = f"{lista_matriz[columnas][fila]}"
            lista_unitaria.append(dato)
        nueva_lista.append(lista_unitaria)
    return nueva_lista

def mostrar_calcular_recaudacion(lista_matriz: list[list]) -> None:
    print(mostrar_matriz_texto_tabla(calcular_recaudacion(lista_matriz), ['Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']))


if __name__ == "__main__":
    print(mostrar_calcular_recaudacion(matriz_concesionaria))

    