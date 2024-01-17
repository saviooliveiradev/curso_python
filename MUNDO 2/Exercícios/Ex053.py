frase = str(input('Digite uma frase: ')).strip().upper() #deixa maiúsculo

palavras = frase.split() # separando as palavras com o espaço na frase
junto = ''.join(palavras) #vai juntar as palavrass com espaço
inverso =  junto[::-1]

print(f'o iverso de {junto} é {inverso}')

if inverso == junto:
    print('temo um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
