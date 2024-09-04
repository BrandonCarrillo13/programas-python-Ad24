#p12-volumen-cilindro
#Se desea calcular el volumen de un cilindro dado su radio y altura, usando la siguiente formula:
#• Volumen = PI * (Radio * Radio) * Altura

import math

# Función para calcular el volumen de un cilindro
def calcular_volumen_cilindro(radio, altura):
    volumen = math.pi * (radio ** 2) * altura
    return volumen

# Solicitar al usuario el radio y la altura del cilindro
try:
    radio = float(input("Introduce el radio del cilindro: "))
    altura = float(input("Introduce la altura del cilindro: "))

  
    if radio <= 0 or altura <= 0:         # Comprobar que el radio y la altura sean valores positivos
        print("El radio y la altura deben ser mayores que 0.")
    else:
        volumen = calcular_volumen_cilindro(radio, altura)
        print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")

