inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja finalizar a contagem? '))

if inicial % 2 != 0:
    inicial += 1
for i in range(inicial, final + 1, 2 ):
    print(i)