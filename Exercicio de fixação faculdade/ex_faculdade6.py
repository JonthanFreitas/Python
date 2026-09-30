print ('CALCULADORA')
print ('+ Adição')
print ('- Subtração')
print('* Mutiplicação')
print ('/ Divisão')
print('Digite qualquer tecla para sair')

op = input ('Qual operaçãoes deseja realizar? ')
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))

if op not in "+-*/":
    print('Calculadora encerrada')

elif op == '+':
    soma = (x + y)
    print(f' O valor da adição entre {x} + {y} = {soma}')
elif op == '-':
    sub = (x - y)
    print(f'O valor da subtração entre {x} - {y} = {sub}')
elif op == '*':
    mult = (x * y)
    print(f'O Valor da multiplicação entre {x} * {y} = {mult}')
elif op == '/':
    div = (x / y)
    print(f'O valor da divisão entre {x} / {y} = {div}')





