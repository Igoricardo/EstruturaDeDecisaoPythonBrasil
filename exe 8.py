print('''
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, '
'sabendo que a decisão é sempre pelo mais barato.''')

p1 = float(input('\nInforme o preço do 1° produto: R$ '))
p2 = float(input('Informe o preço do 2° produto: R$ '))
p3 = float(input('Informe o preço do 3° produto: R$ '))

if p1 < p2 and p1 < p3:
    print(f'R${p1} é o menor preço!')
if p2 < p1 and p2 < p3:
    print(f'R${p2} é o menor preço!')
if p3 < p1 and p3 < p2:
    print(f'R${p3} é o menor preço!')
