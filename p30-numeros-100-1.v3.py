# imprime numero del 1 al n, en decremento de p ,  usando while

import os; os.system("clear")

print("\nimprime numero del 1 al n, en decremento de p ,  usando while\n")


n = int (input("Hasta donde deseas llegar ? "))
p = int (input("En decremento de ?"))
c = n

while c <= n:
    print(c, end=" ")
    c = c + p

print("\nCiclo terminado")