print('6. Faça um Programa que leia três números e mostre o maior deles.')
n1 = float(input('Informe o 1° N°: '))
n2 = float(input('Informe o 2° N°: '))
n3 = float(input('Informe o 3° N°: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é maior que {n2} e {n3}')
if n2 > n1 and n2 > n3:
    print(f'{n2} é maior que {n1} e {n3}')
if n3 > n1 and n3 > n2:
    print(f'{n3} é maior que {n1} e {n2}')
