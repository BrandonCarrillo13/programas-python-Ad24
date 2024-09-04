#numero mayor

print("encuentra cual es el numero mayor")

print("ingresa tres numeros diferentes separados por enter")
num1,num2,num3, = int(input()), int(input()), int(input())

if num1 > num2  and num1 > num3 :
    print(f"el numero mayor es {num1} ")

if num2 > num1  and num2 > num3 :
    print(f"el numero mayor es {num2} ")
   
if num3 > num1  and num3 > num2 :
    print(f"el numero mayor es {num3} ")
 
 