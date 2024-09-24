## Imprimir la tablas de multiplicar

import os


while True:
    os.system("clear")

    n = int(input("Hasta qué tabla quieres ? "))
    m = int(input("Hasta dónde deseas la tabla ? "))

    for i in range(1, n+1):
        print("Tabla del " + str(i))
        for j in range(1, m+1):
            print(f"{i} x {j} = {i*j}")
        print()

    if input("¿Deseas continuar (s/n)? ").lower().startswith("n"): 
        break