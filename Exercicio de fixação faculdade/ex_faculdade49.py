pessoas = {'nome': 'Pedro', 'idade': 25, 'Sexo': 'M'}
pessoas['peso'] = 98.54
print(pessoas.items())
print(pessoas.values())
print(pessoas.keys())
print()
print(pessoas['nome'])
print(f"{pessoas['Sexo']:-^20}")
print(f"{pessoas['idade']:-^20.1f}")
print()
del pessoas['nome']
pessoas['Nome'] = 'Pedro'
for k,v in pessoas.items():
    print(f'{k}: {v}')
brasil = []
estado1 = {"UF": "São Paulo", "Sigla": "SP"}
estado2 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['UF'])
print(brasil[0]['Sigla'])
print(brasil[1]['UF'])
print(brasil[1]['Sigla'])
print()

estado = {}

for i in range (0,3):
    estado['UF'] = str(input('Unidade Federativa:[UF] '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')