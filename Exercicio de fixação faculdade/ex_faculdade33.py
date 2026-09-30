from random import randint

num = tuple(randint(1, 10)for i in range(5))

maior = max(num)
menor = min(num)

print(f'Os numeros sorteados foi {num}')
print(f'O maior numero gerado foi {maior}')
print(f'O menos numero gerado foi {menor}')
