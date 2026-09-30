from datetime import date

dados = {}

dados['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - idade
dados['Ctps'] = int(input('Carteira de trabalho (Digite 0 caso não tenha): '))


if dados['Ctps'] == 0:
    print('-=-' * 20)
    for k,v in dados.items():
        print(f'  - {k} tem o valor {v}')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] =  62 - dados['idade']
    print('-=-' * 20)
    for k,v in dados.items():
        print(f'  - {k} tem o valor {v}')


