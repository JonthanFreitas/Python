palavras = (
    'python',
    'programa',
    'variavel',
    'funcao',
    'laço',
    'tupla',
    'lista',
    'dicionario',
    'condicao',
    'algoritmo'
)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
