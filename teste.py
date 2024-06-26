id1 = int(input('Digite o id da peça 1: '))
unidade1 = int(input('Digite a quantidade de peça 1 que deseja: '))
valor_unidade1 = float(input('Dgite o valor da unidade da peça 1: '))

id2 = int(input('Digite o id da peça 2: '))
unidade2 = int(input('Digite a quantidade de peça 2 que deseja: '))
valor_unidade2 = float(input('Dgite o valor da unidade da peça 2: '))

cal1 = unidade1 * valor_unidade1 + unidade2 * valor_unidade2

print(f'VALOR A PAGAR: R$ {cal1:.2f}')
