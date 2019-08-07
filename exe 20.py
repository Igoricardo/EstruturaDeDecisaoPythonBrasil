print('''
20. Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7,com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
''')
n1 = float(input('Informe a 1° nota: '))
n2 = float(input('Informe a 2° nota: '))
n3 = float(input('Informe a 3° nota: '))
m = (n1+n2+n3)/3
if m >= 7 and m < 10:
    print(f'Média: {m:.2f} / APROVADO')
elif m < 7:
    print(f'Média: {m:.2f} / REPROVADO')
else:
    print(f'Média: {m:.2f} / APROVADO COM DISTINÇÃO')