print('''15. Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;''')

l1 = float(input('Insira o 1° Lado do triângulo: '))
l2 = float(input('Insira o 2° Lado do triângulo: '))
l3 = float(input('Insira o 3° Lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\nÉ possível contruir um triângulo com as informações digitadas!')
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('Este triângulo é equilátero!')
    elif l1 != l2 or l1!= l3 or l2!=l3:
        print('Este triângulo é Escaleno!')
    else:
        print('Este triângulo é Isóceles!')
else:
    print('\nNão se pode formar um triângulo com os dados informados!')
