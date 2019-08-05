print('9 . Faça um Programa que leia três números e mostre-os em ordem decrescente.')
n1 = int(input('Informe o 1° N° inteiro: '))
n2 = int(input('Informe o 2° N° inteiro: '))
n3 = int(input('Informe o 3° N° inteiro: '))
if n1 < n2 and n1 < n3 and n2 < n3:
    print(f'Em ordem decrescente ficou: {n1}, {n2} e {n3}')
elif n1 < n2 and n1 < n3 and n3 < n2:
    print(f'Em ordem decrescente ficou: {n1}, {n3} e {n2}')
elif n2 < n1 and n2 < n3 and n1 < n3:
    print(f'Em ordem decrescente ficou: {n2}, {n1} e {n3}')
elif n2 < n1 and n2 < n3 and n3 < n1:
    print(f'Em ordem decrescente ficou: {n2}, {n3} e {n1}')
elif n3 < n1 and n3 < n2 and n1 < n2:
    print(f'Em ordem decrescente ficou: {n3}, {n1} e {n2}')
elif n3 < n1 and n3 < n2 and n2 < n1:
    print(f'Em ordem decrescente ficou: {n3}, {n2} e {n1}')