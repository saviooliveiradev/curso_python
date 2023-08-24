# aula 12

from random import choices
 
print('Vamos jogar pedra, papel ou tesoura!')
print('-=-' * 20)

lista = ['pedra', 'papel', 'teroura']

ler = str(input('Pedra, papel ou tesoura: '))

pc = print(choices(lista))

if ler == 'pedra' and pc == 'papel':
    print('você perdeu!!!')
elif ler == 'papel' and pc == 'tesoura':
    print('você perdeu!!!')
elif ler == 'tesoura' and pc =='pedra':
    print('você perdeu!!!')
elif pc == 'pedra' and ler == 'papel':
    print('você ganhou!!!')
elif pc == 'papel' and ler == 'tesoura':
    print('você ganhou!!!')
elif pc == 'tesoura' and ler == 'pedra':
    print('você ganhou!!!')
