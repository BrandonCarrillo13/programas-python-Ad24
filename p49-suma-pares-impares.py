#imprime numeros de n a 2 y numeros inpares de 1 a n, o la suma de ambos casos

import os
while True:
    os.system("clear")

    print("[1] imprimir de n a 2")
    print("[2] imprimir de 1 a n")
    print("[3] salir...")
    op = int (input ("elige ?"))
    s = 0
    if op==1:
        s=0
        print("imprimiendo de n a 2")
        n = int(input("desde donde ?"))
        for x in range (n,1,-2):
            print(x, end=" ")
            s = s + x
        print("\nLa suma de pares es " + str(s))
    elif op==2:
        print("imprimiendo numeros impares de 1 a n")
        n = int(input("desde donde ?"))
        n = n if n%2!=0 else n-1
        for x in range (1,n+1, 2):
            print(x, end=" ")
            s = s + x
        print("\nla suma de numeros impares es " + str(s))
    elif op==3:
        break
    else:
        print("\nopcion invalida")

    input("\n < preciona cualquier tecla para continuar >")

    ##if input ("continua (s/n)").upper().startswith("N") : break

#print("\nproceso terminado ...")