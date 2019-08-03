print('''
5. Faça um programa para a leitura de duas notas parciais de um aluno. '
O programa deve calcular a média alcançada por aluno e apresentar:

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.''')
n1 = float(input('\nInforme a 1° nota: '))
n2 = float(input('Informe a 2° nota: '))
m = (n1+n2)/2
if m >= 7 and m < 9:
    print(f'A média do aluno é {m}, está APROVADO!')
if m < 7:
    print(f'A média do aluno é {m}, REPROVADO!')
if m == 10:
    print(f'A média do aluno é {m}, APROVADO COM DISTINÇÃO!')