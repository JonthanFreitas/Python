lista = []
lista_par = []
lista_impar = []

while True:
    n = int(input('Digite um valor: '))

    lista.append(n)

    while True:
        op = input('Quer continuar? [S/N] ').upper().strip()

        if op != 'S' and op != 'N':
            print('Valor invalido! Digite apenas S ou N.')
        else:
            break
    if op == 'N':
        break
for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    if num % 2 == 1:
        lista_impar.append(num)


print(f'Sua lista em numeros impar: {sorted(lista_impar)}')
print(f'Sua lista em numeros par: {sorted(lista_par)}')
print(f'Sua lista {sorted(lista)}')