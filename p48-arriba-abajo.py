#imprime numeros de 1 a n o de n a 1 segun lo que quiera el usuario

import os
while True:
    os.system("clear")

    print("[1] imprimir de 1 a n")
    print("[2] imprimir de n a 1")
    print("[3] salir...")
    op = int (input ("elige ?"))
    if op==1:
        print("imprimiendo de 1 a n")
        n = int(input("desde donde ?"))
        for x in range (n,1,-1):
            print(x, end=" ")
    elif op==2:
        print("imprimiendo de n a 1")
        n = int(input("desde donde ?"))
        for x in range (n,1,-1):
            print(x, end=" ")
    elif op==3:
        break
    else:
        print("\nopcion invalida")

    input("\n < preciona cualquier tecla para continuar >")

    ##if input ("continua (s/n)").upper().startswith("N") : break

#print("\nproceso terminado ...")