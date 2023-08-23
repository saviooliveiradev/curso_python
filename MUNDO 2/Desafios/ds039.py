ano = int(input('Informe o ano do seu nascimento: '))

calculo = 2023 - ano
falta = 17 - calculo

if calculo <= 17:
    print(f'Você não pode ainda se alistar no \033[32mExercito Brasileiro\033[m, falta {falta} anos para você se alistar!.')
elif calculo == 18:
    print('Você já pode se alistar no \033[32mExercito Brasileiro\033[m')
elif calculo > 18:
    print(f'Você já passou do tempo de se alistar, já passou {calculo - 18} ano do alistamento')
