# aula 7

preço = float(input('Digie o preço de um produto:R$ '))

desconto = (preço * 5 / 100)
valor = preço - desconto

print(f'O preço do produto com desconto de 5%  fica de R$ {valor:.2f}')