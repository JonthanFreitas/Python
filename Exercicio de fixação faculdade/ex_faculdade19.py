cadastro = []

mulhes_jovens = []

homens_velhos = []

while True:
    terminal = input('Deseja inserir um cadastro? [S/N]: ')
    if terminal.upper() in 'S':
        break
    if terminal.upper() not in 'N':
        print('Digite S para SIM ou N para NÃO')
        continue

while True:
    nome = input('Qual seu nome? Deseja sair? [S/N]: ')
    if nome.upper() in 'S':
        break
    sexo = input('Qual seu sexo? ')
    ano  = input('Qual seu ano de nascimento? ')

    pessoas = {
        'nome': nome,
        'sexo': sexo,
        'ano': ano,
    }
    cadastro.append(pessoas)

soma_idade = 0
for p in cadastro:
    idade = 2026 - int(p['ano'])
    soma_idade += idade

media_idade = soma_idade / len(cadastro) if len(cadastro) > 0 else 0

for mulher in cadastro:
    if mulher['sexo'] == 'f' and (2026 - int(mulher['ano'])) < 30:
        mulhes_jovens.append(mulher)

idade_homens = 0
for homen in cadastro:
    if homen['sexo'] == 'm':
        idade_homens = 2026 - int(homen['ano'])
        if idade_homens > media_idade:
            homens_velhos.append(homen)

print('\n--- Cadastro de pessoas ---')
print(f'{'nome':<15}{'sexo':<10}{'ano':<10}')
for p in cadastro:
    print(f'{p['nome']:<15}{p['sexo']:<10}{p['ano']:<10}')
print('-' * 55)

print('\n--- Cadastro de Mulhes com menos de 30 anos ---')
print(f'{'nome':<15}{'sexo':<10}{'ano':<10}')
for mulher in mulhes_jovens:
    print(f'{mulher['nome']:<15}{mulher['sexo']:<10}{mulher['ano']:<10}')
print('-' * 55)

print('\n--- Cadastro de Homens com idade a cima da media ---')
print(f'{'nome':<15}{'sexo':<10}{'ano':<10}')
for homen in homens_velhos:
    print(f'{homen['nome']:<15}{homen['sexo']:<10}{homen['ano']:<10}')

print('-' * 55)
print(f'Total de pessoas cadastradas: {len(cadastro)}')
print(f'Média de idade: {media_idade:.1f}')
print('-' * 55)
