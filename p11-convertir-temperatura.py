#Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit, usando la siguiente formula:
# • farenheit = (celcius × 9/5) + 32

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
try:
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    # Calcular la temperatura en grados Fahrenheit
    fahrenheit = celsius_a_fahrenheit(celsius)
    
    print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")



