print('''
19. Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.
''')
n = int(input('Informe um N° maior que 0 e menor que 1000: '))
print(f'{n}')
u = n%10
d = n%100//10
c = n%1000//100
if n > 0 and n < 1000:
    if u:
        print(f'Unidade: {u}')
    if d:
        print(f'Dezena : {d}')
    if c:
        print(f'Centena: {c}')
else:
    print('Digito Inválido!')