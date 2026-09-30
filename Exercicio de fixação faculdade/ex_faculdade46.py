matriz = []

soma_par = 0
soma_linha = 0
soma_coluna = 0
maior = None

for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(n)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^8}]', end='')
    print()
print('-=-' * 30)

print('Numeros par: ', end=' ')
for linha in matriz:
    for par in linha:
        if par % 2 == 0:
            soma_par += par
            print(f'[{par}]', end=' ')

print()
for linha in matriz[1]:
    soma_linha += linha
    if maior is None or linha > maior:
        maior = linha

for pos in range(3):
    soma_coluna += matriz[pos][2]


print(f'A soma dos numeros pares: {soma_par}')
print(f'O maior numero da segunda linha: {maior}')
print(f'Soma da segunda linha: {soma_linha}')
print(f'Soma da tericera coluna: {soma_coluna}')
