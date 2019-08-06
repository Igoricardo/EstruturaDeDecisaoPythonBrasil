print('''14. Faça um programa que lê as duas notas parciais obtidas por um aluno
 numa disciplina ao longo de um semestre, e calcule a sua média.
 A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.''')

n1 = float(input('Informe a 1° Nota: '))
n2 = float(input('Informe a 2° Nota: '))
m = (n1+n2)/2
if m > 9:
    print(f'NP1: {n1} NP2: {n2} MÉDIA: {m} - APROVADO - CONCEITO: A')
elif m > 7.5 and m < 9:
    print(f'NP1: {n1} NP2: {n2} MÉDIA: {m} - APROVADO - CONCEITO: B')
elif m > 6 and m <= 7.5:
    print(f'NP1: {n1} NP2: {n2} MÉDIA: {m} - APROVADO - CONCEITO: C')
elif m > 4 and m <= 6:
    print(f'NP1: {n1} NP2: {n2} MÉDIA: {m} - REPROVADO - CONCEITO: D')
else:
    print(f'NP1: {n1} NP2: {n2} MÉDIA: {m} - REPROVADO - CONCEITO: E')