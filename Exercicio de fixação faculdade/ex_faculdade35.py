compras = (
    ('arroz', 25.90),
    ('feijão', 8.50),
    ('leite', 4.30),
    ('ovos', 12.00),
    ('pão', 7.20),
    ('café', 18.90),
    ('açúcar', 5.40),
    ('manteiga', 14.50)
)
print('-=-' * 14)
print('MERCADINHO DA DEBYS'.center(40))
print('-=-' * 14)

for pos in compras:
    print(f'{pos[0]:.<30}', f'R$ {pos[1]:.2f}')

print('-=-' * 14)