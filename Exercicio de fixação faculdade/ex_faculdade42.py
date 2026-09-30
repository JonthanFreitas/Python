lista = []
valida = True

expr = str(input('Digite uma expressão: '))

for i in expr:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) == 0:
            valida = False
            break
        else:
            lista.pop()

if valida and len(lista) == 0:
    print('Expressão valida')
else:
    print('expreção invalida')
