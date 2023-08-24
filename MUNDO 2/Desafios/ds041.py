# aula 12

ano = int(input('Informe o ano do seu nascimento: '))

calculo = 2023 - ano

if calculo == 9 or calculo == 10 or calculo == 11 or calculo == 12 or calculo == 13:
    print('\033[34mMIRIM\033[34m')
elif calculo == 14 or calculo == 15 or calculo == 16 or calculo == 17 or calculo == 18:
    print('\033[34mINFANTIL\033[34m')
elif calculo == 19:
    print('\033[34mJUNIOR\033[34m')
elif calculo == 20:
    print('\033[34mSÉNIOR\033[34m')
elif calculo >= 21:
    print('\033[34mMASTER\033[m')