print('-' * 20)
print('TABUADA')
print('-' * 20)

x = int(input('Digite o numero para calcular a tabuada: '))
y = int(input('Digite o numero para calcular o fim da tabuada: '))
print('-' * 20)

for numero_atual in range(x, y + 1 ):
    print(f'TABUADA DO {numero_atual}')
    for i in range(1, 11):
        print(f'{numero_atual} x {i} = {numero_atual * i}')

    print('-' * 20)
