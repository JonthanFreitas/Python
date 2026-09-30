def escreva(texto):
    print('-' * len(texto))
    print(texto.center(len(texto)))
    print('-' * len(texto))

while True:
    escreva(input('Digite uma frase: '))


