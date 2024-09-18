#imprime y suma los multiplos m entre 1 y n

import os; os.system("clear")

n = int(input("desde 1 hasta ?"))
m = int(input("multiplos de ?"))

c = s = 0

for i in range (1, n+1):
    if i % m == 0:
        print(i,end= " ")
        c = c + 1
        s = s + 1
    
print(f"\nlos multiplos de {m} fueron {c} y sus suma es {s}")

