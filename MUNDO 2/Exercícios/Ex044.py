# aula 12

print('{:=^40}'.format(' LOJAS BASS ')) # centraliza no meio de 40 espaço cada lado

preço = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/pix
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual opção?'))

if opção == 4:
    parcelas = int(input('Quantas parcelas?'))

dinheiro = preço - (preço * 10 / 100)
cartão = preço - (preço * 5 / 100)
cartão_2x = preço
cartão_3x = preço + (preço * 20 / 100)

if opção == 1:
    print(f'Sua compra será R${dinheiro:.2f} com 10% de desconto.')
elif opção == 2:
    print(f'Sua compra será R${cartão:.2f} com 5% de desconto')
elif opção == 3:
    print(f'Sua compra será R${cartão_2x:.2f} parcelado em 2x sem juros.')
elif opção == 4: 
    divisão = cartão_3x / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${divisão:.2f} com juros de 20%.')
    print(f'Sua compra de R${preço:.2f} vai custar R${cartão_3x:.2f} no final.')
else:
    print('Não termos essa opção. TENTE NOVAMENTE!')
