# print('\033[7;37mOlá, mundo\033[m')

# a = 3
# b = 5
# print(f'Os valores são \033[32m{a} \033[me \033[31m{b}\033[m!!!')

# nome = 'Guanabara'
# print(f'Olá muito prazer em te conhecer, \033[4;34m{nome}\033[m !!')

'limpa'
nome = 'Sávio'
cores = {'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7;37m'}

print('Olá muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))