#Imprime los numeros del 1 a 200 de 10 en 10

import os; os.system("clear")

c=0

while c <= 200:
    c = c + 1
    if c % 10 != 0:
        continue
    print("\nCiclo terminado")
    