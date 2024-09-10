#Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
#imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.

while True:
    print("Ingrese el número final:")
    n = int(input())
    
    if n < 100:
        print("El número final debe ser al menos 100.")
        continue
    
    suma = 0
    print("Los números pares son:")

    for c in range(100, n + 1):
        if c % 2 == 0:
            print(c)
            suma += c

    print(f"La suma es: {suma}")
    
    res = input("¿Deseas continuar? (S/N): ").upper()
    if res != "S":
        break

