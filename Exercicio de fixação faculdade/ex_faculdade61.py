def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input('Digite um numero: '))
print(fatorial(n))

def par (n=0):
    if n % 2 == 0:
        print('É par!')
    else:
        print('Não é par')

num = int(input('Digite um numero: '))
print(par(num))