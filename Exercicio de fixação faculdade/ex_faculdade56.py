def calcula_area(largura, comprimento):
    return largura * comprimento


while True:
    print('Controle de Terrenos')
    print('-' * len('Controle de Terrenos'))
    lar = int(input('Largura (m): '))
    com = int(input('Comprimento (m): '))
    print(f'A área de um terreno {com:.2f} x {lar:.2f} é de {calcula_area(com, lar):.2f}m°')
    while True:
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        print('-' * len('Deseja continuar? [S/N]: '))
        if op != 'S' and op != 'N':
            print('Valor invalido! Digite apenas S ou N')
            continue
        else:
            break
    if op == 'N':
        break
    continue