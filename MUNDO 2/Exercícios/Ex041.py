# aula 12

from datetime import date #usando módulos para pegar o ano atual
atual = date.today().year #usando o método (date.today()), e atribuição de (year)  

ano = int(input('Ano de nascimento: '))
idade = atual - ano 

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('\033[34mMIRIM\033[34m')
elif idade <= 14:
    print('\033[34mINFANTIL\033[34m')
elif idade <=19:
    print('\033[34mJUNIOR\033[34m')
elif idade <=25:
    print('\033[34mSÉNIOR\033[34m')
else:
    print('\033[34mMASTER\033[m')