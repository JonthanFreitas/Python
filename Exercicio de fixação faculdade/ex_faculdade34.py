num = []
cont = 0

for i in range(5):
    i = int(input('Digite um numero: '))
    num.append(i)
    if i == 9:
        cont += 1

print('-' * 30)
tupla = tuple(num)
print(f'Numeros digitados {tupla}')
print('-' * 30)
print(f'O numero 9 aparece {cont} vezes')
print('-' * 30)

try:
    pos = tupla.index(3) + 1
    print(f'A pocisão que o numero 3 aprecere é {pos}ª')
    print('-' * 30)
except ValueError:
    print('O numero 3 não aparece em nenhuma pocisão')
    print('-' * 30)
print('Os numeros pares são', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

