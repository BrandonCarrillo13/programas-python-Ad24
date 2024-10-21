# p113_suma_digitos

# Importa librería para limpiar la terminal
import os

# Limpia el texto de la terminal
os.system("cls")

# Suma digitos 
def sumadigitos(n):
    suma=0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

n = int(input("Dame un número y sumaré sus dígitos :? "))
res = sumadigitos(n)
print(f"La suma de los dígitos de {n} es {res}")