print('-='*10, 'CALCULANDO JUROS', '-='*10)

def continha(a, b, c):
    return(a + (a * b * c / 100))

valor = float(input('Informe o valor: '))
juros = float(input('Informe o juros: '))
anos = int(input('Em quantos será pago? '))

ValorTot = continha(valor, juros, anos)

print(f'O valor {valor:.2f}R$ com {juros}% de juros é de {ValorTot:.2f}R$')
