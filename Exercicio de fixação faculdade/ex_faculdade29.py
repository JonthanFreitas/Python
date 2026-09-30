print('-' * 30)
print('LOJA DA DEBYS'.center(30))
print('-' * 30)

maior = None
menor = None
total_produtos = 0
total = 0
acima_mil = 0
produto_maior = ''
produto_menor = ''

while True:
    produto = str(input('Digite o nome do produto: ')).strip()

    if produto == '':
        print('Nome invalido! Digite o nome do produto')
        print('-' * 30)
        continue

    try:
        preco = float(input('Preço: R$ '))
    except ValueError:
        print('Valor invalido! Digite um valor valido')
        print('-' * 30)
        continue

    if preco <= 0:
        print('Valor invalido! Digite um valor valido')
        print('-' * 30)
        continue

    total_produtos += 1

    if menor is None or preco < menor:
        menor = preco
        produto_menor = produto
    if maior is None or preco > maior:
        maior = preco
        produto_maior = produto

    if preco >= 1000:
        acima_mil += 1
    total += preco

    final = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if final == 'N':
        break


print('-' * 30)

print(f'O total da compra foi R${total:.2f}')
print(f'O total de produtos foi {total_produtos}')
print(f'O maior valor foi {produto_maior} custando R${maior:.2f}')
print(f'O menor valor foi {produto_menor} custando R${menor:.2f}')
print(f'A {acima_mil} produto acima dos R$1.000.00')