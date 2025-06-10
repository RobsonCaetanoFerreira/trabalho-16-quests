print('='*25, 'IMC', '='*25)

def continha(a, b):
    return (b / (a * a))

altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

conta = continha(altura, peso)

print(f'O IMC calculado é de {conta:.2f}.')
