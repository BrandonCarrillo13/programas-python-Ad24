#Aceptar un estudiante en bace a su edad y dos calificaciones
#>=18  c1 >=8  c2 >=8 

import os; os.system ("clean")

print("Universidad patito SA de CV")
print ("Aceptar un estudiante en bace a su edad y dos calificaciones")

nombre = input ("Dame el nombre ?")
edad = int(input("Dame la edad ?"))

if edad >=18 :
    print("Dame 2 cal sepparadas por enter ? ")
    c1, c2 = int(input()), int(input())
    if c1 >=8 and c2 >=8:
        print(f"{nombre} bienbenido a la universidad, tu edad {edad} y tus calificaciones {c1}, {c2} lo permiten ")
    else:
        print("\nSolo aceptamos con cal mayores o iguales de 8")
    print("\nGracias por utilizar este prog")

