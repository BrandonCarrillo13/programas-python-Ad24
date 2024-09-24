##imprime la secuencia de numeros

import os
os.system("cls")

renglon = int(input("Dame un numero? "))
num = 0
for n in range(1,renglon+1):
    num += 1
    for y in range(1,n+1):
        print(num ,end=" ")
    print(" ")  