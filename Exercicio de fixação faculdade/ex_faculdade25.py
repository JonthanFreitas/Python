num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op = int(input('Qual sua opção: '))

if op == 1:
    print(f'{num} convertido para BINARIO {bin(num)[2:]}')
elif op == 2:
    print(f'{num} convertido para OCTAL {oct(num[2:])}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL {hex(num)[2:]}')
