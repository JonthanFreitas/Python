lista = [[] , []]

for i in range(1, 8):
    num = int(input(f'Digite um valor para a posição {i}°: '))

    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)

print(f'Numeros pares digitados: {sorted(lista[0])}')
print(f'Numeros impares digitados: {sorted(lista[1])}')
