print('-'*20, 'DIVISIVEL 3 E 5', '-'*20)

num = int(input('Digite um número para verificação: '))

if num % 3 == 0 and num % 5 == 0:
    print('Este número é divisivel por 3 e 5.')
elif num % 3 == 0 and num % 5 != 0:
    print('Este número so é divisivel por 3.')
elif num % 3 != 0 and num % 5 == 0:
    print('Este número so é divisivel por 5.')
else:
    print('Este número não é divisivel por nenhum dos números.')
