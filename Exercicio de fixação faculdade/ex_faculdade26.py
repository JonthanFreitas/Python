print('-=-' * 20)
#print(f'{Opcções de pagamento':=^40})
print('OPÇÕES DE PAGAMENTO'.center(40))
print('-=-' * 20)
print('1 - á vista no pix/dinheiro')
print('2 - à vista no cartão')
print('3 - em até 2x no cartão')
print('4 - em até 3x ou mais no cartão')
print('PARA SAIR DIGITE 0')
print('-=-' * 20)

while True:
    valor = float(input("Digite o valor do produto:R$ "))
    op = int(input('Digite a opção desejada: '))

    if valor == 0:
        print('Valor do produto invalido!')
        continue

    elif op == 0:
        print('Encerrando o programa...')
        break

    elif op == 1:
        desc = valor - valor * 0.10
        print(f'O valor do produto com desconto de 10% ficara R${desc:.2f}')
    elif op == 2:
        desc = valor - valor * 0.05
        print(f'O valor do produto em descont de 5% ficara R${desc:.2f}')
    elif op == 3:
        desc = valor / 2
        print(f'O valor total do protudo é R${valor:.2f}')
        print(f'O valor das parcelas em 2x ficaram em R${desc:.2f}')
    elif op == 4:
        while True:
            parcela = int(input('Qual a quantidade de parcelas: '))
            if parcela < 3:
                print('Nessa opção somente acima de 3x tente de novo...')
                continue
            else:
                desc = valor + valor * 0.20
                total_parcelas = desc / parcela
                print(f'O valor total do produto em {parcela}x ficara em R${desc:.2f} com os acrescimos')
                print(f'O valor das parcelas ficara em R${total_parcelas:.2f}')
                break
    else:
        print('Opção invalida!')
        continue