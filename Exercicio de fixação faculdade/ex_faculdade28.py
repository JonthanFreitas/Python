from random import randint

print('-=-' * 10)
print('VAMOS JOGAR IMPAR OU PAR'.center(29))
print('-=-' * 10)

cont = 0
jogadas = 0

while True:
    pc = randint(0, 10)

    s = (input('Escolha [I] ou [P]: ')).upper().strip()
    jogador = int(input('Digite um numero de 0 a 10: '))

    soma = pc + jogador

    if jogador <= -1:
        break

    if soma % 2 == 0 and s == 'P':
        print(f'Deu Par você ganhou! O computador escolheu {pc} e Você escolheu {jogador} a soma é {soma}.')
        jogadas += 1

    elif soma % 2 == 0 and s == 'I':
        print(f'Deu Par você perdeu! O computador escolheu {pc} e Você escolheu {jogador} a soma é {soma}.')

    elif soma % 2 == 1 and s == 'I':
        print(f'Deu Impar você ganhou! O computador escolheu {pc} e Você escolheu {jogador} a soma é {soma}.')
        jogadas += 1

    elif soma % 2 == 1 and s == 'P':
        print(f'Deu Impar você Perdeu! O computador escolheu {pc} e Você escolheu {jogador} a soma é {soma}.')

    cont += 1



print(f'Você ganhou {jogadas} vezes e preciso {cont} vezes')




