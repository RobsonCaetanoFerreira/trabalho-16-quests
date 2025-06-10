print('='*20, 'CAFETERIA', '='*20)

def continha (a, b):
    return(a * b)

café = int(input('Quantos cafes você irá comprar? '))
preço = float(input('Qual o preço desse café? '))

conta = continha(preço, café)

print(f'O total a se pagar é {conta}')
