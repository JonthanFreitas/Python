lista = []
media = 0
sair = False

while True:
    print('-' * 30)
    print(f"{'CADASTRO DE ALUNOS':^30}")
    print('-' * 30)
    while True:
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))

        lista.append([nome, nota1, nota2])

        while True:
            st = str(input('Deseja continuar? [S/N] ')).upper().strip()
            if st != 'S' and st != 'N':
                print('Opção invalida! Digite apenas S ou N')
                continue
            else:
                break

        if st == 'N':
            print(f"{'N°':<6}{'Nome':<14}{'Media':<6}")
            print('-' * 30)

            for pos, pos2 in enumerate(lista):
                media = (pos2[1] + pos2[2]) / 2
                print(f'{pos+1:<5} {pos2[0]:<14} {media:<6}')
                print('-' * 30)

            while True:
                print(f"{'OPCÕES':-^30}")
                print('1 - NOTAS GERAIS/CADASTRO')
                print('2 - NOTAS INDIVIDUAL')
                print('3 - MEDIA DE NOTAS INDIVIDUAL')
                print('4 - VOLTAR A CADASTRAR')
                print('5 - SAIR')

                op = int(input('Digite um opção: '))

                if op == 1:
                    for pos in lista:
                        print(f'{pos}')

                if op == 2:
                    op2 = int(input(f'Digite o N° do aluno desejado: (Digite de 1 até {len(lista)}) '))

                    if 1 <= op2 <= len(lista):
                        aluno = op2 - 1
                        print(f'Aluno: {lista[aluno][0]}')
                        print(f'Nota 1°: {lista[aluno][1]}')
                        print(f'Nota 2°: {lista[aluno][2]}')
                    else:
                        print('Numero invalido!')

                if op == 3:
                    op2 = int(input(f'Digite o N° do aluno desejado: (Digite de 1 até {len(lista)})'))

                    if 1 <= op2 <= len(lista):
                        aluno = op2 - 1
                        indmedia = ((lista[aluno][1]) + (lista[aluno][2])) / 2
                        print(f'Aluno: {lista[aluno][0]}')
                        print(f'Media: {indmedia}')

                if op == 4:
                    break

                if op == 5:
                    print('Saindo do sistema')
                    sair = True
                    break

        if sair:
            break

        if st == 'N':
            break

    if sair:
        break
