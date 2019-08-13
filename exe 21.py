print('''
21. Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário o valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
''')
while True:
    nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = 0
    saque = float(input('Qual valor deseja sacar? R$'))
    print(f'O valor sacado foi R${saque} em cédulas de...')
    if saque < 10 or saque > 600:
        saque = float(input('Saque permitido apenas acima de R$10,00 ou até R$600,00! Informe valor do saque: R$'))

    if saque:                                   #notas de R$100,00
        nota_100 = saque%100
        c100 = (saque-nota_100)/100
        print(f'{c100} cédulas de R$100,00')

    if saque:                                   #notas de R$50,00
        nota_50 = nota_100%50
        c50 = (nota_100-nota_50)/50
        print(f'{c50} cédulas de R$50,00')

    if saque:                                   #notas de R$10,00
        nota_10 = nota_50%10
        c10 = (nota_50-nota_10)/10
        print(f'{c10} cédulas de R$10,00')

    if saque:                                   #notas de R$5,00
        nota_5 = nota_10%5
        c5 = (nota_10-nota_5)/5
        print(f'{c5} cédulas de R$5,00')

    if saque:                                   #notas de R$1,00
        nota_1 = nota_5%1
        c1 = (nota_5-nota_1)/1
        print(f'{c1} cédulas de R$1,00')
    break
