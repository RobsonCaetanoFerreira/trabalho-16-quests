print('='*20, 'ÁREA DE UM RETANGULO', '='*20)

def continha(a, b):
    return(a * b)

largura = float(input('Informe a largura do Retângulo: '))
altura = float(input('Informe a altura do Retângulo: '))

conta = continha(largura, altura)

print(f'A área deste retângulo é {conta}Cm.')
