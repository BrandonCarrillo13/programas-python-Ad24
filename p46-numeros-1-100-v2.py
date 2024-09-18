## imprimir numeros del 1 al 100 usando siclo for

import os;os.system("Cls")

##print(list( range(1, 10)))
#print(list( range(1, 10, 2)))#
#print(list( range(1, 10, 3)))#
#print(list( range(10, 0, -1)))#
##print(list( range(10, 0, -1)))##

n = int (input("Hata donde ?"))
i = int (input("incrementos de ?"))
for x in range (0, n+1, i):
    print(x, end=" ")