print('''24. Faça um Programa que leia 2 números e em seguida 
pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
''')
n1 = float(input('Informe o 1° N°:' ))
n2 = float(input('Informe o 2° N°:' ))
opcao = str(input('Qual operador deseja usar? [+][-][*][/]: ')).strip()
if opcao == '+':
    r = n1 + n2
if opcao == '-':
    r = n1 - n2
if opcao == '*':
    r = n1 * n2
if opcao == '/':
    r = n1 / n2
print('O resultado é {}.'.format(r))
if r%2 == 0:
    print('O N° informado é PAR')
else:
    print('O N° informado é ÍMPAR')
if r < 0:
    print('O N° informado é NEGATIVO')
else:
    print('O N° informado é POSITIVO')
if r//1 == r:
    print('O N° informado é INTEIRO')
else:
    print('O N° informado é REAL')


