#Eleva un num base a su exponente

import os; os.system("clear")

base = int(input("base ?"))
exp = int(input("exponenre ?"))

p =1
for i in range(exp):
    p =p *base
print(f"la base {base} elevada a la {exp} es {p}")


p =1
for _ in range(exp):
    p =p *base
print(f"la base {base} elevada a la {exp} es {p}")