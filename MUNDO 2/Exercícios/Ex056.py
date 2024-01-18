soma_idade = 0
médiaidade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'----- {p} PESSOA -----')
    nome = str(input('Nome: ')).strip() #tira o espaço
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()

    soma_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade > 20:
        totmulher20 +=1

médiaidade = soma_idade / 4

print(f'A média de idade do grupo é de {médiaidade} anos')
print('O homem mais velho tem {maior_idade} anos e se chama {nome_velho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
