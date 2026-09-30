from random import randint
from time import sleep
def sort(lista):
    '''
    :param lista: Lista de numeros sorteados
    :return:
    '''
    soma = 0
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        n = (randint(1, 10))
        print(n, end=' ')
        sleep(1)
        lista.append(n)

    print(f'\nOs numeros sorteados foram {lista} e os numeros pares foram: ', end='')

    for num in lista:
        if num % 2 == 0:
            print(num, end=' ')
            soma = soma + num

    print(f'\nE a soma deles foi: {soma}')

lista = []

sort(lista)

