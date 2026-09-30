from time import sleep

print('Bem-vindo a lojá de açai da Debys')
print('-' * 33)
print('Cardapio'.center(30))
print('-' * 33)
print('''   Cupuaçu (CP)
(P) ----- R$  9,00
(M) ----- R$ 14,00
(G) ----- R$ 18,00''')
print('''    Acai (AC)
(P) ----- R$ 11,00
(M) ----- R$ 14,00
(G) ----- R$ 20,00''')
print('-' * len('Bem-vindo a lojá de açai da Debys'))
print('Digite "Sair" para encerrar')
print('-' * 33)

total = 0

while True:
        op = input('Qual Item desja (CP) ou (AC): ').upper().strip()

        if op == 'SAIR':
            print('Encerrando...')
            sleep(1)
            print(f'Total a pagar: R$ {preco:.2f}')
            break

        preco = 0

        if op == 'CP':
            tam = input('Qual Tamanho do Item (P, M ou G): ').upper().strip()
            if tam == 'P':
                preco = 9

            elif tam == 'M':
                preco = 14

            elif tam == 'G':
                preco = 18

        elif op == 'AC':
            tam = input('Qual Tamanho do Item (P, M ou G): ').upper().strip()
            if tam == 'P':
                preco = 11

            elif tam == 'M':
                preco = 14

            elif tam == 'G':
                preco = 20

        else:
            print('Valor invalido, tente novamente!')
            print('-' * 33)
            continue

        total += preco
        print('-' * 33)
        print(f'Você escolheu {op} ({tam}) e o preço é R$ {preco:.2f}!')
        print('-' * 33)

        while True:
            op2 = input('Deseja continuar comprando (S/N): ').upper().strip()
            print('-' * 33)
            if op2 != 'S' and op2 != 'N':
                print('Valor invalido, tente novamente!')
            elif op2 == 'N':
                sleep(1)
                print(f'Total a pagar: R$ {total:.2f}')
                break
            elif op2 == 'S':
                break
        if op2 == 'N':
            break