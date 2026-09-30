lista = []
cont = 0

while True:
    n = int(input('Disgite um numero: '))

    lista.append(n)
    cont += 1
    while True:
        op = input('Deseja continuar? [S/N] ').upper().strip()

        if op != 'S' and op != 'N':
            print('Valor invalido! digite apenas S ou N.')
        else:
            break
    if op == 'N':
        break
if 5 in lista:
    print('Na sua lista se encontra o numero 5')
else:
    print('Na sua lista não se encronta o numero 5')
print(f'Foram digitados {cont} elementos na lista.')
lista.sort(reverse=True)
print(f'Sua lista em ordem decrescente: {lista}')
