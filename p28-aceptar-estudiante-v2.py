
#Acepta estudiante v2 mujer de 21 com prom entre 8 y 9.5

from re import M


print('Universidad Kitty Kat SA')

nombre = input('ingresa tu nombre > ')
sexo = input('ingresa tu sexo |M| O |H|')

edad = int(input('ingresa tu edad > '))

if edad>=21 :
    print('dame 3 calificaciones > ')
    c1, c2, c3  = int(input()), int(input()), int(input())
    suma = c1 + c2 + c3 
    prom = (suma / 3 )
    if sexo == M:
        print("bienbenida")
    else: 
        print("solo aceptamos mujeres ")

        if prom >=8 and prom <= 9.5:
            print(f'{nombre} bienvenid@ a la Universidad, tu edad {edad} y tu pomedio {prom} lo permiten')

        else :
         print('solo aceptamos alumnos con calificaciones entre 8  y 9.5')

else:
    print("no aceptamos menores")