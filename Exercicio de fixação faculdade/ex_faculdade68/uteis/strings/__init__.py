def leiaDinheiro(msg):
    while True:
        entrada = (input(msg).replace(',', '.'))
        try:
            valor = float(entrada)
        except ValueError:
            print(f'ERRO: "{entrada}" não é um valor valido!')
        else:
            return valor
