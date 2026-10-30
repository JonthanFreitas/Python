print(20 * '-')
print('CALCULO DE KWH')
print(20 * '-')
print('1 - Residencial')
print('2 - comercial')
print('3 - industrial')
print('Digite exite para encerrar o programa')

kwh  = float(input('Digite o KWH: '))
tipo = input('Digite a opção desejda: ')

if tipo == '1' and kwh <= 500:
    valor_conta = kwh * 0.40
    print(f'O valor a pagar pela conta residencial será de R$ {valor_conta:.2f}')

elif tipo == '1' and kwh > 500:
    valor_conta = kwh * 0.65
    print(f'O valor a pagar pela conta residencial será de R$ {valor_conta:.2f}')

elif tipo == '2' and kwh <= 1000:
    valor_conta = kwh * 0.55
    print(f'O valor a pagar pela conta Comecial será de R$ {valor_conta:.2f}')

elif tipo == '2' and kwh > 1000:
    valor_conta = kwh * 0.60
    print(f'O valor a pagar pela conta Comecial será de R$ {valor_conta:.2f}')

elif tipo == '3' and kwh <= 5000:
    valor_conta = kwh * 0.55
    print(f'O valor a pagar pela conta industrial será de R$ {valor_conta:.2f}')

elif tipo == '3' and kwh > 5000:
    valor_conta = kwh * 0.60
    print(f'O valor a pagar pela conta industrial será de R$ {valor_conta:.2f}')
    
else:
    print('Encerrando o programa')

