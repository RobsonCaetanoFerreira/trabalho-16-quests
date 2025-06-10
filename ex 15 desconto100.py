print('-'*10, 'DESCONTO 100R$', '-'*10)

preço = float(input('Informe o preço para verificação: '))

if preço > 100:
    desconto = preço / 25 * 100
    print('Este preço tem um desconto de 25%')
    print(f'Com isso o preço muda para {preço - desconto}R$')
else:
    print('Este preço não tem desconto.')
    print(f'Continua sendo {preço}R$')
