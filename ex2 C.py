print('-'*25, 'CONVERSOR DE C° PARA F°', '-'*25)

def continha(a):
    return((a * (9/5)) + 32)

celsius = float(input('Informe a temperatura para ser convertida: '))

conta = continha(celsius)

print(f'A temperatura {celsius}C° em Fahrenheit é de {conta}F°')
