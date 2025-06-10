print('='*10, 'NEGATIVO, POSITIVO OU ZERO', '='*10)

num = int(input('Digite um número: '))

if num < 0:
    print(f'O número {num} é NEGATIVO.')
elif num > 0:
    print(f'O número {num} é POSITIVO.')
elif num == 0:
    print(f'O número {num} é ZERO.')
