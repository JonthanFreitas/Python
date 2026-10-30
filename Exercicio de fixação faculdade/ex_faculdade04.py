preco = float(input('Digite o preço: '))
desc = float(input('Digite o porcentagem de desconto: '))

desconto = preco * (desc / 100)

final = preco - desconto

print(f'O preço do produto é {preco}. Desconto de {desconto}%')
print(f'Valor calculado de desconto: {desconto}. valor final do produto: {final}')




