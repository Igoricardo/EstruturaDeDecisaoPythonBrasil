print('''
Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.
''')
ano = int(input('Informe o ano que deseja analisar: '))
b1 = ano%4
b2 = ano%400
b3 = ano%100
#print(f'{b1} {b2} {b3}')
if b1 == 0 and b2 > 0 and b3 > 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é bissexto!')