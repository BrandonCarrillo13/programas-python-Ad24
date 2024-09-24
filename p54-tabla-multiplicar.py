## Imprimir la tabla de multiplicar

import os


while True:
    os.system("clear")

    t = int(input("Dame la tabla que desas imprimir ? "))
    n = int(input("Hasta donde deseas la tabla ? "))

    for i in range(1, n+1, 1):
        print(f"{t} x {i} = {t*i}")

    if input("¿Deseas continuar (s/n)? ").lower().startswith("n"):  break
print("\nproceso terminado...")