#priramide caracter
import os


while True:
    os.system("clear")

    r = int(input("Renglones ? "))
    c = int(input("Columnas ? "))
    car = input("Caracter ")

    for i in range(1, r+1):
        for j in range(1, i+1):
            print(car, end="")
    print()