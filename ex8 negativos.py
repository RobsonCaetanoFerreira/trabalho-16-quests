print('='*25, 'NÚMEROS NEGATIVOS', '='*25)

cont = 0

for i in range(1,5):
    num = float(input(f'Digite o {i}º número: '))
    if num < 0:
        cont += 1

print(f'A quantidade de números negativos digitados foi de {cont} números.')
