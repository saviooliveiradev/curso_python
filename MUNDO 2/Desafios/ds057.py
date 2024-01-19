s_m = 'M'
s_f = 'F'
sexo = ''

while sexo != s_m and sexo != s_f:
    leitura= str(input('Digite seu sexo: [M/F] '))
    sexo = leitura.upper()
    
    if sexo != s_m and sexo != s_f:
        print('Digite novamente')

print('Acabou')
