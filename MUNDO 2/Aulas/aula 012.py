nome = str(input('Qual é o seu nome? '))

# Estrutura Condicional 
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana cláudia Jéssica Juliana':
    print('Belo nome feminno')    
else:
    print('Seu nome é bem normal!.')


print(f'Tenha um bom dia, {nome}!')
