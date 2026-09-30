num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o numero {num}')
print(f'Unidade de {u}')
print(f'Dezena de {d}')
print(f'Centena de {c}')
print(f'Milhar de {m}')
