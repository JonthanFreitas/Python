print('=' * 30)
print('BANCO DA DEBYS'.center(30))
print('=' * 30)


saque = float(input('Qual Valor deseja sacar? R$'))

if saque // 100 > 0:
    quantidade = saque // 100
    print(f'Quantidade de notas de 100: {quantidade:.0f}')
    saque = saque % 100
if saque // 50 > 0:
    quantidade = saque // 50
    print(f'Quantidade de notas de 50: {quantidade:.0f}')
    saque = saque % 50
if saque // 20 > 0:
    quantidade = saque // 20
    print(f'Quantidade de notas de 20: {quantidade:.0f}')
    saque = saque % 20
if saque // 10 > 0:
    quantidade = saque // 10
    print(f'Quantidade de notas de 10: {quantidade:.0f}')
    saque = saque % 10
if saque // 5 > 0:
    quantidade = saque // 5
    print(f'Quantidade de notas de 5: {quantidade:.0f}')
    saque = saque % 5
if saque // 1 > 0:
    quantidade = saque // 1
    print(f'Quantidade de notas de 1: {quantidade:.0f}')
    saque = saque % 1

