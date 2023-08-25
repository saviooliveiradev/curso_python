#aula 12

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota : '))

média =  (nota_1 + nota_2) / 2 

if média < 5.0:
    print('\033[31mREPROVADO!!!\033[m')
elif média >= 5 and média < 7:
    print('\033[33mRECUPERAÇÃO!!!\033[m')
elif média >= 7.0:
    print('\033[32mAPROVADO, PARABÉNSS!!!\033[32m')