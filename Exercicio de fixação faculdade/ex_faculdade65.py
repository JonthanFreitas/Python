def notas(*num, sit = False):
    """
    Analisa um conjunto de notas e retorna estatísticas básicas.

    Parâmetros:
        *num (float): quantidade variável de notas (ex: 5.5, 7, 10).
        sit (bool, opcional): se True, inclui no resultado a situação
            do aluno com base na média ('BOA', 'RAZUAVEL' ou 'RUIM').
            Padrão: False.

    Retorna:
        dict: dicionário contendo:
            - 'total' (int): quantidade de notas informadas.
            - 'maior' (float): maior nota.
            - 'menor' (float): menor nota.
            - 'Média' (float): média das notas.
            - 'Situação' (str, opcional): presente somente se sit=True.
                'BOA' se média >= 7, 'RAZOÁVEL' se média >= 5,
                'RUIM' caso contrário.

    Exemplo:
        >>> notas(5.5, 2.5, 2, 10, 10, 10, sit=True)
        {'total': 6, 'maior': 10, 'menor': 2, 'Média': 6.666666666666667, 'Situação': 'RAZOÁVEL'}
    """
    alunos = {}
    alunos['total'] = len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['Média'] = sum(num) / len(num)
    if sit:
        if alunos['Média'] >= 7:
            alunos['Situação'] = 'BOA'
        elif alunos['Média'] >= 5:
            alunos['Situação'] = 'RAZOAVEL'
        else:
            alunos['Situação'] = 'RUIM'
    return alunos


resp = notas(5.5, 2.5, 2, 10, 10, 10,  sit = True)
print(resp)

