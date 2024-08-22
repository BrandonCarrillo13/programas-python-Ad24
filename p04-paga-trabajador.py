# p04-paga-trabajador.py - Calcula la paga de un trabajador

print("Calcular la paga de un trabajador : \n")

nombre = input("Dame tu nombre ?")
horas = int(input("horas ?"))
paga = float(input("paga x hora?"))
tasa = 0.03

pagabruta = horas * paga 
impuesto = pagabruta * tasa 
paganeta = pagabruta - impuesto

print(f"El trabajador {nombre}, trabajo {horas} horas a una paga de {paga} peso la hora, con una tasa de {tasa}")
print(f"Paga bruta :{pagabruta:,.2f}")
print(f"Impuesto   :{impuesto:,.2f}")
print(f"Paganeta   :{paganeta:,.2f}") 
