## Listas de multiplicar

def leer_lista(numero_lista):
    lista = []
    print(f"Introduce los 5 elementos de la lista {numero_lista}:")
    for i in range(5):
        while True:
            try:
                elemento = float(input(f"Elemento {i + 1}: "))
                lista.append(elemento)
                break
            except ValueError:
                print("Introduce un nUmero valido.")
    return lista

def multiplicar_listas(lista1, lista2):
    return [a * b for a, b in zip(lista1, lista2)]

def imprimir_listas(lista1, lista2, lista_resultado):
    print("\nLista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista resultado:", lista_resultado)

def main():
    lista1 = leer_lista(1)
    lista2 = leer_lista(2)
    lista_resultado = multiplicar_listas(lista1, lista2)
    imprimir_listas(lista1, lista2, lista_resultado)

if __name__ == "__main__":
    main()