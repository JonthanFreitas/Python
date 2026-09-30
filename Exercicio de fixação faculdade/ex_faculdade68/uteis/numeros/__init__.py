def metade(num=0, formato=False):
    """
    Calcula a metade de um número.

    Parâmetros:
        num (float): número a ser dividido. Padrão: 0.
        formato (bool): se True, retorna o resultado formatado como moeda.
            Padrão: False.

    Retorna:
        float ou str: a metade de num, como número puro ou já formatada
        (ex: 'R$ 50,00'), dependendo de formato.
    """
    res = num/2
    return res if not formato else moeda(res)

def dobro(num=0, formato=False):
    """
    Calcula o dobro de um número.

    Parâmetros:
        num (float): número a ser multiplicado. Padrão: 0.
        formato (bool): se True, retorna o resultado formatado como moeda.
            Padrão: False.

    Retorna:
        float ou str: o dobro de num, como número puro ou já formatada
        (ex: 'R$ 200,00'), dependendo de formato.
    """
    res = num*2
    return res if not formato else moeda(res)

def moeda(preco=0, formato='R$'):
    """
    Formata um valor numérico como moeda.

    Parâmetros:
        preco (float): valor a ser formatado. Padrão: 0.
        formato (str): símbolo da moeda. Padrão: 'R$'.

    Retorna:
        str: o valor formatado com 2 casas decimais e vírgula
        (ex: 'R$  10,50').
    """
    return f'{formato} {preco:5.2f}'.replace('.', ',')

def resumo(num=0, desconto=0, acrescimo=0):
    """
    Exibe um resumo formatado de um valor: original, dobro, metade,
    acréscimo e desconto percentuais.

    Parâmetros:
        num (float): valor base a ser analisado. Padrão: 0.
        desconto (float): percentual de desconto a aplicar. Padrão: 0.
        acrescimo (float): percentual de acréscimo a aplicar. Padrão: 0.

    Retorna:
        None: apenas imprime o resumo no console.
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    d = num - (num * desconto / 100)
    a = num + (num * acrescimo / 100)

    print(f'{"Preço analisado:":<18}{moeda(num)}')
    print(f'{"Dobro do preço:":<18}{dobro(num, True)}')
    print(f'{"Metade do preço:":<18}{metade(num, True)}')
    print(f'{f"Acréscimo de {acrescimo}%:":<18}{moeda(a)}')
    print(f'{f"Desconto de {desconto}%:":<18}{moeda(d)}')
    print('-' * 30)