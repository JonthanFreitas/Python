jogos = {}

jogos['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogos["Nome"]} Jogou? '))

jogos['Gols'] = []

for i in range(1,partidas+1):
    jogos['Gols'].append(int(input(f'   Quantos gols na partida {i}°? ')))

jogos['Total'] = sum(jogos['Gols'])

print('-=-'*20)
print(jogos)
print('-=-'*20)
for k, v in jogos.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-'*20)
print(f'O Jogador {jogos["Nome"]} jogou {partidas} partidas.')


for ind, num in enumerate(jogos['Gols']):
    print(f'  => Na partida {ind+1}°, fez {num} gols.')

print(f'Foi um total de {jogos["Total"]} gols.')
