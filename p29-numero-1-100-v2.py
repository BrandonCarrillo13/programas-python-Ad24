# imprime numero del 1 al n usando while

import os; os.system("clear")

print("\nImprime numero del 1 al 100 usando while\n")

c=1

n = int (input("Hasta donde deseas llegar ? "))

while c <= n:
    print(c, end=" ")
    c = c + 1

print("\nCiclo terminado")
