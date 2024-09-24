# Calcula el factorial de un número

import os; os.system("clear")

n = int(input("Dame un número ? "))

for x in range(1, n+1):
    print(f"{x}!: ", end="")
    f = 1
    for i in range(1, x+1):
        f *= i
        print(f"{i} x " if i != x else f"{i}", end=" ")
    print(f"= {f}")