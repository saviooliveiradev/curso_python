# aula 10

n1 = int(input('Digite um núemro: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))

if n1 >= n2:
    if n1 >= n3:
        print(f'{n1} é maior')

if n2 >= n1:
    if n2 >= n3:
        print(f'{n2} é maior')

if n3 >= n1:
    if n3 >= n2:
        print(f'{n3} é maior')

if n1 <= n2:
    if n1 <= n3:
        print(f'{n1} é menor')

if n2 <= n1:
    if n2 <= n3:
        print(f'{n2} é menor')

if n3 <= n1:
    if n3 <= n2:
        print(f'{n3} é menor')