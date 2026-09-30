numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

Continue = True

while Continue:
    n1 = int(input('Digite um numero de 0 a 20: '))
    if n1 < 0 or n1 > 20:
        print('Numero invalido! Digite um numero entre 0 e 20')
        continue
    print(f'O numero digitado foi {numeros[n1]}')
    print('-' * 30)

    op = ''
    while op != 'N' and op != 'S':
        op = input('Quer continuar? [S/N] ').upper().strip()
        if op != 'S' and op != 'N':
            print('Digite uma opcao valida!')

    if op == 'N':
        Continue = False