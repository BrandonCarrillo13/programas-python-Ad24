import os
os.system("clear")

print("Convertir temperaturas de Celsius a Fahrenheit y viceversa")
print("[1] Convertir Fahrenheit a Celsius")
print("[2] Convertir Celsius a Fahrenheit")
print("[3] Salir")

# Captura la opción del usuario y convierte la entrada a entero
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
    
    elif op == 3:
        print("Te vas porque tú quieres ... gracias")
    
    else:
        print("Opción errónea ... ")
    
    print("\nProceso terminado...")
    
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")

