print('PAGAMENTOS')
print('1 - à vista')
print('2 - Parcelamento em 3x')
print('3 - Parcelamento em 5x')
print('4 - Parcelamento em 10x')
print('Pressione outra tecla para sair')

valor = float(input('Digite o valor da compra: '))
parcela = input('Digite a forma de pagamento: ')

if valor == 0:
    print('Calculo encerrado')
else:

    if parcela not in '1234':
        print('Calculo errado ou sistema encerrado')

    elif parcela == '1':
        avista = valor * 0.95
        print(f'O valor total a pagar à vista é de R${avista:.2f}')

    elif parcela == '2':
        parcela3x = valor / 3
        print(f'O valor parcelado em 3x ficaria 3x de R${parcela3x:.2f}')

    elif parcela == '3':
        parcela5x = (valor * 1.02) / 5
        print(f'O valor a pagar em 5x ficaria 5x de R${parcela5x:.2f}')

    elif parcela == '4':
        parcela10x = (valor * 1.08) / 10
        print(f'O valor a pagar em 10x ficaria 10x de R${parcela10x:.2f}')