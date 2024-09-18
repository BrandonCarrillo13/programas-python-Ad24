# suma n num introducidos por el usuario
import os
os.system("clear")
suma = 0 
n = int(input("cuantas cal ? "))

for i in range (1, n+1):
    print(f"cal {i} ?")
    x = float(input())
    suma = suma + x 
print (f"\nla suma es {suma}")
print(f"\nel promedio es {suma}/n")
