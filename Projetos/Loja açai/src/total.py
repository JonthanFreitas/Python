
def mostra_total(pedido, total):
    """Imprime o recibo do pedido com cada item e o total a pagar.

    Parâmetros:
        pedido: lista de itens; cada item é (código, tamanho, preço),
                por exemplo ('CP', 'M', 14). O código é 'AC' (Açaí)
                ou 'CP' (Cupuaçu).
        total: valor final a pagar, mostrado na última linha. A função
               só imprime esse valor, não soma os itens.

    Não devolve nada; só imprime na tela.
    """
    # Cabeçalho do recibo, com o título centralizado em 33 caracteres
    print("=" * 33)
    print('LOJA DE AÇAÍ DA DEBYS'.center(33))
    print("=" * 33)
    print()

    # Títulos das colunas
    print('Item             Tam.       Valor')

    # Uma linha para cada item do pedido
    for item in pedido:
        op = item[0]      # código do produto: 'AC' ou 'CP'
        tam = item[1]     # tamanho: P, M ou G
        preco = item[2]   # preço do item

        # Troca o código pelo nome do produto
        if op == 'AC':
            produto = 'Açaí'
        elif op == 'CP':
            produto = 'Cupuaçu'

        # Formatação em colunas:
        # {produto:<16} -> alinha à esquerda, ocupando 16 caracteres
        # {tam:<10}     -> alinha à esquerda, ocupando 10 caracteres
        # {preco:>5.2f} -> alinha à direita, 5 caracteres, 2 casas decimais
        print(f'{produto:<16} {tam:<10} R$ {preco:>5.2f}')

    # Rodapé com o total
    print()
    print('-' * 33)
    print(f'{"TOTAL:":<25} R$ {total:>5.2f}')
    print("=" * 33)