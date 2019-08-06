print('''
16. Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo
grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
''')

print('''
EQUAÇÃO: ax2 + bx + c
DELTA:   d = b2 - 4*a*c
''')
while True:
    a = int(input('Informe o valor de A: '))
    if a == 0:
        print('Equação não é de 2° GRAU, aplicação encerrada!')
        break
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de C: '))
    d = (b*b) - (4*a*c)
    if d < 0:
        print(f'O valor de Delta é {d}, portanto não possui raizes reais, Aplicação sendo encerrada!')
        break
    if d == 0:
        print(f'O valor de Delta é igual a {d}, portanto a equação possui apenas 1 raiz real!')
        break
    if d > 0:
        print(f'O valor de Delta é {d}, por ser positivo, a equação possui 2 raizes reais!')
        break
