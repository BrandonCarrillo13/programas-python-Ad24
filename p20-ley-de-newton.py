print("Calculando los valores de la segunda ley de Newton:\n")

print('[a] Calcular la fuerza')
print('[b] Calcular la masa')
print('[c] Calcular la aceleración')

op = input('Elige una opción (a, b, c): ').strip().lower()

if op == 'a':
    print('\nCalculando la fuerza...')
    m = float(input('Dame la masa (kg): '))
    a = float(input('Dame la aceleración (m/s^2): '))
    f = m * a
    print(f'La fuerza es {f} N')
elif op == 'b':
    print('\nCalculando la masa...')
    f = float(input('Dame la fuerza (N): '))
    a = float(input('Dame la aceleración (m/s^2): '))
    m = f / a
    print(f'La masa es {m} kg')
elif op == 'c':
    print('\nCalculando la aceleración...')
    f = float(input('Dame la fuerza (N): '))
    m = float(input('Dame la masa (kg): '))
    a = f / m
    print(f'La aceleración es {a} m/s^2')
else:
    print('Opción inválida!')
