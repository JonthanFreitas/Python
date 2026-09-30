from random import randint
from time import sleep

mega = []
num = []


print('-' * 30)
print('JOGAR NA MEGA SENA'.center(30))
print('-' * 30)

n1 = int(input('Quantos jogos deseja jogar: '))
print('-' * 30)
sleep(1)
print(f'Sorteando {n1} jogos')

for i in range(0, n1):
    for c in range(0, 6):
        rando = randint(1, 60)
        while rando in num:
            rando = randint(1, 60)
        num.append(rando)

    num.sort()
    print(f'Jogo {i+1}:', end='')
    for n in num:
        print(f'[{n:02d}]', end=' ')
    print()
    sleep(0.7)
    mega.append(num[:])
    num.clear()
