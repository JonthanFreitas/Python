palavaras = ('Mario', 'Luigi', 'Peche', 'Yoshi', 'Browser')

for palavra in palavaras:
    print(f'\nPalavra: {palavra.upper()}. vovais:')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')
