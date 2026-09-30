print('-=-' * 20)
str(print('Vamos calcular o triangulo'.center(54)))
print('-=-' * 20)

while True:
    entrada = (input('Deseja sair? [S/N]: ')).upper().strip()

    sair = entrada[0]

    if sair == 'S':
        print('Encerrando o programa...')
        break
    if sair != 'N':
        print('Valor não valido, Digite novamente!')
        continue

    r1 = int(input('Digite um valor: '))
    r2 = int(input('Digite outro valor: '))
    r3 = int(input('Digite outro valor: '))
    print('-=-' * 20)

    if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
        print(f'Os valores digitados {r1}, {r2} e {r3}, formam um triangulo'.center(60))
        print('-=-' * 20)
    else:
        print(f'Os valores digitados {r1}, {r2} e {r3}, não formam um triangulo'.center(60))
        print('-=-' * 20)
