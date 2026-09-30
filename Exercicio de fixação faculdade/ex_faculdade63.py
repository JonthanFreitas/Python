def fac(num, show=False):
    '''
      --> Calcula o fatorial de um número.
    :param num: número a ser calculado o fatorial
    :param show: (opcional) mostra ou não o processo do cálculo
    :return: o valor do fatorial de num
    '''
    fat = 1
    for i in range(num, 0 , -1):
        if show:
            print(i, end = '')
            if i > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        fat *= i
    return fat

n = int(input('Calcule o factorial: '))
print(fac(n, show=True))