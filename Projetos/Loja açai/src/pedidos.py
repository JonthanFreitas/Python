from time import sleep
import mysql.connector
from total import mostra_total

def fazer_pedidos():

    """Recebe os pedidos do cliente e calcula o total a pagar.

    Pergunta o item (CP ou AC) e o tamanho (P, M ou G), busca o preço
    na tabela e soma no total. Pergunta se o cliente quer continuar
    comprando; ao terminar (N ou SAIR), mostra o total a pagar.
    Se o item ou o tamanho não existir, avisa e pergunta de novo.
    """

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SUA_SENHA',
        database='loja_acai'
    )

    cursor = conexao.cursor()

    total = 0  # soma de tudo que o cliente pediu
    pedidos = []



    while True:  # repete até o cliente encerrar
        # Lê o item; .upper() deixa maiúsculo e .strip() tira espaços
        op = input('Qual Item deseja (CP) ou (AC): ').upper().strip()

        if op != 'CP' and op != 'AC':
            print('Valor invalido, tente novamente!')
            continue

        # Se digitou SAIR, mostra o total e termina o programa
        if op == 'SAIR':
            print('Encerrando...')
            sleep(1)
            print(f'Total a pagar: R$ {total:.2f}')
            break

        # Se o item não for CP nem AC, avisa e volta a perguntar
        if op != 'CP' and op != 'AC':
            print('Valor invalido, tente novamente!')
            print('-' * 33)
            continue

        # Lê o tamanho e monta a chave, ex.: 'CP' + '_' + 'M' = 'CP_M'
        tam = input('Qual Tamanho do Item (P, M ou G): ').upper().strip()

        if op == 'CP':
            nome_produto = 'Cupuaçu'
        else:
            nome_produto = 'Açaí'

        cursor.execute(
            "select preco from produtos where nome = %s and tamanho = %s",
            (nome_produto, tam)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            print('Produto ou tamanho não encontrado!')
            print('-' * 33)
            continue

        preco = resultado[0]
        total += preco
        pedidos.append([op, tam, preco])
        print('-' * 33)
        print(f'Você escolheu {op} ({tam}) e o preço é R$ {preco:.2f}!')
        print('-' * 33)

        # Pergunta se quer continuar até receber S ou N
        while True:
            op2 = input('Deseja continuar comprando (S/N): ').upper().strip()
            print('-' * 33)

            if op2 != 'S' and op2 != 'N':
                print('Valor invalido, tente novamente!')

            elif op2 == 'N':
                # N: mostra o total e sai deste laço
                sleep(1)
                mostra_total(pedidos,total)
                break

            elif op2 == 'S':
                # S: sai deste laço e volta a pedir outro item
                break

        # Se a resposta foi N, sai também do laço principal
        if op2 == 'N':
            break