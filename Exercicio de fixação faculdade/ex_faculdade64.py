def ficha(jog = '<Desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')

n = str(input('Jogador: '))
g = str(input('Gol: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)


