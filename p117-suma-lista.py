##p117-suma-lista

def suma(lista):
    s = 0
    for n in lista:
        s += n
        return s

nums = [10, 20, 30, 40, 50]
res = suma(nums)
print('La suma es ', res)