print('4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
letra = str(input('Informe uma letra: ')).upper().strip()
if letra in 'AEIOU':
    print(f'A letra {letra} é uma vogal!')
if letra not in 'AEIOU':
    print(f'A letra {letra} é uma consoante!')