frase = str(input('Digite uma frase: ')).strip().upper() #deixa maiúsculo

palavras = frase.split() # separando as palavras com o espaço na frase
junto = ''.join(palavras) #vai juntar as palavrass com espaço
inverso = ''

print(f'o iverso de {junto} é {inverso}')

for letra in range(len(junto) -1, -1, -1):
    print(junto[letra])
    inverso += junto[letra]

if inverso == junto:
    print('temo um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
