nome = str(input("Digite seu nome completo: ")).strip()

print('Analisando o seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minusculas {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separar = nome.split()
print(f'Seu primeiro nome é {separar[0], len(separar[0])} letras')
