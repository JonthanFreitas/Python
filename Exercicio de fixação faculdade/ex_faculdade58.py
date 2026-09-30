from time import sleep


def cont(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} -> ', end='')
            sleep(0.5)
            cont += passo
        print('Fim!!!!')

    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} -> ', end='')
            sleep(0.5)
            cont -= passo
        print('Fim!!!!')

cont(1,10,1)
cont(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
cont(ini, fim, pas)



