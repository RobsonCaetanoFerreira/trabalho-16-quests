print('=-'*10, 'TRIÂNGULO', '=-'*10)

cat1 = float(input('Informe o primeiro cateto: '))
cat2 = float(input('Informe o segundo cateto: '))
cat3 = float(input('Informe o terceiro cateto: '))

if cat1 < cat2 + cat3 and cat2 < cat1 + cat3 and cat3 < cat1 + cat2:
    if cat1 == cat2 == cat3:
        print('Esse catetos formam um triângulo EQUILATERO.')
    elif cat1 != cat2 != cat3 != cat1:
        print('Esses catetos formam um triângulo ESCALENO.')
    else:
        print('Esses segmentos formam um triângulo ISÓSCELES.')
elif cat1 > cat2 + cat3 and cat2 > cat1 + cat3 and cat3 > cat1 + cat2:
    print('Esses segmentos não formam um triângulo.')
