from random import randint
from time import sleep
cont = 0
jogadas = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)}

pos = sorted(jogadas.items(), key=lambda item: item[1], reverse=True)

for k,v in jogadas.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

print(f'{"RANKING DOS JOGADORES":=^29}')
sleep(1)
for k,v in pos:
    cont += 1
    print(f'  {cont}° Lugar: {k} com {v}')
    sleep(1)
