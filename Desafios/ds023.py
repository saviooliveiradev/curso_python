print('Digite um número de 0 a 9999')

num = str(input('Digite um número: '))

print(f'Unidade: {num[3:4]}')
print(f'Dezena: {num[2:3]}')
print(f'Centena: {num[1:2]}')
print(f'Milhar: {num[0:1]}')
