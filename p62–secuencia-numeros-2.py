#Imprime las seciencoas de num en dos

import os

os.system("cls")

renglon = int(input("Dame un numero? "))

for n in range(1,renglon+1):
    num = 0
    for y in range(1,n+1):
        num += 1
        print(num ,end=" ")
    print(" ")  