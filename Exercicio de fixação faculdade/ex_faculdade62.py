def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade >= 16 and idade < 18 or idade >= 70:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATORIO.')


while True:
    ano = int(input("Digite o ano de nascimento: "))
    if ano == 0:
        break
    voto(ano)
