print('-=-' * 20)
print('Vamos verificar o valor do seu aumento')
print('Para encerrar o programa digite ')
print('-=-' * 20)

while True:
    sair = str(input('Deseja sair? [S/N]: ')).strip().upper()[0]
    if sair == 'SAIR':
        print('programa encerrado...')
        break

    n1 = float(input('Digite o seu salario: '))

    if n1 == 0:
        print('Valor não valido digite outro valor')
        continue

    elif n1 >= 1250:
        n2 = n1 * 1.10
        print(f'O valor do seu aumento será de R${n2:.2f}')
    else:
        n3 = n1 * 1.15
        print(f'O valor do seu aumento é de {n3:.2f}')


