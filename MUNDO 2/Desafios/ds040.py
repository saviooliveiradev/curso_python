# aula 12

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\033[31mREPROVADO!!!\033[m')
elif media == 5.0 in 6.9:
    print('\033[33mRECUPERAÇÃO!!!\033[m')
elif media >= 7.0:
    print('\033[32mAPROVADO, PARABÉNSS!!!\033[32m')