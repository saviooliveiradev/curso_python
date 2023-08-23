num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('\033[1;34mO primeiro valor é maior\033[m')
elif num2 > num1:
    print('\033[1;33mO segundo valor é maior\033[m')
elif num1 == num2:
    print('\033[1;31mNão existe valor maior, os dois são iguais\033[m') 