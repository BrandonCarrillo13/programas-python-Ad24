#Aceptar un estudiante en bace a su edad y dos calificaciones
#>=18  c1 >=8  c2 >=8 

import os; os.system ("clean")

print ("Aceptar un estudiante en bace a su edad y dos calificaciones")

nombre = input ("Dame el nombre ?")
edad = int(input("Dame la edad ?"))

if edad < 18 :
    print("\nSolo aceptamos mayores de edad")
else:
    print("Dame 2 cal sepparadas por enter ? ")
    c1, c2 = int(input()), int(input())
    if c1<8 or c2<8:
        print("\nSolo aceptamos con cal mayores o iguales de 8")
    else:
        print(f"{nombre} bienbenido a la universidad, tu edad {edad} y tus calificaciones {c1}, {c2} lo permiten ")

    print("\nGracias por utilizar este prog")

