#p13-calculo-tiempo
#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos, considerando que:
#• 1 día tiene 24 horas,
#• 1 hora tiene 60 minutos,
#• 1 minuto tiene 60 segundos.

def calcular_tiempo_equivalente(total_horas):
    # Calcular días
    dias = total_horas // 24
    horas_restantes = total_horas % 24
    
    # Calcular minutos
    minutos = horas_restantes * 60
    
    # Calcular segundos
    segundos = minutos * 60
    
    return dias, horas_restantes, minutos, segundos

# Solicitar al usuario la cantidad de horas
try:
    total_horas = float(input("Introduce la cantidad de horas: "))
    
    # Comprobar que la cantidad de horas sea un valor positivo
    if total_horas < 0:
        print("La cantidad de horas debe ser un valor positivo.")
    else:
        # Calcular el tiempo equivalente
        dias, horas_restantes, minutos, segundos = calcular_tiempo_equivalente(total_horas)
        
        # Mostrar el resultado
        print(f"{total_horas} horas equivalen a:")
        print(f"{dias} días")
        print(f"{horas_restantes} horas")
        print(f"{minutos} minutos")
        print(f"{segundos} segundos")
except ValueError:
    print("Por favor, ingresa un valor numérico válido.")
