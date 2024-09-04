import os
os.system("clear")

print("Convertir temperaturas de Celsius a Fahrenheit y viceversa")
print("[1] Convertir Fahrenheit a Celsius")
print("[2] Convertir Celsius a Fahrenheit")

# Capturar la opción del usuario y convertirla a entero
try:
    op = int(input("Elige ? "))
    
    if op == 1:
        print("Convertiendo Fahrenheit a Celsius")
        temp = float(input("Dame los grados Fahrenheit ? "))
        res = (temp - 32) * 5 / 9
        print(f"{temp} Fahrenheit equivale a {res:.2f} Celsius")
        
    elif op == 2:
        print("Convertiendo de Celsius a Fahrenheit")
        temp = float(input("Dame los grados Celsius ? "))
        res = (temp * 9 / 5) + 32
        print(f"{temp} Celsius equivale a {res:.2f} Fahrenheit")
    
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")


    
