import mysql.connector

def mostrar_cardapio():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SUA_SENHA',
        database='loja_acai'
    )
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    print('Bem-vindo a lojá de açai da Debys')
    print('-' * 33)

    print(f'{"Item":<12}{"Tam"}{"Valor":>12}')
    print('-' * 33)

    for item in produtos:
        nome = item[1]
        tam = item[2]
        preco = item[3]

        print(f'{nome:<10} | {tam} | {preco:>10}')


    print('-' * 33)
    print('Digite "Sair" para encerrar')
    print('-' * 33)