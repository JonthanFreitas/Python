lista = []
cadastro = {}

while True:
    cadastro['Nome'] = str(input('Nome: '))
    while True:
        cadastro['Sexo'] = str(input('Sexo: [M/F]  ')).upper().strip()
        if cadastro['Sexo'] != 'M' and cadastro['Sexo'] != 'F':
            print('Valor invalido! Digite apenas M ou F')
            continue
        else:
            break

    cadastro['Idade'] = [int(input('Idade: '))]

    lista.append(cadastro.copy())

    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if op != 'S' and op != 'N':
            print('Valor invalido! Digite apenas S ou N')
        elif op == 'N':
            break
        else:
            break
    if op == 'N':
        break

media = sum(sum(pessoa['Idade']) for pessoa in lista) / len(lista)

nomes = []
for pessoa in lista:
    if pessoa['Sexo'] == 'F':
        nomes.append(pessoa['Nome'])
print('-=-' * 20)
print(f'A)  Ao todo temos {len(lista)} cadastradas')
print(f'B)  A média de idade é de {media} anos.')
print(f'C)  As mulheres cadastradas foram {nomes}')

print('D)  Lista das pessoas que estão acima da média:')
for pessoa in lista:
    if pessoa['Idade'][0] > media:
        print(     f"Nome = {pessoa['Nome']} ; Sexo = {pessoa['Sexo']}; Idade = {pessoa['Idade'][0]};")

mulher = {}
mulher['Mulher'] = nomes
lista.append(mulher.copy())

resumo = {}
resumo['Media'] = [media]
lista.append(resumo.copy())

print(lista)