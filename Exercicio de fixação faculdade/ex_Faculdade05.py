a = int(input('Digite o 1° lado do tiangulo: '))
b = int(input('Digite o 2° lado do tiangulo: '))
c = int(input('Digite o 3° lado do tiangulo: '))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print('Triangulo Escaleno')
        else:
            if (a == b and b == c):
                print('Triangulo Equilatero')
            else:
                print('Triangulo isósceles')

    else:
        print('Ao menos um dos valores indicados não serve para formar um triangulo')

else:
    print ('Ao menos um dos valores indicados não serverem para formar um triangulo')


