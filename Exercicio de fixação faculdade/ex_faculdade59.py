def maior(*num):
    print('-=' * 40)
    print('Analisando os maiores valores passados...')
    m = max(num, default=0)
    if len(num) > 0:
        nums_texto = num
    else:
        nums_texto = 0
    print(f'Os numeros digitados foram {nums_texto}, sendo informados {len(num)} valores ao todo.\nO maior valor informado foi {m}')


maior(2, 5, 3, 4, 8, 9)
maior(4, 5, 6)
maior(8, 9)
maior()
