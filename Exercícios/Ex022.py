# aula 9

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu noome em minúsculo: {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
# print(f'Seu  primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')