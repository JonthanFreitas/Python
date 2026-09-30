from math import factorial

print('Calcule o fatorial')
print()

n1 = int(input('Qual numero deseja calcular? '))

fatorial = factorial(n1)

c = n1

print(f'O fatoria de {n1} = ', end = '')

while c > 0 :
    if c > 1:
        print(f'{c} x ', end = '')
    elif c == 1:
        print(f'{c} = ', end = '')
    c -= 1
    continue
print(fatorial)


