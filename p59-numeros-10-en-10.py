#Imprime los numeros de 10 en 10

import os 
os.system("cls")

num = int(input("Dame un numero ?"))
for n in range(1,num+1,10):
    print(n, end=" ")