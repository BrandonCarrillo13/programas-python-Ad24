# Verifica si la suma de dos numeros es igual a un tercero
# 4 5 o ?     4 9 5 ?    9 4 5 ?    4 4 4 ?     3 5 7 ? 

import os; os.system ("clean")

print("Verifica si la suma de dos numeros es igual a un tercero:\n")
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3 :
    print("f{n1} + {n2} = {n3}")
elif n1 + n3 == n2 :
    print(f"{n1} + {n3} = {n2}")
elif n2 + n3 == n1 :
    print(f"{n2} + {n3} = {n1}")
elif n1 == n2 == n3 :
    print(f"{n1} = {n2} = {n3}")
else:
    print(f"Los numero son diferentes: {n1}, {n2}, {n3}")

print("\nProceso terminado...")
