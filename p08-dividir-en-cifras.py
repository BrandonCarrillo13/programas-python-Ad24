# Divide un numero entero de 3 cifras en centenas, decenas y unidades

import os
os.system("clear")
print("Divide un numero entero de 3 cifras en centenas, decenas y unidades\n ")
n = int (input("Dam un numero entero de 3 ?"))
c = n // 100
d = (n - ( c * 100 ))//10
u = (n - ( c * 100 + d *10))

print("El numero original es ", n)
print("centenas : ",c)
print("decenas : ",d)
print("unidades : ",u)