while True:
    idade =  int(input('Qual sua idade? '))
    sexo = input('Qual seu genero (M ou F)? ')
    if sexo == 'f':
        if idade <= 0:
            print('Fim do programa')
            break
        print(f'Boa noite senhora! Sua idade é {idade} ')
    elif sexo == 'm':
        print(f'Boa noite senhor! Sua idade é {idade} ')
        continue