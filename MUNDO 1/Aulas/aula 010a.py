# nome = str(input('Qual é o seu nome? '))
# if nome == 'gustavo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal')
# print(f'Bom dia {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m >=6.0:
    print('Sua média foi boa! PARABÉNS!!!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print(f'A sua média foi {m:.1f}')