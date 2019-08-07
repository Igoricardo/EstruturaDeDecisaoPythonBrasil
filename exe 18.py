print('''
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida.
''')
while True:
    data = int(input('Informe a DATA: '))
    while data > 31:
        print('Digito inválido! Informe uma data válida!')
        data = int(input('Informe uma data válida: '))
    mes = int(input('Informe o MÊS: '))
    while mes > 12:
        print('Digito inválido! Informe um mês válida!')
        mes = int(input('Informe um mês válido: '))
    ano = int(input('Informe o ANO:'))
    print(f'A data, mês e ano informados são: {data}/{mes}/{ano}')
    break