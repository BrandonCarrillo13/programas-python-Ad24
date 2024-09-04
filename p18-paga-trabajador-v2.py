import os
os.system("clear")

print("Calcula la paga de un trabajador considerando las horas extras de trabajo")

nombre = input("Dame tu nombre ? ")
horas = int(input("Horas trabajadas ? "))
paga = float(input("Paga x hora ? "))
tasa = 0.3

hextra = paganormal = pagoextra = pagabruta = 0

if horas > 40:
    hextra = horas - 40
    paganormal = 40 * paga
    pagaextra = hextra * paga * 2
    pagabruta = paganormal + pagaextra
else:
    pagabruta = horas * paga

impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print(f"\nEl trabajador: {nombre}, trabajó {horas} horas, a una paga de {paga:.2f}")
print(f"\nHoras extra: {hextra}, paga normal: {paganormal:.2f}, paga extra: {pagaextra:.2f}")
print(f"\nPaga bruta: {pagabruta:.2f}")
print(f"\nImpuesto: {impuesto:.2f}")
print(f"\nPaga neta: {paganeta:.2f}")

