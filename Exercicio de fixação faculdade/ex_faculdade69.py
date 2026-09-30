def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor válido!')
        except KeyboardInterrupt:
            print('\nO usuário prefiriu não digitar um valor!')
            return None
        else:
            return valor

def leiaReal(msg):
    while True:
        try:
            valor = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor válido!')
        except KeyboardInterrupt:
            print('\nO usuário prefiriu não digitar um valor!')
            return None
        else:
            return valor

Real = None

num = leiaInt('Digite um numero: ')
if num is not None:
    Real = leiaReal('Digite um valor Real: ')
if num is not None and Real is not None:
    print(f'O valor digitado foi {num} \nE o valor real foi {Real}')