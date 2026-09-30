print('Bem-vindo a lojá de açai da Debys')
print('-' * len('Bem-vindo a lojá de açai da Debys'))
print('Cardapio'.center(30))
print('-' * len('Bem-vindo a lojá de açai da Debys'))

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
print('-' * len('Bem-vindo a lojá de açai da Debys'))

preco = 0
total = 0

while True:
        op = input('Qual Item desja (CP) ou (AC): ').upper().strip()
        if op == 'CP':
            tam = input('Qual Tamanho do Item (P, M ou G): ').upper().strip()
            if tam == 'P':
                preco = 9
                preco += preco
            elif tam == 'M':
                preco = 14
                preco += preco
            elif tam == 'G':
                preco = 18
                preco += preco
        elif op == 'AC':
            tam = input('Qual Tamanho do Item (P, M ou G): ').upper().strip()

        else:
            print('Valor invalido, tente novamente!')

        print(f'Você escolheu {op} e o preço é R$ {preco:.2f}!')
        while True:
            op2 = input('Deseja continuar comprando (S/N): ').upper().strip()
            if op2 != 'S' and op2 != 'N':
                print('Valor invalido, tente novamente!')
            elif op2 == 'N':
                break