#aula 12 

num = int(input('Digite um número inteiro: '))

print('''Escolha umaa das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL ''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BÍNARIO é igual a {bin(num) [2:]}') #convertendo o número para BÍNARIO, usando fatiamento
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num) [2:]}') #convertendo o número para OCTAL, usando fatiamento
elif opção == 3:
    print(f'{num} convertendo para HEXADECIMAL é igual a {hex(num) [2:]}') #convertendo o número para HEXADECIMAL, usando fatiamento
else:
    print('Opção inválida. Tente novamente.')
    print('Opção inválida. Tente novamente.')