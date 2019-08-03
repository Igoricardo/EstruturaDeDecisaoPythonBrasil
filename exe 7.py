print('7. Faça um Programa que leia três números e mostre o maior e o menor deles.')
n1 = int(input('Informe o 1° N° inteiro: '))
n2 = int(input('Informe o 2° N° inteiro: '))
n3 = int(input('Informe o 3° N° inteiro: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior N°')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior N°')
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior N°')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor N°')
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor N°')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor N°')