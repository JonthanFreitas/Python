print('-' * 20)
print('LANCHONETE')
print('-' * 20)
print('1 - Coxinha - R$ 8,00')
print('2 - Pastel  - R$ 7,00')
print('3 - Café    - R$ 4,00')
print('4 - Suco    - R$ 6,00')
print('5 - Sair')
print('-' * 20)

total = 0
while True:
    op = int(input('Qual item gostaria de comprar? '))


    if op == 1:
        qtd = int(input('Quantos itens comprar? '))
        total = total + qtd * 5.00
    elif op == 2:
        qtd= int(input('Quantos itens comprar? '))
        total = total + qtd * 7.00
        qtd= int(input('Quantos itens comprar? '))
    elif op == 3:
        qtd= int(input('Quantos itens comprar? '))
        total = total + qtd * 4.00
    elif op == 4:
        qtd= int(input('Quantos itens comprar? '))
        total = total + qtd * 6.00
    elif op == 5:
        break
    else:
        print('Produto invalido. Selecione outro!')

print(f'O total da compra foi R${total:.2f}')