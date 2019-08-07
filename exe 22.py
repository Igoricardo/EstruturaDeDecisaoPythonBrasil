print('''
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
''')
n = int(input('Informe um número inteiro: '))
if n%2 == 0:
    print(f'{n} é um N° PAR!')
else:
    print(f'{n} é um N° ÍMPAR!')