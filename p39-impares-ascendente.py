#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n),
#además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el
#usuario lo decida.
#impares de 1 a n

while True:
    print("ingrese el numero inicial")
    c = int(input())
    f = 100
    suma = 0
    print("los numeros pares son")

    while c <= f:
        
        if c % 2 != 0:
            print (c)
            suma = suma +c
        c+=1
    print(f"la suma es{suma}")
    res = input("deseas continuar {S/N}").upper()
    if res == "N":
        break