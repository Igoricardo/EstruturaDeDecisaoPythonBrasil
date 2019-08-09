print('''23. Faça um Programa que peça um número e informe 
se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
''')
n = float(input('Informe um N°: '))
if n//1 == n:
    print('INTEIRO')
else:
    print('REAL')
