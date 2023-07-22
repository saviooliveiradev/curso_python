# nome = input('Qual é o seu nome? ')
# print(f'Prazer em te conhecer {nome:=^20}!')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print(f'A soma vale: \n {s}') #quebra de linha 
print(f'A multiplicação vale: {m}', end='') # para juntar as linhas do comando 
print(f'A divisão vale: {d:.3f}')
print(f'A divisão inteira vale: {di}')
print(f'A potência vale: {e}')


