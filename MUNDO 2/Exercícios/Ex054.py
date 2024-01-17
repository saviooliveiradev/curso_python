from datetime import date

atual = date.today().year #pegando o ano atual 
totmaior = 0
totmenor = 0

for pess in range(1,8): # contado 7 pessoas, sempre coloca um mais pro conta -1
    nasc = int(input(f'Em que ano a {pess} pesssoa nasceu? '))
    idade = atual - nasc

    if idade >= 21:
        totmaior =+ 1
    else:
        totmenor =+ 1

print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'E també, tivemmos {totmenor} menores de idade')
 