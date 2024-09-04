#verifica si los numeros son consecutivos

print("Verifica si los números son consecutivos")

print("Ingresa tres números diferentes separados por espacios:")
nums = list(map(int, input().split()))

if len(nums) != 3:
    print("Debes ingresar exactamente tres números.")
else:
    num1, num2, num3 = nums
    
    if num1 != num2 and num2 != num3 and num1 != num3:
        if num1 + 1 == num2 and num2 + 1 == num3:
            print("Los números son consecutivos")
        else:
            print("Los números no son consecutivos")
    else:
        print("Los números no son diferentes")
