lista = []
maior = None
menor = None

while True:
    lista.append([str(input('Nome: ')), float(input('Peso: '))])

    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()

        if op != 'S' and op != 'N':
            print('Valor invalido! Digite apenas S ou N.')
        else:
            break

    if op == 'N':
        break

for sub in lista:
        if maior is None or sub[1] > maior:
            maior = sub[1]
        if menor is None or sub[1] < menor:
            menor = sub[1]

print('Pessoas acima de 100Kg', end = ' ')
for pos in lista:
    if pos[1] >= 100:
        print(f'{pos[0]} ', end = '')
print()

print('Pessoas entre 50kg a 70Kg', end = ' ')
for pos in lista:
    if pos[1] <= 70 and pos[1] >= 50:
        print(f'{pos[0]} ', end='')
print()

print('Lista principal: ', lista)
print(f'Quantidade de pessoas cadastradas: {len(lista)}')

print(f'O maior Peso foi {maior}Kg', end=' ')
for pos in lista:
    if pos[1] == maior:
        print(f'{pos[0]} ', end='')
print()

print(f'O menor Peso foi {menor}Kg', end=' ')
for pos in lista:
    if pos[1] == menor:
        print(f'{pos[0]} ', end='')
print()