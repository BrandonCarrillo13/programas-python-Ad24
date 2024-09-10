#Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
#además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
#decida.

import os

while(True):
    os.system("cls")
    c = sum = prom = 0
    while(True):
        n = int(input("Introuzca un numero ?"))
        if n == 0 : break
        sum += n
        c += 1
        prom = sum/c
        print(f"Se intrujeron {c} numeros")
        print(f"La suma de los numeros es de {sum}")
        print(f"El promedio es de {prom}")    
    resp = input("Deseas continuar (S/N) ?")
    if resp =="N": break 

print("\nProceso terminado...")

            

    

        