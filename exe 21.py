print('''
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário 
o valor do saque e depois informar quans notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
''')
saque = float(input('Qual valor deseja sacar? R$: '))
while saque < 10 or saque > 600:
   print('valor inválido, informe um valor acima de R$10,00 ou menor que R$600,00')
   saque = float(input('Qual valor deseja sacar? R$: '))
if saque > 10 and saque <= 600:
   r = saque%100
   v = saque-r
   cedula = v//100
   print('{} cédula de R$100,00'.format(cedula, v))
if r > 0:
   r2 = r%10
   v2 = r-r2
   cedula2 = v2//50
   print('{} cédula de R$50,00'.format(cedula2, v2))
if r2 > 0:
   r3 = r2%10
   v3 = r2-r3
   cedula3 = v3//10
   print('{} cédula de R$10,00'.format(cedula3, v3))
