#Calculo de notas

print("Calcula el promedio de las 5 calificaciones ingresadas en una sola línea, separadas por espacios:")

calificaciones = list(map(float, input().split()))

if len(calificaciones) != 5:
    print("Debes ingresar exactamente cinco calificaciones.")
else:
    c1, c2, c3, c4, c5 = calificaciones

    suma = c1 + c2 + c3 + c4 + c5
    prom = suma / 5

    print(f"El promedio es {prom:.2f}")

    if prom >= 0 and prom <= 6:
        print("Reprobado")
    elif prom >= 6.1 and prom <= 7:
        print("Panzaso")
    elif prom >= 7.1 and prom <= 8:
        print("Muy bien pero puedes mejorar")
    elif prom >= 8.1 and prom <= 9:
        print("Excelente, sigue así")
    elif prom >= 9.1 and prom <= 10:
        print("Excelente, tu esfuerzo valió la pena")
    else:
        print("Calificación fuera de rango")
