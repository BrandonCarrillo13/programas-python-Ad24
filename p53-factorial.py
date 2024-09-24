## calcula el fact de un num

import os;os.system("clear")

#n=int(inpuy("Dame un numero ?"))
n=5
f=1
print(f"{n}! = ", end=" ")
for i in range (1, n+1):
    f=f*i
    print(f"{i}{"x" if i!=n else""} = ", end=" ")
print(f"/n = {f}")