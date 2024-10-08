##Procesar notas

def leer_notas():
    notas = []
    while True:
        try:
            nota = float(input("Introduce una nota (0 para terminar): "))
            if nota == 0:
                break
            if 0 <= nota <= 100:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    return notas

def procesar_notas(notas):
    if not notas:
        print("No se introdujeron notas.")
        return
    
    cantidad = len(notas)
    suma = sum(notas)
    promedio = suma / cantidad
    menores_al_promedio = [nota for nota in notas if nota < promedio]
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    print(f"\nCantidad de notas: {cantidad}")
    print(f"Notas: {', '.join(map(str, notas))}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Notas menores al promedio ({len(menores_al_promedio)}): {', '.join(map(str, menores_al_promedio))}")
    print(f"Nota máxima: {nota_maxima}")
    print(f"Nota mínima: {nota_minima}")

def main():
    notas = leer_notas()
    procesar_notas(notas)

if __name__ == "__main__":
    main()

    