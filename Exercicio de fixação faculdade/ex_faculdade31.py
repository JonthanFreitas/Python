lanche = ('Hambúger', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(lanche[cont])
print()

for comida in lanche:
    print(f'Eu vou comer {comida}')
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')