from random import randint
print('-=-' * 20 )
print('Adivinhe em que numero estou pensando entre 0 e 5.Digite 10 para sair')
print('-=-' * 20 )

while True:
    computador = randint(0, 5)
    jogador = int(input('Em que numero estou pensando entre 0 e 5? '))

    if jogador == 10:
        print('Programa encerrado')
        break

    if jogador > 5:
        print('Numero invalido')
        continue

    if jogador == computador:
        print(f'Você acertou!, o numero que eu estava pensado era {computador}')
        print('-=-' * 20)
    else:
        print(f'Você perdeu! O numero que eu estava pensado era {computador}')
        print('-=-' * 20)
print('-=-' * 20 )



