import mysql.connector


def cadastro_cliente():
    """Faz o login ou o cadastro de um cliente da loja de açaí.

    Pede o CPF e procura o cliente na tabela `cliente`:
    - Se encontrar, pede a senha até o cliente acertar (login).
    - Se não encontrar, pede nome, telefone, e-mail e senha, confere
      cada campo e grava o novo cliente no banco (cadastro).

    Não recebe parâmetros e não devolve nada: toda a conversa com o
    usuário é feita com input() e print().
    """
    # Cabeçalho da tela, centralizado em 30 caracteres
    print('-' * 30)
    print('Açai da Debys'.center(30))
    print('-' * 30)

    # Abre a conexão com o banco de dados MySQL
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SUA_SENHA',
        database='loja_acai'
    )

    # ---------- Passo 1: ler e validar o CPF ----------
    while True:
        cpf = input('Digite seu CPF: ').strip()  # .strip() tira espaços

        # .isdigit() é False se tiver letra, espaço, ponto ou traço
        if not cpf.isdigit():
            print('CPF deve conter apenas números.')
            continue

        # O CPF precisa ter exatamente 11 dígitos
        if len(cpf) != 11:
            print('CPF deve ter 11 números.')
            continue

        break  # CPF válido: sai do laço

    # ---------- Passo 2: procurar o cliente pelo CPF ----------
    cursor = conexao.cursor()
    # Os %s são preenchidos com segurança pelo conector (evita SQL injection)
    cursor.execute(
        'select * from cliente where cpf = %s',
        (cpf,)
    )

    # fetchone() devolve a primeira linha encontrada, ou None se não houver
    cliente = cursor.fetchone()

    if cliente:
        # ---------- Caminho A: cliente já cadastrado (login) ----------
        print('Cliente encontrado!')

        # cliente é uma linha do banco; o índice 5 é a coluna senha
        # (a ordem é a das colunas da tabela: id, nome, telefone,
        # email, cpf, senha)
        senha_cadastrada = cliente[5]
        while True:
            senha = input('Digite sua senha: ')

            if senha == senha_cadastrada:
                print('Login realizado com sucesso!')
            else:
                print('Senha incorreta.')
                continue  # errou: pergunta de novo

            break  # acertou: sai do laço
    else:
        # ---------- Caminho B: cliente novo (cadastro) ----------
        print('Cliente não encontrado.')
        print('Para continuar, vamos realizar seu cadastro.')
        print('-' * 30)

        # Nome: não pode ficar vazio
        while True:
            nome = input('Digite seu nome: ').strip()

            if not nome:
                print('O nome não pode ficar vazio.')
                continue

            break

        # Telefone: só números e 11 dígitos (DDD + número)
        while True:
            telefone = input('Digite seu telefone: ').strip()

            if not telefone.isdigit():
                print('Telefone deve conter apenas números.')
                continue

            if len(telefone) != 11:
                print('Telefone deve ter 11 números.')
                continue

            break

        # E-mail: confere só se tem "@" e "." (validação simples)
        while True:
            email = input('Digite o seu e-mail: ').strip()

            if "@" not in email or "." not in email:
                print('E-mail inválido.')
                continue

            break

        # Senha: mínimo de 6 caracteres
        while True:
            senha = input('Crie sua senha: ').strip()

            if len(senha) < 6:
                print('A senha deve ter pelo menos 6 caracteres.')
                continue

            break

        # Grava o novo cliente na tabela
        cursor.execute(
            '''
            insert into cliente (nome, cpf, telefone, email, senha)
            values (%s, %s, %s, %s, %s)
            ''',
            (nome, cpf, telefone, email, senha, )
        )

        # commit() confirma a gravação; sem ele o cadastro não fica salvo
        conexao.commit()

        print('Cadastro preenchido com sucesso!')