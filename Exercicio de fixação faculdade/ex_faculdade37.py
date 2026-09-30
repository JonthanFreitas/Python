lista = []
maior = None
menor = None

for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    for n in lista:
        if maior is None or n > maior:
            maior = n
        if menor is None or n < menor:
            menor = n

print('-=' * 30)
print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} nas posiçes ', end='')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f'{pos}... ', end='')

print()

print(f'O menor valor digitado foi {menor} nas posições ', end = '')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(f'{pos}... ', end='')