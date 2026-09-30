def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Digite um valor inteiro valido')

n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n}') 