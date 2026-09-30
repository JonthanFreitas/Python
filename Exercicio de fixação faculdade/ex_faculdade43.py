galera = []
dado = []
maior_idade = 0
menor_idade = 0

for i in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pos in galera:
    if pos[1] >= 18:
        print(f'{pos[0]} é maior de idade.')
        maior_idade += 1

    else:
        print(f'{pos[0]} é menor de idade.')
        menor_idade += 1

print(f'Total de maior de idade: {maior_idade}')
print(f'Total de menor de idade: {menor_idade}')