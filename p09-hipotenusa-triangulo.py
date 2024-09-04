# Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados
# usandon la sig formula: hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math

def calcular_hipotenusa(lado1, lado2):
    # Se Calcula la hipotenusa usando la fórmula dada
    hipotenusa = math.sqrt(lado1 * lado1 + lado2 * lado2)
    return hipotenusa

def main():
    lado1 = float(input("Introduce la longitud del primer lado: "))
    lado2 = float(input("Introduce la longitud del segundo lado: "))

    resultado = calcular_hipotenusa(lado1, lado2)

    print(f"La longitud de la hipotenusa es: {resultado}")

if __name__ == "__main__":
    main()
    

 
 

    

