print('''
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.''')

sexo = str(input('Qual seu sexo? [F / M]: ')).upper().strip()
if sexo == 'F':
    print('Você é do sexo Feminino!')
if sexo == 'M':
    print('Você é do sexo Masculino!')
if sexo != 'FM':
    print('Valor informado inválido!')