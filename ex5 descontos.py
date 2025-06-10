print('='*25, 'CALCULANDO DESCONTOS', '='*25)

def continha_desc(a, b):
    return((a * b) / 100)
def continha(a, b):
    return(a - b)

preço = float(input('Informe o preço do produto: '))
desconto = float(input('Informe a porcetagem de desconto: '))

conta_desc = continha_desc(preço, desconto)
conta = continha(preço, conta_desc)

print(f'O valor {preço:.2f}R$ com o desconto aplicado fica {conta:.2f}R$.')
