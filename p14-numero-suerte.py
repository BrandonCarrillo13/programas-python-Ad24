#p14-numero-suerte
#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. Mostrar los dígitos
#individuales y el número de la suerte.

# año de nacimiento
anio_nacimiento = input("Introduce tu año de nacimiento: ")

# la suma de los dígitos del año
suma_digitos = sum(int(digito) for digito in anio_nacimiento if digito.isdigit())

print(f"Dígitos individuales del año {anio_nacimiento}: {', '.join(anio_nacimiento)}")
print(f"El número de la suerte es: {suma_digitos}")


