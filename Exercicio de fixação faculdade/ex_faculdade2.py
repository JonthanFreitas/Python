km = float(input('Quantos kilometros deseja pagar: '))
dias = int(input('Quantos dias deseja pagar: '))

total_km = km * 0.15
total_dias = dias * 60
total = (total_km + total_dias)

print(f'valor a pagar por km é de R$ {total_km:.2f}')
print(f'Valor a pagar por dias é de R$ {total_dias:.2f}')
print(f'Valor a pagar pelo aluguel é de R$ {total:.2f}')
