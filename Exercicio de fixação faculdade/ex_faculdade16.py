def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo!')
    else:
        print('Arquivo criado com sucesso!')

def cadastrarJogo(arquivo, nomeJogo, nomevideogame):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao criar o arquivo!')
    else:
        a.write(f'{nomeJogo};{nomevideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()
# Programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo existe!')
else:
    print('Arquivo nâo existe!')
    criarArquivo(arquivo)


while True:
    print('MENU')
    print('1 - Cadastro novo item')
    print('2 - Lista de cadastro')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Saindo do sistema...')
        break