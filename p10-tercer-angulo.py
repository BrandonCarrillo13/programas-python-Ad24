#Dados dos ángulos de un triángulo, calcular el 3er ángulo, usando la siguiente formula:
# • angulo3 = 180 – (angulo1 + angulo2)

# Función para calcular el tercer ángulo de un triángulo
def calcular_tercer_angulo(angulo1, angulo2):
    angulo3 = 180 - (angulo1 + angulo2)
    return angulo3

# Pedir que proporcionen los dos angulos
try:
    angulo1 = float(input("Introduce el primer ángulo en grados: "))
    angulo2 = float(input("Introduce el segundo ángulo en grados: "))

    if angulo1 <= 0 or angulo2 <= 0:
        print("Los ángulos deben ser mayores que 0 grados.")
    elif angulo1 + angulo2 >= 180:
        print("La suma de los dos ángulos debe ser menor que 180 grados.")
    else:
        angulo3 = calcular_tercer_angulo(angulo1, angulo2)  # Calcular el tercer ángulo
        print(f"El tercer ángulo del triángulo es: {angulo3:.2f} grados")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")

