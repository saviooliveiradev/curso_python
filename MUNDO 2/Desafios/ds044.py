# aula 12

preço = float(input('Digite o preço do produto:R$ '))
print('-=-' * 20)
print('CONDIÇÕES DE PAGAMENTO!!!')

cal_n1 = preço - (preço * 10 / 100)
cal_n2 = preço - (preço * 5 / 100)
cal_n3 = preço
cal_n4 = preço + (preço * 20 / 100)

print('Digite 1 para dinheiro/cheque, tem 10% de desconto')
print('Digite 2 para á vista no cartão, tem 5% de desconto')
print('Digite 3 em até 2x no cartão, preço normal')
print('Digite 4 em até 3x ou mais no cartão, tem 20% de juros')

num = int(input('Qual forma de Pagamento: '))

if num == 1:
    print(f'O valor ficou de R${cal_n1:.2f}')
elif num == 2:
    print(f'O valor ficou de R${cal_n2:.2f}')
elif num == 3:
    print(f'O valor ficou de R${cal_n3:.2f}')
elif num == 4:
    print(f'O valor ficou de R${cal_n4:.2f}')

