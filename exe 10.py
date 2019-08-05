print('''10. Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.''')
opção = str(input('''\n
Em que turno você estuda? DIGITE:
M - matutino
V - vespertino
N - noturno
''')).upper().strip()
if opção in 'M':
    print('BOM DIA!')
elif opção in 'V':
    print('BOA TARDE!')
elif opção in 'N':
    print('BOA NOITE!')
else:
    print('VALOR INVÁLIDO!')