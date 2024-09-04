# imprime numero del 1 al n, en incrementos de p ,  usando while

import os; os.system("clear")

print("\nimprime numero del 1 al n, en incrementos de p ,  usando while\n")

c=0

n = int (input("Hasta donde deseas llegar ? "))
p = int (input("En incrementos de ?"))

while c <= n:
    print(c, end=" ")
    c = c + p

print("\nCiclo terminado")