time = []
jogadores = {}

while True:
    jogadores['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["Nome"]} Jogou? '))

    jogadores['Gols'] = []

    for i in range(1,partidas+1):
        jogadores['Gols'].append(int(input(f'   Quantos gols na partida {i}°? ')))

    jogadores['Total'] = sum(jogadores['Gols'])
    time.append(jogadores.copy())

    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()
        if op != 'S' and op != 'N':
            print('Opção invalida! Digite apenas S ou N.')
        else:
            break
    if op == 'N':
        break
    continue

print('-=-'*30)
print(f'{"cod":<5} {"Nome":<15} {"Gols":<20} {"Total":<5}')
print('-' * 50)
for ind, jogador in enumerate(time):
    print(f'{ind + 1:<5} {jogador["Nome"]:<15} {str(jogador["Gols"]):<20} {jogador["Total"]:<5}')
print('-' * 50)
while True:
    op1 = int(input('Mostrar dados de qual jogador? (Digite 0 para sair): '))
    if op1 == 0:
        break
    if op1 < 1 or op1 > len(time):
        print(f'Não existe nenhum dado com o Digito {op1}')
        continue
    jogador = time[op1 - 1]

    print(f'-- LEVANTAMENTO DO JOGADOR {jogador["Nome"]}')
    for ind, gols in enumerate(jogador['Gols']):
        print(f' No jogo {ind + 1} fez {gols}')
    continue

