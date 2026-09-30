lista = []


while True:
    valor = (int(input("Digite um numero: ")))

    if valor in lista:
        print('Valor já existenete na lista! Digite outro numero')
    else:
        lista.append(valor)

        while True:
            op = input('Deseja continuar? [S/N] ').upper().strip()

            if op != 'S' and op != 'N':
                print('Digite apenas S ou N')

            else:
                break

        if op == 'N':
            break


print(f'Sua lista em ordem crescente: {sorted(lista)}')