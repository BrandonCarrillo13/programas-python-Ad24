##p133-estadisticas-basicas

import math

def leer_numeros():
    numeros = input("Dame números separados por espacio: ").split()
    return [int(n) for n in numeros]

def mayor(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)

def media(numeros):
    return sum(numeros) / len(numeros)

def varianza(numeros):
    m = media(numeros)
    return sum((x - m) ** 2 for x in numeros) / len(numeros)

def desviacion_estandar(numeros):
    return math.sqrt(varianza(numeros))

def mostrar_estadisticas(numeros):
    print("Lista de números:", numeros)
    print(f"La media: {media(numeros):.3f}")
    print(f"Mayor de los datos: {mayor(numeros)}")
    print(f"Menor de los datos: {menor(numeros)}")
    print(f"Varianza: {varianza(numeros):.3f}")
    print(f"Desviación estándar: {desviacion_estandar(numeros):.3f}")

numeros = leer_numeros()
mostrar_estadisticas(numeros)
