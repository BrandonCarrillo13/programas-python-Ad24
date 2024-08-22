# p03-area-triangulo - calcula el are de un triangulo

print("Calculando el are de un triangulo")

print("Dame la base y la altura separado por un enter")
base,altura = int(input()), int(input())
area = (base * altura)/ 2

print(f"Para un triangulo de base {base} y altura {altura} el area es {area:.2f}")
