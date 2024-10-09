def contar_caracteres(cadena):
    frecuencias = {}  
    for caracter in cadena:
        if caracter in frecuencias:
            frecuencias[caracter] += 1  
        else:
            frecuencias[caracter] = 1  
    return frecuencias


cadena = input("Introduce una cadena: ")

resultado = contar_caracteres(cadena)

print("Frecuencia de cada carácter:")
for caracter, frecuencia in resultado.items():
    print(f"'{caracter}': {frecuencia}")