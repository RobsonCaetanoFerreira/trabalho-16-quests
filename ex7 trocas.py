print('=-'*16, 'TROCA DE VALORES', '=-'*16)

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

num1, num2 = num2, num1

print(f'O primeiro valor é o: {num1}')
print(f'O segundo valor é o: {num2}')
